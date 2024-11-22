from django import forms
from collections_app_api.models.modelsCollections import CollectionsAppApiOccurrence

class OccurrenceForm(forms.ModelForm):
    class Meta:
        model = CollectionsAppApiOccurrence
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # List of fields to keep editable
        editable_fields = ['description']

        # Make all fields read-only except those in editable_fields
        for field in self.fields:
            if field not in editable_fields:
                self.fields[field].widget.attrs['readonly'] = True
                self.fields[field].disabled = True # ensure the fields are read-only