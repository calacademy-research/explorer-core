from django.db.models.signals import pre_save, post_save, post_migrate
from collections_app_api.models.modelsCollections import CollectionsAppApiOccurrence
from django.dispatch import receiver
from django.core.management import call_command
# from django.apps import apps
import logging, re

logger = logging.getLogger(__name__)


# @receiver(pre_save, sender=CollectionsAppApiOccurrence)
# def update_model_url(sender, instance, **kwargs):
#     logger.info("update_model_url()")
#     logger.info(f"instance.model_url pre: {instance.model_url}")
#     if not instance.model_url:
#         if instance.occurrence_id:
#             existing_occurrence = sender.objects.filter(occurrence_id=instance.occurrence_id).first()
#             logger.info(f"Existing occurrence? {existing_occurrence}")
#             if existing_occurrence:
#                 # match = re.match(r"(?<=urn:catalog:CAS:)([A-Za-z]+[0-9]+)", instance.occurrence_id)
#                 # parsed_id = re.search(r"(?<=:CAS:)[A-Z]+[0-9]+", instance.occurrence_id)
#                 match = re.search(r"CAS:([A-Z]+:[0-9]+)", instance.occurrence_id)
#                 if match:
#                     parsed_id = match.group(1).replace(":", "")
#                     logger.info(f"parsed_id: {parsed_id}")
#                     instance.model_url = f"0.0.0.0/static/{parsed_id}"
#                     logger.info(f"instance.model_url: {instance.model_url}")
#             else:
#                 logger.info("Error matching occurrence ID to model_url endpoint")
#     else:
#         print(f"User-provided model_url: {instance.model_url}")

@receiver(post_save, sender=CollectionsAppApiOccurrence)#sender=apps.get_model('collections_app_api', 'CollectionsAppApiOccurrence'))
def my_model_post_save(sender, instance, created, **kwargs):
    if created:
        logger.info(f"A new instance of {sender.__name__} was created: {instance}")
    else:
        logger.info(f"An existing instance of {sender.__name__} was updated: {instance}")

    # Run makemigrations and migrate only if necessary (not recommended for every save)
    # Uncomment cautiously if your use case requires it
    # from django.db.migrations.executor import MigrationExecutor
    # executor = MigrationExecutor(connections['default'])
    # if executor.migration_plan(executor.loader.graph.leaf_nodes()):
    #     call_command('makemigrations', 'collections_app_api')
    #     call_command('migrate', 'collections_app_api')
