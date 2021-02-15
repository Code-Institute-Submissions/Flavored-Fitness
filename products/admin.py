from django.contrib import admin
from .models import Product, Category, Recipe, Program

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rating',
        'image',
    )


class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rating',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Program, ProgramAdmin)