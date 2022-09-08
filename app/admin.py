from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Hospital)
# admin.site.register(Main_Doctor)
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Patient)


@admin.register(Main_Doctor)
class MainDoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age')

    def has_add_permission(self, request):
        return False if Main_Doctor.objects.all() else True

