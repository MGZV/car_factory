from django.db import models


class Detail(models.Model):
    """Модель описывает деталь"""
    type = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ('type',)
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'


class Car(models.Model):
    """Модель описывает машину"""
    name = models.CharField(max_length=60)
    details = models.ManyToManyField(
        Detail,
        through='DetailCar',
        through_fields=('car', 'detail')
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class DetailCar(models.Model):
    """Модель описывает количество деталей в машине"""
    detail = models.ForeignKey('Detail', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('car',)


class CarPrice(models.Model):
    """Модель описывает стоимость машины"""
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    margin = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    labor_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Стоимость {self.car.name}'

    class Meta:
        ordering = ('car',)
        verbose_name = 'Стоимость машины'
        verbose_name_plural = 'Стоимость машин'
