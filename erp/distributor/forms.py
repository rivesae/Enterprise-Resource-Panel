from django import forms

class Search(forms.Form):
    search = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'class':'search', 'placeholder': 'Enter your search here', 'type': 'text'}))