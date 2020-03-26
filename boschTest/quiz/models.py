from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class BaseTimeStamp(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta(object):
		abstract = True


class Category(BaseTimeStamp):
	name = models.CharField(max_length=50)
	description = models.TextField()

	class Meta(object):
		db_table = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


class Question(BaseTimeStamp):
	quiz_number = models.PositiveIntegerField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	text = models.TextField()
	score = models.PositiveIntegerField(default=1)
	option_1 = models.CharField(max_length=500)
	option_2 = models.CharField(max_length=500)
	option_3 = models.CharField(max_length=500)
	option_4 = models.CharField(max_length=500)

	ANSWER_CHOICES = (
			("1", "Option 1"), 
			("2", "Option 2"), 
			("3", "Option 3"), 
			("4", "Option 4"), 
		)
	answer = models.PositiveIntegerField(choices=ANSWER_CHOICES, default=4)

	class Meta(object):
		db_table = 'question'
		verbose_name_plural = 'questions'

	def __str__(self):
		return self.category.name + '-' + self.quiz_number

# class CustomUser(AbstractUser):
# 	username = models.CharField(max_length=30)
# 	email = models.EmailField()
# 	password = models.CharField(max_length=100)
# 	scsore = models.PositiveIntegerField()

# 	class Meta(object):
# 		db_table = 'user'
# 		verbose_name_plural = 'users'