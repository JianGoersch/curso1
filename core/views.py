from django.shortcuts import render, HttpResponse

# Create your views here.
def curso1(request, nome, semestre):
     return HttpResponse('<h1>Hello {} do {} semestre</h1>.'.format(nome,semestre))