from django.urls import path
from crudoperation import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('retrievedata/', views.retrievedata, name="retrievedata"),
    path('updatedata/<int:id>/', views.updatedata, name="updatedata1"),
    path('alldata/', views.alldata, name="alldata1"),
    path('deletedata/<int:id>', views.deletedata, name="deletedata2"),
]