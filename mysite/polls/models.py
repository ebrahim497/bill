from django.db import models
from datetime import datetime, timedelta, tzinfo

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
# Create your models here.

class City(models.Model):
	city_name = models.CharField(max_length=50)

	def __str__(self):
		return self.city_name

class Placetype(models.Model):
	placetype_name = models.CharField(max_length=50)

	def __str__(self):
		return self.placetype_name

class Billtype(models.Model):
	billtype_name = models.CharField(max_length=20)

	def __str__(self):
		return self.billtype_name

class Bill(models.Model):
	city_id = models.ForeignKey(City,on_delete = models.CASCADE)
	place_id = models.ForeignKey(Placetype,on_delete = models.CASCADE)
	billtype_id =models.ForeignKey(Billtype, on_delete = models.CASCADE)
	subscriber_id = models.CharField(max_length=100)
	
	def __str__(self):
		#return str(self.city_id)
		return '%s %s %s  شماره اشتراک%s' % (self.billtype_id, self.place_id, self.city_id, self.subscriber_id)

class Billmonth(models.Model):
	bill_id = models.ForeignKey(Bill, on_delete = models.CASCADE)
	form_id = models.IntegerField(default=0)
	#begin_date = models.DateTimeField(default = timezone.now)
	#end_date=models.DateTimeField(default = timezone.now)
	price = models.IntegerField(default=0)
	status = models.IntegerField(default=0)
	def __str__(self):
		#return str(self.form_id)
		return '%s از فرم شماره %s به مبلغ %s تومان' % (self.bill_id, self.form_id, self.price)
