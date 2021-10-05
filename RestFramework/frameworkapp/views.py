from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse

from rest_framework.views import APIView
from .models import *

class studentPostApi(APIView):
	def post(self,request):
		name = str(request.data["name"])
		no=request.data["no"]

		print(name,"*")
		print(no,"*")
		data = student(name=name,no=no)
		data.save()
		data=student.objects.values()
		print("add to data",data)
		json_data={"student":list(data)}
		return HttpResponse("success to done post")


class studentGetApi(APIView):
	def get(self,request):
		data=student.objects.values()
		print("Database Data",data)
		return HttpResponse({"get the query run data":"success"},{"student":list(data)})
	

