from django.contrib import admin

# Register your models here
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from employees.models import Employee
from main.admin import admin_site
from main.clients import UserApi


class EmployeesCsvResource(resources.ModelResource):
    def __init__(self):
        self.company = None

    def before_import_row(self, row, **kwargs):
        self.company = kwargs['user']

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.company = self.company


    class Meta:
        model = Employee


class EmployeeAdmin(ImportExportActionModelAdmin):
    resource_class = EmployeesCsvResource
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'age',
    )
    list_display_links = ('pk',)
    readonly_fields = ['company', 'okta_id']
    list_editable = (
        'first_name',
        'last_name',
        'age',)

    actions = [
        'register_employees',
    ]

    # actions ------------------------------------------------------------------
    def register_employees(self, request, queryset):
        user_api = UserApi()
        for q in queryset:
            if q.okta_id:
                continue
            payload = {
                "Email": q.email,
                "FirstName": q.first_name,
                "LastName": q.last_name,
                "Password": "Pass123.",
                "organization": q.company.name
            }
            registration_data = user_api.register_user(payload)
            if registration_data:
                q.okta_id = registration_data['id']
                q.save()

    register_employees.short_description = "register employees"

    def queryset(self, request):
        qs = super(EmployeeAdmin, self).queryset(request)
        return qs.filter(company=request.user)


admin_site.register(Employee, EmployeeAdmin)