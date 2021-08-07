from django.db.models.base import ModelState
from rest_framework import serializers

from .models import flight_db, flight_one_db, flight_two_db, booking_db
from django import forms



class get_f_serializer(serializers.ModelSerializer):
    class Meta:
        model = flight_db
        fields = (
            'f_name',
            's_n_d',
            'ava_seat',
        )
        

class get_f_one_status_serializer(serializers.ModelSerializer):
    class Meta:
        model = flight_one_db
        fields = (
            'f_name',
            's_n_d',
            'seat_name',
            'status',
        )



class get_f_two_status_serializer(serializers.ModelSerializer):
    class Meta:
        model = flight_two_db
        fields = (
            'f_name',
            's_n_d',
            'seat_name',
            'status',
        )



class book_seat_serializer(serializers.ModelSerializer):
    class Meta:
        model = booking_db
        fields = (
            'f_name',
            's_n_d',
            'seat_no',
            'booking_name',
            'booking_id',
            'time',
        )
 