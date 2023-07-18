from django.contrib import admin
from .models import Medicament,Ordonnance,LigneOrdonnance,PharmacistPendingOrdoannance,UserPendingOrdoannance
admin.site.register(Medicament)
admin.site.register(Ordonnance)
admin.site.register(LigneOrdonnance)
admin.site.register(PharmacistPendingOrdoannance)
admin.site.register(UserPendingOrdoannance)
# Register your models here.
