from django.db import models

# Create your models here.
'''
    人
    商品
    商品分类
    购物车
    订单
    订单详细
'''
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,null=False,unique=True)
    password = models.CharField(max_length=32,null=False)
    # avatar   = models.FileField(upload_to='avatars/',default='/avatar/default.png')

    class Meta:
        db_table='user'

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=False)
    email = models.CharField(max_length=32)
    zipcode=models.CharField(max_length=8,null=True,blank=True)
    address = models.CharField(max_length=128, null=True,blank=True)
    user = models.OneToOneField(to=User)

    class Meta:
        db_table='userinfo'

# class Goods(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(primary_key=40,null=False)
#     pic = models.FileField(upload_to='pic/',default='/pic/default.png',null=False)
#
#     class Meta:
#         db_table='goods'
#
# class RecentVisit(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(to=User)
#     goods = models.ForeignKey(to=Goods)
#
#     class Meta:
#         db_table='recentvisit'
#
# class GoodsCategory(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=40,null=False)
#
#     class Meta:
#         db_table = 'goodscategory'
#
# class GoodsInfo(models.Model):
#     id    = models.AutoField(primary_key=True)
#     type  = models.ForeignKey(to=GoodsCategory)
#     goods = models.OneToOneField(to=Goods)
#     excerpt = models.CharField(max_length=255)
#     weight = models.DecimalField()
#     price = models.DecimalField(default=0.0)
#     class Meta:
#         db_table = 'goodsinfo'
#
#
# class CartInfo(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(to=User)
#     goods = models.ForeignKey(to=Goods)
#     count = models.IntegerField(default=0)
#     class Meta:
#         db_table="cartinfo"
#
# class Order(models.Model):
#     id = models.AutoField(primary_key=True)
#     money = models.IntegerField(default=0)
#
#     class Meta:
#         db_table="order"
#
#
# class OrderInfo(models.Model):
#     id = models.AutoField(primary_key=True)
#     order = models.OneToOneField(to=Order)
#     create_time = models.DateTimeField(auto_now_add=True)
#     number = models.CharField(max_length=11)
#     goods = models.ForeignKey(to=Goods)
#     count = models.IntegerField(default=0)
#     price = models.DecimalField(default=0.0)
#
#     class Meta:
#         db_table="orderinfo"


