from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {'age':'24','nationality':'Indian','name':'Apurva'}
    return render(request,'index.html',context)
def counter(request):
    words = request.POST['texxxt']
    amount_of_words = len(words.split())
    return render(request,'counter.html',{'amount_of_words':amount_of_words})