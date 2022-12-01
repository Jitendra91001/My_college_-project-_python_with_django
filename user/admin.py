from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'message')

admin.site.register(contact,contactAdmin)

class galleryAdmin(admin.ModelAdmin):
    list_display = ('id','pdes', 'gpic', 'gdate')

admin.site.register(gallery,galleryAdmin)

class recruiterssAdmin(admin.ModelAdmin):
    list_display = ('name', 'rpic', 'rdate')

admin.site.register(recruiterss,recruiterssAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('cname', 'cpic', 'cdate')

admin.site.register(category,categoryAdmin)

class coursesAdmin(admin.ModelAdmin):
    list_display = ('id','cname', 'cpic', 'cdate' ,'cseat' ,'chead' ,'cduration' ,'cdescription' ,'ctotal' ,'cadmission','branch')

admin.site.register(courses,coursesAdmin)

class placementsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'pcourse', 'branch','cmpname','cmplogo','city','pyear','designation','stupic','pdate')

admin.site.register(placements,placementsAdmin)

class ourcourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'coursename', 'coursepic')
admin.site.register(ourcourse, ourcourseAdmin)

