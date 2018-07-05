from django.db import models

class Person(models.Model):

    name = models.CharField(max_length=50)

    age = models.IntegerField()

class Company(models.Model):

    name = models.CharField(max_length=30, verbose_name="名字")

    address = models.CharField(max_length=30, verbose_name="地址")

class Staff(models.Model):

    name = models.CharField(max_length=20)

    position = models.CharField(max_length=20)

    company = models.ForeignKey(Company)

class Grade(models.Model):

    name = models.CharField(max_length=20)

    position = models.CharField(max_length=20)

class Student(models.Model):

    name = models.CharField(max_length=20)

    age = models.IntegerField()


