from django.db import models

# Create your models here.


class BaseTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

	class Meta(object):
		abstract = True


class Question(BaseTimeStamp):
	category = models.CharField(max_length=50)
	text = models.TextField()
	score = models.PositiveIntegerField()
	option_1 = models.CharField(max_length=250)
	option_2 = models.CharField(max_length=250)
	option_3 = models.CharField(max_length=250)
	option_4 = models.CharField(max_length=250)

	ANSWER_CHOICES = (
			("1", "Option 1"), 
			("2", "Option 2"), 
			("3", "Option 3"), 
			("4", "Option 4"), 
		)
	answer = models.ChoiceField(choices=ANSWER_CHOICES)

	class Meta(object):
		db_table = 'question'
		verbose_name_plural = 'questions'

