from django.shortcuts import render
from django.http import JsonResponse
import random, string, json
from django.db.models import F
import re
from django.http import QueryDict


# API imports here

from .models import *
from .serializers import  *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView





class get_f_status_view(APIView):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':

            qs = flight_db.objects.filter(ava_seat__gt = 0)            
            # qss = flight_two_db.objects.filter(status__iexact='AVAILABLE')
            # first_only = qs.first()
            # first_onlyy = qss.first()
            serializer =  get_f_serializer(qs, many=True)
           
            return JsonResponse(serializer.data, safe=False)

  

class get_f_one_status_view(APIView):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            
            f_db = flight_one_db
            qs = flight_one_db.objects.filter(status__iexact='AVAILABLE')
            serializer =  get_f_one_status_serializer(qs, many=True)
            return JsonResponse(serializer.data, safe=False)

class get_f_two_status_view(APIView):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':

            f_db = flight_two_db
            qs = flight_two_db.objects.filter(status__iexact='AVAILABLE')
            serializer =  get_f_two_status_serializer(qs, many=True)
            return JsonResponse(serializer.data, safe=False)



class book_one_view(APIView):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("one")
            serializers =  book_seat_serializer(data = request.data)
           
            f_db = flight_one_db
            out = call_book.post(f_db, serializers )
            return JsonResponse(out, safe = False)

class book_two_view(APIView):

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print("two")
            serializers =  book_seat_serializer(data = request.data)
          
            f_db = flight_two_db
            out = call_book.post(f_db, serializers )
            return JsonResponse(out, safe = False)



class call_book(APIView):

    def post(f_db, serializers):
            
            name = f_db.objects.values_list('f_name')[0]
            name = str(name)
            x = name.split("'")[1::2]
            x = str(x)
            n = x[2:-2]

            s_n_D = f_db.objects.values_list('s_n_d')[0]
            s_n_D = str(s_n_D)
            z = s_n_D.split("'")[1::2]
            z = str(z)
            s = z[2:-2]   
            print(n,s)     
            if serializers.is_valid(): 
                print("EUREKA")
                serializers.save()
                id = serializers['booking_id']; id = str(id); id = id[18:54]
                # fname = f_db.object(f_name)
                # print(id)
                booking_db.objects.filter(booking_id__iexact=id).update(f_name=n)
                booking_db.objects.filter(booking_id__iexact=id).update(s_n_d=s)
    
                seat_no = serializers.data["seat_no"].split(",")
                # name = serializers.data["booking_name"]
               
                for x in seat_no:
                    test = f_db.objects.filter(seat_name__iexact=x).filter(status__iexact='AVAILABLE')
                   
                    if not test:
                        print("CANNOT BOOK")
                        return ({'Cannot Book Ticket': 'Seat Not Avaible'})
                        break
                    else:
                        check = str(test[0])
                        f_db.objects.filter(seat_name__iexact=x).update(status='BOOKED')
                        # # print(n,name)
                        newdict = (serializers.data)
                        print(newdict)
                        newdict['f_name'] = n
                        newdict['s_n_d'] = s
                        print(newdict)
                        flight_db.objects.filter(f_name__iexact = n).update(ava_seat=F('ava_seat') - 1)
                        # flight_db.objects.update(ava_seat=F('ava_seat') - 1)
                              
                # return (serializers.data)
                return (newdict)
            err = serializers.errors
            print("YOU GOT A PROBLEM")
            return ({'Invalid Input': 'Please provide valid Seat number and Booking Name '})


class reset_status_view(APIView):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            flight_one_db.objects.all().update(status='AVAILABLE')
            flight_two_db.objects.all().update(status='AVAILABLE')  
            flight_db.objects.all().update(ava_seat = 100)
          
            # test = flight_one_db.objects.values_list('seat_name')[10]
            # print(test)
            return JsonResponse({'message': 'DONE'})
        

            