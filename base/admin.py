from django.contrib import admin
from .models import *

# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class UniversitateyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class Scientific_titleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class Academic_degreeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}




admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Universitate, UniversitateyAdmin)
admin.site.register(Academic_degree, Academic_degreeAdmin)
admin.site.register(Academic_year)
admin.site.register(All_job_positions)
admin.site.register(Person)
admin.site.register(Scientific_title, Scientific_titleAdmin)
admin.site.register(Department, DepartmentAdmin)

