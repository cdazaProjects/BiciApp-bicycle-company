from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from main.admin import admin_site
from products.models import Bicycle


class BicyclesCsvResource(resources.ModelResource):
    def __init__(self):
        self.company = None

    def before_import_row(self, row, **kwargs):
        self.company = kwargs['user']

    def before_save_instance(self, instance, using_transactions, dry_run):
        instance.company = self.company



    class Meta:
        model = Bicycle


class BicycleAdmin(ImportExportActionModelAdmin):
    resource_class = BicyclesCsvResource
    list_display = (
        'pk',
        'model',
        'address',
        'company',
    )

    def queryset(self, request):
        qs = super(BicycleAdmin, self).queryset(request)
        return qs.filter(company=request.user)


admin_site.register(Bicycle, BicycleAdmin)