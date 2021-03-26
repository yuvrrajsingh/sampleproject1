from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(label='Title', min_length=1, widget=forms.TextInput(attrs={'class':'form-control'}))
    discription = forms.CharField(label='Discription', min_length=1, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}))
    priority = forms.CharField(label='Priority', widget=forms.NumberInput(attrs={'class': 'form-control'}))