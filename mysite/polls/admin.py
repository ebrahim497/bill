from django.contrib import admin

from .models import City,Placetype,Billtype,Bill,Billmonth

class CityAdmin(admin.ModelAdmin):
	list_display=('city_name',)
	search_fields = ('city_name',)

class BillmonthAdmin(admin.ModelAdmin):
	list_display =('bill_id','price','form_id','status')
	search_fields =('bill_id__city_id__city_name','bill_id__place_id__placetype_name','bill_id__billtype_id__billtype_name')
	list_filter =  ('bill_id__city_id__city_name','bill_id__place_id__placetype_name','bill_id__billtype_id__billtype_name')

#admin.site.register_app_label("polls", _("ثبت قبوض"))
admin.site.register(Billtype)
admin.site.register(Bill)
admin.site.register(City, CityAdmin)
admin.site.register(Billmonth , BillmonthAdmin)
admin.site.register(Placetype)
# Register your models here.