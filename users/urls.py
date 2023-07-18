from django.urls import path, include
from . import views
urlpatterns = [ 
 
    path('login_user',views.login_user,name="login"),
    path('logout_user',views.logout_user,name="logout"),
    path('register_user',views.registerRequestForm,name="Register"),
    path('PendingDoctors',views.PendingDoctor,name="PendingDoctor"),
    path('PendingPharmacists',views.PendingPharmacist,name="PendingPharmacist"),
    
]
