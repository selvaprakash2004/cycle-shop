from django import forms 

from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['title', 'desc','category', 'thumbnail', 'price', 'stock']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Product Title'
            }),
            'desc' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Description',
                'rows' : 4
            }),
            'price' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Price'
            }),
            'stock' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Stock'
            }),
            'thumbnail' : forms.ClearableFileInput(attrs={
                'class' : 'form-control'
            })
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage 
        fields = ['image', 'caption']

        widgets = {
            'image' : forms.ClearableFileInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Image'
            }),
            'caption' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Image Caption',
            })
        }
