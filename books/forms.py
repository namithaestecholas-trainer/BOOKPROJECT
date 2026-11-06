from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    price = forms.IntegerField()
    category = forms.CharField(max_length=50)
    available = forms.BooleanField(required=False)
    image = forms.ImageField()