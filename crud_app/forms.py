from django import forms
from .models import Crud
class EntryForm(forms.ModelForm):
    class Meta:
        model=Crud
        fields='__all__'

    def __init__(self, *args, **kwargs):
            super(EntryForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
