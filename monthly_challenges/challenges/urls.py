from django.urls import path
from . import views


urlpatterns = [
    
    path("",views.index,name="index"),
    path('<int:month_selected>', views.month_response_number),
    path('<str:month_selected>', views.month_response, name="month_string")

]
