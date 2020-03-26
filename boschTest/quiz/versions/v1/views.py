
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from quiz.models import Category, Question
from datetime import datetime, timedelta

import json


class QuizCategoryView(APIView):
	def get(self, request):
		quiz_id = int(request.query_params['quiz_id'])
		questions = Question.objects.filter(quiz_number=quiz_id).values('id', 'text', 'score', 'option_1', 'option_2', 'option_3', 'option_4', 'answer')
		ques_list = list(questions)
		return JsonResponse(ques_list, safe=False)
