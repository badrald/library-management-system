from django import forms
from .models import *
class BookForm(forms.ModelForm):
   class Meta:
        model= Book
        fields= [
            'title',
            'author',
            'photo_book',
            'price',
            'pages',
            'amount',
            'retail_price',
            'description',
            'active',
            'status',
            'category',
            
        ]
        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'descritpion':forms.Textarea(attrs={'class':'form-control'}),
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'retail_price':forms.NumberInput(attrs={'class':'form-control','id':'retail_price'}),
            'active':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }

class CategoryForm(forms.ModelForm):
     class Meta:
         model=Category
         fields = ['name']
         widgets={ 'name':forms.TextInput(attrs={'class':'form-control'}) }
