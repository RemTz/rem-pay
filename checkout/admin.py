from django.contrib import admin

from checkout.models import Address, PayWay
from.models import Orderdetails, PayWay, Address, Price, Orderdetails
# Register your models here.

admin.site.register(PayWay)
admin.site.register(Address)
admin.site.register(Price)
admin.site.register(Orderdetails)