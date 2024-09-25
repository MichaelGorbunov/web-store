from django import forms
from catalog.models import Contact, Product, Category


class MyForm(forms.Form):

    # my_choices = (
    #     ('value1', 'Label 1'),
    #     ('value2', 'Label 2'),
    #     ('value3', 'Label 3'),
    # )
    # my_field = forms.ChoiceField(choices=my_choices, widget=forms.Select())
    my_field = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(),empty_label=None)
    username2 = forms.CharField()



