from django.contrib import admin

from .models import (
    CargoType,
    CartonType,
    Cell,
    CellOrderSku,
    Order,
    OrderSku,
    Sku,
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "orderkey",
        "status",
        "created_at",
        "display_selected_cartontypes",
    )
    list_filter = ("status", "created_at")
    search_fields = ("orderkey", "status")
    readonly_fields = (
        "orderkey",
        "created_at",
        "display_selected_cartontypes",
    )
    ordering = ("status",)

    def display_selected_cartontypes(self, obj):
        return ", ".join(str(ct) for ct in obj.selected_cartontypes.all())

    display_selected_cartontypes.short_description = "Selected Carton Types"


@admin.register(Sku)
class SkuAdmin(admin.ModelAdmin):
    list_display = ("sku", "name", "quantity")
    list_filter = ("quantity",)
    search_fields = ("sku", "name")


@admin.register(CargoType)
class CargoTypeAdmin(admin.ModelAdmin):
    list_display = ("cargotype", "description")
    search_fields = ("cargotype", "description")


@admin.register(CartonType)
class CartonTypeAdmin(admin.ModelAdmin):
    list_display = ("cartontype", "length", "width", "height")
    search_fields = ("cartontype",)


@admin.register(OrderSku)
class OrderSkuAdmin(admin.ModelAdmin):
    list_display = ("order", "sku", "amount")
    list_filter = ("order", "sku")
    search_fields = ("order__orderkey", "sku__sku")


@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    list_display = ("barcode", "name", "table")
    list_filter = ("table",)
    search_fields = ("barcode", "name")


@admin.register(CellOrderSku)
class CellOrderSkuAdmin(admin.ModelAdmin):
    list_display = ("cell", "sku", "order", "quantity")
    list_filter = ("cell", "sku", "order")
    search_fields = ("cell__barcode", "sku__sku", "order__orderkey")
