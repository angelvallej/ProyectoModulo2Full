from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.

@login_required
def index(request):
	return render (request, 'index.html')
