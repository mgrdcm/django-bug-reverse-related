from django.contrib import admin

# Register your models here.

from .models import Thing, Category


class ThingAdmin(admin.ModelAdmin):
    list_filter = [

        # This does not work (/admin/rrapp/thing/)
        ('categories', admin.RelatedOnlyFieldListFilter),

        # This works (/admin/rrapp/thing/)
        # 'categories',
    ]


admin.site.register(Category)
admin.site.register(Thing, ThingAdmin)
