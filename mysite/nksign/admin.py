from django.contrib import admin
# Register your models here.
from .models import Nksign
# class NksignAdmin(admin.ModelAdmin):
#     list_display =('signNo', 'userId', 'userNm','signDt','signDtm','signPlace','rec_crt_tm')
#     list_filter = ['userid','signdt']
#     search_fields = ['signdt']
# admin.site.register(Nksign, NksignAdmin)
# admin.site.register(Nksign)
class NksignAdmin(admin.ModelAdmin):
    list_display = ('userNm','signDtm','signPlace')
    list_filter = ['userId','signDt']
    #search_fields = ['userNm']
admin.site.register(Nksign, NksignAdmin)