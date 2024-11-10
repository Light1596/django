from django import forms

from customers.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
            'age': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Age'}),
        }