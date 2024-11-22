from django.db.models.signals import post_save, post_migrate
from collections_app_api.models.modelsCollections import CollectionsAppApiOccurrence
from django.dispatch import receiver
from django.core.management import call_command
from django.apps import apps
import logging

logger = logging.getLogger('collections_app_api')

@receiver(post_save, sender=apps.get_model('collections_app_api', 'CollectionsAppApiOccurrence'))
def my_model_post_save(sender, instance, created, **kwargs):
    if not instance._state.adding:
        return
    if created:
        logger.info(f"A new instance of {sender.__name__} was created: {instance}")
    else:
        logger.info(f"An existing instance of {sender.__name__} was updated: {instance}")
    pass
    if instance:
        call_command('makemigrations', 'collections_app_api')
        call_command('migrate', 'collections_app_api')

# @receiver(post_migrate)
# def run_automigrate(sender, **kwargs):
#     call_command('automigrate')
