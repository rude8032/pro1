from django import forms
from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['item', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].widget = forms.TextInput()  # This sets the item field widget to TextInput
