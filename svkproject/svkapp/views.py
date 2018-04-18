from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from models import Todo
from django.template import loader
from serializers import Todoserializer
# Create your views here.
def index(request):
    return HttpResponse("This is a ToDo TaskManager app")
def demo(request):
   return render(request,'main.html')

class ToDo(APIView):

    def get(self,request):
        c = Todo.objects.all()
        serializer = Todoserializer(c,many=True)
        return Response(serializer.data)
    def post(self,request):
        c = Todo.objects.all()
        serializer = Todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, safe=False)
    def put(self,request,name=None,format=None):
        c = Todo.objects.get(name=name)
        serializer = Todoserializer(c,data=request.data,partial=True)
        if serializer.is_valid():
           serializer.save()
        return JsonResponse(serializer.data, safe=False)
    def delete(self,request):
        c = Todo.objects.all()
        c.delete()
        return Response({"result": "success", "message": ""})