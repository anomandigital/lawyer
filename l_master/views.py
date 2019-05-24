from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from .models import *
from datetime import date


# Create your views here.
def landing(request):
    today = date.today()
    return render(request, 'landing.html', {'date': today})


def add_case(request):
    form_class = forms.CaseForm
    if request.method == 'GET':
        return render(request, 'add_case.html', {'form': form_class})
    if request.method == 'POST':
        form_class = forms.CaseForm(request.POST)
        if form_class.is_valid():
            case = form_class.save(commit=False)
            case.user = request.user
            case.created_by = request.user.id
            case.modified_by = request.user.id
            case.is_active = True
            case.save()
            messages.add_message(request, messages.SUCCESS, 'Case added successfully!')
            return redirect('/view_case')
        else:
            return render(request, 'add_case.html', {'form': form_class})


def add_client(request):
    form_class = forms.ClientForm
    if request.method == 'GET':
        return render(request, 'add_client.html', {'form': form_class})
    if request.method == 'POST':
        form_class = forms.ClientForm(request.POST)
        if form_class.is_valid():
            client = form_class.save(commit=False)
            client.created_by = request.user.id
            client.modified_by = request.user.id
            client.is_active = True
            client.save()
            messages.add_message(request, messages.SUCCESS, 'Client added successfully!')
            return redirect('/view_client')
        else:
            return render(request, 'add_client.html', {'form': form_class})


def view_case(request):
    if request.method == 'GET':
        cases = Case.objects.filter(is_active=True, is_deleted=False)
        return render(request, 'view_case.html', {'cases': cases})


def view_client(request):
    if request.method == 'GET':
        clients = Client.objects.filter(is_active=True, is_deleted=False)
        return render(request, 'view_client.html', {'clients': clients})


def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'edit_profile.html')


def delete_case(request, case_id):
    case = Case.objects.get(case_id=case_id)
    case.is_active = False
    case.save()
    return redirect('/view_case')


def delete_client(request, client_id):
    client = Client.objects.get(client_id=client_id)
    client.is_active = False
    client.save()
    return redirect('/view_client')
