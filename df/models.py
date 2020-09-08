from django.db import models

# Create your models here.
class shops(models.Model):
    '''商品表'''
    shop_name = models.CharField(max_length=20, unique=True, verbose_name=u"商品名称")
    shop_number = models.IntegerField(verbose_name="商品数量",default=0)
    shop_time = models.DateTimeField(verbose_name="创建时间")

    class Meta:
        db_table = "shops"
        verbose_name = '商品表'
        verbose_name_plural = "商品表"

    def __str__(self):
        return self.shop_name
class shopput(models.Model):
    '''入库表'''
    name = models.ForeignKey('df.shops',on_delete=models.CASCADE,verbose_name='入库商品')
    purchase = models.IntegerField(default=0, verbose_name='采购数量')

    def save(self):
        self.name.shop_number += self.purchase
        self.name.save()
    # def purchase_options(self):
    #     self.name.shop_number += self.purchase
    #     self.name.shop_number.save()
    class Meta:
        db_table = 'shopput'
        verbose_name = '入库管理'
        verbose_name_plural = '入库管理'

class shopout(models.Model):
    '''出库表'''
    name = models.ForeignKey('df.shops',on_delete=models.CASCADE,verbose_name='出库商品')
    outchase = models.IntegerField(default=0, verbose_name='出库数量')
    news_type_chices = (
        (1, '小程序出单'),
        (2, '淘宝出单'),
        (3, '线下出单'),
    )
    news_type = models.IntegerField(choices=news_type_chices,verbose_name='出单方式')

    def save(self):
        self.name.shop_number -= self.outchase
        self.name.save()
    # def purchase_options(self):
    #     self.name.shop_number += self.purchase
    #     self.name.shop_number.save()


    class Meta:
        db_table = 'shopout'
        verbose_name = '出库管理'
        verbose_name_plural = '出库管理'






