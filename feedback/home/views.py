from django.shortcuts import render
from . models import *

def index(request):
    feedbacks = CustomerFeedback.objects.all()
    return render(request,'surveys.html')


