from django.core.exceptions import MultipleObjectsReturned
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404

from car_price.forms import MarginForm
from car_price.models import Car, DetailCar, CarPrice


def car_list(request, ):
    """Функция отображает список машин"""
    cars = Car.objects.all()
    return render(request, 'car_price/car_list.html', {'cars': cars})


def car_detail(request, id):
    """Функция отображает из каких деталей состоит машина и позволяет посчитать её стоимость"""
    car = get_object_or_404(Car, id=id)
    if request.method == "POST":
        form = MarginForm(request.POST)
        if form.is_valid():
            form_margin = form.cleaned_data['margin']
            _labor_price = 0
            for car_details in DetailCar.objects.filter(car_id=id):  # перебираем детали в машине
                _labor_price += car_details.amount * car_details.detail.price
            total_price = _labor_price * form_margin
            try:
                CarPrice.objects.create(
                    car_id=id, margin=form_margin, labor_price=_labor_price, total_price=total_price)
            except IntegrityError:
                pass
            try:
                car_price = CarPrice.objects.get(car_id=id, margin=form_margin)
            except MultipleObjectsReturned:
                car_price = CarPrice.objects.filter(car_id=id, margin=form_margin)[0]
        return render(request, 'car_price/car_price.html', {'car': car, 'car_price': car_price})

    else:
        detail_car = DetailCar.objects.filter(car=car)
        form = MarginForm()
        return render(request, 'car_price/car_detail.html',
                      {'car': car,
                       'detail_car': detail_car,
                       'form': form
                       })
