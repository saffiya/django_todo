from django import forms 
from .models import Item 

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'done')
    # meta allows us to provide additional information to django to tell it what we want
    # so we want this form to be based off the the item model and the fields that we want to fill in
    # are the name and the done