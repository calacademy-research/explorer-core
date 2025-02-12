import re, json, logging
from django import forms
from django.core.exceptions import ValidationError
from collections_app_api.models.modelsCollections import CollectionsAppApiOccurrence, OccurrenceGBIF

logger = logging.getLogger(__name__)
field_mapping = {
            "key": "key",
            "occurrenceID": "occurrence_id",
            "publishingCountry": "publishing_country",
            "protocol": "protocol",
            "lastCrawled": "last_crawled",
            "lastParsed": "last_parsed",
            "crawlId": "crawl_id",
            "basisOfRecord": "basis_of_record",
            "occurrenceStatus": "occurrence_status",
            "scientificName": "scientific_name",
            "decimalLatitude": "decimal_latitude",
            "decimalLongitude": "decimal_longitude",
            "continent": "continent",
            "stateProvince": "state_province",
            "waterBody": "water_body",
            "higherGeography": "higher_geography",
            "year": "year",
            "month": "month",
            "day": "day",
            "eventDate": "event_date",
            "startDayOfYear": "start_day_of_year",
            "endDayOfYear": "end_day_of_year",
            "issues": "issues",
            "modified": "modified",
            "lastInterpreted": "last_interpreted",
            "license": "license",
            "isSequenced": "is_sequenced",
            "identifiers": "identifiers",
            "media": "media",
            "relations": "relations",
            "institutionKey": "institution_key",
            "collectionKey": "collection_key",
            "isInCluster": "is_in_cluster",
            "recordedBy": "recorded_by",
            "preparations": "preparations",
            "geodeticDatum": "geodetic_datum",
            "verbatimEventDate": "verbatim_event_date",
            "islandGroup": "island_group",
            "island": "island",
            "verbatimLocality": "locality",
            "collectionCode": "collection_code",
            "higherClassification": "higher_classification",
            "georeferenceSources": "georeference_sources",
            "publishingOrgKey": "publishing_org",
            "datasetKey": "recordsetName_id",
            "taxonKey": "taxon_id",
        }

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
            return self.clean_edit()
        else:
            # Creating a new Occurrence (i.e., CreateOccurrenceForm)
            logger.info("Creating Occurrence")
            return self.clean_json()

        # add more logic checks for occurrence fields input
        # check if the occurrence_id field is present, etc.

    def clean_edit(self):
        cleaned_edits = {}
        # data_to_clean = self.cleaned_data.get()
        for field_name, field_value in self.cleaned_data.items():
            try:
                # validate only for string or string-like values, if input is None
                if isinstance(field_value, (str, int, float)):
                    cleaned_edits[field_name] = self.validate_input(field_name, field_value)
                else:
                    logger.warning(f"Skipping validation for field {field_name} with non-string value or Nonetype: {type(field_value)}")
            except ValidationError as e:
                self.add_error(field_name, e)
        logger.info("Finished cleaning data for Edit Occurrence")
        logger.info(cleaned_edits)
        return cleaned_edits

    def clean_json(self, target_model='RAW'):
        logger.info("within forms.py clean_json()")
        # logger.info(f"cleaned_data: {self.cleaned_data}")
        cleaned_json = {}
        if target_model == 'GBIF':
            logger.info("target_model GBIF")
            try:
                # logger.info(self.cleaned_data.keys())
                # logger.info(type(self.cleaned_data))
                occurrence_identifier = self.cleaned_data['occurrenceID']
            except json.JSONDecodeError:
                raise forms.ValidationError("Invalid occurrence_identifier / no field named occurrenceID in JSON")
            logger.info(occurrence_identifier)
            if OccurrenceGBIF.objects.filter(occurrenceID=occurrence_identifier).exists():
                raise forms.ValidationError("An occurrence with this value already exists in OccurrenceGBIF.")
            else:
                ### do field and value mapping for OccurrenceGBIF
                ### include validate_input for every field name and value
                cleaned_json = self.cleaned_data
                # logger.info(cleaned_json)
                logger.info("Returning data for OccurrenceGBIF object")
                return cleaned_json
        elif target_model == 'CollectionsApp':
            logger.info("target_model CollectionsApp")
            try:
                # test to see if it is occurrenceID or occurrence_id
                logger.info(f"target_model CollectionsApp: {self.cleaned_data}")
                logger.info(self.cleaned_data.keys())
                occurrence_identifier = self.cleaned_data['occurrenceID']
            except json.JSONDecodeError:
                raise forms.ValidationError(f"Unsupported target_model: {target_model}")
            logger.info(occurrence_identifier)
            if CollectionsAppApiOccurrence.objects.filter(occurrence_id=occurrence_identifier).exists():
                raise forms.ValidationError(
                    "An occurrence with this value already exists in CollectionsAppApiOccurrence.")
            else:
                ### do field and value mapping for CollectionsAppAPIOccurrence
                ### include validate_input for every field name and value
                # logger.info(f"cleaned_data: {self.cleaned_data}")
                occurrence_json = self.cleaned_data
                for field, value in occurrence_json.items():
                    # logger.info(f"occurrence_json field: {field}")
                    # logger.info(f"occurrence_json value: {value}")
                    if field in field_mapping.keys():
                        # self.check_for_injections(value)
                        # self.fields[field].initial = value
                        logger.info(f"Inputting value for {field_mapping[field]}: {value} into CAAOccurrence")
                        # cleaned_json[field_mapping[field]] = self.check_for_injections(value)
                        cleaned_json[field_mapping[field]] = value
                else:
                    logger.warning(f"Field '{field}' is not part of the Occurrence model and will be skipped.")
                logger.info(f"cleaned_json.keys(): {cleaned_json.keys()}")
                logger.info("Returning data for CAAOccurrence object")
                return cleaned_json
        elif target_model == 'RAW':
            # logger.info(f"self: {self}")
            logger.info("target_model RAW")
            logger.info(f"cleaned_data: {self.cleaned_data}")
            logger.info(self.cleaned_data.keys())
            # logger.info(type(data_to_clean))
            # occurrence_json = self.cleaned_data.get('occurrence_json_input')
            occurrence_json_input = self.cleaned_data.get('occurrence_json_input')
            logger.info(type(occurrence_json_input))
            if not occurrence_json_input:
                raise forms.ValidationError("Occurrence JSON input is missing")
            try:
                # occurrence_json = json.loads(self.cleaned_data.get('occurrence_json_input'))
                raw_json = json.loads(occurrence_json_input)
                # raw_json = occurrence_json_input
            except json.JSONDecodeError:
                raise forms.ValidationError("occurrence_json_input value is not JSON string")
            logger.info(f"occurrence_json: {raw_json}")
            # logger.info(type(occurrence_json))
            occurrence_identifier = raw_json['occurrenceID']
            if not occurrence_identifier:
                raise forms.ValidationError("OccurrenceID is missing")
            logger.info(occurrence_identifier)
            if OccurrenceGBIF.objects.filter(occurrenceID=occurrence_identifier).exists():
                raise forms.ValidationError("An occurrence with this value already exists in OccurrenceGBIF.")
            else:
            # matching occurrence json into occurrence model db object fields/values
            # try:
            #     # data_parsed = json.loads(data_to_clean['occurrence_json_input'])
            #     # logger.info(type(data_parsed))
            #     # logger.info(data_parsed)
            #     # model_fields = [field.name for field in CollectionsAppApiOccurrence._meta.get_fields() if not field.is_relation]
            #     # logger.info(type(model_fields))
            #     # logger.info(model_fields
            #     for field, value in raw_json.items():
            #         # logger.info(f"occurrence_json field: {field}")
            #         # logger.info(f"occurrence_json value: {value}")
            #
            #         cleaned_json[field] = value
            #         logger.info(f"Formatting value {value} for {field} for OccurrenceGBIF")
            # except json.JSONDecodeError:
            #     raise forms.ValidationError("Invalid JSON format.")
                cleaned_json = raw_json
                cleaned_json["raw_json"] = occurrence_json_input
                logger.info("Finished cleaning RAW for Create Occurrence")
                logger.info(cleaned_json.keys())
                logger.info("Returning cleaned_json....")
                return cleaned_json
        else:
            raise forms.ValidationError(f"Unsupported target model: {target_model}")
        # # occ_data = self.cleaned_data['occurrence_json_input']
        # # logger.info(occ_data)
        # # try:
        # #     logger.info("parsing occurrence json")
        # #     parsed_occ_json = json.loads(occ_data)
        # # except json.JSONDecodeError:
        # #     raise forms.ValidationError("Invalid JSON format. Please provide valid JSON.")
        # # return parsed_occ_json
        # occurrence_json = data_to_clean.get('occurrence_json_input', "")
        # try:
        #     data = json.loads(occurrence_json)
        #
        #     for field, value in data.items():
        #         if field in self.fields:
        #             self.check_for_injections(value)
        #             self.fields[field].initial = value
        #         else:
        #             logger.warning(f"Field '{field}' is not part of the form and will be skipped.")
        # except json.JSONDecodeError:
        #     raise forms.ValidationError("Invalid JSON format.")

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
                raise ValidationError(f"Potential SQL injection detected in input for {field_name}.")
        # Check for other unsafe characters or tags
        if "<script>" in (field_value or "") or any(
                unsafe in (field_value or "") for unsafe in ['--', ';', '/*', '*/']):
            raise ValidationError(f"Potential JS injection detected in input for {field_name}.")
        logger.info(f"validate_input: {type(field_value)}")
        logger.info(f"validate_input: {field_value}")
        return field_value


class CreateOccurrenceForm(CleanOccurrenceForm):
    occurrence_json_input = forms.CharField(required=True,
                                      widget=forms.Textarea,
                                      help_text="Provide GBIF Occurrence JSON to populate fields.")
    class Meta:
        model = OccurrenceGBIF
        fields = ['occurrence_json_input', 'scientificName', 'occurrenceID']
        # widgets = {
        #     'occurrence_json': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the read-only fields
        #self.fields['key'].disabled = True
        self.fields['scientificName'].disabled = True
        self.fields['occurrenceID'].disabled = True


class EditOccurrenceForm(CleanOccurrenceForm):
    class Meta:
        model = CollectionsAppApiOccurrence
        fields = ['occurrence_id', 'scientific_name',
                  'taxon_id', 'occurrence_remarks',
                  'description', 'model_url', 'django_last_modified']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # set the read-only fields that will display on the form page
            self.fields['occurrence_id'].disabled = True
            self.fields['scientific_name'].disabled = True
            self.fields['taxon_id'].disabled = True
            self.fields['occurrence_remarks'].disabled = True
            self.fields['django_last_modified'].disabled = True
