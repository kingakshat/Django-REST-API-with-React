"""ticket_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from ticket_api_app.views import  get_f_status_view, get_f_one_status_view, get_f_two_status_view, book_two_view, book_one_view, reset_status_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('status', get_f_status_view.as_view(), name="status"),
    path('one/status', get_f_one_status_view.as_view(), name="one/status"),
    path('two/status', get_f_two_status_view.as_view(), name="two/status"),
    path('one/book', book_one_view.as_view(), name="one/book"),
    path('two/book', book_two_view.as_view(), name="two/book"),
    path('reset/', reset_status_view.as_view(), name="reset"),

  
]
