# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import *
from .forms import *
from base.models import UserNotification
from base.utils import NotificationUtil
from datetime import datetime

# Create your views here.
def check_shipment(request):
    text = """<h1>Check Shipment Page !</h1>"""
    return HttpResponse(text)

class IndexView(TemplateView):
    template_name = 'logistic/index.html'

    def get_context_data(self,**kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Logistic Solution'
        context['page_heading'] = 'Welcome to our site, the logistic solution for you'
        return context

def get_price(request):
    cargo_type_list = CargoType.objects.filter(enabled='Y').order_by('sequence')
    context = {
                'page_title': 'Logistic Solution - Get Estimated Price',
                'page_heading': 'Please Select Preferred Cargo Type for Getting Estimated Price',
                'page_content': 'Select Cargo Type:',
                'cargo_type_list': cargo_type_list,
              }
    return render(request, 'logistic/get_price.html', context)

def get_price_step_1(request,cargo_type_id):
    try:
        cargo_type = CargoType.objects.get(pk=cargo_type_id)
    except CargoType.DoesNotExist:
        raise Http404('Cargo Type Not Exist')
    transport_service_list = TransportService.objects.filter(enabled='Y').order_by('sequence')
    context = {
                'page_title': 'Logistic Solution - Get Estimated Price',
                'page_heading': 'Please Select Preferred Transport Service for Getting Estimated Price',
                'page_content': 'Select Transport Service:',
                'cargo_type': cargo_type,
                'transport_service_list': transport_service_list,
              }
    return render(request, 'logistic/get_price_step_1.html', context)

def get_price_step_2(request,cargo_type_id,transport_service_id):
    try:
        cargo_type = CargoType.objects.get(pk=cargo_type_id)
    except CargoType.DoesNotExist:
        raise Http404('Cargo Type Not Exist')
    try:
        transport_service = TransportService.objects.get(pk=transport_service_id)
    except TransportService.DoesNotExist:
        raise Http404('Transport Service Type Not Exist')
    transport_list = Transport.objects.filter(enabled='Y').order_by('sequence')
    context = {
                'page_title': 'Logistic Solution - Get Estimated Price',
                'page_heading': 'Please Select Preferred Transport for Getting Estimated Price',
                'page_content': 'Select Transport:',
                'cargo_type': cargo_type,
                'transport_service': transport_service,
                'transport_list': transport_list,
              }
    return render(request, 'logistic/get_price_step_2.html' , context)

def get_price_step_3(request,cargo_type_id,transport_service_id,transport_id):
    try:
        cargo_type = CargoType.objects.get(pk=cargo_type_id)
    except CargoType.DoesNotExist:
        raise Http404('Cargo Type Not Exist')
    try:
        transport_service = TransportService.objects.get(pk=transport_service_id)
    except TransportService.DoesNotExist:
        raise Http404('Transport Service Type Not Exist')
    try:
        transport = Transport.objects.get(pk=transport_id)
    except Transport.DoesNotExist:
        raise Http404('Transport  Not Exist')
    context = {
                'page_title': 'Logistic Solution - Get Estimated Price',
                'page_heading': 'Please Select Preferred Transport for Getting Estimated Price',
                'page_content': 'Select Transport:',
                'cargo_type': cargo_type,
                'transport_service': transport_service,
                'transport': transport,
              }
    return render(request, 'logistic/get_price_step_3.html' , context)

def calculate_price(request):
    if request.method == "POST":
        form = PriceQueryForm(request.POST)
        if form.is_valid():
            try:
                cargo_type = CargoType.objects.get(pk=form.cleaned_data['cargo_type_id'])
            except CargoType.DoesNotExist:
                raise Http404('Cargo Type Not Exist')
            try:
                transport_service = TransportService.objects.get(pk=form.cleaned_data['transport_service_id'])
            except TransportService.DoesNotExist:
                raise Http404('Transport Service Type Not Exist')
            try:
                transport = Transport.objects.get(pk=form.cleaned_data['transport_id'])
            except Transport.DoesNotExist:
                raise Http404('Transport  Not Exist')
            context = {
                        'page_title': 'Logistic Solution - Price Result',
                        'page_heading': 'Please Select Preferred Transport for Getting Estimated Price',
                        'page_content': 'Select Transport:',
                        'cargo_type': cargo_type,
                        'transport_service': transport_service,
                        'transport': transport,
                        'origin': form.cleaned_data['origin'],
                        'destination': form.cleaned_data['destination'],
                        'distance': form.cleaned_data['distance'],
                        'duration': form.cleaned_data['duration'],
                        'price': 'IDR 50,000'
                      }
            return render(request, 'logistic/get_price_result.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return  redirect('logistic:index')
            else:
                return render(request, 'logistic/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'logistic/login.html', {'error_message': 'Invalid login'})
    return render(request, 'logistic/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'logistic/index.html', context)

# class UserFormView for member registration
class UserFormView(View):
    form_class = UserForm
    template_name = 'logistic/register.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('logistic:index')

        return render(request, self.template_name, {'form':form})


def notifications_user(request):
    if not request.user.is_authenticated():
        return render(request, 'logistic/login.html')
    else:
        notification_list = UserNotification.objects.filter(user=request.user,is_archived='N').order_by('-receive_timestamp')
        return render(request, 'logistic/notifications.html', { 'notification_list': notification_list, })

def notifications_user_detail(request, notification_id):
    try:
        usernotification = UserNotification.objects.get(pk=notification_id)
        if usernotification.is_read == 'N':
            util = NotificationUtil()
            util.markNotificationAsRead(usernotification)
    except UserNotification.DoesNotExist:
        raise Http404('User Notification Does Not Exist')
    context = {
                'notification': usernotification,
              }
    return render(request, 'logistic/notification_detail.html', context)


def products_and_services(request):
    cargo_type_list = CargoType.objects.filter(enabled='Y').order_by('sequence')
    transport_service_list = TransportService.objects.filter(enabled='Y').order_by('sequence')
    context = {
                'page_title': 'Logistic Solution - Get Estimated Price',
                'page_heading': 'Please Select Preferred Cargo Type for Getting Estimated Price',
                'page_content': 'Select Cargo Type:',
                'cargo_type_list': cargo_type_list,
                'transport_service_list': transport_service_list,
              }
    return render(request, 'logistic/products_and_services.html', context)
