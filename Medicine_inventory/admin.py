from django.contrib import admin
from Medicine_inventory.models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'brand', 'category', 'dosage', 'price',
        'quantity_in_stock', 'reorder_level', 'manufacture_date',
        'expiry_date', 'batch_number', 'supplier'
    ]
    search_fields = ['name', 'brand', 'category', 'batch_number', 'supplier']
    list_filter = ['category', 'brand', 'expiry_date']
    ordering = ['name', 'brand']