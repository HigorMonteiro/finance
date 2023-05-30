from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CreditCard)
admin.site.register(Category)
admin.site.register(BillCard)
admin.site.register(Bill)
admin.site.register(Income)