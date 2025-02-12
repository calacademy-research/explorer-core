import datetime
from django.urls import path, reverse
from django.http import HttpResponseRedirect
from django.contrib import admin, messages
from .forms import EditOccurrenceForm, CreateOccurrenceForm, re, logging
from .models.modelsCollections import CollectionsAppApiOccurrence, OccurrenceGBIF

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

class OccurrenceRawAdmin(admin.ModelAdmin):
    list_display = ['taxonKey', 'collectionCode', 'occurrenceID', 'scientificName']
    fields_search = ['taxonKey', 'collectionCode', 'occurrenceID', 'scientificName']
    list_filter = ['collectionCode', 'continent', 'stateProvince', 'islandGroup', 'verbatimLocality']

    def get_form(self, request, obj=None, **kwargs):
        logger.info("CreateOccurrenceForm")
        self.form = CreateOccurrenceForm
        # prevent unnecessary re-validation
        if obj and hasattr(obj, "_validated_form"):
            logger.info("Using cached validated form")
            return obj._validated_form
        # get the default form
        form = super().get_form(request, obj, **kwargs)
        # cache the form on the object to prevent multiple validations
        if obj:
            obj._validated_form = form
        return form

    def save_model(self, request, obj, form, change):
        ### add check to see if collectionID and object already exists in OccurrenceGBIF
        logger.info("Saving OccurrenceGBIF obj....")
        logger.info(f"Obj before saving: {obj}")
        logger.info(f"Obj type before saving: {type(obj)}")
        if obj is None:
            logger.error("Object is None before saving!")
            raise ValueError("Invalid object instance: obj is None")
        field_values = {field.name: getattr(obj, field.name) for field in obj._meta.get_fields()}
        logger.info(f"obj field values: {field_values}")
        occurrence_data = obj.json_field
        logger.info(f"obj.json_field in save_model: {obj.json_field}")
        if not isinstance(occurrence_data, dict):
            logger.error("obj.json_field is not a valid dictionary")
            raise forms.ValidationError("Invalid occurrence JSON format.")

        if change: # when editing an existing OccurrenceGBIF object
            try:
                gbif = OccurrenceGBIF.objects.get_or_create(my_model=obj)  # assuming a OneToOne or ForeignKey, or crate if obj doesn't exist yet
                for key, value in occurrence_data.items():
                    setattr(gbif, key, value)  # Update fields dynamically
                gbif.save()
            except ObjectDoesNotExist:
                gbif = OccurrenceGBIF(**occurrence_data)
                gbif.save()
        else:
            logger.info("IN HERE")
            logger.info(f"obj: {obj}")
            logger.info(occurrence_data)
            logger.info(f"occurrence_data.keys(): {occurrence_data.keys()}")
            logger.info(f"occurrence_data['key']: {occurrence_data['key']}")
            try:
                occurrence_data["classField"] = occurrence_data.pop("class", None)
                # gbif = OccurrenceGBIF(**occurrence_data)

                # ignore fields that are not present in OccurrenceGBIF model
                model_fields = {field.name for field in OccurrenceGBIF._meta.get_fields()}
                filtered_data = {key: value for key, value in occurrence_data.items() if key in model_fields}
                gbif = OccurrenceGBIF(**filtered_data)
                gbif.save()
                logger.info("Successfully saved GBIF JSON to OccurrenceGBIF obj")
            except Exception as e:
                logger.error(f"Error saving OccurrenceGBIF obj: {e}")
                raise

            # mapping JSON fields to the CAAOccurrence model fields
            formatted_gbif = form.clean_json(target_model='CollectionsApp')
            logger.info(f"formatted_gbif.keys(): {formatted_gbif.keys()}")
            formatted_gbif["django_last_modified"] = datetime.datetime.now()
            occurrenceID = formatted_gbif.get("occurrence_id", None)
            if not occurrenceID:
                logger.error("Missing occurrence_id in formatted GBIF data")
                raise forms.ValidationError("Occurrence ID is required.")

            occurrence_match = re.search(r"CAS:([A-Z]+:[0-9]+)", occurrenceID)
            # logger.info(f"occurrence_match: {occurrence_match}")
            # logger.info(f"occurrence_match.group(1): {occurrence_match.group(1)}")
            if not occurrence_match:
                logger.error(f"Invalid occurrence ID format within Raw save_model(): {occurrenceID}")
                raise forms.ValidationError("Invalid occurrence ID format.")
            else:
                parsed_id = occurrence_match.group(1).replace(":", "")
                logger.info(f"parsed_id: {parsed_id}")
                formatted_gbif["model_url"] = f"{request.get_host()}/static/{parsed_id}"
                logger.info(formatted_gbif["model_url"])
            occurrence = CollectionsAppApiOccurrence(**formatted_gbif)
            try:
                occurrence.save()
                logger.info("Successfully formatted and saved occurrence to CollectionsAppAPIOccurrence")
            except Exception as e:
                logger.error(f"Error saving Occurrence to CAAOccurrences: {e}")
                raise
            logger.info(f"save_model(): Successfully saved Occurrence {form.cleaned_data.get('occurrence_id')} to OccurrenceGBIF and CAAOccurrence tables.")
            return gbif

    def add_view(self, request, form_url='', extra_context=None):
        if request.method == 'POST':  # Only modify behavior for POST requests (form submission)
            form = self.get_form(request)(request.POST, request.FILES)
            logger.info("POST add_view() invoked")
            if form.is_valid():
                try:
                    raw_gbif = form.clean_json(target_model='GBIF')
                    logger.info(f"raw_gbif here: {raw_gbif}")
                    logger.info(type(raw_gbif))
                    obj = form.save(commit=False)
                    logger.info(f"obj after form.save(): {obj}")
                    obj.json_field = raw_gbif
                    logger.info(f"updated obj.json_field: {obj.json_field}")
                    for key, value in raw_gbif.items():
                        if hasattr(obj, key):
                            setattr(obj, key, value)
                    logger.info(f"Before save_model: obj={obj}, obj.__dict__={obj.__dict__}")
                    self.save_model(request, obj, form, change=False)
                    logger.info(f"After calling self.save_model: {obj.__dict__}")
                    # form.save_m2m()
                    self.message_user(request, "Occurrence obj added successfully!")
                    logger.info("OccurrenceGBIF added successfully")
                    messages.success(request, "Object added successfully.")
                    logger.info("Redirecting.....")
                    return HttpResponseRedirect(
                        # reverse('admin:collections_app_api_occurrencegbif_add', args=[obj.pk])
                        reverse('admin:collections_app_api_occurrencegbif_changelist')
                    )
                except Exception as e:
                    # Handle any errors during saving (e.g., JSON parsing errors, validation errors)
                    messages.error(request, f"Error saving object: {str(e)}")
                    logger.info(f"Error saving Occurrence: {e}")
                    # return self.response_post_save_add(request, form)
                    return super().add_view(request, form_url, extra_context)
            else:
                logger.info(form)
                messages.error(request, "Form is invalid. This occurrence may already exist in table.")
                logger.info("Occurrence Form is invalid.")
                logger.info(form.errors)
                return self.response_post_save_add(request, form)
        # standard add_view if not POST request
        logger.info(f"end of add_view for request: {request}")
        return super().add_view(request, form_url, extra_context)


class OccurrenceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False # prevents adding new Occurrence objects to CollectionsApp occurrence table
    # form = OccurrenceForm

    list_filter = [#['key',
                   'collection_code', 'continent', 'state_province', 'island_group', 'locality', 'description']
    fields_search = [#['key',
                    'occurrence_id', 'taxon_id', 'scientific_name']
    list_display = [#['key',
                    'taxon_id', 'collection_code', 'occurrence_id', 'scientific_name', 'state_province', 'description']
    #exclude = ['publishing_country', 'protocol', 'last_crawled', 'last_parsed', 'crawl_id']

    # readonly_fields = [field.name for field in CollectionsAppApiOccurrence._meta.get_fields() if field.name not in ['description', 'model_url']]#!= 'description']
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('edit/', self.edit_view),
        ]
        return custom_urls + urls

    def get_form(self, request, obj=None, **kwargs):
        # logger.info("OccurrenceAdmin determining form")
        # logger.info("EditOccurrenceForm")
        # self.form = EditOccurrenceForm
        # return super().get_form(request, obj, **kwargs)
        logger.info("EditOccurrenceForm")
        self.form = EditOccurrenceForm
        if obj and hasattr(obj, "_validated_form"):
            logger.info("Using cached validated form (EditOccurrenceForm)")
            return obj._validated_form
        form = super().get_form(request, obj, **kwargs)
        if obj:
            obj._validated_form = form
        return form

    # see if overwriting get_readonly_fields() fixes the read-only fields inconsistencies
    def get_readonly_fields(self, request, obj=None):
        if obj:
            # if editing existing occurrence obj
            return ['occurrence_id', 'scientific_name', 'taxon_id',
                    'occurrence_remarks', 'django_last_modified']
        return []

    def save_model(self, request, obj, form, change):
        logger.info("Called admin save_model()")
        # logger.info(form.is_valid())
        # logger.info(form)
        if form.is_valid() and (self.form == EditOccurrenceForm):
        #if kwargs['form'].is_valid() and (kwargs['form'] == EditOccurrenceForm):
            # logger.info(f"save_model(): Saving Occurrence edits with Admin Panel changes for: {obj.occurrence_id}")
            # obj.django_modified_by = request.user
            obj.django_last_modified = datetime.datetime.now()
            # logger.info(f"obj.occurrence_id: {obj.occurrence_id}")
            # logger.info(f"obj.model_url OG: {obj.model_url}")
            # match = re.match(r"(?<=urn:catalog:CAS:)([A-Za-z]+[0-9]+)", instance.occurrence_id)# parsed_id = re.search(r"(?<=:CAS:)[A-Z]+[0-9]+", instance.occurrence_id)
            if not obj.model_url:
                match = re.search(r"CAS:([A-Z]+:[0-9]+)", obj.occurrence_id)
                if match:
                    parsed_id = match.group(1).replace(":", "")
                    logger.info(f"parsed_id: {parsed_id}")
                    obj.model_url = f"{request.get_host()}/static/{parsed_id}"
                    # logger.info(f"obj.model_url AUTOMATIC: {obj.model_url}")
                    super().save_model(request, obj, form, change)
            else:
                # occurrence_match = re.match(r"(?<=urn:catalog:CAS:)([A-Za-z]+[0-9]+)", str(obj.occurrence_id))
                # obj.model_url = f"{request.get_host()}/static/{occurrence_match}"
                # logger.info(f"obj.model_url INPUT: {obj.model_url}")
                super().save_model(request, obj, form, change)
        else:
            logger.info(form.errors)

    def edit_view(self, request):
        logger.info(f'edit_view(): {self.form}')
        first_instance = self.model.objects.first()
        if first_instance:
            return redirect('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name),
                            first_instance.pk)
        return HttpResponse("No instances available to edit.", status=404)

admin.site.register(OccurrenceGBIF, OccurrenceRawAdmin)
admin.site.register(CollectionsAppApiOccurrence, OccurrenceAdmin)