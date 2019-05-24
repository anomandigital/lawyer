from django import forms
from django.contrib.auth import get_user_model

from .models import *
from .models import *

User = get_user_model()


class CaseForm(forms.ModelForm):
    created_by = forms.Field(required=False)
    modified_by = forms.Field(required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), label="")
    no = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Case No'}), label="")
    filing_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Filling Date'}), label="")
    next_listing_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Next Date'}), label="")
    last_listing_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Last Date'}), label="")
    court = forms.ModelChoiceField(queryset=Court.objects.filter(is_active=True, is_deleted=False),
                                   label='', empty_label='Select Court')
    clients = forms.ModelChoiceField(
        queryset=Client.objects.filter(is_active=True, is_deleted=False), label='',
        empty_label='Select Client')
    total_fee = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Total Fee'}), label="")
    received_fee = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Received Fee'}), label="")
    due_fee = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Due Fee'}), label="")

    class Meta:
        model = Case
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(CaseForm, self).__init__(*args, **kwargs)
    #     self.fields['due_fees'].error_messages = {'required': 'Enter Staff Type'}


class ClientForm(forms.ModelForm):
    created_by = forms.Field(required=False)
    modified_by = forms.Field(required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label="")
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}), label="")
    about = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'About'}), label="")
    birth_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Date of Birth'}), label="")

    country = forms.ModelChoiceField(
        queryset=Country.objects.filter(is_active=True, is_deleted=False), label='',
        empty_label='Select Country')
    state = forms.ModelChoiceField(
        queryset=State.objects.filter(is_active=True, is_deleted=False), label='',
        empty_label='Select State')
    city = forms.ModelChoiceField(
        queryset=City.objects.filter(is_active=True, is_deleted=False), label='',
        empty_label='Select City')
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Postal Address'}), label="")

    class Meta:
        model = Client
        fields = '__all__'
