from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from datetime import datetime

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address', 'birthday']

    def form_valid(self, form):
        self.object = form.save()
        if(self.object.birthday == datetime.date):
            return HttpResponse(f'С днем рождения, {self.object.person}! '
                                f'В качестве подарка, мы сделали Вам скидку в 10%.')
        else:
            print("ДР ", self.object.birthday)
            print("ДАТА ", datetime.date)
            return HttpResponse(f'Спасибо за покупку, {self.object.person}!')

