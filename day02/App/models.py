from django.db import models

class Categary(models.Model):

    name = models.CharField(
        max_length=20,
        verbose_name="分类名"
    )

class Item(models.Model):

    name = models.CharField(
        max_length=30,
        verbose_name="商品名",
        db_index=True
    )
    barcode = models.CharField(
        max_length=15,
        null=True,
        verbose_name="条码"
    )
    price = models.FloatField(
        verbose_name="售价"
    )
    inprice = models.DecimalField(
        max_digits=13,
        decimal_places=2,
        verbose_name = "进货价"
    )
    come_in_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    updatetime = models.DateTimeField(
        auto_now=True,
        verbose_name="修改时间"
    )
    icon = models.CharField(
        max_length=249,
        null=True,
        verbose_name="封面"
    )
    categary = models.ForeignKey(
        Categary,
        verbose_name="所属分类",
        db_index=True
    )
    def __str__(self):
        return self.name

class Cart(models.Model):

    name = models.CharField(
        max_length=10,
        verbose_name="名字"
    )

    item = models.ForeignKey(
        Item,
        verbose_name="商品"
    )
    class Meta:
        db_table ="cart"
        ordering=["-id"]

class Grade(models.Model):

    name = models.CharField(
        max_length=20,
        verbose_name="班级名",
    )
    comeintime = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    is_actice = models.BooleanField(
        default=True,
        verbose_name="是否活跃"
    )

class Students(models.Model):

    name = models.CharField(
        max_length=20,
        verbose_name="学生名",
    )
    comeintime = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    age = models.IntegerField(
        default=18,
        verbose_name="年龄"
    )
    score = models.IntegerField(
        default=80,
        verbose_name="成绩"
    )
    gradeid = models.ForeignKey(
        Grade,
        verbose_name="所属班级",
        db_index=True
    )
    def __str__(self):
        return self.name