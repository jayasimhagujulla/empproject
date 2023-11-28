from django.contrib import admin
from testapp.models import Employee,WorkExperience,Qualifications,projects
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','email','age','gender','phoneno','hno','street','city','state']
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display=['companyname','fromdate','todate','address']
class QualificationsAdmin(admin.ModelAdmin):
    list_display=['QualificationsName','fromdate','todate','percentage']
class projectsAdmin(admin.ModelAdmin):
    list_display=['title','description']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(WorkExperience,WorkExperienceAdmin)
admin.site.register(Qualifications,QualificationsAdmin)
admin.site.register(projects,projectsAdmin)
