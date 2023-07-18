 
from . import views
from django.urls import path
from django.urls import include, path
#int str path for / stuff slug for under and middle scores and UUID for unique identifiers, these are the ones permitted
urlpatterns = [
   
    path('',views.presentation,name="home"),
    path('presentation',views.presentation,name="generalPresentation"),
    path('PrepareOrdonnance',views.prepareOrdonnance,name="PrepareOrdonnance"),
    path('viewOrdonnance',views.visualiseOrdonnance,name="viewOrdonnance"),
    path('viewOrdonnancePending',views.visualiseWaitingOrdonnance,name="viewOrdonnancePending"),
    path('viewOrdonnancePendingInPharmacist',views.visualisePendingPharmacistOrdonnance,name="viewOrdonnancePendingInPharmacist"),
    path('acceptedOrdonnances',views.visualiseAcceptedOronnance,name="acceptedOrdonnances"),
    path('seeWrittenOrdonnace',views.visualiseHistory,name="seeWrittenOrdonnace"),
    path('download/<int:param>/',views.downlaoad,name="downloadSpecificOrdonnance"),


     
]


