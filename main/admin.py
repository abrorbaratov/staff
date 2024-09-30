from django.contrib import admin
from .models import Department, Employee, JobTitle
from django.core.exceptions import ValidationError
from django.contrib import messages


class DepartmentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.check_for_depth()
            obj.save()
        except ValidationError as e:
            messages.set_level(request, messages.ERROR)
            messages.error(request, e)
            return


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee)
admin.site.register(JobTitle)
