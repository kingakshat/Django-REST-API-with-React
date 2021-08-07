from django.db import models
from django.contrib.auth import get_user_model
import uuid


User = get_user_model()


class flight_db(models.Model):
    f_name = models.CharField(max_length = 100)
    s_n_d = models.CharField(max_length = 100)
    ava_seat = models.IntegerField(default = 30)
    
    def __str__(self) -> str:
        return self.f_name


class flight_one_db(models.Model):
    f_name = models.CharField(max_length = 100, default="Air India")
    s_n_d = models.CharField(max_length = 100, default="Mumbai -to- London")
    seat_name = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100, default="AVAILABLE")
    # booking_id = models.CharField(max_length = 100, default="--NA--")
   
    def __str__(self) -> str:
        return self.seat_name

class flight_two_db(models.Model):
    f_name = models.CharField(max_length = 100, default="Vistara")
    s_n_d = models.CharField(max_length = 100, default="Chennai -to- Las Vegas")
    seat_name = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100, default="AVAILABLE")
    # booking_id = models.CharField(max_length = 100, default="--NA--")
   
    def __str__(self) -> str:
        return self.seat_name

class booking_db(models.Model):

    seat_no = models.CharField(max_length = 100)
    booking_name = models.CharField(max_length = 100, default="--NA--")
    booking_id = models.CharField(max_length=12, blank=True, unique=True, default=uuid.uuid4)
    f_name = models.CharField(max_length = 100, default="--NA--")
    s_n_d = models.CharField(max_length = 100, default="--NA--")
    time = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return self.booking_id