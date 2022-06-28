from django.contrib import admin

from car_price.models import Car, Detail, CarPrice


class DetailCarInlineAdmin(admin.TabularInline):
    model = Car.details.through


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in Car._meta.fields if field.name != "id"]
    inlines = (DetailCarInlineAdmin, )


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Detail._meta.fields if field.name != "id"]


@admin.register(CarPrice)
class DetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CarPrice._meta.fields if field.name != "id"]
