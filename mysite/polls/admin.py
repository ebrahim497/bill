from django.contrib import admin

from .models import City,Placetype,Billtype,Bill,Billmonth

class CityAdmin(admin.ModelAdmin):
	list_city=('city_name',)
	search_fields = ('city_name',)
admin.site.register(City, CityAdmin)

admin.site.register(Placetype)
admin.site.register(Billtype)
admin.site.register(Bill)

class BillmonthAdmin(admin.ModelAdmin):
	list_display =('bill_id','form_id')
	search_fields =('bill_id__city_id',)
admin.site.register(Billmonth , BillmonthAdmin)
# Register your models here.