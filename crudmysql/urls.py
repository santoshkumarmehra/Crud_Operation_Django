from django.urls import path
from crudmysql import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('retrievedata4/', views.retrievedata, name="retrievedata4"),
    path('update_data/<int:id>/', views.updatedata, name="update_data"),
    path('alldata2/', views.alldata2, name="alldata2"),    
    path('deletedata/<int:id>', views.deletedata_data, name="deletedata"),
        
]