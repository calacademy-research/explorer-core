from django.contrib import admin
from .forms import OccurrenceForm
from .models.modelsCollections import CollectionsAppApiOccurrence

# Register your models here.
# admin.site.register(Images)
# admin.site.register(Collectionobject)

# def update_occu

# admin.site.register(CollectionsAppApiOccurrence)
#

@admin.register(CollectionsAppApiOccurrence)

class OccurrenceAdmin(admin.ModelAdmin):
    form = OccurrenceForm

    list_filter = ('collection_code', 'continent', 'state_province', 'island_group', 'locality', 'description')
    fields_search = ['occurrence_id', 'taxon_id', 'scientific_name']
    list_display = ['collection_code', 'occurrence_id', 'taxon_id', 'scientific_name', 'state_province', 'description']

    def save_model(self, request, obj, form, change):
        logger.info("Called admin save_model()")
        if form.is_valid():
            logger.info("Saving object with Admin Panel changes....", obj)
            obj.save()
        else:
            logger.info(form.errors)
        super().save_model(request, obj, form, change)