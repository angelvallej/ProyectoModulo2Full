# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from subprocess import Popen, PIPE
from django.conf import settings
import subprocess as sp
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def monitoreo_almacenamiento(request):
	p=Popen(settings.SCRIPT_ALMACENAMIENTO, shell=True, stdout=PIPE).stdout.read()
	r= p.decode('utf-8')
	return HttpResponse(r)

@login_required
def monitoreo_archivos(request):
	p=Popen(settings.SCRIPT_ARCHIVOS, shell=True, stdout=PIPE).stdout.read()
	r= p.decode('utf-8') 
	return HttpResponse(r)
@login_required
def monitoreo_auth(request):
	p=Popen(settings.SCRIPT_AUTH, shell=True, stdout=PIPE).stdout.read()
	r= p.decode('utf-8') 
	return HttpResponse(r)
@login_required
def monitoreo_procesos(request):
	p=Popen(settings.SCRIPT_PROCESOS, shell=True, stdout=PIPE).stdout.read()
	r= p.decode('utf-8') 
	return HttpResponse(r)
@login_required
def monitoreo_red(request):
	p=Popen(settings.SCRIPT_RED, shell=True, stdout=PIPE).stdout.read()
	r= p.decode('utf-8') 
	return HttpResponse(r)

@login_required
def monitoreo_usuarios(request):
	p=Popen(settings.SCRIPT_USUARIOS, shell=True, stdout=PIPE).stdout.read()
	r= p.decode('utf-8') 
	return HttpResponse(r)

@login_required
def monitoreo_apache(request):
	p=Popen(settings.SCRIPT_APACHE, shell=True, stdout=PIPE).stdout.read()
	r= p.decode('utf-8') 
	return HttpResponse(r)

#def seccion2(request):
#	return HttpResponse("Holiiwwiiisss")

