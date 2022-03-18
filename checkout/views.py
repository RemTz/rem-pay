from django.shortcuts import render
from .models import PayWay, Address, Price, Orderdetails

# Create your views here.
def index(request):
    payways = PayWay.objects.all()
    Addresses = Address.objects.all()
    prices = Price.objects.all()
    orders = Orderdetails.objects.all()
    paywaysNo = payways.count()
    addressesNo = Addresses.count()


    context = {
        'number_of_payways': paywaysNo,
        'number_of_addresses': addressesNo,
        'payways': payways,
        'addresse': Addresses,
        'prices': prices,
        'orders': orders
    }

    return render(request, 'index.html', context = context)
