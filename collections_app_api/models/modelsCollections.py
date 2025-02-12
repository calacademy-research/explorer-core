# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

#
# def generate_model_url_default(instance):
#     # generate default model_url of Occurrence obj
#     match = re.search(r"CAS:([A-Z]+:[0-9]+)", instance.occurrence_id)
#     if match:
#         parsed_id = match.group(1).replace(":", "")
#         # logger.info(f"parsed_id: {parsed_id}")
#         model_url_default = f"{request.get_host()}/static/{parsed_id}"
#         logger.info(model_url_default)
#     return f"{model_url_default}"

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class CollectionsAppApiCollectionsrecordset(models.Model):
    recordset_id = models.CharField(primary_key=True, max_length=235)
    recordsetName = models.CharField(db_column='recordsetName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collections_app_api_collectionsrecordset'


class CollectionsAppApiGalapagateway(models.Model):
    galapagatewaykey = models.BigAutoField(db_column='galapagatewayKey', primary_key=True)  # Field name made lowercase.
    recordset_id = models.CharField(max_length=45, blank=True, null=True)
    recordsetName_id = models.CharField(db_column='recordsetName_id', max_length=32)  # Field name made lowercase.
    occurrence_id = models.CharField(db_column='occurrence_id', unique=True, max_length=45)
    scientific_name = models.CharField(max_length=235, blank=True, null=True)
    taxon_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collections_app_api_galapagateway'


class CollectionsAppApiOccurrence(models.Model):
    key = models.BigIntegerField(primary_key=True)
    # maybe look into changing this to ForeignKey with OccurrenceGBIF occurrenceID
    occurrence_id = models.CharField(max_length=255)
    publishing_country = models.CharField(max_length=2)
    protocol = models.CharField(max_length=50)
    last_crawled = models.DateTimeField()
    last_parsed = models.DateTimeField()
    crawl_id = models.IntegerField()
    basis_of_record = models.CharField(max_length=255)
    occurrence_status = models.CharField(max_length=255)
    sex = models.CharField(max_length=50, blank=True, null=True)
    life_stage = models.CharField(max_length=50, blank=True, null=True)
    scientific_name = models.CharField(max_length=255)
    decimal_latitude = models.FloatField(blank=True, null=True)
    decimal_longitude = models.FloatField(blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    continent = models.CharField(max_length=255, blank=True, null=True)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    water_body = models.CharField(max_length=255, blank=True, null=True)
    higher_geography = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    start_day_of_year = models.IntegerField(blank=True, null=True)
    end_day_of_year = models.IntegerField(blank=True, null=True)
    type_status = models.CharField(max_length=255, blank=True, null=True)
    issues = models.JSONField()
    modified = models.DateTimeField()
    last_interpreted = models.DateTimeField()
    license = models.CharField(max_length=200)
    is_sequenced = models.IntegerField()
    identifiers = models.JSONField()
    media = models.JSONField()
    facts = models.JSONField()
    relations = models.JSONField()
    institution_key = models.CharField(max_length=235)
    collection_key = models.CharField(max_length=235)
    is_in_cluster = models.IntegerField()
    recorded_by = models.CharField(max_length=255, blank=True, null=True)
    identified_by = models.CharField(max_length=255, blank=True, null=True)
    preparations = models.CharField(max_length=255, blank=True, null=True)
    geodetic_datum = models.CharField(max_length=255)
    record_number = models.CharField(max_length=255, blank=True, null=True)
    verbatim_event_date = models.CharField(max_length=255, blank=True, null=True)
    island_group = models.CharField(max_length=255, blank=True, null=True)
    island = models.CharField(max_length=255, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    verbatim_locality = models.TextField(blank=True, null=True)
    collection_code = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    occurrence_remarks = models.TextField(blank=True, null=True)
    verbatim_elevation = models.CharField(max_length=255, blank=True, null=True)
    higher_classification = models.TextField(blank=True, null=True)
    georeference_sources = models.TextField(blank=True, null=True)
    publishing_org = models.CharField(max_length=235)
    recordsetName_id = models.CharField(db_column='recordsetName_id', max_length=235)  # Field name made lowercase.
    taxon_id = models.IntegerField()
    model_url = models.TextField(blank=True, null=True)
    # model_url = models.TextField(default=generate_model_url_default)
    #django_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)  # Tracks the admin user who made the modification
    django_last_modified = models.DateTimeField(null=True, blank=True) # will automatically update and save if modified via admin panel (admin.py)

    class Meta:
        managed = True
        db_table = 'collections_app_api_occurrence'

    def __str__(self):
        return self.occurrence_id
    #
    # def save(self, *args, **kwargs):
    #     logger.info("Successfully saved changes to Occurrence table")
    #     super().save(*args, **kwargs)

class OccurrenceGBIF(models.Model):
    raw_json = models.JSONField() # raw GBIF json of occurrence
    # key = models.BigIntegerField(unique=True)
    # occurrenceID = models.CharField(max_length=255, null=True, blank=True)
    # publishingCountry = models.CharField(max_length=10, null=True, blank=True)
    # protocol = models.CharField(max_length=50, null=True, blank=True)
    # lastCrawled = models.DateTimeField(null=True, blank=True)
    # lastParsed = models.DateTimeField(null=True, blank=True)
    # crawlId = models.IntegerField(null=True, blank=True)
    # basisOfRecord = models.CharField(max_length=100, null=True, blank=True)
    # occurrenceStatus = models.CharField(max_length=50, null=True, blank=True)
    # scientificName = models.CharField(max_length=255, null=True, blank=True)
    # decimalLatitude = models.FloatField(null=True, blank=True)
    # decimalLongitude = models.FloatField(null=True, blank=True)
    # continent = models.CharField(max_length=100, null=True, blank=True)
    # stateProvince = models.CharField(max_length=100, null=True, blank=True)
    # waterBody = models.CharField(max_length=255, null=True, blank=True)
    # higherGeography = models.CharField(max_length=255, null=True, blank=True)
    # year = models.IntegerField(null=True, blank=True)
    # month = models.IntegerField(null=True, blank=True)
    # day = models.IntegerField(null=True, blank=True)
    # eventDate = models.DateField(null=True, blank=True)
    # startDayOfYear = models.IntegerField(null=True, blank=True)
    # endDayOfYear = models.IntegerField(null=True, blank=True)
    # issues = models.TextField(null=True, blank=True)
    # modified = models.DateTimeField(null=True, blank=True)
    # lastInterpreted = models.DateTimeField(null=True, blank=True)
    # license = models.URLField(null=True, blank=True)
    # isSequenced = models.BooleanField(null=True, blank=True)
    # identifiers = models.JSONField(null=True, blank=True)
    # # media = models.JSONField(null=True, blank=True)
    # relations = models.JSONField(null=True, blank=True)
    # institutionKey = models.CharField(max_length=36, null=True, blank=True)
    # collectionKey = models.CharField(max_length=36, null=True, blank=True)
    # isInCluster = models.BooleanField(null=True, blank=True)
    # recordedBy = models.CharField(max_length=255, null=True, blank=True)
    # preparations = models.TextField(null=True, blank=True)
    # geodeticDatum = models.CharField(max_length=50, null=True, blank=True)
    # verbatimEventDate = models.CharField(max_length=255, null=True, blank=True)
    # islandGroup = models.CharField(max_length=255, null=True, blank=True)
    # island = models.CharField(max_length=255, null=True, blank=True)
    # verbatimLocality = models.CharField(max_length=255, null=True, blank=True)
    # collectionCode = models.CharField(max_length=255, null=True, blank=True)
    # higherClassification = models.TextField(null=True, blank=True)
    # georeferenceSources = models.TextField(null=True, blank=True)
    # publishingOrgKey = models.CharField(max_length=36, null=True, blank=True)
    # datasetKey = models.CharField(max_length=36, null=True, blank=True)
    # taxonKey = models.IntegerField(null=True, blank=True)
    key = models.BigIntegerField(primary_key=True)
    datasetKey = models.CharField(max_length=36, null=True, blank=True)
    publishingOrgKey = models.CharField(max_length=36, null=True, blank=True)
    networkKeys = models.JSONField(blank=True, null=True)  # Using JSONField for list of keys
    installationKey = models.CharField(max_length=36, null=True, blank=True)
    hostingOrganizationKey = models.CharField(max_length=36, null=True, blank=True)
    publishingCountry = models.CharField(max_length=2, null=True, blank=True)
    protocol = models.CharField(max_length=10, null=True, blank=True)
    lastCrawled = models.DateTimeField(null=True, blank=True)
    lastParsed = models.DateTimeField(null=True, blank=True)
    crawlId = models.IntegerField(null=True, blank=True)

    extensions = models.JSONField(blank=True, null=True)  # Store extensions as JSON
    basisOfRecord = models.CharField(max_length=50, null=True, blank=True)
    occurrenceStatus = models.CharField(max_length=20, null=True, blank=True)
    taxonKey = models.IntegerField(null=True, blank=True)
    kingdomKey = models.IntegerField(null=True, blank=True)
    phylumKey = models.IntegerField(null=True, blank=True)
    classKey = models.IntegerField(null=True, blank=True)
    familyKey = models.IntegerField(null=True, blank=True)
    genusKey = models.IntegerField(null=True, blank=True)
    speciesKey = models.IntegerField(null=True, blank=True)
    acceptedTaxonKey = models.IntegerField(null=True, blank=True)
    scientificName = models.CharField(max_length=255, null=True, blank=True)
    acceptedScientificName = models.CharField(max_length=255, null=True, blank=True)
    kingdom = models.CharField(max_length=255, null=True, blank=True)
    phylum = models.CharField(max_length=255, null=True, blank=True)
    family = models.CharField(max_length=255, null=True, blank=True)
    genus = models.CharField(max_length=255, null=True, blank=True)
    species = models.CharField(max_length=255, null=True, blank=True)
    genericName = models.CharField(max_length=255, null=True, blank=True)
    specificEpithet = models.CharField(max_length=255, null=True, blank=True)
    taxonRank = models.CharField(max_length=50, null=True, blank=True)
    taxonomicStatus = models.CharField(max_length=50, null=True, blank=True)
    iucnRedListCategory = models.CharField(max_length=50, null=True, blank=True)
    decimalLatitude = models.FloatField(null=True, blank=True)
    decimalLongitude = models.FloatField(null=True, blank=True)
    continent = models.CharField(max_length=50, null=True, blank=True)
    stateProvince = models.CharField(max_length=255, null=True, blank=True)

    gadm = models.JSONField(blank=True, null=True)  # Store nested structure in JSON
    waterBody = models.CharField(max_length=255, null=True, blank=True)
    higherGeography = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    eventDate = models.DateField(null=True, blank=True)
    startDayOfYear = models.IntegerField(null=True, blank=True)
    endDayOfYear = models.IntegerField(null=True, blank=True)
    issues = models.JSONField(blank=True, null=True)  # List of issues
    modified = models.DateTimeField(null=True, blank=True)
    lastInterpreted = models.DateTimeField(null=True, blank=True)
    license = models.URLField(null=True, blank=True)
    isSequenced = models.BooleanField(default=False)
    identifiers = models.JSONField(blank=True, null=True)  # Store list of identifiers
    media = models.JSONField(blank=True, null=True)  # Store list of media objects
    facts = models.JSONField(blank=True, null=True)  # Store list of facts
    relations = models.JSONField(blank=True, null=True)  # Store relations in JSON
    institutionKey = models.CharField(max_length=255, null=True, blank=True)
    collectionKey = models.CharField(max_length=255, null=True, blank=True)
    isInCluster = models.BooleanField(default=False)
    recordedBy = models.CharField(max_length=255, null=True, blank=True)
    preparations = models.CharField(max_length=255, null=True, blank=True)
    geodeticDatum = models.CharField(max_length=50, null=True, blank=True)
    classField = models.CharField(max_length=255, null=True, blank=True)  # renamed 'class' to 'classField'
    countryCode = models.CharField(max_length=2, null=True, blank=True)
    recordedByIDs = models.JSONField(blank=True, null=True)
    identifiedByIDs = models.JSONField(blank=True, null=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    gbifRegion = models.CharField(max_length=255, null=True, blank=True)
    publishedByGbifRegion = models.CharField(max_length=255, null=True, blank=True)
    identifier = models.CharField(max_length=255, null=True, blank=True)
    institutionID = models.URLField(null=True, blank=True)
    verbatimEventDate = models.CharField(max_length=255, null=True, blank=True)
    island = models.CharField(max_length=255, null=True, blank=True)
    islandGroup = models.CharField(max_length=255, null=True, blank=True)
    verbatimLocality = models.CharField(max_length=255, null=True, blank=True)
    collectionCode = models.CharField(max_length=255, null=True, blank=True)
    gbifID = models.CharField(max_length=255, null=True, blank=True)
    occurrenceID = models.CharField(max_length=255, null=True, blank=True)
    catalogNumber = models.CharField(max_length=255, null=True, blank=True)
    institutionCode = models.CharField(max_length=255, null=True, blank=True)
    collectionID = models.URLField(null=True, blank=True)
    higherClassification = models.CharField(max_length=255, null=True, blank=True)
    georeferenceSources = models.CharField(max_length=255, null=True, blank=True)

    sex = models.CharField(max_length=50, blank=True, null=True)
    lifeStage = models.CharField(max_length=50, blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    typeStatus = models.CharField(max_length=255, blank=True, null=True)
    identifiedBy = models.CharField(max_length=255, blank=True, null=True)
    recordNumber = models.CharField(max_length=255, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    occurrenceRemarks = models.TextField(blank=True, null=True)
    verbatimElevation = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"OccurrenceGBIF - {self.key}"

    class Meta:
        db_table = 'occurrence_gbif'

class CollectionsAppApiOrganization(models.Model):
    publishing_org = models.CharField(primary_key=True, max_length=235)
    organizationid = models.CharField(db_column='organizationID', max_length=255)  # Field name made lowercase.
    organizationname = models.CharField(db_column='organizationName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collections_app_api_organization'


class CollectionsAppApiSpecies(models.Model):
    key = models.CharField(primary_key=True, max_length=235)
    taxonKey = models.CharField(db_column='taxonKey', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collections_app_api_species'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

