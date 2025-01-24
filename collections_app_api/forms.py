import re
import json
import logging
from django import forms
from django.core.exceptions import ValidationError
from collections_app_api.models.modelsCollections import CollectionsAppApiOccurrence

logger = logging.getLogger(__name__)

class CleanOccurrenceForm(forms.ModelForm):
    class Meta:
        model = CollectionsAppApiOccurrence
        fields = '__all__'

    def clean(self):
        logger.info("clean()")
        data_to_clean = super().clean()
        logger.info("cleaning data")

        if self.instance and self.instance.pk:
            # Editing an existing Occurrence (i.e., EditOccurrenceForm)
            logger.info("Editing Occurrence")
            return self.clean_edit(data_to_clean)
        else:
            # Creating a new Occurrence (i.e., CreateOccurrenceForm)
            logger.info("Creating Occurrence")
            return self.clean_json(data_to_clean)

        # add more logic checks for occurrence fields input
        # check if the occurrence_id field is present, etc.

    def clean_edit(self, data_to_clean):
        cleaned_edits = {}
        for field_name, field_value in data_to_clean.items():
            try:
                # validate only for string or string-like values, if input is None
                if isinstance(field_value, (str, int, float)):
                    cleaned_edits[field_name] = self.validate_input(field_name, field_value)
                else:
                    logger.warning(f"Skipping validation for field {field_name} with non-string value or Nonetype: {type(field_value)}")
            except ValidationError as e:
                self.add_error(field_name, e)
        logger.info("Finished cleaning data for Edit:")
        logger.info(cleaned_edits)
        return cleaned_edits

    def clean_json(self, data_to_clean):
        occurrence_json = data_to_clean.get('occurrence_json', "")
        try:
            data = json.loads(occurrence_json)

            for field, value in data.items():
                if field in self.fields:
                    self.check_for_injections(value)
                    self.fields[field].initial = value
                else:
                    logger.warning(f"Field '{field}' is not part of the form and will be skipped.")
        except json.JSONDecodeError:
            raise forms.ValidationError("Invalid JSON format.")

    def check_for_injections(self, value):
        if not isinstance(value, str):
            value = str(value or "")
            return value #skip non-string values

        # sql_injection_patterns = [
        #     r"(\b(SELECT|INSERT|DELETE|UPDATE|DROP|TRUNCATE|ALTER|CREATE|GRANT|REVOKE|UNION|WHERE|AND|OR|--|#|;|\*|=|>|<)\b)",
        #     r"['\";=]",
        # ]

        sql_injection_patterns = [
        r"(?i)\b(SELECT|INSERT|DELETE|UPDATE|DROP|TRUNCATE|ALTER|CREATE|GRANT|REVOKE|UNION|WHERE)\b.*;",  # SQL with semicolon
        r"(?i)\b(SELECT|INSERT|DELETE|UPDATE|DROP|TRUNCATE|ALTER|CREATE|GRANT|REVOKE|UNION|WHERE)\b.*--",  # SQL with comment
        r"['\";=]",
    ]
        logger.info(f"Checking GBIF JSON value for SQL")
        for pattern in sql_injection_patterns:
            if re.search(pattern, value or ""):#, re.IGNORECASE):
                raise ValidationError("Potential SQL injection detected in provided JSON.")
        logger.info("Checking GBIF JSON value for JS")
        if "<script>" in value or any(unsafe in value for unsafe in ['--', ';', '/*', '*/']):
            raise ValidationError("Potential JS injection detected in provided JSON.")
        if re.search(r"<script.*?>", value, re.IGNORECASE):
            raise ValidationError("Potential JavaScript injection detected in provided JSON")
        return value

    def validate_input(self, field_name, field_value):
        logger.info(f"Validating input for field: {field_name}")

        if not isinstance(field_value, str):
            field_value = str(field_value or "")

        # sql_injection_patterns = [
        #     r"(\b(SELECT|INSERT|DELETE|UPDATE|DROP|TRUNCATE|ALTER|CREATE|GRANT|REVOKE|UNION|WHERE|AND|OR|--|#|;|\*|=|>|<)\b)",
        #     r"['\";=]",
        # ]
        sql_injection_patterns = [
            r"(?i)\b(SELECT|INSERT|DELETE|UPDATE|DROP|TRUNCATE|ALTER|CREATE|GRANT|REVOKE|UNION|WHERE)\b.*;",
            # SQL with semicolon
            r"(?i)\b(SELECT|INSERT|DELETE|UPDATE|DROP|TRUNCATE|ALTER|CREATE|GRANT|REVOKE|UNION|WHERE)\b.*--",
            # SQL with comment
            r"['\";=]",
        ]
        for pattern in sql_injection_patterns:
            if re.search(pattern, field_value or ""):#, re.IGNORECASE):
                raise ValidationError(f"Potential SQL injection detected in input for {field_name_str}.")
        # Check for other unsafe characters or tags
        if "<script>" in (field_value or "") or any(
                unsafe in (field_value or "") for unsafe in ['--', ';', '/*', '*/']):
            raise ValidationError(f"Potential JS injection detected in input for {field_name_str}.")
        logger.info(f"validate_input: {(type(field_value))}")
        logger.info(f"validate_input: {field_value}")
        return field_value


class CreateOccurrenceForm(CleanOccurrenceForm):
    occurrence_json = forms.CharField(required=True,
                                      widget=forms.Textarea,
                                      help_text="Provide GBIF Occurrence JSON to populate fields.")
    class Meta:
        model = CollectionsAppApiOccurrence
        #fields = ['key', 'collection_code', 'scientific_name', 'description', 'model_url']
        fields = ['occurrence_json', 'collection_code', 'scientific_name']
        # widgets = {
        #     'occurrence_json': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the read-only fields
        #self.fields['key'].disabled = True
        self.fields['collection_code'].disabled = True
        self.fields['scientific_name'].disabled = True
    #     # If there's JSON data to parse
    #     if 'occurrence_json' in kwargs:
    #         occurrence_json = kwargs.pop('occurrence_json')
    #         self.parse_json(occurrence_json)

class EditOccurrenceForm(CleanOccurrenceForm):
    class Meta:
        model = CollectionsAppApiOccurrence
        #fields = '__all__'

        # readonly_fields = [field.name for field in CollectionsAppApiOccurrence._meta.get_fields() if
        #                    field.name not in ['description']]  # != 'description']

        fields = ['occurrence_id', 'scientific_name',
                  'taxon_id', 'occurrence_remarks',
                  'description', 'model_url', 'django_last_modified']
        # readonly_fields = ['occurrence_id', 'scientific_name',
        #                    'taxon_id', 'occurrence_remarks',
        #                    'django_last_modified', 'model_url']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # set the read-only fields that will display on the form page
            self.fields['occurrence_id'].disabled = True
            self.fields['scientific_name'].disabled = True
            self.fields['taxon_id'].disabled = True
            self.fields['occurrence_remarks'].disabled = True
            self.fields['django_last_modified'].disabled = True

    # def clean_description(self):
    # logger.info("clean_description()")
        # sql_injection_patterns = [
        #     r"(\b(SELECT|INSERT|DELETE|UPDATE|DROP|TRUNCATE|ALTER|CREATE|GRANT|REVOKE|UNION|WHERE|AND|OR|--|#|;|\*|=|>|<)\b)",
        #     r"['\";=]",  # Characters that could be used in SQL injections
        # ]
        # data_description = self.cleaned_data.get('description')
        # logger.info(data_description)
        # for pattern in sql_injection_patterns:
        #     if re.search(pattern, data_description, re.IGNORECASE):
        #         raise forms.ValidationError("Potential SQL injection detected in Description field entry.")
        # if "<script>" in data_description or any(unsafe in data_description for unsafe in ['--', ';', '/*', '*/']):
        #     raise ValidationError("Invalid input detected!")
        # return data_description

