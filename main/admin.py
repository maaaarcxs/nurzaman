from django.contrib import admin
from .models import Apartment, Block, Object, ObjectImage


class BlockInline(admin.StackedInline):
    model = Block
    extra = 2


class ObjectImageInline(admin.TabularInline):
    model = ObjectImage
    extra = 1


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('type', 'number', 'floor', 'rooms_count', 'area')
    list_display_links = ['number',]
    search_fields = ('number', 'floor')
    list_filter = ('rooms_count', 'area', 'floor')


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'object')
    list_display_links = ['name',]
    search_fields = ('name', 'object')
    list_filter = ('name', 'object')


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'get_blocks_count')
    list_display_links = ['name',]
    search_fields = ('name', 'address')

    def get_blocks_count(self, obj):
        return obj.block_set.count()
    
    get_blocks_count.short_description = "Количество блоков"