import datetime
from django.contrib import admin, messages
from .forms import EditOccurrenceForm, CreateOccurrenceForm, re, logging
from .models.modelsCollections import CollectionsAppApiOccurrence

# Register your models here.
# admin.site.register(Images)
# admin.site.register(Collectionobject)

# def update_occu

# admin.site.register(CollectionsAppApiOccurrence)
#
logger = logging.getLogger(__name__)

class OccurrenceAdmin(admin.ModelAdmin):

    # form = OccurrenceForm

    list_filter = [#['key',
                   'collection_code', 'continent', 'state_province', 'island_group', 'locality', 'description']
    fields_search = [#['key',
                    'occurrence_id', 'taxon_id', 'scientific_name']
    list_display = [#['key',
                    'taxon_id', 'collection_code', 'occurrence_id', 'scientific_name', 'state_province', 'description']
    #exclude = ['publishing_country', 'protocol', 'last_crawled', 'last_parsed', 'crawl_id']

    # readonly_fields = [field.name for field in CollectionsAppApiOccurrence._meta.get_fields() if field.name not in ['description', 'model_url']]#!= 'description']

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = EditOccurrenceForm
        else:
            self.form = CreateOccurrenceForm
        return super().get_form(request, obj, **kwargs)

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
                    # logger.info(f"parsed_id: {parsed_id}")
                    obj.model_url = f"{request.get_host()}/static/{parsed_id}"
                    # logger.info(f"obj.model_url AUTOMATIC: {obj.model_url}")
                    super().save_model(request, obj, form, change)
            else:
                # occurrence_match = re.match(r"(?<=urn:catalog:CAS:)([A-Za-z]+[0-9]+)", str(obj.occurrence_id))
                # obj.model_url = f"{request.get_host()}/static/{occurrence_match}"
                # logger.info(f"obj.model_url INPUT: {obj.model_url}")
                super().save_model(request, obj, form, change)
            #obj.save()
        elif form.is_valid() and (self.form == CreateOccurrenceForm):
        #elif kwargs['form'].is_valid() and (kwargs['form'] == CreateOccurrenceForm):
            logger.info(f"save_model(): Saving new Occurrence with Admin Panel changes for: {form.cleaned_data.get('occurrence_id')}")
            # obj.django_modified_by = request.user
            obj.django_last_modified = datetime.datetime.now()
            occurrence_input = form.cleaned_data.get('occurrence_id')
            occurrence_match = re.match(r"(?<=urn:catalog:CAS:)([A-Za-z]+[0-9]+)", occurrence_input)
            logger.info(f"occurrence_match Type: {type(occurrence_match)}")
            obj.model_url = f"{request.get_host()}/static/{occurrence_match}"
            super().save_model(request, obj, form, change)
        else:
            logger.info(form.errors)
        # obj.save()

    # overriding add_view for adding new Occurrences via json (from GBIF)
    def add_view(self, request, form_url='', extra_context=None):
        if request.method == 'POST':  # Only modify behavior for POST requests (form submission)
            form = self.get_form(request)(request.POST, request.FILES)
            if form.is_valid():
                try:
                    # Custom logic to check the form data before saving, including JSON parsing and injection checks
                    self.save_model(request, form, change=False)
                    logger.info("Occurrence added successfully")
                    messages.success(request, "Object added successfully.")
                    return HttpResponseRedirect(self.get_success_url(request))
                except Exception as e:
                    # Handle any errors during saving (e.g., JSON parsing errors, validation errors)
                    messages.error(request, f"Error saving object: {str(e)}")
                    logger.info("Error saving Occurrence")
                    return self.response_post_save_add(request, form)
            else:
                messages.error(request, "Form is invalid.")
                logger.info("Occurrence Form is invalid.")
                return self.response_post_save_add(request, form)

        # Standard add view if not POST request
        return super().add_view(request, form_url, extra_context)

# @admin.register(CollectionsAppApiOccurrence)
admin.site.register(CollectionsAppApiOccurrence, OccurrenceAdmin)