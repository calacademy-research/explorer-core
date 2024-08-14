import json
from django.core.management.base import BaseCommand
from collections_app_api.models import (
    CollectionsAppApiCollectionsrecordset,
    CollectionsAppApiOrganization,
    CollectionsAppApiSpecies,
    CollectionsAppApiOccurrence
)


class Command(BaseCommand):
    help = 'Load GBIF JSON data into the collections database'

    def handle(self, *args, **kwargs):
        # Open and load the JSON data from the specified file
        with open('collections_app_api/data/gbifORN.json') as f:
            data = json.load(f)

        for item in data:
            # Get or create related models
            recordset, _ = CollectionsAppApiCollectionsrecordset.objects.get_or_create(recordset_id=item['datasetKey'])
            organization, _ = CollectionsAppApiOrganization.objects.get_or_create(publishing_org=item['publishingOrgKey'])
            taxon, _ = CollectionsAppApiSpecies.objects.get_or_create(key=item['taxonKey'])

            # Use update_or_create to update the existing record or create a new one if it doesn't exist
            occurrence, created = CollectionsAppApiOccurrence.objects.update_or_create(
                occurrence_id=item['occurrenceID'],  # Use unique field for lookup
                defaults={
                    'key': item['key'],
                    'recordsetName_id': item['datasetKey'],
                    'publishing_org': organization,
                    'taxonKey_id': taxon,
                    'publishing_country': item['publishingCountry'],
                    'protocol': item['protocol'],
                    'last_crawled': item['lastCrawled'],
                    'last_parsed': item['lastParsed'],
                    'crawl_id': item['crawlId'],
                    'basis_of_record': item['basisOfRecord'],
                    'occurrence_status': item['occurrenceStatus'],
                    'sex': item.get('sex'),
                    'life_stage': item.get('lifeStage'),
                    'scientific_name': item['scientificName'],
                    'decimal_latitude': item.get('decimalLatitude'),
                    'decimal_longitude': item.get('decimalLongitude'),
                    'elevation': item.get('elevation'),
                    'continent': item.get('continent'),
                    'state_province': item.get('stateProvince'),
                    'water_body': item.get('waterBody'),
                    'higher_geography': item.get('higherGeography'),
                    'year': item.get('year'),
                    'month': item.get('month'),
                    'day': item.get('day'),
                    'event_date': item.get('eventDate'),
                    'start_day_of_year': item.get('startDayOfYear'),
                    'end_day_of_year': item.get('endDayOfYear'),
                    'type_status': item.get('typeStatus'),
                    'issues': item['issues'],
                    'modified': item['modified'],
                    'last_interpreted': item['lastInterpreted'],
                    'license': item['license'],
                    'is_sequenced': item['isSequenced'],
                    'identifiers': item['identifiers'],
                    'media': item['media'],
                    'facts': item['facts'],
                    'relations': item['relations'],
                    'institution_key': item['institutionKey'],
                    'collection_key': item['collectionKey'],
                    'is_in_cluster': item['isInCluster'],
                    'recorded_by': item.get('recordedBy'),
                    'identified_by': item.get('identifiedBy'),
                    'preparations': item.get('preparations'),
                    # 'geodetic_datum': item['geodeticDatum'],
                    'record_number': item.get('recordNumber'),
                    'verbatim_event_date': item.get('verbatimEventDate'),
                    'island_group': item.get('islandGroup'),
                    'island': item.get('island'),
                    'locality': item.get('locality'),
                    'verbatim_locality': item.get('verbatimLocality'),
                    'collection_code': item['collectionCode'],
                    'occurrence_remarks': item.get('occurrenceRemarks'),
                    'verbatim_elevation': item.get('verbatimElevation'),
                    'higher_classification': item.get('higherClassification'),
                    'georeference_sources': item.get('georeferenceSources'),
                }
            )

            # Print message to indicate if a new row was created or an existing one was updated
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created occurrence {item["occurrenceID"]}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated occurrence {item["occurrenceID"]}'))
