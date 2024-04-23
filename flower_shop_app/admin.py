from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *

# Register your models here.
admin.site.register(Flower)
admin.site.register(Bouquet)

class CustomerAdmin(UserAdmin):
    model = Customer
    list_display = ['username', 'purchases_counter']
    add_form = CustomerCreationForm
    form = CustomerChangeForm

admin.site.register(Customer, CustomerAdmin)