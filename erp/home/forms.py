from django.contrib.auth.forms import UserChangeForm
from core.models import CustomUser
from people.models import UserInfo
from django import forms

from django.core.validators import RegexValidator

class SettingsForm(UserChangeForm):
    email = forms.EmailField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = [
            'password',
            'email',
            'first_name',
            'last_name',
        ]


class StackedInLineUserForm(forms.ModelForm):
    birthdate = forms.DateField(label='Date of Birth', required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone_number = forms.IntegerField(label='Phone Number', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tin = forms.CharField(label='TIN', max_length=12, required=False, validators=[RegexValidator(r'^[0-9]+$')],widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    sss = forms.CharField(label='SSS', max_length=10, required=False, validators=[RegexValidator(r'^[0-9]+$')],widget=forms.TextInput(attrs={'class': 'form-control'}))
    philhealth = forms.CharField(label='PhilHealth', required=False, max_length=12,validators=[RegexValidator(r'^[0-9]+$')],widget=forms.TextInput(attrs={'class': 'form-control'}))
    pagibig = forms.CharField(label='Pag-ibig', max_length=12, required=False, validators=[RegexValidator(r'^[0-9]+$')],widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = UserInfo
        fields = [
            'birthdate',
            'phone_number',
            'address',
            'tin',
            'sss',
            'philhealth',
            'pagibig',
        ]