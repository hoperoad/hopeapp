from django.db import models


class Customer(models.Model):
    name = models.CharField('名前', max_length=20)
    address = models.CharField('住所', max_length=50)
    lat = models.DecimalField('緯度', max_digits=8, decimal_places=6)
    lng = models.DecimalField('経度', max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = '顧客'

class HopeEmployee(models.Model):
    user_id = models.CharField('社員ID', primary_key=True, max_length=128, default='99999999')
    password = models.CharField('パスワード', max_length=128, default='xxxxxxxx')
    first_name = models.CharField('苗字', max_length=128, null=True)
    last_name = models.CharField('名前', max_length=128, null=True)
    work_address = models.CharField('勤務先', max_length=256, null=True)
    email = models.CharField('Eメール', max_length=128, null=True)
    lat = models.DecimalField('緯度', max_digits=9, decimal_places=7)
    lon = models.DecimalField('経度', max_digits=10, decimal_places=7)
