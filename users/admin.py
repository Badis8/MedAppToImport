from django.contrib import admin
from .models import PendingDoctors
from .models import PendingPharmacists
from .models import actualDoctors
from .models import actualPharmacist
admin.site.register(PendingDoctors)
admin.site.register(PendingPharmacists)
admin.site.register(actualDoctors)
admin.site.register(actualPharmacist)
# Register your models here.
