from django.urls import path
from crudpostgres import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('retrievedata3/', views.retrievedata, name="retrievedata3"),
    path('updatedata/<int:id>/', views.updatedata, name="updatedata"),
    path('alldata/', views.alldata, name="alldata"),    
    path('deletedata/<int:id>', views.deletedata, name="deletedata4"),
        
]