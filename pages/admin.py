from django.contrib import admin

from pages.models import NewsModel, GalleryModel, WorkerModel, ProductModel, CategoryModel


@admin.register(NewsModel)
class ModelNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'created_at']


@admin.register(GalleryModel)
class ModelGalleryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(WorkerModel)
class ModelWorkerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created_at']
    search_fields = ['full_name', 'created_at']


@admin.register(CategoryModel)
class ModelWorkerAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(ProductModel)
class ModelWorkerAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
