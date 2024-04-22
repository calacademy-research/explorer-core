
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accession(models.Model):
    accessionid = models.AutoField(db_column='AccessionID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    accessioncondition = models.CharField(db_column='AccessionCondition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accessionnumber = models.CharField(db_column='AccessionNumber', max_length=60)  # Field name made lowercase.
    dateaccessioned = models.DateField(db_column='DateAccessioned', blank=True, null=True)  # Field name made lowercase.
    dateacknowledged = models.DateField(db_column='DateAcknowledged', blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    totalvalue = models.DecimalField(db_column='TotalValue', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    verbatimdate = models.CharField(db_column='VerbatimDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    divisionid = models.ForeignKey('Division', models.DO_NOTHING, db_column='DivisionID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='accession_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    repositoryagreementid = models.ForeignKey('Repositoryagreement', models.DO_NOTHING, db_column='RepositoryAgreementID', blank=True, null=True)  # Field name made lowercase.
    addressofrecordid = models.ForeignKey('Addressofrecord', models.DO_NOTHING, db_column='AddressOfRecordID', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accession'


class AccessionCopy(models.Model):
    accessionid = models.AutoField(db_column='AccessionID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    accessioncondition = models.CharField(db_column='AccessionCondition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accessionnumber = models.CharField(db_column='AccessionNumber', max_length=60)  # Field name made lowercase.
    dateaccessioned = models.DateField(db_column='DateAccessioned', blank=True, null=True)  # Field name made lowercase.
    dateacknowledged = models.DateField(db_column='DateAcknowledged', blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    number1 = models.FloatField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.FloatField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    totalvalue = models.DecimalField(db_column='TotalValue', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    verbatimdate = models.CharField(db_column='VerbatimDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    divisionid = models.IntegerField(db_column='DivisionID')  # Field name made lowercase.
    createdbyagentid = models.IntegerField(db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.IntegerField(db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    repositoryagreementid = models.IntegerField(db_column='RepositoryAgreementID', blank=True, null=True)  # Field name made lowercase.
    addressofrecordid = models.IntegerField(db_column='AddressOfRecordID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accession_copy'


class Accessionagent(models.Model):
    accessionagentid = models.AutoField(db_column='AccessionAgentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50)  # Field name made lowercase.
    repositoryagreementid = models.ForeignKey('Repositoryagreement', models.DO_NOTHING, db_column='RepositoryAgreementID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='AgentID', related_name='accessionagent_agentid_set')  # Field name made lowercase.
    accessionid = models.ForeignKey(Accession, models.DO_NOTHING, db_column='AccessionID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='accessionagent_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accessionagent'
        unique_together = (('role', 'agentid', 'accessionid'),)


class Accessionattachment(models.Model):
    accessionattachmentid = models.AutoField(db_column='AccessionAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey('Attachment', models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='CreatedByAgentID', related_name='accessionattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    accessionid = models.ForeignKey(Accession, models.DO_NOTHING, db_column='AccessionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accessionattachment'


class Accessionauthorization(models.Model):
    accessionauthorizationid = models.AutoField(db_column='AccessionAuthorizationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='accessionauthorization_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    repositoryagreementid = models.ForeignKey('Repositoryagreement', models.DO_NOTHING, db_column='RepositoryAgreementID', blank=True, null=True)  # Field name made lowercase.
    permitid = models.ForeignKey('Permit', models.DO_NOTHING, db_column='PermitID')  # Field name made lowercase.
    accessionid = models.ForeignKey(Accession, models.DO_NOTHING, db_column='AccessionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accessionauthorization'


class Accessioncitation(models.Model):
    accessioncitationid = models.AutoField(db_column='AccessionCitationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    figurenumber = models.CharField(db_column='FigureNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isfigured = models.TextField(db_column='IsFigured', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pagenumber = models.CharField(db_column='PageNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    accessionid = models.ForeignKey(Accession, models.DO_NOTHING, db_column='AccessionID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='CreatedByAgentID', related_name='accessioncitation_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    referenceworkid = models.ForeignKey('Referencework', models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accessioncitation'


class Address(models.Model):
    addressid = models.AutoField(db_column='AddressID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=400, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=400, blank=True, null=True)  # Field name made lowercase.
    address5 = models.CharField(db_column='Address5', max_length=400, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=64, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=64, blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iscurrent = models.TextField(db_column='IsCurrent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isprimary = models.TextField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isshipping = models.TextField(db_column='IsShipping', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordinal = models.IntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    positionheld = models.CharField(db_column='PositionHeld', max_length=32, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    roomorbuilding = models.CharField(db_column='RoomOrBuilding', max_length=50, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=64, blank=True, null=True)  # Field name made lowercase.
    typeofaddr = models.CharField(db_column='TypeOfAddr', max_length=32, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='AgentID', related_name='address_agentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='CreatedByAgentID', related_name='address_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class Addressofrecord(models.Model):
    addressofrecordid = models.AutoField(db_column='AddressOfRecordID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=64, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=64, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=64, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='AgentID', related_name='addressofrecord_agentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey('Agent', models.DO_NOTHING, db_column='CreatedByAgentID', related_name='addressofrecord_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'addressofrecord'


class Agent(models.Model):
    agentid = models.AutoField(db_column='AgentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    agenttype = models.IntegerField(db_column='AgentType')  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    dateofbirthprecision = models.IntegerField(db_column='DateOfBirthPrecision', blank=True, null=True)  # Field name made lowercase.
    dateofdeath = models.DateField(db_column='DateOfDeath', blank=True, null=True)  # Field name made lowercase.
    dateofdeathprecision = models.IntegerField(db_column='DateOfDeathPrecision', blank=True, null=True)  # Field name made lowercase.
    datetype = models.IntegerField(db_column='DateType', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    initials = models.CharField(db_column='Initials', max_length=8, blank=True, null=True)  # Field name made lowercase.
    interests = models.CharField(db_column='Interests', max_length=255, blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    middleinitial = models.CharField(db_column='MiddleInitial', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    parentorganizationid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentOrganizationID', blank=True, null=True)  # Field name made lowercase.
    institutiontcid = models.ForeignKey('Institution', models.DO_NOTHING, db_column='InstitutionTCID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey('self', models.DO_NOTHING, db_column='CreatedByAgentID', related_name='agent_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    collectiontcid = models.ForeignKey('Collection', models.DO_NOTHING, db_column='CollectionTCID', blank=True, null=True)  # Field name made lowercase.
    collectionccid = models.ForeignKey('Collection', models.DO_NOTHING, db_column='CollectionCCID', related_name='agent_collectionccid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='agent_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    institutionccid = models.ForeignKey('Institution', models.DO_NOTHING, db_column='InstitutionCCID', related_name='agent_institutionccid_set', blank=True, null=True)  # Field name made lowercase.
    specifyuserid = models.ForeignKey('Specifyuser', models.DO_NOTHING, db_column='SpecifyUserID', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.ForeignKey('Division', models.DO_NOTHING, db_column='DivisionID', blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    date2precision = models.IntegerField(db_column='Date2Precision', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    verbatimdate1 = models.CharField(db_column='VerbatimDate1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    verbatimdate2 = models.CharField(db_column='VerbatimDate2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agent'


class Agentattachment(models.Model):
    agentattachmentid = models.AutoField(db_column='AgentAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='agentattachment_agentid_set')  # Field name made lowercase.
    attachmentid = models.ForeignKey('Attachment', models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='agentattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agentattachment'


class Agentgeography(models.Model):
    agentgeographyid = models.AutoField(db_column='AgentGeographyID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=64, blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='agentgeography_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='agentgeography_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    geographyid = models.ForeignKey('Geography', models.DO_NOTHING, db_column='GeographyID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agentgeography'


class Agentidentifier(models.Model):
    agentidentifierid = models.AutoField(db_column='AgentIdentifierID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    date2precision = models.IntegerField(db_column='Date2Precision', blank=True, null=True)  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=2048)  # Field name made lowercase.
    identifiertype = models.CharField(db_column='IdentifierType', max_length=256, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='agentidentifier_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='agentidentifier_agentid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agentidentifier'


class Agentspecialty(models.Model):
    agentspecialtyid = models.AutoField(db_column='AgentSpecialtyID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    specialtyname = models.CharField(db_column='SpecialtyName', max_length=64)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='agentspecialty_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='agentspecialty_agentid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agentspecialty'
        unique_together = (('agentid', 'ordernumber'),)


class Agentvariant(models.Model):
    agentvariantid = models.AutoField(db_column='AgentVariantID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=2, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=2, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vartype = models.IntegerField(db_column='VarType')  # Field name made lowercase.
    variant = models.CharField(db_column='Variant', max_length=2, blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='agentvariant_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='agentvariant_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agentvariant'


class Appraisal(models.Model):
    appraisalid = models.AutoField(db_column='AppraisalID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    appraisaldate = models.DateField(db_column='AppraisalDate')  # Field name made lowercase.
    appraisalnumber = models.CharField(db_column='AppraisalNumber', unique=True, max_length=64)  # Field name made lowercase.
    appraisalvalue = models.DecimalField(db_column='AppraisalValue', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    monetaryunittype = models.CharField(db_column='MonetaryUnitType', max_length=8, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID')  # Field name made lowercase.
    accessionid = models.ForeignKey(Accession, models.DO_NOTHING, db_column='AccessionID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='appraisal_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='appraisal_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appraisal'


class Attachment(models.Model):
    attachmentid = models.AutoField(db_column='AttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    attachmentlocation = models.CharField(db_column='AttachmentLocation', max_length=128, blank=True, null=True)  # Field name made lowercase.
    copyrightdate = models.CharField(db_column='CopyrightDate', max_length=64, blank=True, null=True)  # Field name made lowercase.
    copyrightholder = models.CharField(db_column='CopyrightHolder', max_length=64, blank=True, null=True)  # Field name made lowercase.
    credit = models.CharField(db_column='Credit', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dateimaged = models.CharField(db_column='DateImaged', max_length=64, blank=True, null=True)  # Field name made lowercase.
    filecreateddate = models.DateField(db_column='FileCreatedDate', blank=True, null=True)  # Field name made lowercase.
    license = models.CharField(db_column='License', max_length=64, blank=True, null=True)  # Field name made lowercase.
    mimetype = models.CharField(db_column='MimeType', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    origfilename = models.TextField(db_column='origFilename')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    tableid = models.SmallIntegerField(db_column='TableID', blank=True, null=True)  # Field name made lowercase.
    scopeid = models.IntegerField(db_column='ScopeID', blank=True, null=True)  # Field name made lowercase.
    scopetype = models.IntegerField(db_column='ScopeType', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    visibility = models.IntegerField(db_column='Visibility', blank=True, null=True)  # Field name made lowercase.
    attachmentimageattributeid = models.ForeignKey('Attachmentimageattribute', models.DO_NOTHING, db_column='AttachmentImageAttributeID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='attachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    visibilitysetbyid = models.ForeignKey('Specifyuser', models.DO_NOTHING, db_column='VisibilitySetByID', blank=True, null=True)  # Field name made lowercase.
    ispublic = models.TextField(db_column='IsPublic')  # Field name made lowercase. This field type is a guess.
    creatorid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatorID', related_name='attachment_creatorid_set', blank=True, null=True)  # Field name made lowercase.
    capturedevice = models.CharField(db_column='CaptureDevice', max_length=128, blank=True, null=True)  # Field name made lowercase.
    licenselogourl = models.CharField(db_column='LicenseLogoUrl', max_length=256, blank=True, null=True)  # Field name made lowercase.
    metadatatext = models.CharField(db_column='MetadataText', max_length=256, blank=True, null=True)  # Field name made lowercase.
    subjectorientation = models.CharField(db_column='SubjectOrientation', max_length=64, blank=True, null=True)  # Field name made lowercase.
    subtype = models.CharField(db_column='Subtype', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=64, blank=True, null=True)  # Field name made lowercase.
    attachmentstorageconfig = models.TextField(db_column='AttachmentStorageConfig', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attachment'


class Attachmentimageattribute(models.Model):
    attachmentimageattributeid = models.AutoField(db_column='AttachmentImageAttributeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    creativecommons = models.CharField(db_column='CreativeCommons', max_length=500, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    magnification = models.FloatField(db_column='Magnification', blank=True, null=True)  # Field name made lowercase.
    mbimageid = models.IntegerField(db_column='MBImageID', blank=True, null=True)  # Field name made lowercase.
    resolution = models.FloatField(db_column='Resolution', blank=True, null=True)  # Field name made lowercase.
    timestamplastsend = models.DateTimeField(db_column='TimestampLastSend', blank=True, null=True)  # Field name made lowercase.
    timestamplastupdatecheck = models.DateTimeField(db_column='TimestampLastUpdateCheck', blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='attachmentimageattribute_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    morphbankviewid = models.ForeignKey('Morphbankview', models.DO_NOTHING, db_column='MorphBankViewID', blank=True, null=True)  # Field name made lowercase.
    imagetype = models.CharField(db_column='ImageType', max_length=80, blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    viewdescription = models.CharField(db_column='ViewDescription', max_length=80, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'attachmentimageattribute'


class Attachmentmetadata(models.Model):
    attachmentmetadataid = models.AutoField(db_column='AttachmentMetadataID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=128)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='attachmentmetadata_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attachmentmetadata'


class Attachmenttag(models.Model):
    attachmenttagid = models.AutoField(db_column='AttachmentTagID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=64)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='attachmenttag_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attachmenttag'


class Attributedef(models.Model):
    attributedefid = models.AutoField(db_column='AttributeDefID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    datatype = models.SmallIntegerField(db_column='DataType', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    tabletype = models.SmallIntegerField(db_column='TableType', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    preptypeid = models.ForeignKey('Preptype', models.DO_NOTHING, db_column='PrepTypeID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='attributedef_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey('Discipline', models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attributedef'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class Author(models.Model):
    authorid = models.AutoField(db_column='AuthorID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.SmallIntegerField(db_column='OrderNumber')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    referenceworkid = models.ForeignKey('Referencework', models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='author_agentid_set')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='author_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'author'
        unique_together = (('referenceworkid', 'agentid'),)


class Autonumberingscheme(models.Model):
    autonumberingschemeid = models.AutoField(db_column='AutoNumberingSchemeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    formatname = models.CharField(db_column='FormatName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isnumericonly = models.TextField(db_column='IsNumericOnly')  # Field name made lowercase. This field type is a guess.
    schemeclassname = models.CharField(db_column='SchemeClassName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    schemename = models.CharField(db_column='SchemeName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tablenumber = models.IntegerField(db_column='TableNumber')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='autonumberingscheme_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autonumberingscheme'


class AutonumschColl(models.Model):
    collectionid = models.OneToOneField('Collection', models.DO_NOTHING, db_column='CollectionID', primary_key=True)  # Field name made lowercase. The composite primary key (CollectionID, AutoNumberingSchemeID) found, that is not supported. The first column is selected.
    autonumberingschemeid = models.ForeignKey(Autonumberingscheme, models.DO_NOTHING, db_column='AutoNumberingSchemeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autonumsch_coll'
        unique_together = (('collectionid', 'autonumberingschemeid'),)


class AutonumschDiv(models.Model):
    divisionid = models.OneToOneField('Division', models.DO_NOTHING, db_column='DivisionID', primary_key=True)  # Field name made lowercase. The composite primary key (DivisionID, AutoNumberingSchemeID) found, that is not supported. The first column is selected.
    autonumberingschemeid = models.ForeignKey(Autonumberingscheme, models.DO_NOTHING, db_column='AutoNumberingSchemeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autonumsch_div'
        unique_together = (('divisionid', 'autonumberingschemeid'),)


class AutonumschDsp(models.Model):
    disciplineid = models.OneToOneField('Discipline', models.DO_NOTHING, db_column='DisciplineID', primary_key=True)  # Field name made lowercase. The composite primary key (DisciplineID, AutoNumberingSchemeID) found, that is not supported. The first column is selected.
    autonumberingschemeid = models.ForeignKey(Autonumberingscheme, models.DO_NOTHING, db_column='AutoNumberingSchemeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autonumsch_dsp'
        unique_together = (('disciplineid', 'autonumberingschemeid'),)


class Borrow(models.Model):
    borrowid = models.AutoField(db_column='BorrowID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    currentduedate = models.DateField(db_column='CurrentDueDate', blank=True, null=True)  # Field name made lowercase.
    dateclosed = models.DateField(db_column='DateClosed', blank=True, null=True)  # Field name made lowercase.
    invoicenumber = models.CharField(db_column='InvoiceNumber', max_length=50)  # Field name made lowercase.
    isclosed = models.TextField(db_column='IsClosed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isfinancialresponsibility = models.TextField(db_column='IsFinancialResponsibility', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    originalduedate = models.DateField(db_column='OriginalDueDate', blank=True, null=True)  # Field name made lowercase.
    receiveddate = models.DateField(db_column='ReceivedDate', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='borrow_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    addressofrecordid = models.ForeignKey(Addressofrecord, models.DO_NOTHING, db_column='AddressOfRecordID', blank=True, null=True)  # Field name made lowercase.
    borrowdate = models.DateField(db_column='BorrowDate', blank=True, null=True)  # Field name made lowercase.
    borrowdateprecision = models.IntegerField(db_column='BorrowDatePrecision', blank=True, null=True)  # Field name made lowercase.
    numberofitemsborrowed = models.IntegerField(db_column='NumberOfItemsBorrowed', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'borrow'


class Borrowagent(models.Model):
    borrowagentid = models.AutoField(db_column='BorrowAgentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=32)  # Field name made lowercase.
    borrowid = models.ForeignKey(Borrow, models.DO_NOTHING, db_column='BorrowID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='borrowagent_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='borrowagent_agentid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'borrowagent'
        unique_together = (('role', 'agentid', 'borrowid'),)


class Borrowattachment(models.Model):
    borrowattachmentid = models.AutoField(db_column='BorrowAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='borrowattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    borrowid = models.ForeignKey(Borrow, models.DO_NOTHING, db_column='BorrowID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'borrowattachment'


class Borrowmaterial(models.Model):
    borrowmaterialid = models.AutoField(db_column='BorrowMaterialID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250, blank=True, null=True)  # Field name made lowercase.
    incomments = models.TextField(db_column='InComments', blank=True, null=True)  # Field name made lowercase.
    materialnumber = models.CharField(db_column='MaterialNumber', max_length=50)  # Field name made lowercase.
    outcomments = models.TextField(db_column='OutComments', blank=True, null=True)  # Field name made lowercase.
    quantity = models.SmallIntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    quantityresolved = models.SmallIntegerField(db_column='QuantityResolved', blank=True, null=True)  # Field name made lowercase.
    quantityreturned = models.SmallIntegerField(db_column='QuantityReturned', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='borrowmaterial_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    borrowid = models.ForeignKey(Borrow, models.DO_NOTHING, db_column='BorrowID')  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'borrowmaterial'


class Borrowreturnmaterial(models.Model):
    borrowreturnmaterialid = models.AutoField(db_column='BorrowReturnMaterialID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    quantity = models.SmallIntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    returneddate = models.DateField(db_column='ReturnedDate', blank=True, null=True)  # Field name made lowercase.
    borrowmaterialid = models.ForeignKey(Borrowmaterial, models.DO_NOTHING, db_column='BorrowMaterialID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='borrowreturnmaterial_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    returnedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ReturnedByID', related_name='borrowreturnmaterial_returnedbyid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'borrowreturnmaterial'


class Botmap(models.Model):
    botmapid = models.IntegerField(db_column='botmapId', primary_key=True)  # Field name made lowercase.
    herbarium = models.CharField(db_column='Herbarium', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accession_number = models.CharField(db_column='Accession_number', max_length=64, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    order = models.CharField(db_column='Order', max_length=500, blank=True, null=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=500, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(db_column='Genus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    species = models.CharField(db_column='Species', max_length=500, blank=True, null=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    preparations = models.TextField(db_column='Preparations', blank=True, null=True)  # Field name made lowercase.
    collection_object_attachments = models.TextField(db_column='Collection_Object_Attachments', blank=True, null=True)  # Field name made lowercase.
    collectors = models.TextField(db_column='Collectors', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='Modified_Date', blank=True, null=True)  # Field name made lowercase.
    redact_locality_co = models.TextField(db_column='Redact_Locality_CO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    redact_locality_taxon = models.TextField(db_column='Redact_Locality_Taxon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'botmap'


class Botportal(models.Model):
    botportalid = models.IntegerField(db_column='botportalId', primary_key=True)  # Field name made lowercase.
    accession_number = models.CharField(db_column='Accession_Number', max_length=64, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    order = models.CharField(db_column='Order', max_length=500, blank=True, null=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=500, blank=True, null=True)  # Field name made lowercase.
    herbarium = models.CharField(db_column='Herbarium', max_length=50, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(db_column='Genus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    species = models.CharField(db_column='Species', max_length=500, blank=True, null=True)  # Field name made lowercase.
    scientific_name = models.TextField(db_column='Scientific_name', blank=True, null=True)  # Field name made lowercase.
    type_status = models.CharField(db_column='Type_status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    determiner = models.CharField(db_column='Determiner', max_length=500, blank=True, null=True)  # Field name made lowercase.
    determined_date = models.DateField(db_column='Determined_Date', blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=500, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=500, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=500, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(db_column='County', max_length=500, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=500, blank=True, null=True)  # Field name made lowercase.
    locality = models.TextField(db_column='Locality', blank=True, null=True)  # Field name made lowercase.
    locality_continued = models.TextField(db_column='Locality_continued', blank=True, null=True)  # Field name made lowercase.
    latitude = models.CharField(db_column='Latitude', max_length=20, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length=20, blank=True, null=True)  # Field name made lowercase.
    min_elevation = models.DecimalField(db_column='Min__Elevation', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    max_elevation = models.DecimalField(db_column='Max__Elevation', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    elevation_unit = models.CharField(db_column='Elevation_Unit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verbatim_date = models.CharField(db_column='Verbatim_Date', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collectors = models.TextField(db_column='Collectors', blank=True, null=True)  # Field name made lowercase.
    collector_number = models.CharField(db_column='Collector_Number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_date_year_field = models.IntegerField(db_column='Start_Date_(Year)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    start_date_month_field = models.IntegerField(db_column='Start_Date_(Month)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    start_date_day_field = models.IntegerField(db_column='Start_Date_(Day)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    end_date_year_field = models.IntegerField(db_column='End_Date_(Year)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    end_date_month_field = models.IntegerField(db_column='End_Date_(Month)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    end_date_day_field = models.IntegerField(db_column='End_Date_(Day)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    habitat = models.TextField(db_column='Habitat', blank=True, null=True)  # Field name made lowercase.
    phenology = models.CharField(db_column='Phenology', max_length=50, blank=True, null=True)  # Field name made lowercase.
    preparations = models.TextField(db_column='Preparations', blank=True, null=True)  # Field name made lowercase.
    specimen_description = models.TextField(db_column='Specimen_description', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    timestamp_modified = models.DateTimeField(db_column='Timestamp_Modified', blank=True, null=True)  # Field name made lowercase.
    collection_object_attachments = models.TextField(db_column='Collection_Object_Attachments', blank=True, null=True)  # Field name made lowercase.
    redact_locality_taxon = models.TextField(db_column='Redact_Locality_Taxon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    redact_locality_co = models.TextField(db_column='Redact_Locality_CO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    redact_locality_accepted_taxon = models.TextField(db_column='Redact_Locality_Accepted_Taxon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'botportal'


class BryoImages(models.Model):
    coreid = models.IntegerField()
    identifier = models.CharField(primary_key=True, max_length=255)
    accessuri = models.CharField(db_column='accessURI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumbnailaccessuri = models.CharField(db_column='thumbnailAccessURI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    goodqualityaccessuri = models.CharField(db_column='goodQualityAccessURI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rights = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    creator = models.CharField(max_length=100, blank=True, null=True)
    usageterms = models.CharField(db_column='usageTerms', max_length=100, blank=True, null=True)  # Field name made lowercase.
    webstatement = models.CharField(db_column='webStatement', max_length=255, blank=True, null=True)  # Field name made lowercase.
    caption = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    providermanagedid = models.CharField(db_column='providerManagedID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    metadatadate = models.CharField(db_column='metadataDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(max_length=100, blank=True, null=True)
    associatedspecimenreference = models.CharField(db_column='associatedSpecimenReference', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=100, blank=True, null=True)
    subtype = models.CharField(max_length=100, blank=True, null=True)
    metatdatalanguage = models.CharField(db_column='metatdataLanguage', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bryo_images'


class BryoNobarcode(models.Model):
    collectionobjectid = models.IntegerField(primary_key=True)
    stationfieldnumber = models.CharField(max_length=50, blank=True, null=True)
    recordedby = models.CharField(db_column='recordedBy', max_length=358, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bryo_nobarcode'


class Bryoportal(models.Model):
    id = models.IntegerField(primary_key=True)
    institutioncode = models.CharField(db_column='institutionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    collectioncode = models.CharField(db_column='collectionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ownerinstitutioncode = models.CharField(db_column='ownerInstitutionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    collectionid = models.CharField(db_column='collectionID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    basisofrecord = models.CharField(db_column='basisOfRecord', max_length=100, blank=True, null=True)  # Field name made lowercase.
    occurrenceid = models.CharField(db_column='occurrenceID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    catalognumber = models.CharField(db_column='catalogNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    othercatalognumbers = models.CharField(db_column='otherCatalogNumbers', max_length=100, blank=True, null=True)  # Field name made lowercase.
    higherclassification = models.CharField(db_column='higherClassification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kingdom = models.CharField(max_length=100, blank=True, null=True)
    phylum = models.CharField(max_length=100, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=100, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    scientificname = models.CharField(db_column='scientificName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxonid = models.CharField(db_column='taxonID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scientificnameauthorship = models.CharField(db_column='scientificNameAuthorship', max_length=100, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(max_length=100, blank=True, null=True)
    subgenus = models.CharField(max_length=100, blank=True, null=True)
    specificepithet = models.CharField(db_column='specificEpithet', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimtaxonrank = models.CharField(db_column='verbatimTaxonRank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    infraspecificepithet = models.CharField(db_column='infraspecificEpithet', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxonrank = models.CharField(db_column='taxonRank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identifiedby = models.CharField(db_column='identifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateidentified = models.CharField(db_column='dateIdentified', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationreferences = models.CharField(db_column='identificationReferences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationremarks = models.TextField(db_column='identificationRemarks', blank=True, null=True)  # Field name made lowercase.
    taxonremarks = models.CharField(db_column='taxonRemarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationqualifier = models.CharField(db_column='identificationQualifier', max_length=100, blank=True, null=True)  # Field name made lowercase.
    typestatus = models.CharField(db_column='typeStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordedby = models.CharField(db_column='recordedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    associatedcollectors = models.CharField(db_column='associatedCollectors', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordnumber = models.CharField(db_column='recordNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventdate = models.CharField(db_column='eventDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(max_length=100, blank=True, null=True)
    month = models.CharField(max_length=100, blank=True, null=True)
    day = models.CharField(max_length=100, blank=True, null=True)
    startdayofyear = models.CharField(db_column='startDayOfYear', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enddayofyear = models.CharField(db_column='endDayOfYear', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimeventdate = models.CharField(db_column='verbatimEventDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    occurrenceremarks = models.TextField(db_column='occurrenceRemarks', blank=True, null=True)  # Field name made lowercase.
    habitat = models.TextField(blank=True, null=True)
    substrate = models.CharField(max_length=255, blank=True, null=True)
    verbatimattributes = models.TextField(db_column='verbatimAttributes', blank=True, null=True)  # Field name made lowercase.
    fieldnumber = models.CharField(db_column='fieldNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    informationwithheld = models.CharField(db_column='informationWithheld', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datageneralizations = models.CharField(db_column='dataGeneralizations', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dynamicproperties = models.CharField(db_column='dynamicProperties', max_length=255, blank=True, null=True)  # Field name made lowercase.
    associatedoccurrences = models.CharField(db_column='associatedOccurrences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    associatedsequences = models.CharField(db_column='associatedSequences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    associatedtaxa = models.TextField(db_column='associatedTaxa', blank=True, null=True)  # Field name made lowercase.
    reproductivecondition = models.CharField(db_column='reproductiveCondition', max_length=100, blank=True, null=True)  # Field name made lowercase.
    establishmentmeans = models.CharField(db_column='establishmentMeans', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cultivationstatus = models.CharField(db_column='cultivationStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lifestage = models.CharField(db_column='lifeStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=100, blank=True, null=True)
    individualcount = models.CharField(db_column='individualCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    preparations = models.CharField(max_length=100, blank=True, null=True)
    locationid = models.CharField(db_column='locationID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(max_length=100, blank=True, null=True)
    waterbody = models.CharField(db_column='waterBody', max_length=100, blank=True, null=True)  # Field name made lowercase.
    islandgroup = models.CharField(db_column='islandGroup', max_length=100, blank=True, null=True)  # Field name made lowercase.
    island = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    stateprovince = models.CharField(db_column='stateProvince', max_length=100, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    locationremarks = models.TextField(db_column='locationRemarks', blank=True, null=True)  # Field name made lowercase.
    localitysecurity = models.CharField(db_column='localitySecurity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    localitysecurityreason = models.CharField(db_column='localitySecurityReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    decimallatitude = models.CharField(db_column='decimalLatitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    decimallongitude = models.CharField(db_column='decimalLongitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    geodeticdatum = models.CharField(db_column='geodeticDatum', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinateuncertaintyinmeters = models.CharField(db_column='coordinateUncertaintyInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimcoordinates = models.CharField(db_column='verbatimCoordinates', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferencedby = models.CharField(db_column='georeferencedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferenceprotocol = models.CharField(db_column='georeferenceProtocol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferencesources = models.TextField(db_column='georeferenceSources', blank=True, null=True)  # Field name made lowercase.
    georeferenceverificationstatus = models.CharField(db_column='georeferenceVerificationStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferenceremarks = models.TextField(db_column='georeferenceRemarks', blank=True, null=True)  # Field name made lowercase.
    minimumelevationinmeters = models.CharField(db_column='minimumElevationInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maximumelevationinmeters = models.CharField(db_column='maximumElevationInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    minimumdepthinmeters = models.CharField(db_column='minimumDepthInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maximumdepthinmeters = models.CharField(db_column='maximumDepthInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimdepth = models.CharField(db_column='verbatimDepth', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimelevation = models.CharField(db_column='verbatimElevation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disposition = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    observeruid = models.CharField(db_column='observerUid', max_length=100, blank=True, null=True)  # Field name made lowercase.
    processingstatus = models.CharField(db_column='processingStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duplicatequantity = models.CharField(db_column='duplicateQuantity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    labelproject = models.CharField(db_column='labelProject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordenteredby = models.CharField(db_column='recordEnteredBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateentered = models.CharField(db_column='dateEntered', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datelastmodified = models.CharField(db_column='dateLastModified', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modified = models.CharField(max_length=100, blank=True, null=True)
    rights = models.CharField(max_length=100, blank=True, null=True)
    rightsholder = models.CharField(db_column='rightsHolder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accessrights = models.CharField(db_column='accessRights', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sourceprimarykey_dbpk = models.CharField(db_column='sourcePrimaryKey-dbpk', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collid = models.CharField(db_column='collID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='recordID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    references = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bryoportal'


class Cch2Bryophyte(models.Model):
    id = models.IntegerField(primary_key=True)
    institutioncode = models.CharField(db_column='institutionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    collectioncode = models.CharField(db_column='collectionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ownerinstitutioncode = models.CharField(db_column='ownerInstitutionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    collectionid = models.CharField(db_column='collectionID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    basisofrecord = models.CharField(db_column='basisOfRecord', max_length=100, blank=True, null=True)  # Field name made lowercase.
    occurrenceid = models.CharField(db_column='occurrenceID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    catalognumber = models.CharField(db_column='catalogNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    othercatalognumbers = models.CharField(db_column='otherCatalogNumbers', max_length=100, blank=True, null=True)  # Field name made lowercase.
    higherclassification = models.CharField(db_column='higherClassification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kingdom = models.CharField(max_length=100, blank=True, null=True)
    phylum = models.CharField(max_length=100, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=100, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    scientificname = models.CharField(db_column='scientificName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxonid = models.CharField(db_column='taxonID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scientificnameauthorship = models.CharField(db_column='scientificNameAuthorship', max_length=100, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(max_length=100, blank=True, null=True)
    subgenus = models.CharField(max_length=100, blank=True, null=True)
    specificepithet = models.CharField(db_column='specificEpithet', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimtaxonrank = models.CharField(db_column='verbatimTaxonRank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    infraspecificepithet = models.CharField(db_column='infraspecificEpithet', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxonrank = models.CharField(db_column='taxonRank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identifiedby = models.CharField(db_column='identifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateidentified = models.CharField(db_column='dateIdentified', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationreferences = models.CharField(db_column='identificationReferences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationremarks = models.TextField(db_column='identificationRemarks', blank=True, null=True)  # Field name made lowercase.
    taxonremarks = models.CharField(db_column='taxonRemarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationqualifier = models.CharField(db_column='identificationQualifier', max_length=100, blank=True, null=True)  # Field name made lowercase.
    typestatus = models.CharField(db_column='typeStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordedby = models.CharField(db_column='recordedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    associatedcollectors = models.CharField(db_column='associatedCollectors', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordnumber = models.CharField(db_column='recordNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventdate = models.CharField(db_column='eventDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventdate2 = models.CharField(db_column='eventDate2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(max_length=100, blank=True, null=True)
    month = models.CharField(max_length=100, blank=True, null=True)
    day = models.CharField(max_length=100, blank=True, null=True)
    startdayofyear = models.CharField(db_column='startDayOfYear', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enddayofyear = models.CharField(db_column='endDayOfYear', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimeventdate = models.CharField(db_column='verbatimEventDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    occurrenceremarks = models.TextField(db_column='occurrenceRemarks', blank=True, null=True)  # Field name made lowercase.
    habitat = models.TextField(blank=True, null=True)
    substrate = models.CharField(max_length=255, blank=True, null=True)
    verbatimattributes = models.TextField(db_column='verbatimAttributes', blank=True, null=True)  # Field name made lowercase.
    fieldnumber = models.CharField(db_column='fieldNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    informationwithheld = models.CharField(db_column='informationWithheld', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datageneralizations = models.CharField(db_column='dataGeneralizations', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dynamicproperties = models.CharField(db_column='dynamicProperties', max_length=255, blank=True, null=True)  # Field name made lowercase.
    associatedoccurrences = models.CharField(db_column='associatedOccurrences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    associatedsequences = models.CharField(db_column='associatedSequences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    associatedtaxa = models.TextField(db_column='associatedTaxa', blank=True, null=True)  # Field name made lowercase.
    reproductivecondition = models.CharField(db_column='reproductiveCondition', max_length=100, blank=True, null=True)  # Field name made lowercase.
    establishmentmeans = models.CharField(db_column='establishmentMeans', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cultivationstatus = models.CharField(db_column='cultivationStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lifestage = models.CharField(db_column='lifeStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=100, blank=True, null=True)
    individualcount = models.CharField(db_column='individualCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    preparations = models.CharField(max_length=100, blank=True, null=True)
    locationid = models.CharField(db_column='locationID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(max_length=100, blank=True, null=True)
    waterbody = models.CharField(db_column='waterBody', max_length=100, blank=True, null=True)  # Field name made lowercase.
    islandgroup = models.CharField(db_column='islandGroup', max_length=100, blank=True, null=True)  # Field name made lowercase.
    island = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    stateprovince = models.CharField(db_column='stateProvince', max_length=100, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    locationremarks = models.TextField(db_column='locationRemarks', blank=True, null=True)  # Field name made lowercase.
    localitysecurity = models.CharField(db_column='localitySecurity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    localitysecurityreason = models.CharField(db_column='localitySecurityReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    decimallatitude = models.CharField(db_column='decimalLatitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    decimallongitude = models.CharField(db_column='decimalLongitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    geodeticdatum = models.CharField(db_column='geodeticDatum', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinateuncertaintyinmeters = models.CharField(db_column='coordinateUncertaintyInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimcoordinates = models.CharField(db_column='verbatimCoordinates', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferencedby = models.CharField(db_column='georeferencedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferenceprotocol = models.CharField(db_column='georeferenceProtocol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferencesources = models.TextField(db_column='georeferenceSources', blank=True, null=True)  # Field name made lowercase.
    georeferenceverificationstatus = models.CharField(db_column='georeferenceVerificationStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferenceremarks = models.TextField(db_column='georeferenceRemarks', blank=True, null=True)  # Field name made lowercase.
    minimumelevationinmeters = models.CharField(db_column='minimumElevationInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maximumelevationinmeters = models.CharField(db_column='maximumElevationInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    minimumdepthinmeters = models.CharField(db_column='minimumDepthInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maximumdepthinmeters = models.CharField(db_column='maximumDepthInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimdepth = models.CharField(db_column='verbatimDepth', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimelevation = models.CharField(db_column='verbatimElevation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disposition = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    observeruid = models.CharField(db_column='observerUid', max_length=100, blank=True, null=True)  # Field name made lowercase.
    processingstatus = models.CharField(db_column='processingStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duplicatequantity = models.CharField(db_column='duplicateQuantity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    labelproject = models.CharField(db_column='labelProject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordenteredby = models.CharField(db_column='recordEnteredBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateentered = models.CharField(db_column='dateEntered', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datelastmodified = models.CharField(db_column='dateLastModified', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modified = models.CharField(max_length=100, blank=True, null=True)
    rights = models.CharField(max_length=100, blank=True, null=True)
    rightsholder = models.CharField(db_column='rightsHolder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accessrights = models.CharField(db_column='accessRights', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sourceprimarykey_dbpk = models.CharField(db_column='sourcePrimaryKey-dbpk', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collid = models.CharField(db_column='collID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='recordID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    references = models.TextField(blank=True, null=True)
    catnum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cch2_bryophyte'


class Cch2Extra(models.Model):
    id = models.IntegerField(primary_key=True)
    institutioncode = models.CharField(db_column='institutionCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    collectioncode = models.CharField(db_column='collectionCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ownerinstitutioncode = models.CharField(db_column='ownerInstitutionCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    collectionid = models.CharField(db_column='collectionID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    basisofrecord = models.CharField(db_column='basisOfRecord', max_length=32, blank=True, null=True)  # Field name made lowercase.
    occurrenceid = models.CharField(db_column='occurrenceID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    catalognumber = models.CharField(db_column='catalogNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    othercatalognumbers = models.CharField(db_column='otherCatalogNumbers', max_length=255, blank=True, null=True)  # Field name made lowercase.
    higherclassification = models.CharField(db_column='higherClassification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kingdom = models.CharField(max_length=100, blank=True, null=True)
    phylum = models.CharField(max_length=100, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    scientificname = models.CharField(db_column='scientificName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxonid = models.CharField(db_column='taxonID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scientificnameauthorship = models.CharField(db_column='scientificNameAuthorship', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(max_length=255, blank=True, null=True)
    subgenus = models.CharField(max_length=100, blank=True, null=True)
    specificepithet = models.CharField(db_column='specificEpithet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    verbatimtaxonrank = models.CharField(db_column='verbatimTaxonRank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    infraspecificepithet = models.CharField(db_column='infraspecificEpithet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxonrank = models.CharField(db_column='taxonRank', max_length=32, blank=True, null=True)  # Field name made lowercase.
    identifiedby = models.CharField(db_column='identifiedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateidentified = models.CharField(db_column='dateIdentified', max_length=45, blank=True, null=True)  # Field name made lowercase.
    identificationreferences = models.TextField(db_column='identificationReferences', blank=True, null=True)  # Field name made lowercase.
    identificationremarks = models.CharField(db_column='identificationRemarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxonremarks = models.CharField(db_column='taxonRemarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationqualifier = models.CharField(db_column='identificationQualifier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    typestatus = models.CharField(db_column='typeStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recordedby = models.CharField(db_column='recordedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    associatedcollectors = models.CharField(db_column='associatedCollectors', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recordnumber = models.CharField(db_column='recordNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    eventdate = models.DateField(db_column='eventDate', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    startdayofyear = models.IntegerField(db_column='startDayOfYear', blank=True, null=True)  # Field name made lowercase.
    enddayofyear = models.IntegerField(db_column='endDayOfYear', blank=True, null=True)  # Field name made lowercase.
    verbatimeventdate = models.CharField(db_column='verbatimEventDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    occurrenceremarks = models.TextField(db_column='occurrenceRemarks', blank=True, null=True)  # Field name made lowercase.
    habitat = models.TextField(blank=True, null=True)
    substrate = models.CharField(max_length=500, blank=True, null=True)
    verbatimattributes = models.TextField(db_column='verbatimAttributes', blank=True, null=True)  # Field name made lowercase.
    fieldnumber = models.CharField(db_column='fieldNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    informationwithheld = models.CharField(db_column='informationWithheld', max_length=250, blank=True, null=True)  # Field name made lowercase.
    datageneralizations = models.CharField(db_column='dataGeneralizations', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dynamicproperties = models.TextField(db_column='dynamicProperties', blank=True, null=True)  # Field name made lowercase.
    associatedoccurrences = models.TextField(db_column='associatedOccurrences', blank=True, null=True)  # Field name made lowercase.
    associatedsequences = models.CharField(db_column='associatedSequences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    associatedtaxa = models.TextField(db_column='associatedTaxa', blank=True, null=True)  # Field name made lowercase.
    reproductivecondition = models.CharField(db_column='reproductiveCondition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    establishmentmeans = models.CharField(db_column='establishmentMeans', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cultivationstatus = models.IntegerField(db_column='cultivationStatus', blank=True, null=True)  # Field name made lowercase.
    lifestage = models.CharField(db_column='lifeStage', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=45, blank=True, null=True)
    individualcount = models.CharField(db_column='individualCount', max_length=45, blank=True, null=True)  # Field name made lowercase.
    preparations = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    stateprovince = models.CharField(db_column='stateProvince', max_length=255, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(max_length=255, blank=True, null=True)
    municipality = models.CharField(max_length=255, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    locationremarks = models.TextField(db_column='locationRemarks', blank=True, null=True)  # Field name made lowercase.
    localitysecurity = models.IntegerField(db_column='localitySecurity', blank=True, null=True)  # Field name made lowercase.
    localitysecurityreason = models.CharField(db_column='localitySecurityReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    decimallatitude = models.FloatField(db_column='decimalLatitude', blank=True, null=True)  # Field name made lowercase.
    decimallongitude = models.FloatField(db_column='decimalLongitude', blank=True, null=True)  # Field name made lowercase.
    geodeticdatum = models.CharField(db_column='geodeticDatum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coordinateuncertaintyinmeters = models.IntegerField(db_column='coordinateUncertaintyInMeters', blank=True, null=True)  # Field name made lowercase.
    verbatimcoordinates = models.CharField(db_column='verbatimCoordinates', max_length=255, blank=True, null=True)  # Field name made lowercase.
    georeferencedby = models.CharField(db_column='georeferencedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    georeferenceprotocol = models.CharField(db_column='georeferenceProtocol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    georeferencesources = models.CharField(db_column='georeferenceSources', max_length=255, blank=True, null=True)  # Field name made lowercase.
    georeferenceverificationstatus = models.CharField(db_column='georeferenceVerificationStatus', max_length=32, blank=True, null=True)  # Field name made lowercase.
    georeferenceremarks = models.CharField(db_column='georeferenceRemarks', max_length=500, blank=True, null=True)  # Field name made lowercase.
    minimumelevationinmeters = models.IntegerField(db_column='minimumElevationInMeters', blank=True, null=True)  # Field name made lowercase.
    maximumelevationinmeters = models.IntegerField(db_column='maximumElevationInMeters', blank=True, null=True)  # Field name made lowercase.
    minimumdepthinmeters = models.IntegerField(db_column='minimumDepthInMeters', blank=True, null=True)  # Field name made lowercase.
    maximumdepthinmeters = models.IntegerField(db_column='maximumDepthInMeters', blank=True, null=True)  # Field name made lowercase.
    verbatimdepth = models.CharField(db_column='verbatimDepth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verbatimelevation = models.CharField(db_column='verbatimElevation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disposition = models.CharField(max_length=250, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    observeruid = models.CharField(db_column='observerUid', max_length=100, blank=True, null=True)  # Field name made lowercase.
    processingstatus = models.CharField(db_column='processingStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    duplicatequantity = models.IntegerField(db_column='duplicateQuantity', blank=True, null=True)  # Field name made lowercase.
    labelproject = models.CharField(db_column='labelProject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordenteredby = models.CharField(db_column='recordEnteredBy', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dateentered = models.DateTimeField(db_column='dateEntered', blank=True, null=True)  # Field name made lowercase.
    datelastmodified = models.DateTimeField(db_column='dateLastModified')  # Field name made lowercase.
    modified = models.CharField(max_length=100, blank=True, null=True)
    rights = models.CharField(max_length=100, blank=True, null=True)
    rightsholder = models.CharField(db_column='rightsHolder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accessrights = models.CharField(db_column='accessRights', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sourceprimarykey_dbpk = models.CharField(db_column='sourcePrimaryKey-dbpk', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collid = models.CharField(db_column='collID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='recordID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    references = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cch2_extra'


class Cch2Images(models.Model):
    coreid = models.IntegerField()
    identifier = models.CharField(max_length=255)
    accessuri = models.CharField(db_column='accessURI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumbnailaccessuri = models.CharField(db_column='thumbnailAccessURI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    goodqualityaccessuri = models.CharField(db_column='goodQualityAccessURI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rights = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    creator = models.CharField(max_length=100, blank=True, null=True)
    usageterms = models.CharField(db_column='usageTerms', max_length=100, blank=True, null=True)  # Field name made lowercase.
    webstatement = models.CharField(db_column='webStatement', max_length=255, blank=True, null=True)  # Field name made lowercase.
    caption = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    providermanagedid = models.CharField(db_column='providerManagedID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    metadatadate = models.CharField(db_column='metadataDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(max_length=100, blank=True, null=True)
    associatedspecimenreference = models.CharField(db_column='associatedSpecimenReference', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=100, blank=True, null=True)
    subtype = models.CharField(max_length=100, blank=True, null=True)
    metatdatalanguage = models.CharField(db_column='metatdataLanguage', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cch2_images'


class Cch2Nobarcode(models.Model):
    collectionobjectid = models.IntegerField(primary_key=True)
    stationfieldnumber = models.CharField(max_length=50, blank=True, null=True)
    recordedby = models.CharField(db_column='recordedBy', max_length=358, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cch2_nobarcode'


class Cch2NotInSpecify(models.Model):
    institutioncode = models.CharField(db_column='institutionCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    collectioncode = models.CharField(db_column='collectionCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ownerinstitutioncode = models.CharField(db_column='ownerInstitutionCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    collectionid = models.CharField(db_column='collectionID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    basisofrecord = models.CharField(db_column='basisOfRecord', max_length=32, blank=True, null=True)  # Field name made lowercase.
    occurrenceid = models.CharField(db_column='occurrenceID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    catalognumber = models.CharField(db_column='catalogNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    othercatalognumbers = models.CharField(db_column='otherCatalogNumbers', max_length=255, blank=True, null=True)  # Field name made lowercase.
    higherclassification = models.CharField(db_column='higherClassification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kingdom = models.CharField(max_length=100, blank=True, null=True)
    phylum = models.CharField(max_length=100, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=255, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    scientificname = models.CharField(db_column='scientificName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxonid = models.CharField(db_column='taxonID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scientificnameauthorship = models.CharField(db_column='scientificNameAuthorship', max_length=255, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(max_length=255, blank=True, null=True)
    subgenus = models.CharField(max_length=100, blank=True, null=True)
    specificepithet = models.CharField(db_column='specificEpithet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    verbatimtaxonrank = models.CharField(db_column='verbatimTaxonRank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    infraspecificepithet = models.CharField(db_column='infraspecificEpithet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxonrank = models.CharField(db_column='taxonRank', max_length=32, blank=True, null=True)  # Field name made lowercase.
    identifiedby = models.CharField(db_column='identifiedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateidentified = models.CharField(db_column='dateIdentified', max_length=45, blank=True, null=True)  # Field name made lowercase.
    identificationreferences = models.TextField(db_column='identificationReferences', blank=True, null=True)  # Field name made lowercase.
    identificationremarks = models.CharField(db_column='identificationRemarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxonremarks = models.CharField(db_column='taxonRemarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationqualifier = models.CharField(db_column='identificationQualifier', max_length=255, blank=True, null=True)  # Field name made lowercase.
    typestatus = models.CharField(db_column='typeStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recordedby = models.CharField(db_column='recordedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    associatedcollectors = models.CharField(db_column='associatedCollectors', max_length=255, blank=True, null=True)  # Field name made lowercase.
    recordnumber = models.CharField(db_column='recordNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    eventdate = models.DateField(db_column='eventDate', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    startdayofyear = models.IntegerField(db_column='startDayOfYear', blank=True, null=True)  # Field name made lowercase.
    enddayofyear = models.IntegerField(db_column='endDayOfYear', blank=True, null=True)  # Field name made lowercase.
    verbatimeventdate = models.CharField(db_column='verbatimEventDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    occurrenceremarks = models.TextField(db_column='occurrenceRemarks', blank=True, null=True)  # Field name made lowercase.
    habitat = models.TextField(blank=True, null=True)
    substrate = models.CharField(max_length=500, blank=True, null=True)
    verbatimattributes = models.TextField(db_column='verbatimAttributes', blank=True, null=True)  # Field name made lowercase.
    fieldnumber = models.CharField(db_column='fieldNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=150, blank=True, null=True)  # Field name made lowercase.
    informationwithheld = models.CharField(db_column='informationWithheld', max_length=250, blank=True, null=True)  # Field name made lowercase.
    datageneralizations = models.CharField(db_column='dataGeneralizations', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dynamicproperties = models.TextField(db_column='dynamicProperties', blank=True, null=True)  # Field name made lowercase.
    associatedoccurrences = models.TextField(db_column='associatedOccurrences', blank=True, null=True)  # Field name made lowercase.
    associatedsequences = models.CharField(db_column='associatedSequences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    associatedtaxa = models.TextField(db_column='associatedTaxa', blank=True, null=True)  # Field name made lowercase.
    reproductivecondition = models.CharField(db_column='reproductiveCondition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    establishmentmeans = models.CharField(db_column='establishmentMeans', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cultivationstatus = models.IntegerField(db_column='cultivationStatus', blank=True, null=True)  # Field name made lowercase.
    lifestage = models.CharField(db_column='lifeStage', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=45, blank=True, null=True)
    individualcount = models.CharField(db_column='individualCount', max_length=45, blank=True, null=True)  # Field name made lowercase.
    preparations = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    stateprovince = models.CharField(db_column='stateProvince', max_length=255, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(max_length=255, blank=True, null=True)
    municipality = models.CharField(max_length=255, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    locationremarks = models.TextField(db_column='locationRemarks', blank=True, null=True)  # Field name made lowercase.
    localitysecurity = models.IntegerField(db_column='localitySecurity', blank=True, null=True)  # Field name made lowercase.
    localitysecurityreason = models.CharField(db_column='localitySecurityReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    decimallatitude = models.FloatField(db_column='decimalLatitude', blank=True, null=True)  # Field name made lowercase.
    decimallongitude = models.FloatField(db_column='decimalLongitude', blank=True, null=True)  # Field name made lowercase.
    geodeticdatum = models.CharField(db_column='geodeticDatum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coordinateuncertaintyinmeters = models.IntegerField(db_column='coordinateUncertaintyInMeters', blank=True, null=True)  # Field name made lowercase.
    verbatimcoordinates = models.CharField(db_column='verbatimCoordinates', max_length=255, blank=True, null=True)  # Field name made lowercase.
    georeferencedby = models.CharField(db_column='georeferencedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    georeferenceprotocol = models.CharField(db_column='georeferenceProtocol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    georeferencesources = models.CharField(db_column='georeferenceSources', max_length=255, blank=True, null=True)  # Field name made lowercase.
    georeferenceverificationstatus = models.CharField(db_column='georeferenceVerificationStatus', max_length=32, blank=True, null=True)  # Field name made lowercase.
    georeferenceremarks = models.CharField(db_column='georeferenceRemarks', max_length=500, blank=True, null=True)  # Field name made lowercase.
    minimumelevationinmeters = models.IntegerField(db_column='minimumElevationInMeters', blank=True, null=True)  # Field name made lowercase.
    maximumelevationinmeters = models.IntegerField(db_column='maximumElevationInMeters', blank=True, null=True)  # Field name made lowercase.
    minimumdepthinmeters = models.IntegerField(db_column='minimumDepthInMeters', blank=True, null=True)  # Field name made lowercase.
    maximumdepthinmeters = models.IntegerField(db_column='maximumDepthInMeters', blank=True, null=True)  # Field name made lowercase.
    verbatimdepth = models.CharField(db_column='verbatimDepth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verbatimelevation = models.CharField(db_column='verbatimElevation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disposition = models.CharField(max_length=250, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    observeruid = models.CharField(db_column='observerUid', max_length=100, blank=True, null=True)  # Field name made lowercase.
    processingstatus = models.CharField(db_column='processingStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    duplicatequantity = models.IntegerField(db_column='duplicateQuantity', blank=True, null=True)  # Field name made lowercase.
    labelproject = models.CharField(db_column='labelProject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordenteredby = models.CharField(db_column='recordEnteredBy', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dateentered = models.DateTimeField(db_column='dateEntered', blank=True, null=True)  # Field name made lowercase.
    datelastmodified = models.DateTimeField(db_column='dateLastModified')  # Field name made lowercase.
    modified = models.CharField(max_length=100, blank=True, null=True)
    rights = models.CharField(max_length=100, blank=True, null=True)
    rightsholder = models.CharField(db_column='rightsHolder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accessrights = models.CharField(db_column='accessRights', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sourceprimarykey_dbpk = models.CharField(db_column='sourcePrimaryKey-dbpk', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collid = models.CharField(db_column='collID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='recordID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    references = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cch2_not_in_specify'


class Collectingevent(models.Model):
    collectingeventid = models.AutoField(db_column='CollectingEventID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    enddateprecision = models.IntegerField(db_column='EndDatePrecision', blank=True, null=True)  # Field name made lowercase.
    enddateverbatim = models.CharField(db_column='EndDateVerbatim', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endtime = models.SmallIntegerField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    startdateprecision = models.IntegerField(db_column='StartDatePrecision', blank=True, null=True)  # Field name made lowercase.
    startdateverbatim = models.CharField(db_column='StartDateVerbatim', max_length=50, blank=True, null=True)  # Field name made lowercase.
    starttime = models.SmallIntegerField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    stationfieldnumber = models.CharField(db_column='StationFieldNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verbatimdate = models.CharField(db_column='VerbatimDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verbatimlocality = models.TextField(db_column='VerbatimLocality', blank=True, null=True)  # Field name made lowercase.
    visibility = models.IntegerField(db_column='Visibility', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    localityid = models.ForeignKey('Locality', models.DO_NOTHING, db_column='LocalityID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='collectingevent_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey('Discipline', models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    visibilitysetbyid = models.ForeignKey('Specifyuser', models.DO_NOTHING, db_column='VisibilitySetByID', blank=True, null=True)  # Field name made lowercase.
    collectingtripid = models.ForeignKey('Collectingtrip', models.DO_NOTHING, db_column='CollectingTripID', blank=True, null=True)  # Field name made lowercase.
    collectingeventattributeid = models.ForeignKey('Collectingeventattribute', models.DO_NOTHING, db_column='CollectingEventAttributeID', blank=True, null=True)  # Field name made lowercase.
    sgrstatus = models.IntegerField(db_column='SGRStatus', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    reservedinteger3 = models.IntegerField(db_column='ReservedInteger3', blank=True, null=True)  # Field name made lowercase.
    reservedinteger4 = models.IntegerField(db_column='ReservedInteger4', blank=True, null=True)  # Field name made lowercase.
    reservedtext1 = models.CharField(db_column='ReservedText1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    reservedtext2 = models.CharField(db_column='ReservedText2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    paleocontextid = models.ForeignKey('Paleocontext', models.DO_NOTHING, db_column='PaleoContextID', blank=True, null=True)  # Field name made lowercase.
    stationfieldnumbermodifier1 = models.CharField(db_column='StationFieldNumberModifier1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stationfieldnumbermodifier2 = models.CharField(db_column='StationFieldNumberModifier2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stationfieldnumbermodifier3 = models.CharField(db_column='StationFieldNumberModifier3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    text6 = models.TextField(db_column='Text6', blank=True, null=True)  # Field name made lowercase.
    text7 = models.TextField(db_column='Text7', blank=True, null=True)  # Field name made lowercase.
    text8 = models.TextField(db_column='Text8', blank=True, null=True)  # Field name made lowercase.
    uniqueidentifier = models.CharField(db_column='UniqueIdentifier', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingevent'
        unique_together = (('disciplineid', 'uniqueidentifier'),)


class CollectingeventDupes(models.Model):
    collectingeventid = models.AutoField(db_column='CollectingEventID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    enddateprecision = models.IntegerField(db_column='EndDatePrecision', blank=True, null=True)  # Field name made lowercase.
    enddateverbatim = models.CharField(db_column='EndDateVerbatim', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endtime = models.SmallIntegerField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    startdateprecision = models.IntegerField(db_column='StartDatePrecision', blank=True, null=True)  # Field name made lowercase.
    startdateverbatim = models.CharField(db_column='StartDateVerbatim', max_length=50, blank=True, null=True)  # Field name made lowercase.
    starttime = models.SmallIntegerField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    stationfieldnumber = models.CharField(db_column='StationFieldNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verbatimdate = models.CharField(db_column='VerbatimDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verbatimlocality = models.TextField(db_column='VerbatimLocality', blank=True, null=True)  # Field name made lowercase.
    visibility = models.IntegerField(db_column='Visibility', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.IntegerField(db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    localityid = models.IntegerField(db_column='LocalityID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.IntegerField(db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.IntegerField(db_column='DisciplineID')  # Field name made lowercase.
    visibilitysetbyid = models.IntegerField(db_column='VisibilitySetByID', blank=True, null=True)  # Field name made lowercase.
    collectingtripid = models.IntegerField(db_column='CollectingTripID', blank=True, null=True)  # Field name made lowercase.
    collectingeventattributeid = models.IntegerField(db_column='CollectingEventAttributeID', blank=True, null=True)  # Field name made lowercase.
    sgrstatus = models.IntegerField(db_column='SGRStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingevent_dupes'


class Collectingeventattachment(models.Model):
    collectingeventattachmentid = models.AutoField(db_column='CollectingEventAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    collectingeventid = models.ForeignKey(Collectingevent, models.DO_NOTHING, db_column='CollectingEventID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='collectingeventattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingeventattachment'


class Collectingeventattr(models.Model):
    attrid = models.AutoField(db_column='AttrID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    doublevalue = models.FloatField(db_column='DoubleValue', blank=True, null=True)  # Field name made lowercase.
    strvalue = models.CharField(db_column='StrValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectingeventid = models.ForeignKey(Collectingevent, models.DO_NOTHING, db_column='CollectingEventID')  # Field name made lowercase.
    attributedefid = models.ForeignKey(Attributedef, models.DO_NOTHING, db_column='AttributeDefID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='collectingeventattr_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingeventattr'


class Collectingeventattribute(models.Model):
    collectingeventattributeid = models.AutoField(db_column='CollectingEventAttributeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number10 = models.DecimalField(db_column='Number10', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number11 = models.DecimalField(db_column='Number11', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number12 = models.DecimalField(db_column='Number12', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number13 = models.DecimalField(db_column='Number13', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number6 = models.DecimalField(db_column='Number6', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number7 = models.DecimalField(db_column='Number7', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number8 = models.DecimalField(db_column='Number8', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number9 = models.DecimalField(db_column='Number9', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text10 = models.TextField(db_column='Text10', blank=True, null=True)  # Field name made lowercase.
    text11 = models.TextField(db_column='Text11', blank=True, null=True)  # Field name made lowercase.
    text12 = models.TextField(db_column='Text12', blank=True, null=True)  # Field name made lowercase.
    text13 = models.TextField(db_column='Text13', blank=True, null=True)  # Field name made lowercase.
    text14 = models.TextField(db_column='Text14', blank=True, null=True)  # Field name made lowercase.
    text15 = models.TextField(db_column='Text15', blank=True, null=True)  # Field name made lowercase.
    text16 = models.TextField(db_column='Text16', blank=True, null=True)  # Field name made lowercase.
    text17 = models.TextField(db_column='Text17', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    text6 = models.TextField(db_column='Text6', blank=True, null=True)  # Field name made lowercase.
    text7 = models.TextField(db_column='Text7', blank=True, null=True)  # Field name made lowercase.
    text8 = models.TextField(db_column='Text8', blank=True, null=True)  # Field name made lowercase.
    text9 = models.TextField(db_column='Text9', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey('Discipline', models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collectingeventattribute_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    hosttaxonid = models.ForeignKey('Taxon', models.DO_NOTHING, db_column='HostTaxonID', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer10 = models.IntegerField(db_column='Integer10', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.IntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.IntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    integer6 = models.IntegerField(db_column='Integer6', blank=True, null=True)  # Field name made lowercase.
    integer7 = models.IntegerField(db_column='Integer7', blank=True, null=True)  # Field name made lowercase.
    integer8 = models.IntegerField(db_column='Integer8', blank=True, null=True)  # Field name made lowercase.
    integer9 = models.IntegerField(db_column='Integer9', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingeventattribute'


class Collectingeventauthorization(models.Model):
    collectingeventauthorizationid = models.AutoField(db_column='CollectingEventAuthorizationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    permitid = models.ForeignKey('Permit', models.DO_NOTHING, db_column='PermitID')  # Field name made lowercase.
    collectingeventid = models.ForeignKey(Collectingevent, models.DO_NOTHING, db_column='CollectingEventID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='collectingeventauthorization_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingeventauthorization'


class Collectingtrip(models.Model):
    collectingtripid = models.AutoField(db_column='CollectingTripID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectingtripname = models.CharField(db_column='Collectingtripname', max_length=400, blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    enddateverbatim = models.CharField(db_column='EndDateVerbatim', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endtime = models.SmallIntegerField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    sponsor = models.CharField(db_column='Sponsor', max_length=64, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    startdateverbatim = models.CharField(db_column='StartDateVerbatim', max_length=50, blank=True, null=True)  # Field name made lowercase.
    starttime = models.SmallIntegerField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey('Discipline', models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='collectingtrip_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    enddateprecision = models.IntegerField(db_column='EndDatePrecision', blank=True, null=True)  # Field name made lowercase.
    number1 = models.IntegerField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.IntegerField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    startdateprecision = models.IntegerField(db_column='StartDatePrecision', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=64, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cruise = models.CharField(db_column='Cruise', max_length=250, blank=True, null=True)  # Field name made lowercase.
    expedition = models.CharField(db_column='Expedition', max_length=250, blank=True, null=True)  # Field name made lowercase.
    vessel = models.CharField(db_column='Vessel', max_length=250, blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    date2precision = models.IntegerField(db_column='Date2Precision', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    text6 = models.TextField(db_column='Text6', blank=True, null=True)  # Field name made lowercase.
    text7 = models.TextField(db_column='Text7', blank=True, null=True)  # Field name made lowercase.
    text8 = models.TextField(db_column='Text8', blank=True, null=True)  # Field name made lowercase.
    text9 = models.TextField(db_column='Text9', blank=True, null=True)  # Field name made lowercase.
    agent1id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent1ID', related_name='collectingtrip_agent1id_set', blank=True, null=True)  # Field name made lowercase.
    collectingtripattributeid = models.ForeignKey('Collectingtripattribute', models.DO_NOTHING, db_column='CollectingTripAttributeID', blank=True, null=True)  # Field name made lowercase.
    agent2id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent2ID', related_name='collectingtrip_agent2id_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingtrip'


class Collectingtripattachment(models.Model):
    collectingtripattachmentid = models.AutoField(db_column='CollectingTripAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    collectingtripid = models.ForeignKey(Collectingtrip, models.DO_NOTHING, db_column='CollectingTripID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collectingtripattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingtripattachment'


class Collectingtripattribute(models.Model):
    collectingtripattributeid = models.AutoField(db_column='CollectingTripAttributeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer10 = models.IntegerField(db_column='Integer10', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.IntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.IntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    integer6 = models.IntegerField(db_column='Integer6', blank=True, null=True)  # Field name made lowercase.
    integer7 = models.IntegerField(db_column='Integer7', blank=True, null=True)  # Field name made lowercase.
    integer8 = models.IntegerField(db_column='Integer8', blank=True, null=True)  # Field name made lowercase.
    integer9 = models.IntegerField(db_column='Integer9', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number10 = models.DecimalField(db_column='Number10', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number11 = models.DecimalField(db_column='Number11', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number12 = models.DecimalField(db_column='Number12', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number13 = models.DecimalField(db_column='Number13', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number6 = models.DecimalField(db_column='Number6', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number7 = models.DecimalField(db_column='Number7', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number8 = models.DecimalField(db_column='Number8', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number9 = models.DecimalField(db_column='Number9', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text10 = models.CharField(db_column='Text10', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text11 = models.CharField(db_column='Text11', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text12 = models.CharField(db_column='Text12', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text13 = models.CharField(db_column='Text13', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text14 = models.CharField(db_column='Text14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text15 = models.CharField(db_column='Text15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text16 = models.CharField(db_column='Text16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text17 = models.CharField(db_column='Text17', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text6 = models.CharField(db_column='Text6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text7 = models.CharField(db_column='Text7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text8 = models.CharField(db_column='Text8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text9 = models.CharField(db_column='Text9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    disciplineid = models.ForeignKey('Discipline', models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='collectingtripattribute_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingtripattribute'


class Collectingtripauthorization(models.Model):
    collectingtripauthorizationid = models.AutoField(db_column='CollectingTripAuthorizationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    permitid = models.ForeignKey('Permit', models.DO_NOTHING, db_column='PermitID')  # Field name made lowercase.
    collectingtripid = models.ForeignKey(Collectingtrip, models.DO_NOTHING, db_column='CollectingTripID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collectingtripauthorization_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectingtripauthorization'


class Collection(models.Model):
    usergroupscopeid = models.IntegerField(db_column='UserGroupScopeId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collection_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    catalogformatnumname = models.CharField(db_column='CatalogFormatNumName', max_length=64)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collectionid = models.IntegerField(db_column='collectionId', blank=True, null=True)  # Field name made lowercase.
    collectionname = models.CharField(db_column='CollectionName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collectiontype = models.CharField(db_column='CollectionType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dbcontentversion = models.CharField(db_column='DbContentVersion', max_length=32, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    developmentstatus = models.CharField(db_column='DevelopmentStatus', max_length=32, blank=True, null=True)  # Field name made lowercase.
    estimatedsize = models.IntegerField(db_column='EstimatedSize', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    institutiontype = models.CharField(db_column='InstitutionType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isembeddedcollectingevent = models.TextField(db_column='IsEmbeddedCollectingEvent')  # Field name made lowercase. This field type is a guess.
    isanumber = models.CharField(db_column='IsaNumber', max_length=24, blank=True, null=True)  # Field name made lowercase.
    kingdomcoverage = models.CharField(db_column='KingdomCoverage', max_length=32, blank=True, null=True)  # Field name made lowercase.
    preservationmethodtype = models.CharField(db_column='PreservationMethodType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    primaryfocus = models.CharField(db_column='PrimaryFocus', max_length=32, blank=True, null=True)  # Field name made lowercase.
    primarypurpose = models.CharField(db_column='PrimaryPurpose', max_length=32, blank=True, null=True)  # Field name made lowercase.
    regnumber = models.CharField(db_column='RegNumber', max_length=24, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    scope = models.TextField(db_column='Scope', blank=True, null=True)  # Field name made lowercase.
    webportaluri = models.CharField(db_column='WebPortalURI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    websiteuri = models.CharField(db_column='WebSiteURI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey('Discipline', models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    institutionnetworkid = models.ForeignKey('Institution', models.DO_NOTHING, db_column='InstitutionNetworkID', blank=True, null=True)  # Field name made lowercase.
    admincontactid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AdminContactID', related_name='collection_admincontactid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collection'


class Collectionobject(models.Model):
    collectionobjectid = models.AutoField(db_column='CollectionObjectID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    altcatalognumber = models.CharField(db_column='AltCatalogNumber', max_length=64, blank=True, null=True)  # Field name made lowercase.
    availability = models.CharField(db_column='Availability', max_length=32, blank=True, null=True)  # Field name made lowercase.
    catalognumber = models.CharField(db_column='CatalogNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    catalogeddate = models.DateField(db_column='CatalogedDate', blank=True, null=True)  # Field name made lowercase.
    catalogeddateprecision = models.IntegerField(db_column='CatalogedDatePrecision', blank=True, null=True)  # Field name made lowercase.
    catalogeddateverbatim = models.CharField(db_column='CatalogedDateVerbatim', max_length=32, blank=True, null=True)  # Field name made lowercase.
    countamt = models.IntegerField(db_column='CountAmt', blank=True, null=True)  # Field name made lowercase.
    deaccessioned = models.TextField(db_column='Deaccessioned', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    fieldnumber = models.CharField(db_column='FieldNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    inventorydate = models.DateField(db_column='InventoryDate', blank=True, null=True)  # Field name made lowercase.
    modifier = models.CharField(db_column='Modifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    notifications = models.CharField(db_column='Notifications', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    objectcondition = models.CharField(db_column='ObjectCondition', max_length=64, blank=True, null=True)  # Field name made lowercase.
    projectnumber = models.CharField(db_column='ProjectNumber', max_length=64, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    restrictions = models.CharField(db_column='Restrictions', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    totalvalue = models.DecimalField(db_column='TotalValue', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ocr = models.TextField(db_column='OCR', blank=True, null=True)  # Field name made lowercase.
    visibility = models.IntegerField(db_column='Visibility', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno6 = models.TextField(db_column='YesNo6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collectionid = models.ForeignKey(Collection, models.DO_NOTHING, db_column='CollectionID')  # Field name made lowercase.
    collectingeventid = models.ForeignKey(Collectingevent, models.DO_NOTHING, db_column='CollectingEventID', blank=True, null=True)  # Field name made lowercase.
    containerid = models.ForeignKey('Container', models.DO_NOTHING, db_column='ContainerID', blank=True, null=True)  # Field name made lowercase.
    fieldnotebookpageid = models.ForeignKey('Fieldnotebookpage', models.DO_NOTHING, db_column='FieldNotebookPageID', blank=True, null=True)  # Field name made lowercase.
    paleocontextid = models.ForeignKey('Paleocontext', models.DO_NOTHING, db_column='PaleoContextID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    accessionid = models.ForeignKey(Accession, models.DO_NOTHING, db_column='AccessionID', blank=True, null=True)  # Field name made lowercase.
    containerownerid = models.ForeignKey('Container', models.DO_NOTHING, db_column='ContainerOwnerID', related_name='collectionobject_containerownerid_set', blank=True, null=True)  # Field name made lowercase.
    collectionobjectattributeid = models.ForeignKey('Collectionobjectattribute', models.DO_NOTHING, db_column='CollectionObjectAttributeID', blank=True, null=True)  # Field name made lowercase.
    appraisalid = models.ForeignKey(Appraisal, models.DO_NOTHING, db_column='AppraisalID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collectionobject_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    visibilitysetbyid = models.ForeignKey('Specifyuser', models.DO_NOTHING, db_column='VisibilitySetByID', blank=True, null=True)  # Field name made lowercase.
    catalogerid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CatalogerID', related_name='collectionobject_catalogerid_set', blank=True, null=True)  # Field name made lowercase.
    sgrstatus = models.IntegerField(db_column='SGRStatus', blank=True, null=True)  # Field name made lowercase.
    reservedtext = models.CharField(db_column='ReservedText', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    reservedinteger3 = models.IntegerField(db_column='ReservedInteger3', blank=True, null=True)  # Field name made lowercase.
    reservedinteger4 = models.IntegerField(db_column='ReservedInteger4', blank=True, null=True)  # Field name made lowercase.
    reservedtext2 = models.CharField(db_column='ReservedText2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    reservedtext3 = models.CharField(db_column='ReservedText3', max_length=128, blank=True, null=True)  # Field name made lowercase.
    inventorizedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='InventorizedByID', related_name='collectionobject_inventorizedbyid_set', blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    inventorydateprecision = models.IntegerField(db_column='InventoryDatePrecision', blank=True, null=True)  # Field name made lowercase.
    agent1id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent1ID', related_name='collectionobject_agent1id_set', blank=True, null=True)  # Field name made lowercase.
    numberofduplicates = models.IntegerField(db_column='NumberOfDuplicates', blank=True, null=True)  # Field name made lowercase.
    embargoreason = models.TextField(db_column='EmbargoReason', blank=True, null=True)  # Field name made lowercase.
    embargoreleasedate = models.DateField(db_column='EmbargoReleaseDate', blank=True, null=True)  # Field name made lowercase.
    embargoreleasedateprecision = models.IntegerField(db_column='EmbargoReleaseDatePrecision', blank=True, null=True)  # Field name made lowercase.
    embargostartdate = models.DateField(db_column='EmbargoStartDate', blank=True, null=True)  # Field name made lowercase.
    embargostartdateprecision = models.IntegerField(db_column='EmbargoStartDatePrecision', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    text6 = models.TextField(db_column='Text6', blank=True, null=True)  # Field name made lowercase.
    text7 = models.TextField(db_column='Text7', blank=True, null=True)  # Field name made lowercase.
    text8 = models.TextField(db_column='Text8', blank=True, null=True)  # Field name made lowercase.
    uniqueidentifier = models.CharField(db_column='UniqueIdentifier', max_length=128, blank=True, null=True)  # Field name made lowercase.
    embargoauthorityid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='EmbargoAuthorityID', related_name='collectionobject_embargoauthorityid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectionobject'
        unique_together = (('collectionid', 'uniqueidentifier'), ('collectionid', 'catalognumber'),)


class CollectionobjectDupes(models.Model):
    collectionobjectid = models.AutoField(db_column='CollectionObjectID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    altcatalognumber = models.CharField(db_column='AltCatalogNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    availability = models.CharField(db_column='Availability', max_length=32, blank=True, null=True)  # Field name made lowercase.
    catalognumber = models.CharField(db_column='CatalogNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    catalogeddate = models.DateField(db_column='CatalogedDate', blank=True, null=True)  # Field name made lowercase.
    catalogeddateprecision = models.IntegerField(db_column='CatalogedDatePrecision', blank=True, null=True)  # Field name made lowercase.
    catalogeddateverbatim = models.CharField(db_column='CatalogedDateVerbatim', max_length=32, blank=True, null=True)  # Field name made lowercase.
    countamt = models.IntegerField(db_column='CountAmt', blank=True, null=True)  # Field name made lowercase.
    deaccessioned = models.TextField(db_column='Deaccessioned', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fieldnumber = models.CharField(db_column='FieldNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    inventorydate = models.DateField(db_column='InventoryDate', blank=True, null=True)  # Field name made lowercase.
    modifier = models.CharField(db_column='Modifier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    notifications = models.CharField(db_column='Notifications', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number1 = models.FloatField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.FloatField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    objectcondition = models.CharField(db_column='ObjectCondition', max_length=64, blank=True, null=True)  # Field name made lowercase.
    projectnumber = models.CharField(db_column='ProjectNumber', max_length=64, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    restrictions = models.CharField(db_column='Restrictions', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    totalvalue = models.DecimalField(db_column='TotalValue', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    visibility = models.IntegerField(db_column='Visibility', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno6 = models.TextField(db_column='YesNo6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collectionid = models.IntegerField(db_column='CollectionID')  # Field name made lowercase.
    collectingeventid = models.IntegerField(db_column='CollectingEventID', blank=True, null=True)  # Field name made lowercase.
    containerid = models.IntegerField(db_column='ContainerID', blank=True, null=True)  # Field name made lowercase.
    fieldnotebookpageid = models.IntegerField(db_column='FieldNotebookPageID', blank=True, null=True)  # Field name made lowercase.
    paleocontextid = models.IntegerField(db_column='PaleoContextID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.IntegerField(db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    accessionid = models.IntegerField(db_column='AccessionID', blank=True, null=True)  # Field name made lowercase.
    containerownerid = models.IntegerField(db_column='ContainerOwnerID', blank=True, null=True)  # Field name made lowercase.
    collectionobjectattributeid = models.IntegerField(db_column='CollectionObjectAttributeID', blank=True, null=True)  # Field name made lowercase.
    appraisalid = models.IntegerField(db_column='AppraisalID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.IntegerField(db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    visibilitysetbyid = models.IntegerField(db_column='VisibilitySetByID', blank=True, null=True)  # Field name made lowercase.
    catalogerid = models.IntegerField(db_column='CatalogerID', blank=True, null=True)  # Field name made lowercase.
    sgrstatus = models.IntegerField(db_column='SGRStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectionobject_dupes'
        unique_together = (('collectionid', 'catalognumber'),)


class Collectionobjectattachment(models.Model):
    collectionobjectattachmentid = models.AutoField(db_column='CollectionObjectAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collectionobjectattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectionobjectattachment'


class Collectionobjectattr(models.Model):
    attrid = models.AutoField(db_column='AttrID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    doublevalue = models.FloatField(db_column='DoubleValue', blank=True, null=True)  # Field name made lowercase.
    strvalue = models.CharField(db_column='StrValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    attributedefid = models.ForeignKey(Attributedef, models.DO_NOTHING, db_column='AttributeDefID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='collectionobjectattr_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectionobjectattr'


class Collectionobjectattribute(models.Model):
    collectionobjectattributeid = models.AutoField(db_column='CollectionObjectAttributeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number10 = models.DecimalField(db_column='Number10', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number11 = models.DecimalField(db_column='Number11', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number12 = models.DecimalField(db_column='Number12', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number13 = models.DecimalField(db_column='Number13', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number14 = models.DecimalField(db_column='Number14', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number15 = models.DecimalField(db_column='Number15', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number16 = models.DecimalField(db_column='Number16', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number17 = models.DecimalField(db_column='Number17', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number18 = models.DecimalField(db_column='Number18', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number19 = models.DecimalField(db_column='Number19', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number20 = models.DecimalField(db_column='Number20', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number21 = models.DecimalField(db_column='Number21', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number22 = models.DecimalField(db_column='Number22', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number23 = models.DecimalField(db_column='Number23', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number24 = models.DecimalField(db_column='Number24', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number25 = models.DecimalField(db_column='Number25', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number26 = models.DecimalField(db_column='Number26', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number27 = models.DecimalField(db_column='Number27', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number28 = models.DecimalField(db_column='Number28', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number29 = models.DecimalField(db_column='Number29', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number30 = models.IntegerField(blank=True, null=True)
    number31 = models.DecimalField(db_column='Number31', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number32 = models.DecimalField(db_column='Number32', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number33 = models.DecimalField(db_column='Number33', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number34 = models.DecimalField(db_column='Number34', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number35 = models.DecimalField(db_column='Number35', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number36 = models.DecimalField(db_column='Number36', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number37 = models.DecimalField(db_column='Number37', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number38 = models.DecimalField(db_column='Number38', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number39 = models.DecimalField(db_column='Number39', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number40 = models.DecimalField(db_column='Number40', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number41 = models.DecimalField(db_column='Number41', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number42 = models.DecimalField(db_column='Number42', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number6 = models.DecimalField(db_column='Number6', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number7 = models.DecimalField(db_column='Number7', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number8 = models.IntegerField(blank=True, null=True)
    number9 = models.DecimalField(db_column='Number9', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text10 = models.CharField(db_column='Text10', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text11 = models.CharField(db_column='Text11', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text12 = models.CharField(db_column='Text12', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text13 = models.CharField(db_column='Text13', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text14 = models.CharField(db_column='Text14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text15 = models.CharField(db_column='Text15', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text6 = models.CharField(db_column='Text6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text7 = models.CharField(db_column='Text7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text8 = models.CharField(db_column='Text8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text9 = models.CharField(db_column='Text9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno6 = models.TextField(db_column='YesNo6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno7 = models.TextField(db_column='YesNo7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collectionobjectattribute_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    bottomdistance = models.DecimalField(db_column='BottomDistance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    direction = models.CharField(db_column='Direction', max_length=32, blank=True, null=True)  # Field name made lowercase.
    distanceunits = models.CharField(db_column='DistanceUnits', max_length=16, blank=True, null=True)  # Field name made lowercase.
    positionstate = models.CharField(db_column='PositionState', max_length=32, blank=True, null=True)  # Field name made lowercase.
    topdistance = models.DecimalField(db_column='TopDistance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    text16 = models.TextField(db_column='Text16', blank=True, null=True)  # Field name made lowercase.
    text17 = models.TextField(db_column='Text17', blank=True, null=True)  # Field name made lowercase.
    text18 = models.TextField(db_column='Text18', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer10 = models.IntegerField(db_column='Integer10', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.IntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.IntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    integer6 = models.IntegerField(db_column='Integer6', blank=True, null=True)  # Field name made lowercase.
    integer7 = models.IntegerField(db_column='Integer7', blank=True, null=True)  # Field name made lowercase.
    integer8 = models.IntegerField(db_column='Integer8', blank=True, null=True)  # Field name made lowercase.
    integer9 = models.IntegerField(db_column='Integer9', blank=True, null=True)  # Field name made lowercase.
    text19 = models.TextField(db_column='Text19', blank=True, null=True)  # Field name made lowercase.
    text20 = models.TextField(db_column='Text20', blank=True, null=True)  # Field name made lowercase.
    text21 = models.TextField(db_column='Text21', blank=True, null=True)  # Field name made lowercase.
    text22 = models.TextField(db_column='Text22', blank=True, null=True)  # Field name made lowercase.
    text23 = models.TextField(db_column='Text23', blank=True, null=True)  # Field name made lowercase.
    text24 = models.TextField(db_column='Text24', blank=True, null=True)  # Field name made lowercase.
    text25 = models.TextField(db_column='Text25', blank=True, null=True)  # Field name made lowercase.
    text26 = models.TextField(db_column='Text26', blank=True, null=True)  # Field name made lowercase.
    text27 = models.TextField(db_column='Text27', blank=True, null=True)  # Field name made lowercase.
    text28 = models.TextField(db_column='Text28', blank=True, null=True)  # Field name made lowercase.
    text29 = models.TextField(db_column='Text29', blank=True, null=True)  # Field name made lowercase.
    text30 = models.TextField(db_column='Text30', blank=True, null=True)  # Field name made lowercase.
    yesno10 = models.TextField(db_column='YesNo10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno11 = models.TextField(db_column='YesNo11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno12 = models.TextField(db_column='YesNo12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno13 = models.TextField(db_column='YesNo13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno14 = models.TextField(db_column='YesNo14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno15 = models.TextField(db_column='YesNo15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno16 = models.TextField(db_column='YesNo16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno17 = models.TextField(db_column='YesNo17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno18 = models.TextField(db_column='YesNo18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno19 = models.TextField(db_column='YesNo19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno20 = models.TextField(db_column='YesNo20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno8 = models.TextField(db_column='YesNo8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno9 = models.TextField(db_column='YesNo9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    agent1id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent1ID', related_name='collectionobjectattribute_agent1id_set', blank=True, null=True)  # Field name made lowercase.
    text31 = models.TextField(db_column='Text31', blank=True, null=True)  # Field name made lowercase.
    text32 = models.TextField(db_column='Text32', blank=True, null=True)  # Field name made lowercase.
    text33 = models.TextField(db_column='Text33', blank=True, null=True)  # Field name made lowercase.
    text34 = models.TextField(db_column='Text34', blank=True, null=True)  # Field name made lowercase.
    text35 = models.TextField(db_column='Text35', blank=True, null=True)  # Field name made lowercase.
    text36 = models.TextField(db_column='Text36', blank=True, null=True)  # Field name made lowercase.
    text37 = models.TextField(db_column='Text37', blank=True, null=True)  # Field name made lowercase.
    text38 = models.TextField(db_column='Text38', blank=True, null=True)  # Field name made lowercase.
    text39 = models.TextField(db_column='Text39', blank=True, null=True)  # Field name made lowercase.
    text40 = models.TextField(db_column='Text40', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectionobjectattribute'


class Collectionobjectcitation(models.Model):
    collectionobjectcitationid = models.AutoField(db_column='CollectionObjectCitationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    isfigured = models.TextField(db_column='IsFigured', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    referenceworkid = models.ForeignKey('Referencework', models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collectionobjectcitation_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    figurenumber = models.CharField(db_column='FigureNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pagenumber = models.CharField(db_column='PageNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectionobjectcitation'


class Collectionobjectproperty(models.Model):
    collectionobjectpropertyid = models.AutoField(db_column='CollectionObjectPropertyID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date10 = models.DateField(db_column='Date10', blank=True, null=True)  # Field name made lowercase.
    date11 = models.DateField(db_column='Date11', blank=True, null=True)  # Field name made lowercase.
    date12 = models.DateField(db_column='Date12', blank=True, null=True)  # Field name made lowercase.
    date13 = models.DateField(db_column='Date13', blank=True, null=True)  # Field name made lowercase.
    date14 = models.DateField(db_column='Date14', blank=True, null=True)  # Field name made lowercase.
    date15 = models.DateField(db_column='Date15', blank=True, null=True)  # Field name made lowercase.
    date16 = models.DateField(db_column='Date16', blank=True, null=True)  # Field name made lowercase.
    date17 = models.DateField(db_column='Date17', blank=True, null=True)  # Field name made lowercase.
    date18 = models.DateField(db_column='Date18', blank=True, null=True)  # Field name made lowercase.
    date19 = models.DateField(db_column='Date19', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    date20 = models.DateField(db_column='Date20', blank=True, null=True)  # Field name made lowercase.
    date3 = models.DateField(db_column='Date3', blank=True, null=True)  # Field name made lowercase.
    date4 = models.DateField(db_column='Date4', blank=True, null=True)  # Field name made lowercase.
    date5 = models.DateField(db_column='Date5', blank=True, null=True)  # Field name made lowercase.
    date6 = models.DateField(db_column='Date6', blank=True, null=True)  # Field name made lowercase.
    date7 = models.DateField(db_column='Date7', blank=True, null=True)  # Field name made lowercase.
    date8 = models.DateField(db_column='Date8', blank=True, null=True)  # Field name made lowercase.
    date9 = models.DateField(db_column='Date9', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    integer1 = models.SmallIntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer10 = models.SmallIntegerField(db_column='Integer10', blank=True, null=True)  # Field name made lowercase.
    integer11 = models.SmallIntegerField(db_column='Integer11', blank=True, null=True)  # Field name made lowercase.
    integer12 = models.SmallIntegerField(db_column='Integer12', blank=True, null=True)  # Field name made lowercase.
    integer13 = models.SmallIntegerField(db_column='Integer13', blank=True, null=True)  # Field name made lowercase.
    integer14 = models.SmallIntegerField(db_column='Integer14', blank=True, null=True)  # Field name made lowercase.
    integer15 = models.SmallIntegerField(db_column='Integer15', blank=True, null=True)  # Field name made lowercase.
    integer16 = models.SmallIntegerField(db_column='Integer16', blank=True, null=True)  # Field name made lowercase.
    integer17 = models.SmallIntegerField(db_column='Integer17', blank=True, null=True)  # Field name made lowercase.
    integer18 = models.SmallIntegerField(db_column='Integer18', blank=True, null=True)  # Field name made lowercase.
    integer19 = models.SmallIntegerField(db_column='Integer19', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.SmallIntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer20 = models.SmallIntegerField(db_column='Integer20', blank=True, null=True)  # Field name made lowercase.
    integer21 = models.IntegerField(db_column='Integer21', blank=True, null=True)  # Field name made lowercase.
    integer22 = models.IntegerField(db_column='Integer22', blank=True, null=True)  # Field name made lowercase.
    integer23 = models.IntegerField(db_column='Integer23', blank=True, null=True)  # Field name made lowercase.
    integer24 = models.IntegerField(db_column='Integer24', blank=True, null=True)  # Field name made lowercase.
    integer25 = models.IntegerField(db_column='Integer25', blank=True, null=True)  # Field name made lowercase.
    integer26 = models.IntegerField(db_column='Integer26', blank=True, null=True)  # Field name made lowercase.
    integer27 = models.IntegerField(db_column='Integer27', blank=True, null=True)  # Field name made lowercase.
    integer28 = models.IntegerField(db_column='Integer28', blank=True, null=True)  # Field name made lowercase.
    integer29 = models.IntegerField(db_column='Integer29', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.SmallIntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer30 = models.IntegerField(db_column='Integer30', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.SmallIntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.SmallIntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    integer6 = models.SmallIntegerField(db_column='Integer6', blank=True, null=True)  # Field name made lowercase.
    integer7 = models.SmallIntegerField(db_column='Integer7', blank=True, null=True)  # Field name made lowercase.
    integer8 = models.SmallIntegerField(db_column='Integer8', blank=True, null=True)  # Field name made lowercase.
    integer9 = models.SmallIntegerField(db_column='Integer9', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number10 = models.DecimalField(db_column='Number10', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number11 = models.DecimalField(db_column='Number11', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number12 = models.DecimalField(db_column='Number12', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number13 = models.DecimalField(db_column='Number13', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number14 = models.DecimalField(db_column='Number14', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number15 = models.DecimalField(db_column='Number15', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number16 = models.DecimalField(db_column='Number16', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number17 = models.DecimalField(db_column='Number17', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number18 = models.DecimalField(db_column='Number18', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number19 = models.DecimalField(db_column='Number19', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number20 = models.DecimalField(db_column='Number20', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number21 = models.DecimalField(db_column='Number21', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number22 = models.DecimalField(db_column='Number22', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number23 = models.DecimalField(db_column='Number23', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number24 = models.DecimalField(db_column='Number24', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number25 = models.DecimalField(db_column='Number25', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number26 = models.DecimalField(db_column='Number26', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number27 = models.DecimalField(db_column='Number27', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number28 = models.DecimalField(db_column='Number28', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number29 = models.DecimalField(db_column='Number29', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number30 = models.DecimalField(db_column='Number30', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number6 = models.DecimalField(db_column='Number6', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number7 = models.DecimalField(db_column='Number7', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number8 = models.DecimalField(db_column='Number8', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number9 = models.DecimalField(db_column='Number9', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text10 = models.CharField(db_column='Text10', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text11 = models.CharField(db_column='Text11', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text12 = models.CharField(db_column='Text12', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text13 = models.CharField(db_column='Text13', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text14 = models.CharField(db_column='Text14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text15 = models.CharField(db_column='Text15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text16 = models.CharField(db_column='Text16', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text17 = models.CharField(db_column='Text17', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text18 = models.CharField(db_column='Text18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text19 = models.CharField(db_column='Text19', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text20 = models.CharField(db_column='Text20', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text21 = models.CharField(db_column='Text21', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text22 = models.CharField(db_column='Text22', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text23 = models.CharField(db_column='Text23', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text24 = models.CharField(db_column='Text24', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text25 = models.CharField(db_column='Text25', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text26 = models.CharField(db_column='Text26', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text27 = models.CharField(db_column='Text27', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text28 = models.CharField(db_column='Text28', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text29 = models.CharField(db_column='Text29', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text30 = models.CharField(db_column='Text30', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text31 = models.TextField(db_column='Text31', blank=True, null=True)  # Field name made lowercase.
    text32 = models.TextField(db_column='Text32', blank=True, null=True)  # Field name made lowercase.
    text33 = models.TextField(db_column='Text33', blank=True, null=True)  # Field name made lowercase.
    text34 = models.TextField(db_column='Text34', blank=True, null=True)  # Field name made lowercase.
    text35 = models.TextField(db_column='Text35', blank=True, null=True)  # Field name made lowercase.
    text36 = models.TextField(db_column='Text36', blank=True, null=True)  # Field name made lowercase.
    text37 = models.TextField(db_column='Text37', blank=True, null=True)  # Field name made lowercase.
    text38 = models.TextField(db_column='Text38', blank=True, null=True)  # Field name made lowercase.
    text39 = models.TextField(db_column='Text39', blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text40 = models.TextField(db_column='Text40', blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text6 = models.CharField(db_column='Text6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text7 = models.CharField(db_column='Text7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text8 = models.CharField(db_column='Text8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text9 = models.CharField(db_column='Text9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno10 = models.TextField(db_column='YesNo10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno11 = models.TextField(db_column='YesNo11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno12 = models.TextField(db_column='YesNo12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno13 = models.TextField(db_column='YesNo13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno14 = models.TextField(db_column='YesNo14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno15 = models.TextField(db_column='YesNo15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno16 = models.TextField(db_column='YesNo16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno17 = models.TextField(db_column='YesNo17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno18 = models.TextField(db_column='YesNo18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno19 = models.TextField(db_column='YesNo19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno20 = models.TextField(db_column='YesNo20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno6 = models.TextField(db_column='YesNo6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno7 = models.TextField(db_column='YesNo7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno8 = models.TextField(db_column='YesNo8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno9 = models.TextField(db_column='YesNo9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    agent7id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent7ID', related_name='collectionobjectproperty_agent7id_set', blank=True, null=True)  # Field name made lowercase.
    agent18id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent18ID', related_name='collectionobjectproperty_agent18id_set', blank=True, null=True)  # Field name made lowercase.
    agent15id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent15ID', related_name='collectionobjectproperty_agent15id_set', blank=True, null=True)  # Field name made lowercase.
    agent4id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent4ID', related_name='collectionobjectproperty_agent4id_set', blank=True, null=True)  # Field name made lowercase.
    agent8d = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent8D', related_name='collectionobjectproperty_agent8d_set', blank=True, null=True)  # Field name made lowercase.
    agent19id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent19ID', related_name='collectionobjectproperty_agent19id_set', blank=True, null=True)  # Field name made lowercase.
    agent1id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent1ID', related_name='collectionobjectproperty_agent1id_set', blank=True, null=True)  # Field name made lowercase.
    agent10id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent10ID', related_name='collectionobjectproperty_agent10id_set', blank=True, null=True)  # Field name made lowercase.
    agent14id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent14ID', related_name='collectionobjectproperty_agent14id_set', blank=True, null=True)  # Field name made lowercase.
    agent20id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent20ID', related_name='collectionobjectproperty_agent20id_set', blank=True, null=True)  # Field name made lowercase.
    agent11id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent11ID', related_name='collectionobjectproperty_agent11id_set', blank=True, null=True)  # Field name made lowercase.
    agent12id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent12ID', related_name='collectionobjectproperty_agent12id_set', blank=True, null=True)  # Field name made lowercase.
    agent13id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent13ID', related_name='collectionobjectproperty_agent13id_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='collectionobjectproperty_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agent3id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent3ID', related_name='collectionobjectproperty_agent3id_set', blank=True, null=True)  # Field name made lowercase.
    agent5id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent5ID', related_name='collectionobjectproperty_agent5id_set', blank=True, null=True)  # Field name made lowercase.
    agent16id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent16ID', related_name='collectionobjectproperty_agent16id_set', blank=True, null=True)  # Field name made lowercase.
    agent17id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent17ID', related_name='collectionobjectproperty_agent17id_set', blank=True, null=True)  # Field name made lowercase.
    agent9id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent9ID', related_name='collectionobjectproperty_agent9id_set', blank=True, null=True)  # Field name made lowercase.
    agent6id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent6ID', related_name='collectionobjectproperty_agent6id_set', blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.
    agent2id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent2ID', related_name='collectionobjectproperty_agent2id_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectionobjectproperty'


class Collectionrelationship(models.Model):
    collectionrelationshipid = models.AutoField(db_column='CollectionRelationshipID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    collectionreltypeid = models.ForeignKey('Collectionreltype', models.DO_NOTHING, db_column='CollectionRelTypeID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='collectionrelationship_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    rightsidecollectionid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='RightSideCollectionID')  # Field name made lowercase.
    leftsidecollectionid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='LeftSideCollectionID', related_name='collectionrelationship_leftsidecollectionid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectionrelationship'


class Collectionreltype(models.Model):
    collectionreltypeid = models.AutoField(db_column='CollectionRelTypeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    rightsidecollectionid = models.ForeignKey(Collection, models.DO_NOTHING, db_column='RightSideCollectionID', blank=True, null=True)  # Field name made lowercase.
    leftsidecollectionid = models.ForeignKey(Collection, models.DO_NOTHING, db_column='LeftSideCollectionID', related_name='collectionreltype_leftsidecollectionid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collectionreltype_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collectionreltype'


class Collector(models.Model):
    collectorid = models.AutoField(db_column='CollectorID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.TextField(db_column='IsPrimary')  # Field name made lowercase. This field type is a guess.
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.ForeignKey('Division', models.DO_NOTHING, db_column='DivisionID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='collector_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    collectingeventid = models.ForeignKey(Collectingevent, models.DO_NOTHING, db_column='CollectingEventID')  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='collector_agentid_set')  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'collector'
        unique_together = (('agentid', 'collectingeventid'),)


class CollectorDupes(models.Model):
    collectorid = models.AutoField(db_column='CollectorID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.TextField(db_column='IsPrimary')  # Field name made lowercase. This field type is a guess.
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.IntegerField(db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.IntegerField(db_column='DivisionID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.IntegerField(db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    collectingeventid = models.IntegerField(db_column='CollectingEventID')  # Field name made lowercase.
    agentid = models.IntegerField(db_column='AgentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collector_dupes'
        unique_together = (('agentid', 'collectingeventid'),)


class Colombia2012SpecimenDescription(models.Model):
    specimen_description = models.TextField(db_column='Specimen description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collector_number = models.IntegerField(db_column='Collector number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'colombia_2012_specimen_description'


class Colombia2013SpecimenDescriptionCopy(models.Model):
    specimen_description = models.TextField(db_column='Specimen description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collector_number = models.CharField(db_column='Collector number', max_length=11, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'colombia_2013_specimen_description_copy'


class Commonnametx(models.Model):
    commonnametxid = models.AutoField(db_column='CommonNameTxID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=128, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=2, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=2, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    variant = models.CharField(db_column='Variant', max_length=2, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    taxonid = models.ForeignKey('Taxon', models.DO_NOTHING, db_column='TaxonID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='commonnametx_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commonnametx'


class Commonnametxcitation(models.Model):
    commonnametxcitationid = models.AutoField(db_column='CommonNameTxCitationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    referenceworkid = models.ForeignKey('Referencework', models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='commonnametxcitation_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    commonnametxid = models.ForeignKey(Commonnametx, models.DO_NOTHING, db_column='CommonNameTxID')  # Field name made lowercase.
    figurenumber = models.CharField(db_column='FigureNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isfigured = models.TextField(db_column='IsFigured', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pagenumber = models.CharField(db_column='PageNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commonnametxcitation'


class Conservdescription(models.Model):
    conservdescriptionid = models.AutoField(db_column='ConservDescriptionID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    backgroundinfo = models.TextField(db_column='BackgroundInfo', blank=True, null=True)  # Field name made lowercase.
    composition = models.TextField(db_column='Composition', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    displayrecommendations = models.TextField(db_column='DisplayRecommendations', blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    lightrecommendations = models.TextField(db_column='LightRecommendations', blank=True, null=True)  # Field name made lowercase.
    objlength = models.DecimalField(db_column='ObjLength', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    otherrecommendations = models.TextField(db_column='OtherRecommendations', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    shortdesc = models.CharField(db_column='ShortDesc', max_length=128, blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=16, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.ForeignKey('Division', models.DO_NOTHING, db_column='DivisionID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='conservdescription_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID', blank=True, null=True)  # Field name made lowercase.
    catalogeddate = models.DateField(db_column='CatalogedDate', blank=True, null=True)  # Field name made lowercase.
    determineddateprecision = models.IntegerField(db_column='determinedDatePrecision', blank=True, null=True)  # Field name made lowercase.
    preparationid = models.ForeignKey('Preparation', models.DO_NOTHING, db_column='PreparationID', blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    date2precision = models.IntegerField(db_column='Date2Precision', blank=True, null=True)  # Field name made lowercase.
    date3 = models.DateField(db_column='Date3', blank=True, null=True)  # Field name made lowercase.
    date3precision = models.IntegerField(db_column='Date3Precision', blank=True, null=True)  # Field name made lowercase.
    date4 = models.DateField(db_column='Date4', blank=True, null=True)  # Field name made lowercase.
    date4precision = models.IntegerField(db_column='Date4Precision', blank=True, null=True)  # Field name made lowercase.
    date5 = models.DateField(db_column='Date5', blank=True, null=True)  # Field name made lowercase.
    date5precision = models.IntegerField(db_column='Date5Precision', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.IntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.IntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'conservdescription'


class Conservdescriptionattachment(models.Model):
    conservdescriptionattachmentid = models.AutoField(db_column='ConservDescriptionAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    conservdescriptionid = models.ForeignKey(Conservdescription, models.DO_NOTHING, db_column='ConservDescriptionID')  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='conservdescriptionattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conservdescriptionattachment'


class Conservevent(models.Model):
    conserveventid = models.AutoField(db_column='ConservEventID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    advtestingexam = models.TextField(db_column='AdvTestingExam', blank=True, null=True)  # Field name made lowercase.
    advtestingexamresults = models.TextField(db_column='AdvTestingExamResults', blank=True, null=True)  # Field name made lowercase.
    completedcomments = models.TextField(db_column='CompletedComments', blank=True, null=True)  # Field name made lowercase.
    completeddate = models.DateField(db_column='CompletedDate', blank=True, null=True)  # Field name made lowercase.
    conditionreport = models.TextField(db_column='ConditionReport', blank=True, null=True)  # Field name made lowercase.
    curatorapprovaldate = models.DateField(db_column='CuratorApprovalDate', blank=True, null=True)  # Field name made lowercase.
    examdate = models.DateField(db_column='ExamDate', blank=True, null=True)  # Field name made lowercase.
    number1 = models.IntegerField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.IntegerField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    photodocs = models.TextField(db_column='PhotoDocs', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=64, blank=True, null=True)  # Field name made lowercase.
    treatmentcompdate = models.DateField(db_column='TreatmentCompDate', blank=True, null=True)  # Field name made lowercase.
    treatmentreport = models.TextField(db_column='TreatmentReport', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conservdescriptionid = models.ForeignKey(Conservdescription, models.DO_NOTHING, db_column='ConservDescriptionID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='conservevent_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    treatedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='TreatedByAgentID', related_name='conservevent_treatedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    examinedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ExaminedByAgentID', related_name='conservevent_examinedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    curatorid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CuratorID', related_name='conservevent_curatorid_set', blank=True, null=True)  # Field name made lowercase.
    completeddateprecision = models.IntegerField(db_column='CompletedDatePrecision', blank=True, null=True)  # Field name made lowercase.
    curatorapprovaldateprecision = models.IntegerField(db_column='CuratorApprovalDatePrecision', blank=True, null=True)  # Field name made lowercase.
    examdateprecision = models.IntegerField(db_column='ExamDatePrecision', blank=True, null=True)  # Field name made lowercase.
    treatmentcompdateprecision = models.IntegerField(db_column='TreatmentCompDatePrecision', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conservevent'


class Conserveventattachment(models.Model):
    conserveventattachmentid = models.AutoField(db_column='ConservEventAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    conserveventid = models.ForeignKey(Conservevent, models.DO_NOTHING, db_column='ConservEventID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='conserveventattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conserveventattachment'


class Container(models.Model):
    containerid = models.AutoField(db_column='ContainerID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    storageid = models.ForeignKey('Storage', models.DO_NOTHING, db_column='StorageID', blank=True, null=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='container_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'container'


class Continentcodes(models.Model):
    code = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    geonameid = models.IntegerField(db_column='geonameId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'continentcodes'


class Countryinfo(models.Model):
    iso_alpha2 = models.CharField(max_length=2, blank=True, null=True)
    iso_alpha3 = models.CharField(max_length=3, blank=True, null=True)
    iso_numeric = models.IntegerField(blank=True, null=True)
    fips_code = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(primary_key=True, max_length=255)
    capital = models.CharField(max_length=255, blank=True, null=True)
    areainsqkm = models.CharField(max_length=16, blank=True, null=True)
    population = models.CharField(max_length=16, blank=True, null=True)
    continent = models.CharField(max_length=2, blank=True, null=True)
    tld = models.CharField(max_length=32, blank=True, null=True)
    currencycode = models.CharField(max_length=3, blank=True, null=True)
    currencyname = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    postalformat = models.CharField(max_length=128, blank=True, null=True)
    postalregex = models.TextField(blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)
    geonameid = models.IntegerField(db_column='geonameId', blank=True, null=True)  # Field name made lowercase.
    neighbors = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countryinfo'


class Darwincoretdwg14(models.Model):
    darwincoretdwg1_4id = models.IntegerField(db_column='darwincoretdwg1_4Id', primary_key=True)  # Field name made lowercase.
    catalognumber = models.CharField(db_column='CatalogNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=500, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    collector = models.TextField(db_column='Collector', blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=500, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=500, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(db_column='County', max_length=500, blank=True, null=True)  # Field name made lowercase.
    datelastmodified = models.DateTimeField(db_column='DateLastModified', blank=True, null=True)  # Field name made lowercase.
    earliestdatecollected = models.DateField(db_column='EarliestDateCollected', blank=True, null=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=500, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(db_column='Genus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    globaluniqueidentifier = models.CharField(db_column='GlobalUniqueIdentifier', max_length=128, blank=True, null=True)  # Field name made lowercase.
    highergeography = models.CharField(db_column='HigherGeography', max_length=500, blank=True, null=True)  # Field name made lowercase.
    identificationqualifier = models.CharField(db_column='IdentificationQualifier', max_length=16, blank=True, null=True)  # Field name made lowercase.
    kingdom = models.CharField(db_column='Kingdom', max_length=500, blank=True, null=True)  # Field name made lowercase.
    locality = models.CharField(db_column='Locality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maximumelevationinmeters = models.FloatField(db_column='MaximumElevationInMeters', blank=True, null=True)  # Field name made lowercase.
    minimumelevationinmeters = models.FloatField(db_column='MinimumElevationInMeters', blank=True, null=True)  # Field name made lowercase.
    order = models.CharField(db_column='Order', max_length=500, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    scientificname = models.CharField(db_column='ScientificName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specificepithet = models.CharField(db_column='SpecificEpithet', max_length=500, blank=True, null=True)  # Field name made lowercase.
    stateprovince = models.CharField(db_column='StateProvince', max_length=500, blank=True, null=True)  # Field name made lowercase.
    relatedinformation = models.CharField(db_column='RelatedInformation', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'darwincoretdwg1_4'


class Datatype(models.Model):
    datatypeid = models.AutoField(db_column='DataTypeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='datatype_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datatype'


class Deaccession(models.Model):
    deaccessionid = models.AutoField(db_column='DeaccessionID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    deaccessiondate = models.DateField(db_column='DeaccessionDate', blank=True, null=True)  # Field name made lowercase.
    deaccessionnumber = models.CharField(db_column='DeaccessionNumber', max_length=50)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.IntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.IntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=64, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    agent1id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent1ID', related_name='deaccession_agent1id_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='deaccession_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agent2id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent2ID', related_name='deaccession_agent2id_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deaccession'


class Deaccessionagent(models.Model):
    deaccessionagentid = models.AutoField(db_column='DeaccessionAgentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='deaccessionagent_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='deaccessionagent_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    deaccessionid = models.ForeignKey(Deaccession, models.DO_NOTHING, db_column='DeaccessionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deaccessionagent'
        unique_together = (('role', 'agentid', 'deaccessionid'),)


class Deaccessionattachment(models.Model):
    deaccessionattachmentid = models.AutoField(db_column='DeaccessionAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    deaccessionid = models.ForeignKey(Deaccession, models.DO_NOTHING, db_column='DeaccessionID')  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='deaccessionattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deaccessionattachment'


class Determination(models.Model):
    determinationid = models.AutoField(db_column='DeterminationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    addendum = models.CharField(db_column='Addendum', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alternatename = models.CharField(db_column='AlternateName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    confidence = models.CharField(db_column='Confidence', max_length=50, blank=True, null=True)  # Field name made lowercase.
    determineddate = models.DateField(db_column='DeterminedDate', blank=True, null=True)  # Field name made lowercase.
    determineddateprecision = models.IntegerField(db_column='DeterminedDatePrecision', blank=True, null=True)  # Field name made lowercase.
    featureorbasis = models.CharField(db_column='FeatureOrBasis', max_length=250, blank=True, null=True)  # Field name made lowercase.
    iscurrent = models.TextField(db_column='IsCurrent')  # Field name made lowercase. This field type is a guess.
    method = models.CharField(db_column='Method', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nameusage = models.CharField(db_column='NameUsage', max_length=64, blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    qualifier = models.CharField(db_column='Qualifier', max_length=16, blank=True, null=True)  # Field name made lowercase.
    varqualifer = models.CharField(db_column='VarQualifer', max_length=16, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    subspqualifier = models.CharField(db_column='SubSpQualifier', max_length=16, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    typestatusname = models.CharField(db_column='TypeStatusName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    varqualifier = models.CharField(db_column='VarQualifier', max_length=16, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    taxonid = models.ForeignKey('Taxon', models.DO_NOTHING, db_column='TaxonID', blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    determinerid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='DeterminerID', related_name='determination_determinerid_set', blank=True, null=True)  # Field name made lowercase.
    preferredtaxonid = models.ForeignKey('Taxon', models.DO_NOTHING, db_column='PreferredTaxonID', related_name='determination_preferredtaxonid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='determination_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.IntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.IntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text6 = models.CharField(db_column='Text6', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text7 = models.CharField(db_column='Text7', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text8 = models.CharField(db_column='Text8', max_length=128, blank=True, null=True)  # Field name made lowercase.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'determination'


class DeterminationDupes(models.Model):
    determinationid = models.AutoField(db_column='DeterminationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    addendum = models.CharField(db_column='Addendum', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alternatename = models.CharField(db_column='AlternateName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    confidence = models.CharField(db_column='Confidence', max_length=50, blank=True, null=True)  # Field name made lowercase.
    determineddate = models.DateField(db_column='DeterminedDate', blank=True, null=True)  # Field name made lowercase.
    determineddateprecision = models.IntegerField(db_column='DeterminedDatePrecision', blank=True, null=True)  # Field name made lowercase.
    featureorbasis = models.CharField(db_column='FeatureOrBasis', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iscurrent = models.TextField(db_column='IsCurrent')  # Field name made lowercase. This field type is a guess.
    method = models.CharField(db_column='Method', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nameusage = models.CharField(db_column='NameUsage', max_length=64, blank=True, null=True)  # Field name made lowercase.
    number1 = models.FloatField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.FloatField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    qualifier = models.CharField(db_column='Qualifier', max_length=16, blank=True, null=True)  # Field name made lowercase.
    varqualifer = models.CharField(db_column='VarQualifer', max_length=16, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    subspqualifier = models.CharField(db_column='SubSpQualifier', max_length=16, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    typestatusname = models.CharField(db_column='TypeStatusName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    varqualifier = models.CharField(db_column='VarQualifier', max_length=16, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    taxonid = models.IntegerField(db_column='TaxonID', blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.IntegerField(db_column='CollectionObjectID')  # Field name made lowercase.
    modifiedbyagentid = models.IntegerField(db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    determinerid = models.IntegerField(db_column='DeterminerID', blank=True, null=True)  # Field name made lowercase.
    preferredtaxonid = models.IntegerField(db_column='PreferredTaxonID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.IntegerField(db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'determination_dupes'


class Determinationcitation(models.Model):
    determinationcitationid = models.AutoField(db_column='DeterminationCitationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='determinationcitation_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    referenceworkid = models.ForeignKey('Referencework', models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.
    determinationid = models.ForeignKey(Determination, models.DO_NOTHING, db_column='DeterminationID')  # Field name made lowercase.
    figurenumber = models.CharField(db_column='FigureNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isfigured = models.TextField(db_column='IsFigured', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pagenumber = models.CharField(db_column='PageNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'determinationcitation'
        unique_together = (('referenceworkid', 'determinationid'),)


class Determiner(models.Model):
    determinerid = models.AutoField(db_column='DeterminerID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.TextField(db_column='IsPrimary')  # Field name made lowercase. This field type is a guess.
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    determinationid = models.ForeignKey(Determination, models.DO_NOTHING, db_column='DeterminationID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='determiner_agentid_set')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='determiner_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'determiner'
        unique_together = (('agentid', 'determinationid'),)


class Discipline(models.Model):
    usergroupscopeid = models.IntegerField(db_column='UserGroupScopeId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='discipline_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.IntegerField(db_column='disciplineId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    regnumber = models.CharField(db_column='RegNumber', max_length=24, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=64, blank=True, null=True)  # Field name made lowercase.
    geologictimeperiodtreedefid = models.ForeignKey('Geologictimeperiodtreedef', models.DO_NOTHING, db_column='GeologicTimePeriodTreeDefID')  # Field name made lowercase.
    lithostrattreedefid = models.ForeignKey('Lithostrattreedef', models.DO_NOTHING, db_column='LithoStratTreeDefID', blank=True, null=True)  # Field name made lowercase.
    geographytreedefid = models.ForeignKey('Geographytreedef', models.DO_NOTHING, db_column='GeographyTreeDefID')  # Field name made lowercase.
    datatypeid = models.ForeignKey(Datatype, models.DO_NOTHING, db_column='DataTypeID')  # Field name made lowercase.
    divisionid = models.ForeignKey('Division', models.DO_NOTHING, db_column='DivisionID')  # Field name made lowercase.
    taxontreedefid = models.ForeignKey('Taxontreedef', models.DO_NOTHING, db_column='TaxonTreeDefID', blank=True, null=True)  # Field name made lowercase.
    ispaleocontextembedded = models.TextField(db_column='IsPaleoContextEmbedded', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    paleocontextchildtable = models.CharField(db_column='PaleoContextChildTable', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discipline'


class Disposal(models.Model):
    disposalid = models.AutoField(db_column='DisposalID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    disposaldate = models.DateField(db_column='DisposalDate', blank=True, null=True)  # Field name made lowercase.
    disposalnumber = models.CharField(db_column='DisposalNumber', max_length=50)  # Field name made lowercase.
    donotexport = models.TextField(db_column='doNotExport', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=64, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deaccessionid = models.ForeignKey(Deaccession, models.DO_NOTHING, db_column='DeaccessionID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='disposal_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disposal'


class Disposalagent(models.Model):
    disposalagentid = models.AutoField(db_column='DisposalAgentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50)  # Field name made lowercase.
    disposalid = models.ForeignKey(Disposal, models.DO_NOTHING, db_column='DisposalID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='disposalagent_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='disposalagent_agentid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disposalagent'
        unique_together = (('role', 'agentid', 'disposalid'),)


class Disposalattachment(models.Model):
    disposalattachmentid = models.AutoField(db_column='DisposalAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    disposalid = models.ForeignKey(Disposal, models.DO_NOTHING, db_column='DisposalID')  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='disposalattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disposalattachment'


class Disposalpreparation(models.Model):
    disposalpreparationid = models.AutoField(db_column='DisposalPreparationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    loanreturnpreparationid = models.ForeignKey('Loanreturnpreparation', models.DO_NOTHING, db_column='LoanReturnPreparationID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    disposalid = models.ForeignKey(Disposal, models.DO_NOTHING, db_column='DisposalID')  # Field name made lowercase.
    preparationid = models.ForeignKey('Preparation', models.DO_NOTHING, db_column='PreparationID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='disposalpreparation_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disposalpreparation'


class Division(models.Model):
    usergroupscopeid = models.IntegerField(db_column='UserGroupScopeId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='division_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    abbrev = models.CharField(db_column='Abbrev', max_length=64, blank=True, null=True)  # Field name made lowercase.
    altname = models.CharField(db_column='AltName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    disciplinetype = models.CharField(db_column='DisciplineType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    divisionid = models.IntegerField(db_column='divisionId', blank=True, null=True)  # Field name made lowercase.
    iconuri = models.CharField(db_column='IconURI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regnumber = models.CharField(db_column='RegNumber', max_length=24, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    uri = models.CharField(db_column='Uri', max_length=255, blank=True, null=True)  # Field name made lowercase.
    institutionid = models.ForeignKey('Institution', models.DO_NOTHING, db_column='InstitutionID')  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'division'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
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


class Dnaprimer(models.Model):
    dnaprimerid = models.AutoField(db_column='DNAPrimerID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    primerdesignator = models.CharField(db_column='PrimerDesignator', max_length=64, blank=True, null=True)  # Field name made lowercase.
    primernameforward = models.CharField(db_column='PrimerNameForward', max_length=64, blank=True, null=True)  # Field name made lowercase.
    primernamereverse = models.CharField(db_column='PrimerNameReverse', max_length=64, blank=True, null=True)  # Field name made lowercase.
    primerreferencecitationforward = models.CharField(db_column='PrimerReferenceCitationForward', max_length=300, blank=True, null=True)  # Field name made lowercase.
    primerreferencecitationreverse = models.CharField(db_column='PrimerReferenceCitationReverse', max_length=300, blank=True, null=True)  # Field name made lowercase.
    primerreferencelinkforward = models.CharField(db_column='PrimerReferenceLinkForward', max_length=300, blank=True, null=True)  # Field name made lowercase.
    primerreferencelinkreverse = models.CharField(db_column='PrimerReferenceLinkReverse', max_length=300, blank=True, null=True)  # Field name made lowercase.
    primersequenceforward = models.CharField(db_column='PrimerSequenceForward', max_length=128, blank=True, null=True)  # Field name made lowercase.
    primersequencereverse = models.CharField(db_column='PrimerSequenceReverse', max_length=128, blank=True, null=True)  # Field name made lowercase.
    purificationmethod = models.CharField(db_column='purificationMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    reservedinteger3 = models.IntegerField(db_column='ReservedInteger3', blank=True, null=True)  # Field name made lowercase.
    reservedinteger4 = models.IntegerField(db_column='ReservedInteger4', blank=True, null=True)  # Field name made lowercase.
    reservednumber3 = models.DecimalField(db_column='ReservedNumber3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    reservednumber4 = models.DecimalField(db_column='ReservedNumber4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    reservedtext3 = models.TextField(db_column='ReservedText3', blank=True, null=True)  # Field name made lowercase.
    reservedtext4 = models.TextField(db_column='ReservedText4', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='dnaprimer_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dnaprimer'


class Dnasequence(models.Model):
    dnasequenceid = models.AutoField(db_column='DnaSequenceID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    ambiguousresidues = models.IntegerField(db_column='AmbiguousResidues', blank=True, null=True)  # Field name made lowercase.
    boldbarcodeid = models.CharField(db_column='BOLDBarcodeID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    boldlastupdatedate = models.DateField(db_column='BOLDLastUpdateDate', blank=True, null=True)  # Field name made lowercase.
    boldsampleid = models.CharField(db_column='BOLDSampleID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    boldtranslationmatrix = models.CharField(db_column='BOLDTranslationMatrix', max_length=64, blank=True, null=True)  # Field name made lowercase.
    compa = models.IntegerField(db_column='CompA', blank=True, null=True)  # Field name made lowercase.
    compc = models.IntegerField(db_column='CompC', blank=True, null=True)  # Field name made lowercase.
    compg = models.IntegerField(db_column='CompG', blank=True, null=True)  # Field name made lowercase.
    compt = models.IntegerField(db_column='compT', blank=True, null=True)  # Field name made lowercase.
    genbankaccessionnumber = models.CharField(db_column='GenBankAccessionNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    genesequence = models.TextField(db_column='GeneSequence', blank=True, null=True)  # Field name made lowercase.
    moleculetype = models.CharField(db_column='MoleculeType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    targetmarker = models.CharField(db_column='TargetMarker', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=64, blank=True, null=True)  # Field name made lowercase.
    totalresidues = models.IntegerField(db_column='TotalResidues', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='dnasequence_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='dnasequence_agentid_set', blank=True, null=True)  # Field name made lowercase.
    materialsampleid = models.ForeignKey('Materialsample', models.DO_NOTHING, db_column='MaterialSampleID', blank=True, null=True)  # Field name made lowercase.
    extractiondate = models.DateField(db_column='ExtractionDate', blank=True, null=True)  # Field name made lowercase.
    extractiondateprecision = models.IntegerField(db_column='ExtractionDatePrecision', blank=True, null=True)  # Field name made lowercase.
    sequencedate = models.DateField(db_column='SequenceDate', blank=True, null=True)  # Field name made lowercase.
    sequencedateprecision = models.IntegerField(db_column='SequenceDatePrecision', blank=True, null=True)  # Field name made lowercase.
    extractorid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ExtractorID', related_name='dnasequence_extractorid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dnasequence'


class Dnasequenceattachment(models.Model):
    dnasequenceattachmentid = models.AutoField(db_column='DnaSequenceAttachmentId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    dnasequenceid = models.ForeignKey(Dnasequence, models.DO_NOTHING, db_column='DnaSequenceID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='dnasequenceattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dnasequenceattachment'


class Dnasequencerunattachment(models.Model):
    dnasequencingrunattachmentid = models.AutoField(db_column='DnaSequencingRunAttachmentId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='dnasequencerunattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    dnasequencingrunid = models.ForeignKey('Dnasequencingrun', models.DO_NOTHING, db_column='DnaSequencingRunID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dnasequencerunattachment'


class Dnasequencingrun(models.Model):
    dnasequencingrunid = models.AutoField(db_column='DNASequencingRunID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.
    pcrcocktailprimer = models.TextField(db_column='PCRCocktailPrimer', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pcrforwardprimercode = models.CharField(db_column='PCRForwardPrimerCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    pcrprimername = models.CharField(db_column='PCRPrimerName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    pcrprimersequence5_3 = models.CharField(db_column='PCRPrimerSequence5_3', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pcrreverseprimercode = models.CharField(db_column='PCRReversePrimerCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    readdirection = models.CharField(db_column='ReadDirection', max_length=16, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    rundate = models.DateField(db_column='RunDate', blank=True, null=True)  # Field name made lowercase.
    scorefilename = models.CharField(db_column='ScoreFileName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sequencecocktailprimer = models.TextField(db_column='SequenceCocktailPrimer', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sequenceprimercode = models.CharField(db_column='SequencePrimerCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sequenceprimername = models.CharField(db_column='SequencePrimerName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sequenceprimersequence5_3 = models.CharField(db_column='SequencePrimerSequence5_3', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tracefilename = models.CharField(db_column='TraceFileName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preparedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='PreparedByAgentID', blank=True, null=True)  # Field name made lowercase.
    runbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='RunByAgentID', related_name='dnasequencingrun_runbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    dnasequenceid = models.ForeignKey(Dnasequence, models.DO_NOTHING, db_column='DNASequenceID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='dnasequencingrun_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='dnasequencingrun_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    genesequence = models.TextField(db_column='GeneSequence', blank=True, null=True)  # Field name made lowercase.
    dryaddoi = models.CharField(db_column='DryadDOI', max_length=256, blank=True, null=True)  # Field name made lowercase.
    sraexperimentid = models.CharField(db_column='SRAExperimentID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    srarunid = models.CharField(db_column='SRARunID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    srasubmissionid = models.CharField(db_column='SRASubmissionID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dnaprimerid = models.ForeignKey(Dnaprimer, models.DO_NOTHING, db_column='DNAPrimerID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dnasequencingrun'


class Dnasequencingruncitation(models.Model):
    dnasequencingruncitationid = models.AutoField(db_column='DNASequencingRunCitationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    referenceworkid = models.ForeignKey('Referencework', models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='dnasequencingruncitation_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    dnasequencingrunid = models.ForeignKey(Dnasequencingrun, models.DO_NOTHING, db_column='DNASequencingRunID')  # Field name made lowercase.
    figurenumber = models.CharField(db_column='FigureNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isfigured = models.TextField(db_column='IsFigured', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pagenumber = models.CharField(db_column='PageNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dnasequencingruncitation'


class Exchangein(models.Model):
    exchangeinid = models.AutoField(db_column='ExchangeInID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    descriptionofmaterial = models.CharField(db_column='DescriptionOfMaterial', max_length=120, blank=True, null=True)  # Field name made lowercase.
    exchangedate = models.DateField(db_column='ExchangeDate', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    quantityexchanged = models.SmallIntegerField(db_column='QuantityExchanged', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    srcgeography = models.CharField(db_column='SrcGeography', max_length=32, blank=True, null=True)  # Field name made lowercase.
    srctaxonomy = models.CharField(db_column='SrcTaxonomy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.ForeignKey(Division, models.DO_NOTHING, db_column='DivisionID')  # Field name made lowercase.
    addressofrecordid = models.ForeignKey(Addressofrecord, models.DO_NOTHING, db_column='AddressOfRecordID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='exchangein_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    receivedfromorganizationid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ReceivedFromOrganizationID', related_name='exchangein_receivedfromorganizationid_set')  # Field name made lowercase.
    catalogedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CatalogedByID', related_name='exchangein_catalogedbyid_set')  # Field name made lowercase.
    contents = models.TextField(db_column='Contents', blank=True, null=True)  # Field name made lowercase.
    exchangeinnumber = models.CharField(db_column='ExchangeInNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangein'


class Exchangeinattachment(models.Model):
    exchangeinattachmentid = models.AutoField(db_column='ExchangeInAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='exchangeinattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    exchangeinid = models.ForeignKey(Exchangein, models.DO_NOTHING, db_column='ExchangeInID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangeinattachment'


class Exchangeinprep(models.Model):
    exchangeinprepid = models.AutoField(db_column='ExchangeInPrepID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    descriptionofmaterial = models.CharField(db_column='DescriptionOfMaterial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number1 = models.IntegerField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    exchangeinid = models.ForeignKey(Exchangein, models.DO_NOTHING, db_column='ExchangeInID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    preparationid = models.ForeignKey('Preparation', models.DO_NOTHING, db_column='PreparationID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='exchangeinprep_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangeinprep'


class Exchangeout(models.Model):
    exchangeoutid = models.AutoField(db_column='ExchangeOutID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    descriptionofmaterial = models.CharField(db_column='DescriptionOfMaterial', max_length=120, blank=True, null=True)  # Field name made lowercase.
    exchangedate = models.DateField(db_column='ExchangeDate', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    quantityexchanged = models.SmallIntegerField(db_column='QuantityExchanged', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    srcgeography = models.CharField(db_column='SrcGeography', max_length=32, blank=True, null=True)  # Field name made lowercase.
    srctaxonomy = models.CharField(db_column='SrcTaxonomy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    senttoorganizationid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='SentToOrganizationID', related_name='exchangeout_senttoorganizationid_set')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='exchangeout_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    addressofrecordid = models.ForeignKey(Addressofrecord, models.DO_NOTHING, db_column='AddressOfRecordID', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.ForeignKey(Division, models.DO_NOTHING, db_column='DivisionID')  # Field name made lowercase.
    catalogedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CatalogedByID', related_name='exchangeout_catalogedbyid_set')  # Field name made lowercase.
    contents = models.TextField(db_column='Contents', blank=True, null=True)  # Field name made lowercase.
    exchangeoutnumber = models.CharField(db_column='ExchangeOutNumber', max_length=50)  # Field name made lowercase.
    deaccessionid = models.ForeignKey(Deaccession, models.DO_NOTHING, db_column='DeaccessionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangeout'


class Exchangeoutattachment(models.Model):
    exchangeoutattachmentid = models.AutoField(db_column='ExchangeOutAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='exchangeoutattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    exchangeoutid = models.ForeignKey(Exchangeout, models.DO_NOTHING, db_column='ExchangeOutID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangeoutattachment'


class Exchangeoutprep(models.Model):
    exchangeoutprepid = models.AutoField(db_column='ExchangeOutPrepID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    descriptionofmaterial = models.CharField(db_column='DescriptionOfMaterial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number1 = models.IntegerField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    preparationid = models.ForeignKey('Preparation', models.DO_NOTHING, db_column='PreparationID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='exchangeoutprep_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    exchangeoutid = models.ForeignKey(Exchangeout, models.DO_NOTHING, db_column='ExchangeOutID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchangeoutprep'


class Exsiccata(models.Model):
    exsiccataid = models.AutoField(db_column='ExsiccataID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    referenceworkid = models.ForeignKey('Referencework', models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='exsiccata_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    schedae = models.CharField(db_column='Schedae', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exsiccata'


class Exsiccataitem(models.Model):
    exsiccataitemid = models.AutoField(db_column='ExsiccataItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fascicle = models.CharField(db_column='Fascicle', max_length=16, blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=16, blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='exsiccataitem_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    exsiccataid = models.ForeignKey(Exsiccata, models.DO_NOTHING, db_column='ExsiccataID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exsiccataitem'


class Extractor(models.Model):
    extractorid = models.AutoField(db_column='ExtractorID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    dnasequenceid = models.ForeignKey(Dnasequence, models.DO_NOTHING, db_column='DNASequenceID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='extractor_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='extractor_agentid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extractor'
        unique_together = (('agentid', 'dnasequenceid'),)


class Fieldnotebook(models.Model):
    fieldnotebookid = models.AutoField(db_column='FieldNotebookID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    storage = models.CharField(db_column='Storage', max_length=64, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='fieldnotebook_agentid_set')  # Field name made lowercase.
    collectionid = models.ForeignKey(Collection, models.DO_NOTHING, db_column='CollectionID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='fieldnotebook_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fieldnotebook'


class Fieldnotebookattachment(models.Model):
    fieldnotebookattachmentid = models.AutoField(db_column='FieldNotebookAttachmentId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    fieldnotebookid = models.ForeignKey(Fieldnotebook, models.DO_NOTHING, db_column='FieldNotebookID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='fieldnotebookattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fieldnotebookattachment'


class Fieldnotebookpage(models.Model):
    fieldnotebookpageid = models.AutoField(db_column='FieldNotebookPageID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=128, blank=True, null=True)  # Field name made lowercase.
    pagenumber = models.CharField(db_column='PageNumber', max_length=32)  # Field name made lowercase.
    scandate = models.DateField(db_column='ScanDate', blank=True, null=True)  # Field name made lowercase.
    fieldnotebookpagesetid = models.ForeignKey('Fieldnotebookpageset', models.DO_NOTHING, db_column='FieldNotebookPageSetID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='fieldnotebookpage_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fieldnotebookpage'


class Fieldnotebookpageattachment(models.Model):
    fieldnotebookpageattachmentid = models.AutoField(db_column='FieldNotebookPageAttachmentId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='fieldnotebookpageattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    fieldnotebookpageid = models.ForeignKey(Fieldnotebookpage, models.DO_NOTHING, db_column='FieldNotebookPageID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fieldnotebookpageattachment'


class Fieldnotebookpageset(models.Model):
    fieldnotebookpagesetid = models.AutoField(db_column='FieldNotebookPageSetID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=128, blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.SmallIntegerField(db_column='OrderNumber', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', blank=True, null=True)  # Field name made lowercase.
    fieldnotebookid = models.ForeignKey(Fieldnotebook, models.DO_NOTHING, db_column='FieldNotebookID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='fieldnotebookpageset_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='fieldnotebookpageset_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fieldnotebookpageset'


class Fieldnotebookpagesetattachment(models.Model):
    fieldnotebookpagesetattachmentid = models.AutoField(db_column='FieldNotebookPageSetAttachmentId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    fieldnotebookpagesetid = models.ForeignKey(Fieldnotebookpageset, models.DO_NOTHING, db_column='FieldNotebookPageSetID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='fieldnotebookpagesetattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fieldnotebookpagesetattachment'


class Fundingagent(models.Model):
    fundingagentid = models.AutoField(db_column='FundingAgentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.TextField(db_column='IsPrimary')  # Field name made lowercase. This field type is a guess.
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='fundingagent_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    collectingtripid = models.ForeignKey(Collectingtrip, models.DO_NOTHING, db_column='CollectingTripID')  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='fundingagent_agentid_set')  # Field name made lowercase.
    divisionid = models.ForeignKey(Division, models.DO_NOTHING, db_column='DivisionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fundingagent'
        unique_together = (('agentid', 'collectingtripid'),)


class Geocoorddetail(models.Model):
    geocoorddetailid = models.AutoField(db_column='GeoCoordDetailID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    georefaccuracyunits = models.CharField(db_column='GeoRefAccuracyUnits', max_length=20, blank=True, null=True)  # Field name made lowercase.
    georefdetdate = models.DateTimeField(db_column='GeoRefDetDate', blank=True, null=True)  # Field name made lowercase.
    georefdetref = models.CharField(db_column='GeoRefDetRef', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georefremarks = models.TextField(db_column='GeoRefRemarks', blank=True, null=True)  # Field name made lowercase.
    georefverificationstatus = models.CharField(db_column='GeoRefVerificationStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maxuncertaintyest = models.DecimalField(db_column='MaxUncertaintyEst', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    maxuncertaintyestunit = models.CharField(db_column='MaxUncertaintyEstUnit', max_length=8, blank=True, null=True)  # Field name made lowercase.
    uncertaintypolygon = models.TextField(db_column='UncertaintyPolygon', blank=True, null=True)  # Field name made lowercase.
    errorpolygon = models.TextField(db_column='ErrorPolygon', blank=True, null=True)  # Field name made lowercase.
    namedplaceextent = models.DecimalField(db_column='NamedPlaceExtent', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    nogeorefbecause = models.CharField(db_column='NoGeoRefBecause', max_length=100, blank=True, null=True)  # Field name made lowercase.
    originalcoordsystem = models.CharField(db_column='OriginalCoordSystem', max_length=32, blank=True, null=True)  # Field name made lowercase.
    protocol = models.CharField(db_column='Protocol', max_length=64, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=64, blank=True, null=True)  # Field name made lowercase.
    validation = models.CharField(db_column='Validation', max_length=64, blank=True, null=True)  # Field name made lowercase.
    localityid = models.ForeignKey('Locality', models.DO_NOTHING, db_column='LocalityID', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='geocoorddetail_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='geocoorddetail_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    georefaccuracy = models.DecimalField(db_column='GeoRefAccuracy', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    georefcompileddate = models.DateTimeField(db_column='GeoRefCompiledDate', blank=True, null=True)  # Field name made lowercase.
    compiledbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CompiledByID', related_name='geocoorddetail_compiledbyid_set', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.IntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.IntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'geocoorddetail'


class Geography(models.Model):
    geographyid = models.AutoField(db_column='GeographyID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    abbrev = models.CharField(db_column='Abbrev', max_length=16, blank=True, null=True)  # Field name made lowercase.
    centroidlat = models.DecimalField(db_column='CentroidLat', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    centroidlon = models.DecimalField(db_column='CentroidLon', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    geographycode = models.CharField(db_column='GeographyCode', max_length=24, blank=True, null=True)  # Field name made lowercase.
    gml = models.TextField(db_column='GML', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    highestchildnodenumber = models.IntegerField(db_column='HighestChildNodeNumber', blank=True, null=True)  # Field name made lowercase.
    isaccepted = models.TextField(db_column='IsAccepted', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iscurrent = models.TextField(db_column='IsCurrent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nodenumber = models.IntegerField(db_column='NodeNumber', blank=True, null=True)  # Field name made lowercase.
    number1 = models.IntegerField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.IntegerField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    timestampversion = models.DateTimeField(db_column='TimestampVersion', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='geography_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    geographytreedefid = models.ForeignKey('Geographytreedef', models.DO_NOTHING, db_column='GeographyTreeDefID')  # Field name made lowercase.
    acceptedid = models.ForeignKey('self', models.DO_NOTHING, db_column='AcceptedID', related_name='geography_acceptedid_set', blank=True, null=True)  # Field name made lowercase.
    geographytreedefitemid = models.ForeignKey('Geographytreedefitem', models.DO_NOTHING, db_column='GeographyTreeDefItemID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geography'


class Geographytreedef(models.Model):
    geographytreedefid = models.AutoField(db_column='GeographyTreeDefID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullnamedirection = models.IntegerField(db_column='FullNameDirection', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='geographytreedef_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geographytreedef'


class Geographytreedefitem(models.Model):
    geographytreedefitemid = models.AutoField(db_column='GeographyTreeDefItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullnameseparator = models.CharField(db_column='FullNameSeparator', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isenforced = models.TextField(db_column='IsEnforced', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isinfullname = models.TextField(db_column='IsInFullName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    textafter = models.CharField(db_column='TextAfter', max_length=64, blank=True, null=True)  # Field name made lowercase.
    textbefore = models.CharField(db_column='TextBefore', max_length=64, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    geographytreedefid = models.ForeignKey(Geographytreedef, models.DO_NOTHING, db_column='GeographyTreeDefID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    parentitemid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentItemID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='geographytreedefitem_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geographytreedefitem'


class Geologictimeperiod(models.Model):
    geologictimeperiodid = models.AutoField(db_column='GeologicTimePeriodID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    endperiod = models.DecimalField(db_column='EndPeriod', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    enduncertainty = models.DecimalField(db_column='EndUncertainty', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    highestchildnodenumber = models.IntegerField(db_column='HighestChildNodeNumber', blank=True, null=True)  # Field name made lowercase.
    isaccepted = models.TextField(db_column='IsAccepted', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isbiostrat = models.TextField(db_column='IsBioStrat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    nodenumber = models.IntegerField(db_column='NodeNumber', blank=True, null=True)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    standard = models.CharField(db_column='Standard', max_length=64, blank=True, null=True)  # Field name made lowercase.
    startperiod = models.DecimalField(db_column='StartPeriod', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    startuncertainty = models.DecimalField(db_column='StartUncertainty', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    geologictimeperiodtreedefitemid = models.ForeignKey('Geologictimeperiodtreedefitem', models.DO_NOTHING, db_column='GeologicTimePeriodTreeDefItemID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    geologictimeperiodtreedefid = models.ForeignKey('Geologictimeperiodtreedef', models.DO_NOTHING, db_column='GeologicTimePeriodTreeDefID')  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    acceptedid = models.ForeignKey('self', models.DO_NOTHING, db_column='AcceptedID', related_name='geologictimeperiod_acceptedid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='geologictimeperiod_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geologictimeperiod'


class Geologictimeperiodtreedef(models.Model):
    geologictimeperiodtreedefid = models.AutoField(db_column='GeologicTimePeriodTreeDefID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullnamedirection = models.IntegerField(db_column='FullNameDirection', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='geologictimeperiodtreedef_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geologictimeperiodtreedef'


class Geologictimeperiodtreedefitem(models.Model):
    geologictimeperiodtreedefitemid = models.AutoField(db_column='GeologicTimePeriodTreeDefItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullnameseparator = models.CharField(db_column='FullNameSeparator', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isenforced = models.TextField(db_column='IsEnforced', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isinfullname = models.TextField(db_column='IsInFullName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    textafter = models.CharField(db_column='TextAfter', max_length=64, blank=True, null=True)  # Field name made lowercase.
    textbefore = models.CharField(db_column='TextBefore', max_length=64, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    geologictimeperiodtreedefid = models.ForeignKey(Geologictimeperiodtreedef, models.DO_NOTHING, db_column='GeologicTimePeriodTreeDefID')  # Field name made lowercase.
    parentitemid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentItemID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='geologictimeperiodtreedefitem_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geologictimeperiodtreedefitem'


class Geoname(models.Model):
    geonameid = models.IntegerField(db_column='geonameId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    asciiname = models.CharField(max_length=255, blank=True, null=True)
    alternatenames = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=7, blank=True, null=True)
    fclass = models.CharField(max_length=1, blank=True, null=True)
    fcode = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    cc2 = models.CharField(max_length=60, blank=True, null=True)
    admin1 = models.CharField(max_length=20, blank=True, null=True)
    admin2 = models.CharField(max_length=80, blank=True, null=True)
    admin3 = models.CharField(max_length=20, blank=True, null=True)
    admin4 = models.CharField(max_length=20, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    gtopo30 = models.IntegerField(blank=True, null=True)
    timezone = models.CharField(max_length=40, blank=True, null=True)
    moddate = models.DateField(blank=True, null=True)
    isocode = models.CharField(db_column='ISOCode', max_length=24, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geoname'


class GeorefCch(models.Model):
    herbariumaccnum = models.CharField(db_column='HerbariumAccNum', primary_key=True, max_length=50)  # Field name made lowercase.
    latitudedegreesdecimal = models.DecimalField(db_column='LatitudeDegreesDecimal', max_digits=18, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    longitudedegreesdecimal = models.DecimalField(db_column='LongitudeDegreesDecimal', max_digits=18, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=64, blank=True, null=True)  # Field name made lowercase.
    datum = models.CharField(db_column='Datum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errorradius = models.CharField(db_column='ErrorRadius', max_length=50, blank=True, null=True)  # Field name made lowercase.
    errorunits = models.CharField(db_column='ErrorUnits', max_length=50, blank=True, null=True)  # Field name made lowercase.
    georeferencer = models.CharField(db_column='Georeferencer', max_length=128, blank=True, null=True)  # Field name made lowercase.
    herbarium = models.CharField(db_column='Herbarium', max_length=3, blank=True, null=True)  # Field name made lowercase.
    accessionnumber = models.CharField(db_column='AccessionNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.IntegerField(blank=True, null=True)
    localityid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'georef_cch'


class Gift(models.Model):
    giftid = models.AutoField(db_column='GiftID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    giftdate = models.DateField(db_column='GiftDate', blank=True, null=True)  # Field name made lowercase.
    giftnumber = models.CharField(db_column='GiftNumber', max_length=50)  # Field name made lowercase.
    isfinancialresponsibility = models.TextField(db_column='IsFinancialResponsibility', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    purposeofgift = models.CharField(db_column='PurposeOfGift', max_length=64, blank=True, null=True)  # Field name made lowercase.
    receivedcomments = models.CharField(db_column='ReceivedComments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    specialconditions = models.TextField(db_column='SpecialConditions', blank=True, null=True)  # Field name made lowercase.
    srcgeography = models.CharField(db_column='SrcGeography', max_length=500, blank=True, null=True)  # Field name made lowercase.
    srctaxonomy = models.CharField(db_column='SrcTaxonomy', max_length=500, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    addressofrecordid = models.ForeignKey(Addressofrecord, models.DO_NOTHING, db_column='AddressOfRecordID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='gift_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.ForeignKey(Division, models.DO_NOTHING, db_column='DivisionID', blank=True, null=True)  # Field name made lowercase.
    contents = models.TextField(db_column='Contents', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deaccessionid = models.ForeignKey(Deaccession, models.DO_NOTHING, db_column='DeaccessionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gift'


class Giftagent(models.Model):
    giftagentid = models.AutoField(db_column='GiftAgentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='giftagent_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='giftagent_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    giftid = models.ForeignKey(Gift, models.DO_NOTHING, db_column='GiftID')  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'giftagent'
        unique_together = (('role', 'giftid', 'agentid'),)


class Giftattachment(models.Model):
    giftattachmentid = models.AutoField(db_column='GiftAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='giftattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    giftid = models.ForeignKey(Gift, models.DO_NOTHING, db_column='GiftID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'giftattachment'


class Giftpreparation(models.Model):
    giftpreparationid = models.AutoField(db_column='GiftPreparationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    descriptionofmaterial = models.CharField(db_column='DescriptionOfMaterial', max_length=255, blank=True, null=True)  # Field name made lowercase.
    incomments = models.TextField(db_column='InComments', blank=True, null=True)  # Field name made lowercase.
    outcomments = models.TextField(db_column='OutComments', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    receivedcomments = models.TextField(db_column='ReceivedComments', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='giftpreparation_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    giftid = models.ForeignKey(Gift, models.DO_NOTHING, db_column='GiftID', blank=True, null=True)  # Field name made lowercase.
    preparationid = models.ForeignKey('Preparation', models.DO_NOTHING, db_column='PreparationID', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'giftpreparation'


class Groupperson(models.Model):
    grouppersonid = models.AutoField(db_column='GroupPersonID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.SmallIntegerField(db_column='OrderNumber')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    memberid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='MemberID', related_name='groupperson_memberid_set')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='groupperson_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    groupid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='GroupID', related_name='groupperson_groupid_set')  # Field name made lowercase.
    divisionid = models.ForeignKey(Division, models.DO_NOTHING, db_column='DivisionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'groupperson'
        unique_together = (('ordernumber', 'groupid'),)


class HibernateUniqueKey(models.Model):
    next_hi = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hibernate_unique_key'


class Inforequest(models.Model):
    inforequestid = models.AutoField(db_column='InfoRequestID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inforeqnumber = models.CharField(db_column='InfoReqNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    institution = models.CharField(db_column='Institution', max_length=127, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    replydate = models.DateField(db_column='ReplyDate', blank=True, null=True)  # Field name made lowercase.
    requestdate = models.DateField(db_column='RequestDate', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='inforequest_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='inforequest_agentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inforequest'


class Institution(models.Model):
    usergroupscopeid = models.IntegerField(db_column='UserGroupScopeId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='institution_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    altname = models.CharField(db_column='AltName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=64, blank=True, null=True)  # Field name made lowercase.
    copyright = models.TextField(db_column='Copyright', blank=True, null=True)  # Field name made lowercase.
    currentmanagedrelversion = models.CharField(db_column='CurrentManagedRelVersion', max_length=8, blank=True, null=True)  # Field name made lowercase.
    currentmanagedschemaversion = models.CharField(db_column='CurrentManagedSchemaVersion', max_length=8, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    disclaimer = models.TextField(db_column='Disclaimer', blank=True, null=True)  # Field name made lowercase.
    hasbeenasked = models.TextField(db_column='HasBeenAsked', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iconuri = models.CharField(db_column='IconURI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    institutionid = models.IntegerField(db_column='institutionId', blank=True, null=True)  # Field name made lowercase.
    ipr = models.TextField(db_column='Ipr', blank=True, null=True)  # Field name made lowercase.
    isaccessionsglobal = models.TextField(db_column='IsAccessionsGlobal')  # Field name made lowercase. This field type is a guess.
    isanonymous = models.TextField(db_column='IsAnonymous', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isreleasemanagedglobally = models.TextField(db_column='IsReleaseManagedGlobally', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    issecurityon = models.TextField(db_column='IsSecurityOn')  # Field name made lowercase. This field type is a guess.
    isserverbased = models.TextField(db_column='IsServerBased')  # Field name made lowercase. This field type is a guess.
    issharinglocalities = models.TextField(db_column='IsSharingLocalities')  # Field name made lowercase. This field type is a guess.
    issinglegeographytree = models.TextField(db_column='IsSingleGeographyTree')  # Field name made lowercase. This field type is a guess.
    license = models.TextField(db_column='License', blank=True, null=True)  # Field name made lowercase.
    lsidauthority = models.CharField(db_column='LsidAuthority', max_length=64, blank=True, null=True)  # Field name made lowercase.
    minimumpwdlength = models.IntegerField(db_column='MinimumPwdLength', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regnumber = models.CharField(db_column='RegNumber', max_length=24, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    termsofuse = models.TextField(db_column='TermsOfUse', blank=True, null=True)  # Field name made lowercase.
    uri = models.CharField(db_column='Uri', max_length=255, blank=True, null=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    storagetreedefid = models.ForeignKey('Storagetreedef', models.DO_NOTHING, db_column='StorageTreeDefID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'institution'


class Institutionnetwork(models.Model):
    institutionnetworkid = models.AutoField(db_column='InstitutionNetworkID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    altname = models.CharField(db_column='AltName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=64, blank=True, null=True)  # Field name made lowercase.
    copyright = models.TextField(db_column='Copyright', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    disclaimer = models.TextField(db_column='Disclaimer', blank=True, null=True)  # Field name made lowercase.
    iconuri = models.CharField(db_column='IconURI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ipr = models.TextField(db_column='Ipr', blank=True, null=True)  # Field name made lowercase.
    license = models.TextField(db_column='License', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    termsofuse = models.TextField(db_column='TermsOfUse', blank=True, null=True)  # Field name made lowercase.
    uri = models.CharField(db_column='Uri', max_length=255, blank=True, null=True)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='institutionnetwork_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'institutionnetwork'


class IosColobjagents(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_colobjagents'


class IosColobjbio(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_colobjbio'


class IosColobjchron(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_colobjchron'


class IosColobjcnts(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_colobjcnts'


class IosColobjgeo(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_colobjgeo'


class IosColobjlitho(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_colobjlitho'


class IosGeogeoCnt(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_geogeo_cnt'


class IosGeogeoCty(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_geogeo_cty'


class IosGeoloc(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_geoloc'


class IosGeolocCnt(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_geoloc_cnt'


class IosGeolocCty(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_geoloc_cty'


class IosTaxonPid(models.Model):
    oldid = models.IntegerField(db_column='OldID', primary_key=True)  # Field name made lowercase.
    newid = models.IntegerField(db_column='NewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ios_taxon_pid'


class Journal(models.Model):
    journalid = models.AutoField(db_column='JournalID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    issn = models.CharField(db_column='ISSN', max_length=16, blank=True, null=True)  # Field name made lowercase.
    journalabbreviation = models.CharField(db_column='JournalAbbreviation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    journalname = models.CharField(db_column='JournalName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institution, models.DO_NOTHING, db_column='InstitutionID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='journal_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'journal'


class Latlonpolygon(models.Model):
    latlonpolygonid = models.AutoField(db_column='LatLonPolygonID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    ispolyline = models.TextField(db_column='IsPolyline')  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    localityid = models.ForeignKey('Locality', models.DO_NOTHING, db_column='LocalityID', blank=True, null=True)  # Field name made lowercase.
    spvisualqueryid = models.ForeignKey('Spvisualquery', models.DO_NOTHING, db_column='SpVisualQueryID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='latlonpolygon_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'latlonpolygon'


class Latlonpolygonpnt(models.Model):
    latlonpolygonpntid = models.AutoField(db_column='LatLonPolygonPntID', primary_key=True)  # Field name made lowercase.
    elevation = models.IntegerField(db_column='Elevation', blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=12, decimal_places=10)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=12, decimal_places=10)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    latlonpolygonid = models.ForeignKey(Latlonpolygon, models.DO_NOTHING, db_column='LatLonPolygonID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'latlonpolygonpnt'


class LichenFamilyGenus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    family = models.CharField(db_column='Family', max_length=50, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(db_column='Genus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lichen_family_genus'


class Lichenportal(models.Model):
    id = models.IntegerField(primary_key=True)
    institutioncode = models.CharField(db_column='institutionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    collectioncode = models.CharField(db_column='collectionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ownerinstitutioncode = models.CharField(db_column='ownerInstitutionCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    collectionid = models.CharField(db_column='collectionID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    basisofrecord = models.CharField(db_column='basisOfRecord', max_length=100, blank=True, null=True)  # Field name made lowercase.
    occurrenceid = models.CharField(db_column='occurrenceID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    catalognumber = models.CharField(db_column='catalogNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    othercatalognumbers = models.CharField(db_column='otherCatalogNumbers', max_length=100, blank=True, null=True)  # Field name made lowercase.
    higherclassification = models.CharField(db_column='higherClassification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kingdom = models.CharField(max_length=100, blank=True, null=True)
    phylum = models.CharField(max_length=100, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    order = models.CharField(max_length=100, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    scientificname = models.CharField(db_column='scientificName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxonid = models.CharField(db_column='taxonID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scientificnameauthorship = models.CharField(db_column='scientificNameAuthorship', max_length=100, blank=True, null=True)  # Field name made lowercase.
    genus = models.CharField(max_length=100, blank=True, null=True)
    subgenus = models.CharField(max_length=100, blank=True, null=True)
    specificepithet = models.CharField(db_column='specificEpithet', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimtaxonrank = models.CharField(db_column='verbatimTaxonRank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    infraspecificepithet = models.CharField(db_column='infraspecificEpithet', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxonrank = models.CharField(db_column='taxonRank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identifiedby = models.CharField(db_column='identifiedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateidentified = models.CharField(db_column='dateIdentified', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationreferences = models.CharField(db_column='identificationReferences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationremarks = models.TextField(db_column='identificationRemarks', blank=True, null=True)  # Field name made lowercase.
    taxonremarks = models.CharField(db_column='taxonRemarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    identificationqualifier = models.CharField(db_column='identificationQualifier', max_length=100, blank=True, null=True)  # Field name made lowercase.
    typestatus = models.CharField(db_column='typeStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordedby = models.CharField(db_column='recordedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    associatedcollectors = models.CharField(db_column='associatedCollectors', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordnumber = models.CharField(db_column='recordNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventdate = models.CharField(db_column='eventDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventdate2 = models.CharField(db_column='eventDate2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(max_length=100, blank=True, null=True)
    month = models.CharField(max_length=100, blank=True, null=True)
    day = models.CharField(max_length=100, blank=True, null=True)
    startdayofyear = models.CharField(db_column='startDayOfYear', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enddayofyear = models.CharField(db_column='endDayOfYear', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimeventdate = models.CharField(db_column='verbatimEventDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    occurrenceremarks = models.TextField(db_column='occurrenceRemarks', blank=True, null=True)  # Field name made lowercase.
    habitat = models.TextField(blank=True, null=True)
    substrate = models.CharField(max_length=255, blank=True, null=True)
    verbatimattributes = models.TextField(db_column='verbatimAttributes', blank=True, null=True)  # Field name made lowercase.
    fieldnumber = models.CharField(db_column='fieldNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    informationwithheld = models.CharField(db_column='informationWithheld', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datageneralizations = models.CharField(db_column='dataGeneralizations', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dynamicproperties = models.TextField(db_column='dynamicProperties', blank=True, null=True)  # Field name made lowercase.
    associatedoccurrences = models.TextField(db_column='associatedOccurrences', blank=True, null=True)  # Field name made lowercase.
    associatedsequences = models.CharField(db_column='associatedSequences', max_length=100, blank=True, null=True)  # Field name made lowercase.
    associatedtaxa = models.TextField(db_column='associatedTaxa', blank=True, null=True)  # Field name made lowercase.
    reproductivecondition = models.CharField(db_column='reproductiveCondition', max_length=100, blank=True, null=True)  # Field name made lowercase.
    establishmentmeans = models.CharField(db_column='establishmentMeans', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cultivationstatus = models.CharField(db_column='cultivationStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lifestage = models.CharField(db_column='lifeStage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=100, blank=True, null=True)
    individualcount = models.CharField(db_column='individualCount', max_length=100, blank=True, null=True)  # Field name made lowercase.
    preparations = models.CharField(max_length=100, blank=True, null=True)
    locationid = models.CharField(db_column='locationID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(max_length=100, blank=True, null=True)
    waterbody = models.CharField(db_column='waterBody', max_length=100, blank=True, null=True)  # Field name made lowercase.
    islandgroup = models.CharField(db_column='islandGroup', max_length=100, blank=True, null=True)  # Field name made lowercase.
    island = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    stateprovince = models.CharField(db_column='stateProvince', max_length=100, blank=True, null=True)  # Field name made lowercase.
    county = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    locationremarks = models.TextField(db_column='locationRemarks', blank=True, null=True)  # Field name made lowercase.
    localitysecurity = models.CharField(db_column='localitySecurity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    localitysecurityreason = models.CharField(db_column='localitySecurityReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    decimallatitude = models.CharField(db_column='decimalLatitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    decimallongitude = models.CharField(db_column='decimalLongitude', max_length=100, blank=True, null=True)  # Field name made lowercase.
    geodeticdatum = models.CharField(db_column='geodeticDatum', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coordinateuncertaintyinmeters = models.CharField(db_column='coordinateUncertaintyInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimcoordinates = models.CharField(db_column='verbatimCoordinates', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferencedby = models.CharField(db_column='georeferencedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferenceprotocol = models.CharField(db_column='georeferenceProtocol', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferencesources = models.TextField(db_column='georeferenceSources', blank=True, null=True)  # Field name made lowercase.
    georeferenceverificationstatus = models.CharField(db_column='georeferenceVerificationStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    georeferenceremarks = models.TextField(db_column='georeferenceRemarks', blank=True, null=True)  # Field name made lowercase.
    minimumelevationinmeters = models.CharField(db_column='minimumElevationInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maximumelevationinmeters = models.CharField(db_column='maximumElevationInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    minimumdepthinmeters = models.CharField(db_column='minimumDepthInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maximumdepthinmeters = models.CharField(db_column='maximumDepthInMeters', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimdepth = models.CharField(db_column='verbatimDepth', max_length=100, blank=True, null=True)  # Field name made lowercase.
    verbatimelevation = models.CharField(db_column='verbatimElevation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disposition = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    observeruid = models.CharField(db_column='observerUid', max_length=100, blank=True, null=True)  # Field name made lowercase.
    processingstatus = models.CharField(db_column='processingStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duplicatequantity = models.CharField(db_column='duplicateQuantity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    labelproject = models.CharField(db_column='labelProject', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordenteredby = models.CharField(db_column='recordEnteredBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateentered = models.CharField(db_column='dateEntered', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datelastmodified = models.CharField(db_column='dateLastModified', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modified = models.CharField(max_length=100, blank=True, null=True)
    rights = models.CharField(max_length=100, blank=True, null=True)
    rightsholder = models.CharField(db_column='rightsHolder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accessrights = models.CharField(db_column='accessRights', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sourceprimarykey_dbpk = models.CharField(db_column='sourcePrimaryKey-dbpk', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collid = models.CharField(db_column='collID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='recordID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    references = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lichenportal'


class Lithostrat(models.Model):
    lithostratid = models.AutoField(db_column='LithoStratID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    highestchildnodenumber = models.IntegerField(db_column='HighestChildNodeNumber', blank=True, null=True)  # Field name made lowercase.
    isaccepted = models.TextField(db_column='IsAccepted', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    nodenumber = models.IntegerField(db_column='NodeNumber', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    acceptedid = models.ForeignKey('self', models.DO_NOTHING, db_column='AcceptedID', related_name='lithostrat_acceptedid_set', blank=True, null=True)  # Field name made lowercase.
    lithostrattreedefid = models.ForeignKey('Lithostrattreedef', models.DO_NOTHING, db_column='LithoStratTreeDefID')  # Field name made lowercase.
    lithostrattreedefitemid = models.ForeignKey('Lithostrattreedefitem', models.DO_NOTHING, db_column='LithoStratTreeDefItemID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='lithostrat_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lithostrat'


class Lithostrattreedef(models.Model):
    lithostrattreedefid = models.AutoField(db_column='LithoStratTreeDefID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullnamedirection = models.IntegerField(db_column='FullNameDirection', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='lithostrattreedef_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lithostrattreedef'


class Lithostrattreedefitem(models.Model):
    lithostrattreedefitemid = models.AutoField(db_column='LithoStratTreeDefItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullnameseparator = models.CharField(db_column='FullNameSeparator', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isenforced = models.TextField(db_column='IsEnforced', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isinfullname = models.TextField(db_column='IsInFullName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    textafter = models.CharField(db_column='TextAfter', max_length=64, blank=True, null=True)  # Field name made lowercase.
    textbefore = models.CharField(db_column='TextBefore', max_length=64, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    lithostrattreedefid = models.ForeignKey(Lithostrattreedef, models.DO_NOTHING, db_column='LithoStratTreeDefID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    parentitemid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentItemID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='lithostrattreedefitem_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lithostrattreedefitem'


class Loan(models.Model):
    loanid = models.AutoField(db_column='LoanID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    currentduedate = models.DateField(db_column='CurrentDueDate', blank=True, null=True)  # Field name made lowercase.
    dateclosed = models.DateField(db_column='DateClosed', blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    isclosed = models.TextField(db_column='IsClosed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isfinancialresponsibility = models.TextField(db_column='IsFinancialResponsibility', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    loandate = models.DateField(db_column='LoanDate', blank=True, null=True)  # Field name made lowercase.
    loannumber = models.CharField(db_column='LoanNumber', max_length=50)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    originalduedate = models.DateField(db_column='OriginalDueDate', blank=True, null=True)  # Field name made lowercase.
    overduenotisetdate = models.DateField(db_column='OverdueNotiSetDate', blank=True, null=True)  # Field name made lowercase.
    purposeofloan = models.CharField(db_column='PurposeOfLoan', max_length=64, blank=True, null=True)  # Field name made lowercase.
    receivedcomments = models.CharField(db_column='ReceivedComments', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    specialconditions = models.TextField(db_column='SpecialConditions', blank=True, null=True)  # Field name made lowercase.
    srcgeography = models.CharField(db_column='SrcGeography', max_length=500, blank=True, null=True)  # Field name made lowercase.
    srctaxonomy = models.CharField(db_column='SrcTaxonomy', max_length=500, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    addressofrecordid = models.ForeignKey(Addressofrecord, models.DO_NOTHING, db_column='AddressOfRecordID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.ForeignKey(Division, models.DO_NOTHING, db_column='DivisionID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='loan_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    contents = models.TextField(db_column='Contents', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loan'


class Loanagent(models.Model):
    loanagentid = models.AutoField(db_column='LoanAgentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='loanagent_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    loanid = models.ForeignKey(Loan, models.DO_NOTHING, db_column='LoanID')  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='loanagent_agentid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loanagent'
        unique_together = (('role', 'loanid', 'agentid'),)


class Loanattachment(models.Model):
    loanattachmentid = models.AutoField(db_column='LoanAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    loanid = models.ForeignKey(Loan, models.DO_NOTHING, db_column='LoanID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='loanattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loanattachment'


class Loanpreparation(models.Model):
    loanpreparationid = models.AutoField(db_column='LoanPreparationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    descriptionofmaterial = models.TextField(db_column='DescriptionOfMaterial', blank=True, null=True)  # Field name made lowercase.
    incomments = models.TextField(db_column='InComments', blank=True, null=True)  # Field name made lowercase.
    isresolved = models.TextField(db_column='IsResolved')  # Field name made lowercase. This field type is a guess.
    outcomments = models.TextField(db_column='OutComments', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    quantityresolved = models.IntegerField(db_column='QuantityResolved', blank=True, null=True)  # Field name made lowercase.
    quantityreturned = models.IntegerField(db_column='QuantityReturned', blank=True, null=True)  # Field name made lowercase.
    receivedcomments = models.TextField(db_column='ReceivedComments', blank=True, null=True)  # Field name made lowercase.
    loanid = models.ForeignKey(Loan, models.DO_NOTHING, db_column='LoanID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    preparationid = models.ForeignKey('Preparation', models.DO_NOTHING, db_column='PreparationID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='loanpreparation_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loanpreparation'


class Loanreturnpreparation(models.Model):
    loanreturnpreparationid = models.AutoField(db_column='LoanReturnPreparationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    quantityresolved = models.IntegerField(db_column='QuantityResolved', blank=True, null=True)  # Field name made lowercase.
    quantityreturned = models.IntegerField(db_column='QuantityReturned', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    returneddate = models.DateField(db_column='ReturnedDate', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    loanpreparationid = models.ForeignKey(Loanpreparation, models.DO_NOTHING, db_column='LoanPreparationID')  # Field name made lowercase.
    receivedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ReceivedByID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='loanreturnpreparation_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='loanreturnpreparation_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    deaccessionpreparationid = models.IntegerField(db_column='DeaccessionPreparationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loanreturnpreparation'


class Locality(models.Model):
    localityid = models.AutoField(db_column='LocalityID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    datum = models.CharField(db_column='Datum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    elevationaccuracy = models.DecimalField(db_column='ElevationAccuracy', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    elevationmethod = models.CharField(db_column='ElevationMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gml = models.TextField(db_column='GML', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    lat1text = models.CharField(db_column='Lat1Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lat2text = models.CharField(db_column='Lat2Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latlongaccuracy = models.DecimalField(db_column='LatLongAccuracy', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    latlongmethod = models.CharField(db_column='LatLongMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latlongtype = models.CharField(db_column='LatLongType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude1 = models.DecimalField(db_column='Latitude1', max_digits=12, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    latitude2 = models.DecimalField(db_column='Latitude2', max_digits=12, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    localityname = models.CharField(db_column='LocalityName', max_length=1024)  # Field name made lowercase.
    long1text = models.CharField(db_column='Long1Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    long2text = models.CharField(db_column='Long2Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    longitude1 = models.DecimalField(db_column='Longitude1', max_digits=13, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    longitude2 = models.DecimalField(db_column='Longitude2', max_digits=13, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    maxelevation = models.DecimalField(db_column='MaxElevation', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    minelevation = models.DecimalField(db_column='MinElevation', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    namedplace = models.CharField(db_column='NamedPlace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalelevationunit = models.CharField(db_column='OriginalElevationUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    originallatlongunit = models.IntegerField(db_column='OriginalLatLongUnit', blank=True, null=True)  # Field name made lowercase.
    relationtonamedplace = models.CharField(db_column='RelationToNamedPlace', max_length=120, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    srclatlongunit = models.IntegerField(db_column='SrcLatLongUnit')  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    verbatimelevation = models.CharField(db_column='VerbatimElevation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    visibility = models.IntegerField(db_column='Visibility', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    geographyid = models.ForeignKey(Geography, models.DO_NOTHING, db_column='GeographyID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='locality_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    visibilitysetbyid = models.ForeignKey('Specifyuser', models.DO_NOTHING, db_column='VisibilitySetByID', blank=True, null=True)  # Field name made lowercase.
    sgrstatus = models.IntegerField(db_column='SGRStatus', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    verbatimlatitude = models.CharField(db_column='VerbatimLatitude', max_length=50, blank=True, null=True)  # Field name made lowercase.
    verbatimlongitude = models.CharField(db_column='VerbatimLongitude', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paleocontextid = models.ForeignKey('Paleocontext', models.DO_NOTHING, db_column='PaleoContextID', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    uniqueidentifier = models.CharField(db_column='UniqueIdentifier', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'locality'
        unique_together = (('disciplineid', 'uniqueidentifier'),)


class LocalityDupes(models.Model):
    localityid = models.AutoField(db_column='LocalityID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    datum = models.CharField(db_column='Datum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    elevationaccuracy = models.FloatField(db_column='ElevationAccuracy', blank=True, null=True)  # Field name made lowercase.
    elevationmethod = models.CharField(db_column='ElevationMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gml = models.TextField(db_column='GML', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    lat1text = models.CharField(db_column='Lat1Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lat2text = models.CharField(db_column='Lat2Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latlongaccuracy = models.FloatField(db_column='LatLongAccuracy', blank=True, null=True)  # Field name made lowercase.
    latlongmethod = models.CharField(db_column='LatLongMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latlongtype = models.CharField(db_column='LatLongType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude1 = models.DecimalField(db_column='Latitude1', max_digits=12, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    latitude2 = models.DecimalField(db_column='Latitude2', max_digits=12, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    localityname = models.CharField(db_column='LocalityName', max_length=255)  # Field name made lowercase.
    long1text = models.CharField(db_column='Long1Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    long2text = models.CharField(db_column='Long2Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    longitude1 = models.DecimalField(db_column='Longitude1', max_digits=13, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    longitude2 = models.DecimalField(db_column='Longitude2', max_digits=13, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    maxelevation = models.FloatField(db_column='MaxElevation', blank=True, null=True)  # Field name made lowercase.
    minelevation = models.FloatField(db_column='MinElevation', blank=True, null=True)  # Field name made lowercase.
    namedplace = models.CharField(db_column='NamedPlace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    originalelevationunit = models.CharField(db_column='OriginalElevationUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    originallatlongunit = models.IntegerField(db_column='OriginalLatLongUnit', blank=True, null=True)  # Field name made lowercase.
    relationtonamedplace = models.CharField(db_column='RelationToNamedPlace', max_length=120, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    srclatlongunit = models.IntegerField(db_column='SrcLatLongUnit')  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    verbatimelevation = models.CharField(db_column='VerbatimElevation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    visibility = models.IntegerField(db_column='Visibility', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.IntegerField(db_column='DisciplineID')  # Field name made lowercase.
    geographyid = models.IntegerField(db_column='GeographyID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.IntegerField(db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.IntegerField(db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    visibilitysetbyid = models.IntegerField(db_column='VisibilitySetByID', blank=True, null=True)  # Field name made lowercase.
    sgrstatus = models.IntegerField(db_column='SGRStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'locality_dupes'


class Localityattachment(models.Model):
    localityattachmentid = models.AutoField(db_column='LocalityAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='localityattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    localityid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='LocalityID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localityattachment'


class Localitycitation(models.Model):
    localitycitationid = models.AutoField(db_column='LocalityCitationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    referenceworkid = models.ForeignKey('Referencework', models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='localitycitation_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    localityid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='LocalityID')  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    figurenumber = models.CharField(db_column='FigureNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isfigured = models.TextField(db_column='IsFigured', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pagenumber = models.CharField(db_column='PageNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localitycitation'
        unique_together = (('referenceworkid', 'localityid'),)


class Localitydetail(models.Model):
    localitydetailid = models.AutoField(db_column='LocalityDetailID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    basemeridian = models.CharField(db_column='BaseMeridian', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drainage = models.CharField(db_column='Drainage', max_length=64, blank=True, null=True)  # Field name made lowercase.
    enddepth = models.DecimalField(db_column='EndDepth', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    enddepthunit = models.CharField(max_length=23, blank=True, null=True)
    enddepthverbatim = models.CharField(db_column='EndDepthVerbatim', max_length=32, blank=True, null=True)  # Field name made lowercase.
    gml = models.TextField(db_column='GML', blank=True, null=True)  # Field name made lowercase.
    huccode = models.CharField(db_column='HucCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    island = models.CharField(db_column='Island', max_length=64, blank=True, null=True)  # Field name made lowercase.
    islandgroup = models.CharField(db_column='IslandGroup', max_length=64, blank=True, null=True)  # Field name made lowercase.
    mgrszone = models.CharField(db_column='MgrsZone', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nationalparkname = models.CharField(db_column='NationalParkName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    rangedesc = models.CharField(db_column='RangeDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rangedirection = models.CharField(db_column='RangeDirection', max_length=50, blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sectionpart = models.CharField(db_column='SectionPart', max_length=50, blank=True, null=True)  # Field name made lowercase.
    startdepth = models.DecimalField(db_column='StartDepth', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    startdepthunit = models.CharField(max_length=23, blank=True, null=True)
    startdepthverbatim = models.CharField(db_column='StartDepthVerbatim', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    township = models.CharField(db_column='Township', max_length=50, blank=True, null=True)  # Field name made lowercase.
    townshipdirection = models.CharField(db_column='TownshipDirection', max_length=50, blank=True, null=True)  # Field name made lowercase.
    utmdatum = models.CharField(db_column='UtmDatum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utmeasting = models.DecimalField(db_column='UtmEasting', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    utmfalseeasting = models.IntegerField(db_column='UtmFalseEasting', blank=True, null=True)  # Field name made lowercase.
    utmfalsenorthing = models.IntegerField(db_column='UtmFalseNorthing', blank=True, null=True)  # Field name made lowercase.
    utmnorthing = models.DecimalField(db_column='UtmNorthing', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    utmoriglatitude = models.DecimalField(db_column='UtmOrigLatitude', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    utmoriglongitude = models.DecimalField(db_column='UtmOrigLongitude', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    utmscale = models.DecimalField(db_column='UtmScale', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    utmzone = models.SmallIntegerField(db_column='UtmZone', blank=True, null=True)  # Field name made lowercase.
    waterbody = models.CharField(db_column='WaterBody', max_length=64, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='localitydetail_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    localityid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='LocalityID', blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    paleolat = models.CharField(db_column='PaleoLat', max_length=32, blank=True, null=True)  # Field name made lowercase.
    paleolng = models.CharField(db_column='PaleoLng', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'localitydetail'


class Localitynamealias(models.Model):
    localitynamealiasid = models.AutoField(db_column='LocalityNameAliasID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=64)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    localityid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='LocalityID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='localitynamealias_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localitynamealias'


class Materialsample(models.Model):
    materialsampleid = models.AutoField(db_column='MaterialSampleID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    ggbnabsorbanceratio260_230 = models.DecimalField(db_column='GGBNAbsorbanceRatio260_230', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ggbnabsorbanceratio260_280 = models.DecimalField(db_column='GGBNAbsorbanceRatio260_280', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ggbnrabsorbanceratiomethod = models.CharField(db_column='GGBNRAbsorbanceRatioMethod', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ggbnconcentration = models.DecimalField(db_column='GGBNConcentration', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ggbnconcentrationunit = models.CharField(db_column='GGBNConcentrationUnit', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ggbnmaterialsampletype = models.CharField(db_column='GGBNMaterialSampleType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ggbnmedium = models.CharField(db_column='GGBNMedium', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ggbnpurificationmethod = models.CharField(db_column='GGBNPurificationMethod', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ggbnquality = models.CharField(db_column='GGBNQuality', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ggbnqualitycheckdate = models.DateField(db_column='GGBNQualityCheckDate', blank=True, null=True)  # Field name made lowercase.
    ggbnqualityremarks = models.TextField(db_column='GGBNQualityRemarks', blank=True, null=True)  # Field name made lowercase.
    ggbnsampledesignation = models.CharField(db_column='GGBNSampleDesignation', max_length=128, blank=True, null=True)  # Field name made lowercase.
    ggbnsamplesize = models.DecimalField(db_column='GGBNSampleSize', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ggbnvolume = models.DecimalField(db_column='GGBNVolume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ggbnvolumeunit = models.CharField(db_column='GGBNVolumeUnit', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ggbnweight = models.DecimalField(db_column='GGBNWeight', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ggbnweightmethod = models.CharField(db_column='GGBNWeightMethod', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ggbnweightunit = models.CharField(db_column='GGBNWeightUnit', max_length=64, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    reservedinteger3 = models.IntegerField(db_column='ReservedInteger3', blank=True, null=True)  # Field name made lowercase.
    reservedinteger4 = models.IntegerField(db_column='ReservedInteger4', blank=True, null=True)  # Field name made lowercase.
    reservednumber3 = models.DecimalField(db_column='ReservedNumber3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    reservednumber4 = models.DecimalField(db_column='ReservedNumber4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    reservedtext3 = models.TextField(db_column='ReservedText3', blank=True, null=True)  # Field name made lowercase.
    reservedtext4 = models.TextField(db_column='ReservedText4', blank=True, null=True)  # Field name made lowercase.
    srabioprojectid = models.CharField(db_column='SRABioProjectID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    srabiosampleid = models.CharField(db_column='SRABioSampleID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    sraprojectid = models.CharField(db_column='SRAProjectID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    srasampleid = models.CharField(db_column='SRASampleID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='materialsample_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    preparationid = models.ForeignKey('Preparation', models.DO_NOTHING, db_column='PreparationID')  # Field name made lowercase.
    extractiondate = models.DateField(db_column='ExtractionDate', blank=True, null=True)  # Field name made lowercase.
    extractorid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ExtractorID', related_name='materialsample_extractorid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materialsample'


class Morphbankview(models.Model):
    morphbankviewid = models.AutoField(db_column='MorphBankViewID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    developmentstate = models.CharField(db_column='DevelopmentState', max_length=128, blank=True, null=True)  # Field name made lowercase.
    form = models.CharField(db_column='Form', max_length=128, blank=True, null=True)  # Field name made lowercase.
    imagingpreparationtechnique = models.CharField(db_column='ImagingPreparationTechnique', max_length=128, blank=True, null=True)  # Field name made lowercase.
    imagingtechnique = models.CharField(db_column='ImagingTechnique', max_length=128, blank=True, null=True)  # Field name made lowercase.
    morphbankexternalviewid = models.IntegerField(db_column='MorphBankExternalViewID', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=32, blank=True, null=True)  # Field name made lowercase.
    specimenpart = models.CharField(db_column='SpecimenPart', max_length=128, blank=True, null=True)  # Field name made lowercase.
    viewangle = models.CharField(db_column='ViewAngle', max_length=128, blank=True, null=True)  # Field name made lowercase.
    viewname = models.CharField(db_column='ViewName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='morphbankview_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'morphbankview'


class NotificationsMessage(models.Model):
    timestampcreated = models.DateTimeField()
    content = models.TextField()
    user = models.ForeignKey('Specifyuser', models.DO_NOTHING)
    read = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notifications_message'


class Otheridentifier(models.Model):
    otheridentifierid = models.AutoField(db_column='OtherIdentifierID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    identifier = models.CharField(db_column='Identifier', max_length=64)  # Field name made lowercase.
    institution = models.CharField(db_column='Institution', max_length=64, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='otheridentifier_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    date2precision = models.IntegerField(db_column='Date2Precision', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    agent2id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent2ID', related_name='otheridentifier_agent2id_set', blank=True, null=True)  # Field name made lowercase.
    agent1id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent1ID', related_name='otheridentifier_agent1id_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otheridentifier'


class Paleocontext(models.Model):
    paleocontextid = models.AutoField(db_column='PaleoContextID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=64, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    biostratid = models.ForeignKey(Geologictimeperiod, models.DO_NOTHING, db_column='BioStratID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    chronosstratendid = models.ForeignKey(Geologictimeperiod, models.DO_NOTHING, db_column='ChronosStratEndID', related_name='paleocontext_chronosstratendid_set', blank=True, null=True)  # Field name made lowercase.
    chronosstratid = models.ForeignKey(Geologictimeperiod, models.DO_NOTHING, db_column='ChronosStratID', related_name='paleocontext_chronosstratid_set', blank=True, null=True)  # Field name made lowercase.
    lithostratid = models.ForeignKey(Lithostrat, models.DO_NOTHING, db_column='LithoStratID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='paleocontext_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    paleocontextname = models.CharField(db_column='PaleoContextName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=500, blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=500, blank=True, null=True)  # Field name made lowercase.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paleocontext'


class Pcrperson(models.Model):
    pcrpersonid = models.AutoField(db_column='PcrPersonID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='pcrperson_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    dnasequenceid = models.ForeignKey(Dnasequence, models.DO_NOTHING, db_column='DNASequenceID')  # Field name made lowercase.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID', related_name='pcrperson_agentid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pcrperson'
        unique_together = (('agentid', 'dnasequenceid'),)


class Permit(models.Model):
    permitid = models.AutoField(db_column='PermitID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    issueddate = models.DateField(db_column='IssuedDate', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    permitnumber = models.CharField(db_column='PermitNumber', max_length=50)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    renewaldate = models.DateField(db_column='RenewalDate', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    issuedtoid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='IssuedToID', blank=True, null=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institution, models.DO_NOTHING, db_column='InstitutionID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='permit_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='permit_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    issuedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='IssuedByID', related_name='permit_issuedbyid_set', blank=True, null=True)  # Field name made lowercase.
    copyright = models.CharField(db_column='Copyright', max_length=256, blank=True, null=True)  # Field name made lowercase.
    isavailable = models.TextField(db_column='IsAvailable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isrequired = models.TextField(db_column='IsRequired', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    permittext = models.TextField(db_column='PermitText', blank=True, null=True)  # Field name made lowercase.
    reservedinteger1 = models.IntegerField(db_column='ReservedInteger1', blank=True, null=True)  # Field name made lowercase.
    reservedinteger2 = models.IntegerField(db_column='ReservedInteger2', blank=True, null=True)  # Field name made lowercase.
    reservedtext3 = models.CharField(db_column='ReservedText3', max_length=128, blank=True, null=True)  # Field name made lowercase.
    reservedtext4 = models.CharField(db_column='ReservedText4', max_length=128, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=64, blank=True, null=True)  # Field name made lowercase.
    statusqualifier = models.CharField(db_column='StatusQualifier', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permit'


class Permitattachment(models.Model):
    permitattachmentid = models.AutoField(db_column='PermitAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    permitid = models.ForeignKey(Permit, models.DO_NOTHING, db_column='PermitID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='permitattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permitattachment'


class Picklist(models.Model):
    picklistid = models.AutoField(db_column='PickListID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    filterfieldname = models.CharField(db_column='FilterFieldName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    filtervalue = models.CharField(db_column='FilterValue', max_length=32, blank=True, null=True)  # Field name made lowercase.
    formatter = models.CharField(db_column='Formatter', max_length=64, blank=True, null=True)  # Field name made lowercase.
    issystem = models.TextField(db_column='IsSystem')  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    readonly = models.TextField(db_column='ReadOnly')  # Field name made lowercase. This field type is a guess.
    sizelimit = models.IntegerField(db_column='SizeLimit', blank=True, null=True)  # Field name made lowercase.
    sorttype = models.IntegerField(db_column='SortType', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='picklist_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    collectionid = models.ForeignKey(Collection, models.DO_NOTHING, db_column='CollectionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'picklist'


class Picklistitem(models.Model):
    picklistitemid = models.AutoField(db_column='PickListItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=1024)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='picklistitem_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    picklistid = models.ForeignKey(Picklist, models.DO_NOTHING, db_column='PickListID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'picklistitem'


class Preparation(models.Model):
    preparationid = models.AutoField(db_column='PreparationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    countamt = models.IntegerField(db_column='CountAmt', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    prepareddate = models.DateField(db_column='PreparedDate', blank=True, null=True)  # Field name made lowercase.
    prepareddateprecision = models.IntegerField(db_column='PreparedDatePrecision', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    samplenumber = models.CharField(db_column='SampleNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=32, blank=True, null=True)  # Field name made lowercase.
    storagelocation = models.CharField(db_column='StorageLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preparedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='PreparedByID', blank=True, null=True)  # Field name made lowercase.
    storageid = models.ForeignKey('Storage', models.DO_NOTHING, db_column='StorageID', blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='preparation_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    preparationattributeid = models.ForeignKey('Preparationattribute', models.DO_NOTHING, db_column='PreparationAttributeID', blank=True, null=True)  # Field name made lowercase.
    preptypeid = models.ForeignKey('Preptype', models.DO_NOTHING, db_column='PrepTypeID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='preparation_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    reservedinteger3 = models.IntegerField(db_column='ReservedInteger3', blank=True, null=True)  # Field name made lowercase.
    reservedinteger4 = models.IntegerField(db_column='ReservedInteger4', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', unique=True, max_length=128, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    date2precision = models.IntegerField(db_column='Date2Precision', blank=True, null=True)  # Field name made lowercase.
    date3 = models.DateField(db_column='Date3', blank=True, null=True)  # Field name made lowercase.
    date3precision = models.IntegerField(db_column='Date3Precision', blank=True, null=True)  # Field name made lowercase.
    date4 = models.DateField(db_column='Date4', blank=True, null=True)  # Field name made lowercase.
    date4precision = models.IntegerField(db_column='Date4Precision', blank=True, null=True)  # Field name made lowercase.
    text6 = models.TextField(db_column='Text6', blank=True, null=True)  # Field name made lowercase.
    text7 = models.TextField(db_column='Text7', blank=True, null=True)  # Field name made lowercase.
    text8 = models.TextField(db_column='Text8', blank=True, null=True)  # Field name made lowercase.
    text9 = models.TextField(db_column='Text9', blank=True, null=True)  # Field name made lowercase.
    alternatestorageid = models.ForeignKey('Storage', models.DO_NOTHING, db_column='AlternateStorageID', related_name='preparation_alternatestorageid_set', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text10 = models.TextField(db_column='Text10', blank=True, null=True)  # Field name made lowercase.
    text11 = models.TextField(db_column='Text11', blank=True, null=True)  # Field name made lowercase.
    text12 = models.CharField(db_column='Text12', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text13 = models.CharField(db_column='Text13', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preparation'
        unique_together = (('collectionmemberid', 'barcode'),)


class PreparationDupes(models.Model):
    preparationid = models.AutoField(db_column='PreparationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    countamt = models.IntegerField(db_column='CountAmt', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number1 = models.FloatField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.FloatField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    prepareddate = models.DateField(db_column='PreparedDate', blank=True, null=True)  # Field name made lowercase.
    prepareddateprecision = models.IntegerField(db_column='PreparedDatePrecision', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    samplenumber = models.CharField(db_column='SampleNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=32, blank=True, null=True)  # Field name made lowercase.
    storagelocation = models.CharField(db_column='StorageLocation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preparedbyid = models.IntegerField(db_column='PreparedByID', blank=True, null=True)  # Field name made lowercase.
    storageid = models.IntegerField(db_column='StorageID', blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.IntegerField(db_column='CollectionObjectID')  # Field name made lowercase.
    createdbyagentid = models.IntegerField(db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    preparationattributeid = models.IntegerField(db_column='PreparationAttributeID', blank=True, null=True)  # Field name made lowercase.
    preptypeid = models.IntegerField(db_column='PrepTypeID')  # Field name made lowercase.
    modifiedbyagentid = models.IntegerField(db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preparation_dupes'


class Preparationattachment(models.Model):
    preparationattachmentid = models.AutoField(db_column='PreparationAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    preparationid = models.ForeignKey(Preparation, models.DO_NOTHING, db_column='PreparationID')  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='preparationattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preparationattachment'


class Preparationattr(models.Model):
    attrid = models.AutoField(db_column='AttrID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    doublevalue = models.FloatField(db_column='DoubleValue', blank=True, null=True)  # Field name made lowercase.
    strvalue = models.CharField(db_column='StrValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='preparationattr_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    preparationid = models.ForeignKey(Preparation, models.DO_NOTHING, db_column='PreparationId')  # Field name made lowercase.
    attributedefid = models.ForeignKey(Attributedef, models.DO_NOTHING, db_column='AttributeDefID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preparationattr'


class Preparationattribute(models.Model):
    preparationattributeid = models.AutoField(db_column='PreparationAttributeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    attrdate = models.DateField(blank=True, null=True)
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.IntegerField(db_column='Number4', blank=True, null=True)  # Field name made lowercase.
    number5 = models.IntegerField(db_column='Number5', blank=True, null=True)  # Field name made lowercase.
    number6 = models.IntegerField(db_column='Number6', blank=True, null=True)  # Field name made lowercase.
    number7 = models.IntegerField(db_column='Number7', blank=True, null=True)  # Field name made lowercase.
    number8 = models.IntegerField(db_column='Number8', blank=True, null=True)  # Field name made lowercase.
    number9 = models.SmallIntegerField(db_column='Number9', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text10 = models.TextField(db_column='Text10', blank=True, null=True)  # Field name made lowercase.
    text11 = models.CharField(db_column='Text11', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text12 = models.CharField(db_column='Text12', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text13 = models.CharField(db_column='Text13', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text14 = models.CharField(db_column='Text14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text15 = models.CharField(db_column='Text15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text16 = models.CharField(db_column='Text16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text17 = models.CharField(db_column='Text17', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text18 = models.CharField(db_column='Text18', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text19 = models.CharField(db_column='Text19', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text20 = models.CharField(db_column='Text20', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text21 = models.CharField(db_column='Text21', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text22 = models.CharField(db_column='Text22', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text23 = models.CharField(db_column='Text23', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text24 = models.CharField(db_column='Text24', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text25 = models.CharField(db_column='Text25', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text26 = models.CharField(db_column='Text26', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text6 = models.CharField(db_column='Text6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text7 = models.CharField(db_column='Text7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text8 = models.CharField(db_column='Text8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text9 = models.CharField(db_column='Text9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='preparationattribute_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preparationattribute'


class Preparationproperty(models.Model):
    preparationpropertyid = models.AutoField(db_column='PreparationPropertyID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date10 = models.DateField(db_column='Date10', blank=True, null=True)  # Field name made lowercase.
    date11 = models.DateField(db_column='Date11', blank=True, null=True)  # Field name made lowercase.
    date12 = models.DateField(db_column='Date12', blank=True, null=True)  # Field name made lowercase.
    date13 = models.DateField(db_column='Date13', blank=True, null=True)  # Field name made lowercase.
    date14 = models.DateField(db_column='Date14', blank=True, null=True)  # Field name made lowercase.
    date15 = models.DateField(db_column='Date15', blank=True, null=True)  # Field name made lowercase.
    date16 = models.DateField(db_column='Date16', blank=True, null=True)  # Field name made lowercase.
    date17 = models.DateField(db_column='Date17', blank=True, null=True)  # Field name made lowercase.
    date18 = models.DateField(db_column='Date18', blank=True, null=True)  # Field name made lowercase.
    date19 = models.DateField(db_column='Date19', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    date20 = models.DateField(db_column='Date20', blank=True, null=True)  # Field name made lowercase.
    date3 = models.DateField(db_column='Date3', blank=True, null=True)  # Field name made lowercase.
    date4 = models.DateField(db_column='Date4', blank=True, null=True)  # Field name made lowercase.
    date5 = models.DateField(db_column='Date5', blank=True, null=True)  # Field name made lowercase.
    date6 = models.DateField(db_column='Date6', blank=True, null=True)  # Field name made lowercase.
    date7 = models.DateField(db_column='Date7', blank=True, null=True)  # Field name made lowercase.
    date8 = models.DateField(db_column='Date8', blank=True, null=True)  # Field name made lowercase.
    date9 = models.DateField(db_column='Date9', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    integer1 = models.SmallIntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer10 = models.SmallIntegerField(db_column='Integer10', blank=True, null=True)  # Field name made lowercase.
    integer11 = models.SmallIntegerField(db_column='Integer11', blank=True, null=True)  # Field name made lowercase.
    integer12 = models.SmallIntegerField(db_column='Integer12', blank=True, null=True)  # Field name made lowercase.
    integer13 = models.SmallIntegerField(db_column='Integer13', blank=True, null=True)  # Field name made lowercase.
    integer14 = models.SmallIntegerField(db_column='Integer14', blank=True, null=True)  # Field name made lowercase.
    integer15 = models.SmallIntegerField(db_column='Integer15', blank=True, null=True)  # Field name made lowercase.
    integer16 = models.SmallIntegerField(db_column='Integer16', blank=True, null=True)  # Field name made lowercase.
    integer17 = models.SmallIntegerField(db_column='Integer17', blank=True, null=True)  # Field name made lowercase.
    integer18 = models.SmallIntegerField(db_column='Integer18', blank=True, null=True)  # Field name made lowercase.
    integer19 = models.SmallIntegerField(db_column='Integer19', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.SmallIntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer20 = models.SmallIntegerField(db_column='Integer20', blank=True, null=True)  # Field name made lowercase.
    integer21 = models.IntegerField(db_column='Integer21', blank=True, null=True)  # Field name made lowercase.
    integer22 = models.IntegerField(db_column='Integer22', blank=True, null=True)  # Field name made lowercase.
    integer23 = models.IntegerField(db_column='Integer23', blank=True, null=True)  # Field name made lowercase.
    integer24 = models.IntegerField(db_column='Integer24', blank=True, null=True)  # Field name made lowercase.
    integer25 = models.IntegerField(db_column='Integer25', blank=True, null=True)  # Field name made lowercase.
    integer26 = models.IntegerField(db_column='Integer26', blank=True, null=True)  # Field name made lowercase.
    integer27 = models.IntegerField(db_column='Integer27', blank=True, null=True)  # Field name made lowercase.
    integer28 = models.IntegerField(db_column='Integer28', blank=True, null=True)  # Field name made lowercase.
    integer29 = models.IntegerField(db_column='Integer29', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.SmallIntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer30 = models.IntegerField(db_column='Integer30', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.SmallIntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.SmallIntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    integer6 = models.SmallIntegerField(db_column='Integer6', blank=True, null=True)  # Field name made lowercase.
    integer7 = models.SmallIntegerField(db_column='Integer7', blank=True, null=True)  # Field name made lowercase.
    integer8 = models.SmallIntegerField(db_column='Integer8', blank=True, null=True)  # Field name made lowercase.
    integer9 = models.SmallIntegerField(db_column='Integer9', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number10 = models.DecimalField(db_column='Number10', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number11 = models.DecimalField(db_column='Number11', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number12 = models.DecimalField(db_column='Number12', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number13 = models.DecimalField(db_column='Number13', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number14 = models.DecimalField(db_column='Number14', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number15 = models.DecimalField(db_column='Number15', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number16 = models.DecimalField(db_column='Number16', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number17 = models.DecimalField(db_column='Number17', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number18 = models.DecimalField(db_column='Number18', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number19 = models.DecimalField(db_column='Number19', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number20 = models.DecimalField(db_column='Number20', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number21 = models.DecimalField(db_column='Number21', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number22 = models.DecimalField(db_column='Number22', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number23 = models.DecimalField(db_column='Number23', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number24 = models.DecimalField(db_column='Number24', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number25 = models.DecimalField(db_column='Number25', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number26 = models.DecimalField(db_column='Number26', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number27 = models.DecimalField(db_column='Number27', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number28 = models.DecimalField(db_column='Number28', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number29 = models.DecimalField(db_column='Number29', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number30 = models.DecimalField(db_column='Number30', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number6 = models.DecimalField(db_column='Number6', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number7 = models.DecimalField(db_column='Number7', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number8 = models.DecimalField(db_column='Number8', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number9 = models.DecimalField(db_column='Number9', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text10 = models.CharField(db_column='Text10', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text11 = models.CharField(db_column='Text11', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text12 = models.CharField(db_column='Text12', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text13 = models.CharField(db_column='Text13', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text14 = models.CharField(db_column='Text14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text15 = models.CharField(db_column='Text15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text16 = models.CharField(db_column='Text16', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text17 = models.CharField(db_column='Text17', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text18 = models.CharField(db_column='Text18', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text19 = models.CharField(db_column='Text19', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text20 = models.CharField(db_column='Text20', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text21 = models.CharField(db_column='Text21', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text22 = models.CharField(db_column='Text22', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text23 = models.CharField(db_column='Text23', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text24 = models.CharField(db_column='Text24', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text25 = models.CharField(db_column='Text25', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text26 = models.CharField(db_column='Text26', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text27 = models.CharField(db_column='Text27', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text28 = models.CharField(db_column='Text28', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text29 = models.CharField(db_column='Text29', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text30 = models.CharField(db_column='Text30', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text31 = models.TextField(db_column='Text31', blank=True, null=True)  # Field name made lowercase.
    text32 = models.TextField(db_column='Text32', blank=True, null=True)  # Field name made lowercase.
    text33 = models.TextField(db_column='Text33', blank=True, null=True)  # Field name made lowercase.
    text34 = models.TextField(db_column='Text34', blank=True, null=True)  # Field name made lowercase.
    text35 = models.TextField(db_column='Text35', blank=True, null=True)  # Field name made lowercase.
    text36 = models.TextField(db_column='Text36', blank=True, null=True)  # Field name made lowercase.
    text37 = models.TextField(db_column='Text37', blank=True, null=True)  # Field name made lowercase.
    text38 = models.TextField(db_column='Text38', blank=True, null=True)  # Field name made lowercase.
    text39 = models.TextField(db_column='Text39', blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text40 = models.TextField(db_column='Text40', blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text6 = models.CharField(db_column='Text6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text7 = models.CharField(db_column='Text7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text8 = models.CharField(db_column='Text8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text9 = models.CharField(db_column='Text9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno10 = models.TextField(db_column='YesNo10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno11 = models.TextField(db_column='YesNo11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno12 = models.TextField(db_column='YesNo12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno13 = models.TextField(db_column='YesNo13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno14 = models.TextField(db_column='YesNo14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno15 = models.TextField(db_column='YesNo15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno16 = models.TextField(db_column='YesNo16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno17 = models.TextField(db_column='YesNo17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno18 = models.TextField(db_column='YesNo18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno19 = models.TextField(db_column='YesNo19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno20 = models.TextField(db_column='YesNo20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno6 = models.TextField(db_column='YesNo6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno7 = models.TextField(db_column='YesNo7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno8 = models.TextField(db_column='YesNo8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno9 = models.TextField(db_column='YesNo9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    agent12id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent12ID', blank=True, null=True)  # Field name made lowercase.
    agent8d = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent8D', related_name='preparationproperty_agent8d_set', blank=True, null=True)  # Field name made lowercase.
    agent17id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent17ID', related_name='preparationproperty_agent17id_set', blank=True, null=True)  # Field name made lowercase.
    agent10id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent10ID', related_name='preparationproperty_agent10id_set', blank=True, null=True)  # Field name made lowercase.
    agent15id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent15ID', related_name='preparationproperty_agent15id_set', blank=True, null=True)  # Field name made lowercase.
    agent14id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent14ID', related_name='preparationproperty_agent14id_set', blank=True, null=True)  # Field name made lowercase.
    agent1id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent1ID', related_name='preparationproperty_agent1id_set', blank=True, null=True)  # Field name made lowercase.
    agent20id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent20ID', related_name='preparationproperty_agent20id_set', blank=True, null=True)  # Field name made lowercase.
    agent11id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent11ID', related_name='preparationproperty_agent11id_set', blank=True, null=True)  # Field name made lowercase.
    agent16id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent16ID', related_name='preparationproperty_agent16id_set', blank=True, null=True)  # Field name made lowercase.
    agent2id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent2ID', related_name='preparationproperty_agent2id_set', blank=True, null=True)  # Field name made lowercase.
    agent13id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent13ID', related_name='preparationproperty_agent13id_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='preparationproperty_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agent4id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent4ID', related_name='preparationproperty_agent4id_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='preparationproperty_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    agent9id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent9ID', related_name='preparationproperty_agent9id_set', blank=True, null=True)  # Field name made lowercase.
    agent18id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent18ID', related_name='preparationproperty_agent18id_set', blank=True, null=True)  # Field name made lowercase.
    agent5id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent5ID', related_name='preparationproperty_agent5id_set', blank=True, null=True)  # Field name made lowercase.
    agent6id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent6ID', related_name='preparationproperty_agent6id_set', blank=True, null=True)  # Field name made lowercase.
    agent7id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent7ID', related_name='preparationproperty_agent7id_set', blank=True, null=True)  # Field name made lowercase.
    preparationid = models.ForeignKey(Preparation, models.DO_NOTHING, db_column='PreparationID')  # Field name made lowercase.
    agent3id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent3ID', related_name='preparationproperty_agent3id_set', blank=True, null=True)  # Field name made lowercase.
    agent19id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent19ID', related_name='preparationproperty_agent19id_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preparationproperty'


class Preptype(models.Model):
    preptypeid = models.AutoField(db_column='PrepTypeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    isloanable = models.TextField(db_column='IsLoanable')  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    collectionid = models.ForeignKey(Collection, models.DO_NOTHING, db_column='CollectionID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='preptype_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preptype'


class Project(models.Model):
    projectid = models.AutoField(db_column='ProjectID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    grantagency = models.CharField(db_column='GrantAgency', max_length=64, blank=True, null=True)  # Field name made lowercase.
    grantnumber = models.CharField(db_column='GrantNumber', max_length=64, blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    projectdescription = models.CharField(db_column='ProjectDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectName', max_length=128)  # Field name made lowercase.
    projectnumber = models.CharField(db_column='ProjectNumber', max_length=64, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    projectagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ProjectAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='project_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='project_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'


class ProjectColobj(models.Model):
    projectid = models.OneToOneField(Project, models.DO_NOTHING, db_column='ProjectID', primary_key=True)  # Field name made lowercase. The composite primary key (ProjectID, CollectionObjectID) found, that is not supported. The first column is selected.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_colobj'
        unique_together = (('projectid', 'collectionobjectid'),)


class Recordset(models.Model):
    recordsetid = models.AutoField(db_column='RecordSetID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    allpermissionlevel = models.IntegerField(db_column='AllPermissionLevel', blank=True, null=True)  # Field name made lowercase.
    tableid = models.IntegerField(db_column='TableID')  # Field name made lowercase.
    grouppermissionlevel = models.IntegerField(db_column='GroupPermissionLevel', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=280)  # Field name made lowercase.
    ownerpermissionlevel = models.IntegerField(db_column='OwnerPermissionLevel', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    spprincipalid = models.ForeignKey('Spprincipal', models.DO_NOTHING, db_column='SpPrincipalID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='recordset_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    specifyuserid = models.ForeignKey('Specifyuser', models.DO_NOTHING, db_column='SpecifyUserID')  # Field name made lowercase.
    inforequestid = models.ForeignKey(Inforequest, models.DO_NOTHING, db_column='InfoRequestID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recordset'


class Recordsetitem(models.Model):
    recordsetitemid = models.AutoField(db_column='RecordSetItemID', primary_key=True)  # Field name made lowercase.
    recordid = models.IntegerField(db_column='RecordId')  # Field name made lowercase.
    recordsetid = models.ForeignKey(Recordset, models.DO_NOTHING, db_column='RecordSetID')  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='OrderNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recordsetitem'


class Referencework(models.Model):
    referenceworkid = models.AutoField(db_column='ReferenceWorkID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    ispublished = models.TextField(db_column='IsPublished', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isbn = models.CharField(db_column='ISBN', max_length=16, blank=True, null=True)  # Field name made lowercase.
    librarynumber = models.CharField(db_column='LibraryNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='Pages', max_length=50, blank=True, null=True)  # Field name made lowercase.
    placeofpublication = models.CharField(db_column='PlaceOfPublication', max_length=50, blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=250, blank=True, null=True)  # Field name made lowercase.
    referenceworktype = models.IntegerField(db_column='ReferenceWorkType')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=400, blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=25, blank=True, null=True)  # Field name made lowercase.
    workdate = models.CharField(db_column='WorkDate', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    journalid = models.ForeignKey(Journal, models.DO_NOTHING, db_column='JournalID', blank=True, null=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institution, models.DO_NOTHING, db_column='InstitutionID')  # Field name made lowercase.
    containedrfparentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ContainedRFParentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='referencework_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    doi = models.TextField(db_column='Doi', blank=True, null=True)  # Field name made lowercase.
    uri = models.TextField(db_column='Uri', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referencework'


class Referenceworkattachment(models.Model):
    referenceworkattachmentid = models.AutoField(db_column='ReferenceWorkAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    referenceworkid = models.ForeignKey(Referencework, models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='referenceworkattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referenceworkattachment'


class Repositoryagreement(models.Model):
    repositoryagreementid = models.AutoField(db_column='RepositoryAgreementID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    repositoryagreementnumber = models.CharField(db_column='RepositoryAgreementNumber', max_length=60)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    agentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AgentID')  # Field name made lowercase.
    addressofrecordid = models.ForeignKey(Addressofrecord, models.DO_NOTHING, db_column='AddressOfRecordID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='repositoryagreement_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='repositoryagreement_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.ForeignKey(Division, models.DO_NOTHING, db_column='DivisionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'repositoryagreement'


class Repositoryagreementattachment(models.Model):
    repositoryagreementattachmentid = models.AutoField(db_column='RepositoryAgreementAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    repositoryagreementid = models.ForeignKey(Repositoryagreement, models.DO_NOTHING, db_column='RepositoryAgreementID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='repositoryagreementattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'repositoryagreementattachment'


class Sgrbatchmatchresultitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    matchedid = models.CharField(db_column='matchedId', max_length=128)  # Field name made lowercase.
    maxscore = models.FloatField(db_column='maxScore')  # Field name made lowercase.
    batchmatchresultsetid = models.ForeignKey('Sgrbatchmatchresultset', models.DO_NOTHING, db_column='batchMatchResultSetId')  # Field name made lowercase.
    qtime = models.IntegerField(db_column='qTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sgrbatchmatchresultitem'


class Sgrbatchmatchresultset(models.Model):
    id = models.BigAutoField(primary_key=True)
    inserttime = models.DateTimeField(db_column='insertTime')  # Field name made lowercase.
    name = models.CharField(max_length=128)
    recordsetid = models.BigIntegerField(db_column='recordSetID', blank=True, null=True)  # Field name made lowercase.
    matchconfigurationid = models.ForeignKey('Sgrmatchconfiguration', models.DO_NOTHING, db_column='matchConfigurationId')  # Field name made lowercase.
    query = models.TextField()
    remarks = models.TextField()
    dbtableid = models.IntegerField(db_column='dbTableId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sgrbatchmatchresultset'


class Sgrmatchconfiguration(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    similarityfields = models.TextField(db_column='similarityFields')  # Field name made lowercase.
    serverurl = models.TextField(db_column='serverUrl')  # Field name made lowercase.
    filterquery = models.CharField(db_column='filterQuery', max_length=128)  # Field name made lowercase.
    queryfields = models.TextField(db_column='queryFields')  # Field name made lowercase.
    remarks = models.TextField()
    boostinterestingterms = models.IntegerField(db_column='boostInterestingTerms')  # Field name made lowercase.
    nrows = models.IntegerField(db_column='nRows')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sgrmatchconfiguration'


class Shipment(models.Model):
    shipmentid = models.AutoField(db_column='ShipmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    insuredforamount = models.CharField(db_column='InsuredForAmount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    numberofpackages = models.SmallIntegerField(db_column='NumberOfPackages', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    shipmentdate = models.DateField(db_column='ShipmentDate', blank=True, null=True)  # Field name made lowercase.
    shipmentmethod = models.CharField(db_column='ShipmentMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shipmentnumber = models.CharField(db_column='ShipmentNumber', max_length=50)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shipperid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ShipperID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    exchangeoutid = models.ForeignKey(Exchangeout, models.DO_NOTHING, db_column='ExchangeOutID', blank=True, null=True)  # Field name made lowercase.
    shippedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ShippedByID', related_name='shipment_shippedbyid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='shipment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='shipment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    giftid = models.ForeignKey(Gift, models.DO_NOTHING, db_column='GiftID', blank=True, null=True)  # Field name made lowercase.
    shippedtoid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ShippedToID', related_name='shipment_shippedtoid_set', blank=True, null=True)  # Field name made lowercase.
    borrowid = models.ForeignKey(Borrow, models.DO_NOTHING, db_column='BorrowID', blank=True, null=True)  # Field name made lowercase.
    loanid = models.ForeignKey(Loan, models.DO_NOTHING, db_column='LoanID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipment'


class SpSchemaMapping(models.Model):
    spexportschemamappingid = models.OneToOneField('Spexportschemamapping', models.DO_NOTHING, db_column='SpExportSchemaMappingID', primary_key=True)  # Field name made lowercase. The composite primary key (SpExportSchemaMappingID, SpExportSchemaID) found, that is not supported. The first column is selected.
    spexportschemaid = models.ForeignKey('Spexportschema', models.DO_NOTHING, db_column='SpExportSchemaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sp_schema_mapping'
        unique_together = (('spexportschemamappingid', 'spexportschemaid'),)


class Spappresource(models.Model):
    spappresourceid = models.AutoField(db_column='SpAppResourceID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    allpermissionlevel = models.IntegerField(db_column='AllPermissionLevel', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grouppermissionlevel = models.IntegerField(db_column='GroupPermissionLevel', blank=True, null=True)  # Field name made lowercase.
    level = models.SmallIntegerField(db_column='Level')  # Field name made lowercase.
    metadata = models.CharField(db_column='MetaData', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mimetype = models.CharField(db_column='MimeType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    ownerpermissionlevel = models.IntegerField(db_column='OwnerPermissionLevel', blank=True, null=True)  # Field name made lowercase.
    specifyuserid = models.ForeignKey('Specifyuser', models.DO_NOTHING, db_column='SpecifyUserID')  # Field name made lowercase.
    spappresourcedirid = models.ForeignKey('Spappresourcedir', models.DO_NOTHING, db_column='SpAppResourceDirID')  # Field name made lowercase.
    spprincipalid = models.ForeignKey('Spprincipal', models.DO_NOTHING, db_column='SpPrincipalID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spappresource_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spappresource'


class Spappresourcedata(models.Model):
    spappresourcedataid = models.AutoField(db_column='SpAppResourceDataID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spappresourcedata_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    spappresourceid = models.ForeignKey(Spappresource, models.DO_NOTHING, db_column='SpAppResourceID', blank=True, null=True)  # Field name made lowercase.
    spviewsetobjid = models.ForeignKey('Spviewsetobj', models.DO_NOTHING, db_column='SpViewSetObjID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spappresourcedata'


class Spappresourcedir(models.Model):
    spappresourcedirid = models.AutoField(db_column='SpAppResourceDirID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    disciplinetype = models.CharField(db_column='DisciplineType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ispersonal = models.TextField(db_column='IsPersonal')  # Field name made lowercase. This field type is a guess.
    usertype = models.CharField(db_column='UserType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    specifyuserid = models.ForeignKey('Specifyuser', models.DO_NOTHING, db_column='SpecifyUserID', blank=True, null=True)  # Field name made lowercase.
    collectionid = models.ForeignKey(Collection, models.DO_NOTHING, db_column='CollectionID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spappresourcedir_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spappresourcedir'


class Spauditlog(models.Model):
    spauditlogid = models.AutoField(db_column='SpAuditLogID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    action = models.IntegerField(db_column='Action')  # Field name made lowercase.
    parentrecordid = models.IntegerField(db_column='ParentRecordId', blank=True, null=True)  # Field name made lowercase.
    parenttablenum = models.SmallIntegerField(db_column='ParentTableNum', blank=True, null=True)  # Field name made lowercase.
    recordid = models.IntegerField(db_column='RecordId', blank=True, null=True)  # Field name made lowercase.
    recordversion = models.IntegerField(db_column='RecordVersion')  # Field name made lowercase.
    tablenum = models.SmallIntegerField(db_column='TableNum')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spauditlog_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spauditlog'


class Spauditlogfield(models.Model):
    spauditlogfieldid = models.AutoField(db_column='SpAuditLogFieldID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    newvalue = models.TextField(db_column='NewValue', blank=True, null=True)  # Field name made lowercase.
    oldvalue = models.TextField(db_column='OldValue', blank=True, null=True)  # Field name made lowercase.
    spauditlogid = models.ForeignKey(Spauditlog, models.DO_NOTHING, db_column='SpAuditLogID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spauditlogfield_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spauditlogfield'


class Spdataset(models.Model):
    name = models.CharField(max_length=256)
    columns = models.TextField(db_collation='utf8mb4_bin')
    data = models.TextField(db_collation='utf8mb4_bin')
    uploadplan = models.TextField(blank=True, null=True)
    uploaderstatus = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    uploadresult = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    rowresults = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(Collection, models.DO_NOTHING)
    specifyuser = models.ForeignKey('Specifyuser', models.DO_NOTHING)
    visualorder = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    importedfilename = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    timestampcreated = models.DateTimeField()
    timestampmodified = models.DateTimeField()
    createdbyagent = models.ForeignKey(Agent, models.DO_NOTHING, blank=True, null=True)
    modifiedbyagent = models.ForeignKey(Agent, models.DO_NOTHING, related_name='spdataset_modifiedbyagent_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spdataset'


class Specifyuser(models.Model):
    specifyuserid = models.AutoField(db_column='SpecifyUserID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    accumminloggedin = models.BigIntegerField(db_column='AccumMinLoggedIn', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isloggedin = models.TextField(db_column='IsLoggedIn')  # Field name made lowercase. This field type is a guess.
    isloggedinreport = models.TextField(db_column='IsLoggedInReport')  # Field name made lowercase. This field type is a guess.
    logincollectionname = models.CharField(db_column='LoginCollectionName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    logindisciplinename = models.CharField(db_column='LoginDisciplineName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    loginouttime = models.DateTimeField(db_column='LoginOutTime', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='specifyuser_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specifyuser'


class SpecifyuserSpprincipal(models.Model):
    specifyuserid = models.OneToOneField(Specifyuser, models.DO_NOTHING, db_column='SpecifyUserID', primary_key=True)  # Field name made lowercase. The composite primary key (SpecifyUserID, SpPrincipalID) found, that is not supported. The first column is selected.
    spprincipalid = models.ForeignKey('Spprincipal', models.DO_NOTHING, db_column='SpPrincipalID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specifyuser_spprincipal'
        unique_together = (('specifyuserid', 'spprincipalid'),)


class Spexportschema(models.Model):
    spexportschemaid = models.AutoField(db_column='SpExportSchemaID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schemaname = models.CharField(db_column='SchemaName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    schemaversion = models.CharField(db_column='SchemaVersion', max_length=80, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spexportschema_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spexportschema'


class Spexportschemaitem(models.Model):
    spexportschemaitemid = models.AutoField(db_column='SpExportSchemaItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    datatype = models.CharField(db_column='DataType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    formatter = models.CharField(db_column='Formatter', max_length=32, blank=True, null=True)  # Field name made lowercase.
    spexportschemaid = models.ForeignKey(Spexportschema, models.DO_NOTHING, db_column='SpExportSchemaID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    splocalecontaineritemid = models.ForeignKey('Splocalecontaineritem', models.DO_NOTHING, db_column='SpLocaleContainerItemID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spexportschemaitem_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spexportschemaitem'


class Spexportschemaitemmapping(models.Model):
    spexportschemaitemmappingid = models.AutoField(db_column='SpExportSchemaItemMappingID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    spqueryfieldid = models.ForeignKey('Spqueryfield', models.DO_NOTHING, db_column='SpQueryFieldID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='spexportschemaitemmapping_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    exportschemaitemid = models.ForeignKey(Spexportschemaitem, models.DO_NOTHING, db_column='ExportSchemaItemID', blank=True, null=True)  # Field name made lowercase.
    spexportschemamappingid = models.ForeignKey('Spexportschemamapping', models.DO_NOTHING, db_column='SpExportSchemaMappingID', blank=True, null=True)  # Field name made lowercase.
    exportedfieldname = models.CharField(db_column='ExportedFieldName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    extensionitem = models.TextField(db_column='ExtensionItem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rowtype = models.CharField(db_column='RowType', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spexportschemaitemmapping'


class Spexportschemamapping(models.Model):
    spexportschemamappingid = models.AutoField(db_column='SpExportSchemaMappingID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mappingname = models.CharField(db_column='MappingName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    timestampexported = models.DateTimeField(db_column='TimeStampExported', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spexportschemamapping_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spexportschemamapping'


class Spfieldvaluedefault(models.Model):
    spfieldvaluedefaultid = models.AutoField(db_column='SpFieldValueDefaultID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    idvalue = models.IntegerField(db_column='IdValue', blank=True, null=True)  # Field name made lowercase.
    strvalue = models.CharField(db_column='StrValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='spfieldvaluedefault_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spfieldvaluedefault'


class Splibraryrole(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'splibraryrole'


class Splibraryrolepolicy(models.Model):
    resource = models.CharField(max_length=1024)
    action = models.CharField(max_length=1024)
    role = models.ForeignKey(Splibraryrole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'splibraryrolepolicy'


class Splocalecontainer(models.Model):
    splocalecontainerid = models.AutoField(db_column='SpLocaleContainerID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ishidden = models.TextField(db_column='IsHidden')  # Field name made lowercase. This field type is a guess.
    issystem = models.TextField(db_column='IsSystem')  # Field name made lowercase. This field type is a guess.
    isuiformatter = models.TextField(db_column='IsUIFormatter', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    picklistname = models.CharField(db_column='PickListName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    aggregator = models.CharField(db_column='Aggregator', max_length=64, blank=True, null=True)  # Field name made lowercase.
    defaultui = models.CharField(db_column='DefaultUI', max_length=64, blank=True, null=True)  # Field name made lowercase.
    schematype = models.IntegerField(db_column='SchemaType')  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='splocalecontainer_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'splocalecontainer'


class Splocalecontaineritem(models.Model):
    splocalecontaineritemid = models.AutoField(db_column='SpLocaleContainerItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ishidden = models.TextField(db_column='IsHidden')  # Field name made lowercase. This field type is a guess.
    issystem = models.TextField(db_column='IsSystem')  # Field name made lowercase. This field type is a guess.
    isuiformatter = models.TextField(db_column='IsUIFormatter', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    picklistname = models.CharField(db_column='PickListName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isrequired = models.TextField(db_column='IsRequired', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weblinkname = models.CharField(db_column='WebLinkName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='splocalecontaineritem_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    splocalecontainerid = models.ForeignKey(Splocalecontainer, models.DO_NOTHING, db_column='SpLocaleContainerID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'splocalecontaineritem'


class Splocaleitemstr(models.Model):
    splocaleitemstrid = models.AutoField(db_column='SpLocaleItemStrID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=2, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=2)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=2048)  # Field name made lowercase.
    variant = models.CharField(db_column='Variant', max_length=2, blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    splocalecontainernameid = models.ForeignKey(Splocalecontainer, models.DO_NOTHING, db_column='SpLocaleContainerNameID', blank=True, null=True)  # Field name made lowercase.
    splocalecontaineritemdescid = models.ForeignKey(Splocalecontaineritem, models.DO_NOTHING, db_column='SpLocaleContainerItemDescID', blank=True, null=True)  # Field name made lowercase.
    splocalecontainerdescid = models.ForeignKey(Splocalecontainer, models.DO_NOTHING, db_column='SpLocaleContainerDescID', related_name='splocaleitemstr_splocalecontainerdescid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='splocaleitemstr_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    splocalecontaineritemnameid = models.ForeignKey(Splocalecontaineritem, models.DO_NOTHING, db_column='SpLocaleContainerItemNameID', related_name='splocaleitemstr_splocalecontaineritemnameid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'splocaleitemstr'


class Spmerging(models.Model):
    name = models.CharField(max_length=256)
    taskid = models.CharField(max_length=256)
    mergingstatus = models.CharField(max_length=256)
    response = models.TextField()
    table = models.CharField(max_length=256)
    newrecordid = models.IntegerField(blank=True, null=True)
    newrecordata = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    oldrecordids = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    collection = models.ForeignKey(Collection, models.DO_NOTHING)
    specifyuser = models.ForeignKey(Specifyuser, models.DO_NOTHING)
    timestampcreated = models.DateTimeField()
    timestampmodified = models.DateTimeField()
    createdbyagent = models.ForeignKey(Agent, models.DO_NOTHING, blank=True, null=True)
    modifiedbyagent = models.ForeignKey(Agent, models.DO_NOTHING, related_name='spmerging_modifiedbyagent_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spmerging'


class Sppermission(models.Model):
    sppermissionid = models.AutoField(db_column='SpPermissionID', primary_key=True)  # Field name made lowercase.
    actions = models.TextField(db_column='Actions', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    permissionclass = models.TextField(db_column='PermissionClass')  # Field name made lowercase.
    targetid = models.IntegerField(db_column='TargetId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sppermission'


class Spprincipal(models.Model):
    spprincipalid = models.AutoField(db_column='SpPrincipalID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    groupsubclass = models.CharField(db_column='GroupSubClass', max_length=255)  # Field name made lowercase.
    grouptype = models.CharField(db_column='groupType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    usergroupscopeid = models.IntegerField(db_column='userGroupScopeID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spprincipal_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spprincipal'


class SpprincipalSppermission(models.Model):
    sppermissionid = models.OneToOneField(Sppermission, models.DO_NOTHING, db_column='SpPermissionID', primary_key=True)  # Field name made lowercase. The composite primary key (SpPermissionID, SpPrincipalID) found, that is not supported. The first column is selected.
    spprincipalid = models.ForeignKey(Spprincipal, models.DO_NOTHING, db_column='SpPrincipalID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spprincipal_sppermission'
        unique_together = (('sppermissionid', 'spprincipalid'),)


class Spquery(models.Model):
    spqueryid = models.AutoField(db_column='SpQueryID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    contextname = models.CharField(db_column='ContextName', max_length=64)  # Field name made lowercase.
    contexttableid = models.SmallIntegerField(db_column='ContextTableId')  # Field name made lowercase.
    countonly = models.TextField(db_column='CountOnly', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isfavorite = models.TextField(db_column='IsFavorite', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    ordinal = models.SmallIntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    searchsynonymy = models.TextField(db_column='SearchSynonymy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    selectdistinct = models.TextField(db_column='SelectDistinct', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sqlstr = models.TextField(db_column='SqlStr', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spquery_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    specifyuserid = models.ForeignKey(Specifyuser, models.DO_NOTHING, db_column='SpecifyUserID')  # Field name made lowercase.
    smushed = models.TextField(db_column='Smushed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    formatauditrecids = models.TextField(db_column='FormatAuditRecIds', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'spquery'


class Spqueryfield(models.Model):
    spqueryfieldid = models.AutoField(db_column='SpQueryFieldID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    allownulls = models.TextField(db_column='AllowNulls', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    alwaysfilter = models.TextField(db_column='AlwaysFilter', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    columnalias = models.CharField(db_column='ColumnAlias', max_length=64, blank=True, null=True)  # Field name made lowercase.
    contexttableident = models.IntegerField(db_column='ContextTableIdent', blank=True, null=True)  # Field name made lowercase.
    endvalue = models.TextField(db_column='EndValue', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=32)  # Field name made lowercase.
    formatname = models.CharField(db_column='FormatName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isdisplay = models.TextField(db_column='IsDisplay')  # Field name made lowercase. This field type is a guess.
    isnot = models.TextField(db_column='IsNot')  # Field name made lowercase. This field type is a guess.
    isprompt = models.TextField(db_column='IsPrompt', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isrelfld = models.TextField(db_column='IsRelFld', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operend = models.IntegerField(db_column='OperEnd', blank=True, null=True)  # Field name made lowercase.
    operstart = models.IntegerField(db_column='OperStart')  # Field name made lowercase.
    position = models.SmallIntegerField(db_column='Position')  # Field name made lowercase.
    sorttype = models.IntegerField(db_column='SortType')  # Field name made lowercase.
    startvalue = models.TextField(db_column='StartValue', blank=True, null=True)  # Field name made lowercase.
    stringid = models.TextField(db_column='StringId')  # Field name made lowercase.
    tablelist = models.TextField(db_column='TableList')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spqueryfield_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    spqueryid = models.ForeignKey(Spquery, models.DO_NOTHING, db_column='SpQueryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spqueryfield'


class Spreport(models.Model):
    spreportid = models.AutoField(db_column='SpReportId', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    repeatcount = models.IntegerField(db_column='RepeatCount', blank=True, null=True)  # Field name made lowercase.
    repeatfield = models.CharField(db_column='RepeatField', max_length=255, blank=True, null=True)  # Field name made lowercase.
    appresourceid = models.ForeignKey(Spappresource, models.DO_NOTHING, db_column='AppResourceID')  # Field name made lowercase.
    spqueryid = models.ForeignKey(Spquery, models.DO_NOTHING, db_column='SpQueryID', blank=True, null=True)  # Field name made lowercase.
    workbenchtemplateid = models.ForeignKey('Workbenchtemplate', models.DO_NOTHING, db_column='WorkbenchTemplateID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    specifyuserid = models.ForeignKey(Specifyuser, models.DO_NOTHING, db_column='SpecifyUserID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spreport_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spreport'


class Sprole(models.Model):
    name = models.CharField(max_length=1024)
    collection = models.ForeignKey(Collection, models.DO_NOTHING)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'sprole'


class Sprolepolicy(models.Model):
    resource = models.CharField(max_length=1024)
    action = models.CharField(max_length=1024)
    role = models.ForeignKey(Sprole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sprolepolicy'


class Spstynthy(models.Model):
    spstynthyid = models.AutoField(db_column='SpStynthyID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    metaxml = models.TextField(db_column='MetaXML', blank=True, null=True)  # Field name made lowercase.
    updateperioddays = models.IntegerField(db_column='UpdatePeriodDays')  # Field name made lowercase.
    lastexported = models.DateTimeField(db_column='LastExported', blank=True, null=True)  # Field name made lowercase.
    collectionid = models.IntegerField(db_column='CollectionID')  # Field name made lowercase.
    mappingxml = models.TextField(db_column='MappingXML', blank=True, null=True)  # Field name made lowercase.
    key1 = models.CharField(db_column='Key1', max_length=256, blank=True, null=True)  # Field name made lowercase.
    key2 = models.CharField(db_column='Key2', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spstynthy'


class Spsymbiotainstance(models.Model):
    spsymbiotainstanceid = models.AutoField(db_column='SpSymbiotaInstanceID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    instancename = models.CharField(db_column='InstanceName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    lastcachebuild = models.DateTimeField(db_column='LastCacheBuild', blank=True, null=True)  # Field name made lowercase.
    lastpull = models.DateTimeField(db_column='LastPull', blank=True, null=True)  # Field name made lowercase.
    lastpush = models.DateTimeField(db_column='LastPush', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    symbiotakey = models.CharField(db_column='SymbiotaKey', max_length=128, blank=True, null=True)  # Field name made lowercase.
    schemamappingid = models.ForeignKey(Spexportschemamapping, models.DO_NOTHING, db_column='SchemaMappingID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='spsymbiotainstance_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spsymbiotainstance'


class Sptasksemaphore(models.Model):
    tasksemaphoreid = models.AutoField(db_column='TaskSemaphoreID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    context = models.CharField(db_column='Context', max_length=32, blank=True, null=True)  # Field name made lowercase.
    islocked = models.TextField(db_column='IsLocked', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lockedtime = models.DateTimeField(db_column='LockedTime', blank=True, null=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='MachineName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    scope = models.IntegerField(db_column='Scope', blank=True, null=True)  # Field name made lowercase.
    taskname = models.CharField(db_column='TaskName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    usagecount = models.IntegerField(db_column='UsageCount', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.ForeignKey(Specifyuser, models.DO_NOTHING, db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    disciplineid = models.ForeignKey(Discipline, models.DO_NOTHING, db_column='DisciplineID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='sptasksemaphore_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    collectionid = models.ForeignKey(Collection, models.DO_NOTHING, db_column='CollectionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sptasksemaphore'


class Spuserexternalid(models.Model):
    provider = models.CharField(max_length=256)
    providerid = models.CharField(max_length=4095)
    specifyuser = models.ForeignKey(Specifyuser, models.DO_NOTHING)
    enabled = models.IntegerField()
    idtoken = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spuserexternalid'


class Spuserpolicy(models.Model):
    resource = models.CharField(max_length=1024)
    action = models.CharField(max_length=1024)
    collection = models.ForeignKey(Collection, models.DO_NOTHING, blank=True, null=True)
    specifyuser = models.ForeignKey(Specifyuser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spuserpolicy'


class Spuserrole(models.Model):
    role = models.ForeignKey(Sprole, models.DO_NOTHING)
    specifyuser = models.ForeignKey(Specifyuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'spuserrole'


class Spversion(models.Model):
    spversionid = models.AutoField(db_column='SpVersionID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    appname = models.CharField(db_column='AppName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    appversion = models.CharField(db_column='AppVersion', max_length=16, blank=True, null=True)  # Field name made lowercase.
    schemaversion = models.CharField(db_column='SchemaVersion', max_length=16, blank=True, null=True)  # Field name made lowercase.
    isdbclosed = models.TextField(db_column='IsDBClosed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dbclosedby = models.CharField(db_column='DbClosedBy', max_length=32, blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='spversion_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    workbenchschemaversion = models.CharField(db_column='WorkbenchSchemaVersion', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spversion'


class Spviewsetobj(models.Model):
    spviewsetobjid = models.AutoField(db_column='SpViewSetObjID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    level = models.SmallIntegerField(db_column='Level')  # Field name made lowercase.
    metadata = models.CharField(db_column='MetaData', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    spappresourcedirid = models.ForeignKey(Spappresourcedir, models.DO_NOTHING, db_column='SpAppResourceDirID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='spviewsetobj_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spviewsetobj'


class Spvisualquery(models.Model):
    spvisualqueryid = models.AutoField(db_column='SpVisualQueryID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='spvisualquery_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    specifyuserid = models.ForeignKey(Specifyuser, models.DO_NOTHING, db_column='SpecifyUserID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spvisualquery'


class Storage(models.Model):
    storageid = models.AutoField(db_column='StorageID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    abbrev = models.CharField(db_column='Abbrev', max_length=16, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    highestchildnodenumber = models.IntegerField(db_column='HighestChildNodeNumber', blank=True, null=True)  # Field name made lowercase.
    isaccepted = models.TextField(db_column='IsAccepted', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    nodenumber = models.IntegerField(db_column='NodeNumber', blank=True, null=True)  # Field name made lowercase.
    number1 = models.IntegerField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.IntegerField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    timestampversion = models.DateTimeField(db_column='TimestampVersion', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    acceptedid = models.ForeignKey('self', models.DO_NOTHING, db_column='AcceptedID', blank=True, null=True)  # Field name made lowercase.
    storagetreedefitemid = models.ForeignKey('Storagetreedefitem', models.DO_NOTHING, db_column='StorageTreeDefItemID')  # Field name made lowercase.
    storagetreedefid = models.ForeignKey('Storagetreedef', models.DO_NOTHING, db_column='StorageTreeDefID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='storage_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentID', related_name='storage_parentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storage'


class Storageattachment(models.Model):
    storageattachmentid = models.AutoField(db_column='StorageAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='storageattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    storageid = models.ForeignKey(Storage, models.DO_NOTHING, db_column='StorageID')  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storageattachment'


class Storagetreedef(models.Model):
    storagetreedefid = models.AutoField(db_column='StorageTreeDefID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullnamedirection = models.IntegerField(db_column='FullNameDirection', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='storagetreedef_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storagetreedef'


class Storagetreedefitem(models.Model):
    storagetreedefitemid = models.AutoField(db_column='StorageTreeDefItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullnameseparator = models.CharField(db_column='FullNameSeparator', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isenforced = models.TextField(db_column='IsEnforced', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isinfullname = models.TextField(db_column='IsInFullName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    textafter = models.CharField(db_column='TextAfter', max_length=64, blank=True, null=True)  # Field name made lowercase.
    textbefore = models.CharField(db_column='TextBefore', max_length=64, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    parentitemid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentItemID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='storagetreedefitem_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    storagetreedefid = models.ForeignKey(Storagetreedef, models.DO_NOTHING, db_column='StorageTreeDefID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storagetreedefitem'


class Taxon(models.Model):
    taxonid = models.AutoField(db_column='TaxonID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=128, blank=True, null=True)  # Field name made lowercase.
    citesstatus = models.CharField(db_column='CitesStatus', max_length=32, blank=True, null=True)  # Field name made lowercase.
    colstatus = models.CharField(db_column='COLStatus', max_length=32, blank=True, null=True)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    cultivarname = models.CharField(db_column='CultivarName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    environmentalprotectionstatus = models.CharField(db_column='EnvironmentalProtectionStatus', max_length=64, blank=True, null=True)  # Field name made lowercase.
    esastatus = models.CharField(db_column='EsaStatus', max_length=64, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=512, blank=True, null=True)  # Field name made lowercase.
    groupnumber = models.CharField(db_column='GroupNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    highestchildnodenumber = models.IntegerField(db_column='HighestChildNodeNumber', blank=True, null=True)  # Field name made lowercase.
    isaccepted = models.TextField(db_column='IsAccepted', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ishybrid = models.TextField(db_column='IsHybrid', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isisnumber = models.CharField(db_column='IsisNumber', max_length=16, blank=True, null=True)  # Field name made lowercase.
    labelformat = models.CharField(db_column='LabelFormat', max_length=64, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    ncbitaxonnumber = models.CharField(db_column='NcbiTaxonNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nodenumber = models.IntegerField(db_column='NodeNumber', blank=True, null=True)  # Field name made lowercase.
    number1 = models.IntegerField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.IntegerField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=64, blank=True, null=True)  # Field name made lowercase.
    taxonomicserialnumber = models.CharField(db_column='TaxonomicSerialNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    unitind1 = models.CharField(db_column='UnitInd1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitind2 = models.CharField(db_column='UnitInd2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitind3 = models.CharField(db_column='UnitInd3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitind4 = models.CharField(db_column='UnitInd4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitname1 = models.CharField(db_column='UnitName1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitname2 = models.CharField(db_column='UnitName2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitname3 = models.CharField(db_column='UnitName3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitname4 = models.CharField(db_column='UnitName4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usfwscode = models.CharField(db_column='UsfwsCode', max_length=16, blank=True, null=True)  # Field name made lowercase.
    visibility = models.IntegerField(db_column='Visibility', blank=True, null=True)  # Field name made lowercase.
    acceptedid = models.ForeignKey('self', models.DO_NOTHING, db_column='AcceptedID', blank=True, null=True)  # Field name made lowercase.
    taxontreedefid = models.ForeignKey('Taxontreedef', models.DO_NOTHING, db_column='TaxonTreeDefID')  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentID', related_name='taxon_parentid_set', blank=True, null=True)  # Field name made lowercase.
    hybridparent1id = models.ForeignKey('self', models.DO_NOTHING, db_column='HybridParent1ID', related_name='taxon_hybridparent1id_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='taxon_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    visibilitysetbyid = models.ForeignKey(Specifyuser, models.DO_NOTHING, db_column='VisibilitySetByID', blank=True, null=True)  # Field name made lowercase.
    taxontreedefitemid = models.ForeignKey('Taxontreedefitem', models.DO_NOTHING, db_column='TaxonTreeDefItemID')  # Field name made lowercase.
    hybridparent2id = models.ForeignKey('self', models.DO_NOTHING, db_column='HybridParent2ID', related_name='taxon_hybridparent2id_set', blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    integer1 = models.BigIntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.BigIntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.BigIntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    integer4 = models.IntegerField(db_column='Integer4', blank=True, null=True)  # Field name made lowercase.
    integer5 = models.IntegerField(db_column='Integer5', blank=True, null=True)  # Field name made lowercase.
    text10 = models.CharField(db_column='Text10', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text11 = models.CharField(db_column='Text11', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text12 = models.CharField(db_column='Text12', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text13 = models.CharField(db_column='Text13', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text14 = models.CharField(db_column='Text14', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text15 = models.CharField(db_column='Text15', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text16 = models.CharField(db_column='Text16', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text17 = models.CharField(db_column='Text17', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text18 = models.CharField(db_column='Text18', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text19 = models.CharField(db_column='Text19', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text20 = models.CharField(db_column='Text20', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text6 = models.TextField(db_column='Text6', blank=True, null=True)  # Field name made lowercase.
    text7 = models.TextField(db_column='Text7', blank=True, null=True)  # Field name made lowercase.
    text8 = models.TextField(db_column='Text8', blank=True, null=True)  # Field name made lowercase.
    text9 = models.TextField(db_column='Text9', blank=True, null=True)  # Field name made lowercase.
    yesno10 = models.TextField(db_column='YesNo10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno11 = models.TextField(db_column='YesNo11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno12 = models.TextField(db_column='YesNo12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno13 = models.TextField(db_column='YesNo13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno14 = models.TextField(db_column='YesNo14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno15 = models.TextField(db_column='YesNo15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno16 = models.TextField(db_column='YesNo16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno17 = models.TextField(db_column='YesNo17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno18 = models.TextField(db_column='YesNo18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno19 = models.TextField(db_column='YesNo19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno6 = models.TextField(db_column='YesNo6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno7 = models.TextField(db_column='YesNo7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno8 = models.TextField(db_column='YesNo8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno9 = models.TextField(db_column='YesNo9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lsid = models.TextField(db_column='LSID', blank=True, null=True)  # Field name made lowercase.
    taxonattributeid = models.ForeignKey('Taxonattribute', models.DO_NOTHING, db_column='TaxonAttributeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxon'


class Taxonattachment(models.Model):
    taxonattachmentid = models.AutoField(db_column='TaxonAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='taxonattachment_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    taxonid = models.ForeignKey(Taxon, models.DO_NOTHING, db_column='TaxonID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxonattachment'


class Taxonattribute(models.Model):
    taxonattributeid = models.AutoField(db_column='TaxonAttributeID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date1precision = models.IntegerField(db_column='Date1Precision', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number10 = models.DecimalField(db_column='Number10', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number11 = models.DecimalField(db_column='Number11', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number12 = models.DecimalField(db_column='Number12', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number13 = models.DecimalField(db_column='Number13', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number14 = models.DecimalField(db_column='Number14', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number15 = models.DecimalField(db_column='Number15', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number16 = models.DecimalField(db_column='Number16', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number17 = models.DecimalField(db_column='Number17', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number18 = models.DecimalField(db_column='Number18', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number19 = models.DecimalField(db_column='Number19', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number20 = models.DecimalField(db_column='Number20', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number6 = models.DecimalField(db_column='Number6', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number7 = models.DecimalField(db_column='Number7', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number8 = models.DecimalField(db_column='Number8', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number9 = models.DecimalField(db_column='Number9', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text10 = models.CharField(db_column='Text10', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text11 = models.CharField(db_column='Text11', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text12 = models.CharField(db_column='Text12', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text13 = models.CharField(db_column='Text13', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text14 = models.CharField(db_column='Text14', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text15 = models.CharField(db_column='Text15', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text16 = models.CharField(db_column='Text16', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text17 = models.CharField(db_column='Text17', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text18 = models.CharField(db_column='Text18', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text19 = models.CharField(db_column='Text19', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text20 = models.CharField(db_column='Text20', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text21 = models.CharField(db_column='Text21', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text22 = models.CharField(db_column='Text22', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text23 = models.CharField(db_column='Text23', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text24 = models.CharField(db_column='Text24', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text25 = models.CharField(db_column='Text25', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text26 = models.CharField(db_column='Text26', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text27 = models.CharField(db_column='Text27', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text28 = models.CharField(db_column='Text28', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text29 = models.CharField(db_column='Text29', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text30 = models.CharField(db_column='Text30', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text31 = models.CharField(db_column='Text31', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text32 = models.CharField(db_column='Text32', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text33 = models.CharField(db_column='Text33', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text34 = models.CharField(db_column='Text34', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text35 = models.CharField(db_column='Text35', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text36 = models.CharField(db_column='Text36', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text37 = models.CharField(db_column='Text37', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text38 = models.CharField(db_column='Text38', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text39 = models.CharField(db_column='Text39', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text40 = models.CharField(db_column='Text40', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text41 = models.CharField(db_column='Text41', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text42 = models.CharField(db_column='Text42', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text43 = models.CharField(db_column='Text43', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text44 = models.CharField(db_column='Text44', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text45 = models.CharField(db_column='Text45', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text46 = models.CharField(db_column='Text46', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text47 = models.CharField(db_column='Text47', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text48 = models.CharField(db_column='Text48', max_length=256, blank=True, null=True)  # Field name made lowercase.
    text49 = models.TextField(db_column='Text49', blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text50 = models.TextField(db_column='Text50', blank=True, null=True)  # Field name made lowercase.
    text51 = models.TextField(db_column='Text51', blank=True, null=True)  # Field name made lowercase.
    text52 = models.TextField(db_column='Text52', blank=True, null=True)  # Field name made lowercase.
    text53 = models.TextField(db_column='Text53', blank=True, null=True)  # Field name made lowercase.
    text54 = models.TextField(db_column='Text54', blank=True, null=True)  # Field name made lowercase.
    text55 = models.TextField(db_column='Text55', blank=True, null=True)  # Field name made lowercase.
    text56 = models.TextField(db_column='Text56', blank=True, null=True)  # Field name made lowercase.
    text57 = models.TextField(db_column='Text57', blank=True, null=True)  # Field name made lowercase.
    text58 = models.TextField(db_column='Text58', blank=True, null=True)  # Field name made lowercase.
    text6 = models.CharField(db_column='Text6', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text7 = models.CharField(db_column='Text7', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text8 = models.CharField(db_column='Text8', max_length=128, blank=True, null=True)  # Field name made lowercase.
    text9 = models.CharField(db_column='Text9', max_length=128, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno10 = models.TextField(db_column='YesNo10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno11 = models.TextField(db_column='YesNo11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno12 = models.TextField(db_column='YesNo12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno13 = models.TextField(db_column='YesNo13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno14 = models.TextField(db_column='YesNo14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno15 = models.TextField(db_column='YesNo15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno16 = models.TextField(db_column='YesNo16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno17 = models.TextField(db_column='YesNo17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno18 = models.TextField(db_column='YesNo18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno19 = models.TextField(db_column='YesNo19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno20 = models.TextField(db_column='YesNo20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno21 = models.TextField(db_column='YesNo21', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno22 = models.TextField(db_column='YesNo22', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno23 = models.TextField(db_column='YesNo23', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno24 = models.TextField(db_column='YesNo24', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno25 = models.TextField(db_column='YesNo25', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno26 = models.TextField(db_column='YesNo26', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno27 = models.TextField(db_column='YesNo27', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno28 = models.TextField(db_column='YesNo28', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno29 = models.TextField(db_column='YesNo29', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno30 = models.TextField(db_column='YesNo30', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno31 = models.TextField(db_column='YesNo31', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno32 = models.TextField(db_column='YesNo32', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno33 = models.TextField(db_column='YesNo33', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno34 = models.TextField(db_column='YesNo34', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno35 = models.TextField(db_column='YesNo35', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno36 = models.TextField(db_column='YesNo36', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno37 = models.TextField(db_column='YesNo37', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno38 = models.TextField(db_column='YesNo38', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno39 = models.TextField(db_column='YesNo39', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno4 = models.TextField(db_column='YesNo4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno40 = models.TextField(db_column='YesNo40', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno41 = models.TextField(db_column='YesNo41', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno42 = models.TextField(db_column='YesNo42', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno43 = models.TextField(db_column='YesNo43', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno44 = models.TextField(db_column='YesNo44', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno45 = models.TextField(db_column='YesNo45', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno46 = models.TextField(db_column='YesNo46', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno47 = models.TextField(db_column='YesNo47', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno48 = models.TextField(db_column='YesNo48', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno49 = models.TextField(db_column='YesNo49', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno5 = models.TextField(db_column='YesNo5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno50 = models.TextField(db_column='YesNo50', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno51 = models.TextField(db_column='YesNo51', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno52 = models.TextField(db_column='YesNo52', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno53 = models.TextField(db_column='YesNo53', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno54 = models.TextField(db_column='YesNo54', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno55 = models.TextField(db_column='YesNo55', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno56 = models.TextField(db_column='YesNo56', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno57 = models.TextField(db_column='YesNo57', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno58 = models.TextField(db_column='YesNo58', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno59 = models.TextField(db_column='YesNo59', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno6 = models.TextField(db_column='YesNo6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno60 = models.TextField(db_column='YesNo60', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno61 = models.TextField(db_column='YesNo61', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno62 = models.TextField(db_column='YesNo62', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno63 = models.TextField(db_column='YesNo63', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno64 = models.TextField(db_column='YesNo64', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno65 = models.TextField(db_column='YesNo65', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno66 = models.TextField(db_column='YesNo66', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno67 = models.TextField(db_column='YesNo67', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno68 = models.TextField(db_column='YesNo68', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno69 = models.TextField(db_column='YesNo69', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno7 = models.TextField(db_column='YesNo7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno70 = models.TextField(db_column='YesNo70', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno71 = models.TextField(db_column='YesNo71', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno72 = models.TextField(db_column='YesNo72', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno73 = models.TextField(db_column='YesNo73', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno74 = models.TextField(db_column='YesNo74', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno75 = models.TextField(db_column='YesNo75', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno76 = models.TextField(db_column='YesNo76', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno77 = models.TextField(db_column='YesNo77', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno78 = models.TextField(db_column='YesNo78', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno79 = models.TextField(db_column='YesNo79', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno8 = models.TextField(db_column='YesNo8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno80 = models.TextField(db_column='YesNo80', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno81 = models.TextField(db_column='YesNo81', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno82 = models.TextField(db_column='YesNo82', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno9 = models.TextField(db_column='YesNo9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    agent1id = models.ForeignKey(Agent, models.DO_NOTHING, db_column='Agent1ID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='taxonattribute_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='taxonattribute_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxonattribute'


class Taxoncitation(models.Model):
    taxoncitationid = models.AutoField(db_column='TaxonCitationID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='taxoncitation_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    taxonid = models.ForeignKey(Taxon, models.DO_NOTHING, db_column='TaxonID')  # Field name made lowercase.
    referenceworkid = models.ForeignKey(Referencework, models.DO_NOTHING, db_column='ReferenceWorkID')  # Field name made lowercase.
    figurenumber = models.CharField(db_column='FigureNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isfigured = models.TextField(db_column='IsFigured', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pagenumber = models.CharField(db_column='PageNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    platenumber = models.CharField(db_column='PlateNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxoncitation'


class Taxontreedef(models.Model):
    taxontreedefid = models.AutoField(db_column='TaxonTreeDefID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    fullnamedirection = models.IntegerField(db_column='FullNameDirection', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='taxontreedef_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxontreedef'


class Taxontreedefitem(models.Model):
    taxontreedefitemid = models.AutoField(db_column='TaxonTreeDefItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    formattoken = models.CharField(db_column='FormatToken', max_length=32, blank=True, null=True)  # Field name made lowercase.
    fullnameseparator = models.CharField(db_column='FullNameSeparator', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isenforced = models.TextField(db_column='IsEnforced', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isinfullname = models.TextField(db_column='IsInFullName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    rankid = models.IntegerField(db_column='RankID')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    textafter = models.CharField(db_column='TextAfter', max_length=64, blank=True, null=True)  # Field name made lowercase.
    textbefore = models.CharField(db_column='TextBefore', max_length=64, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    taxontreedefid = models.ForeignKey(Taxontreedef, models.DO_NOTHING, db_column='TaxonTreeDefID')  # Field name made lowercase.
    parentitemid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentItemID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='taxontreedefitem_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxontreedefitem'


class Treatmentevent(models.Model):
    treatmenteventid = models.AutoField(db_column='TreatmentEventID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    dateboxed = models.DateField(db_column='DateBoxed', blank=True, null=True)  # Field name made lowercase.
    datecleaned = models.DateField(db_column='DateCleaned', blank=True, null=True)  # Field name made lowercase.
    datecompleted = models.DateField(db_column='DateCompleted', blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    datetoisolation = models.DateField(db_column='DateToIsolation', blank=True, null=True)  # Field name made lowercase.
    datetreatmentended = models.DateField(db_column='DateTreatmentEnded', blank=True, null=True)  # Field name made lowercase.
    datetreatmentstarted = models.DateField(db_column='DateTreatmentStarted', blank=True, null=True)  # Field name made lowercase.
    fieldnumber = models.CharField(db_column='FieldNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    storage = models.CharField(db_column='Storage', max_length=64, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    treatmentnumber = models.CharField(db_column='TreatmentNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=128, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    accessionid = models.ForeignKey(Accession, models.DO_NOTHING, db_column='AccessionID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='treatmentevent_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.ForeignKey(Division, models.DO_NOTHING, db_column='DivisionID', blank=True, null=True)  # Field name made lowercase.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID', blank=True, null=True)  # Field name made lowercase.
    number1 = models.IntegerField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.IntegerField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number4 = models.DecimalField(db_column='Number4', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number5 = models.DecimalField(db_column='Number5', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    text4 = models.TextField(db_column='Text4', blank=True, null=True)  # Field name made lowercase.
    text5 = models.TextField(db_column='Text5', blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    authorizedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='AuthorizedByID', related_name='treatmentevent_authorizedbyid_set', blank=True, null=True)  # Field name made lowercase.
    performedbyid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='PerformedByID', related_name='treatmentevent_performedbyid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'treatmentevent'


class Treatmenteventattachment(models.Model):
    treatmenteventattachmentid = models.AutoField(db_column='TreatmentEventAttachmentID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    treatmenteventid = models.ForeignKey(Treatmentevent, models.DO_NOTHING, db_column='TreatmentEventID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    attachmentid = models.ForeignKey(Attachment, models.DO_NOTHING, db_column='AttachmentID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='treatmenteventattachment_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'treatmenteventattachment'


class UserCreatedLichenGenera(models.Model):
    lichen_genus = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_created_lichen_genera'


class Voucherrelationship(models.Model):
    voucherrelationshipid = models.AutoField(db_column='VoucherRelationshipID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    collectionmemberid = models.IntegerField(db_column='CollectionMemberID')  # Field name made lowercase.
    collectioncode = models.CharField(db_column='CollectionCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    institutioncode = models.CharField(db_column='InstitutionCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    integer1 = models.IntegerField(db_column='Integer1', blank=True, null=True)  # Field name made lowercase.
    integer2 = models.IntegerField(db_column='Integer2', blank=True, null=True)  # Field name made lowercase.
    integer3 = models.IntegerField(db_column='Integer3', blank=True, null=True)  # Field name made lowercase.
    number1 = models.DecimalField(db_column='Number1', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number2 = models.DecimalField(db_column='Number2', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    number3 = models.DecimalField(db_column='Number3', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    text1 = models.TextField(db_column='Text1', blank=True, null=True)  # Field name made lowercase.
    text2 = models.TextField(db_column='Text2', blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase.
    urllink = models.CharField(db_column='UrlLink', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    vouchernumber = models.CharField(db_column='VoucherNumber', max_length=256, blank=True, null=True)  # Field name made lowercase.
    yesno1 = models.TextField(db_column='YesNo1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno2 = models.TextField(db_column='YesNo2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yesno3 = models.TextField(db_column='YesNo3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collectionobjectid = models.ForeignKey(Collectionobject, models.DO_NOTHING, db_column='CollectionObjectID')  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='voucherrelationship_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voucherrelationship'


class Workbench(models.Model):
    workbenchid = models.AutoField(db_column='WorkbenchID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    allpermissionlevel = models.IntegerField(db_column='AllPermissionLevel', blank=True, null=True)  # Field name made lowercase.
    tableid = models.IntegerField(db_column='TableID', blank=True, null=True)  # Field name made lowercase.
    exportinstitutionname = models.CharField(db_column='ExportInstitutionName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    exportedfromtablename = models.CharField(db_column='ExportedFromTableName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    formid = models.IntegerField(db_column='FormId', blank=True, null=True)  # Field name made lowercase.
    grouppermissionlevel = models.IntegerField(db_column='GroupPermissionLevel', blank=True, null=True)  # Field name made lowercase.
    lockedbyusername = models.CharField(db_column='LockedByUserName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    ownerpermissionlevel = models.IntegerField(db_column='OwnerPermissionLevel', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    srcfilepath = models.CharField(db_column='SrcFilePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specifyuserid = models.ForeignKey(Specifyuser, models.DO_NOTHING, db_column='SpecifyUserID')  # Field name made lowercase.
    workbenchtemplateid = models.ForeignKey('Workbenchtemplate', models.DO_NOTHING, db_column='WorkbenchTemplateID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    spprincipalid = models.ForeignKey(Spprincipal, models.DO_NOTHING, db_column='SpPrincipalID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='workbench_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workbench'


class Workbenchdataitem(models.Model):
    workbenchdataitemid = models.AutoField(db_column='WorkbenchDataItemID', primary_key=True)  # Field name made lowercase.
    celldata = models.TextField(db_column='CellData', blank=True, null=True)  # Field name made lowercase.
    rownumber = models.SmallIntegerField(db_column='RowNumber', blank=True, null=True)  # Field name made lowercase.
    validationstatus = models.SmallIntegerField(db_column='ValidationStatus', blank=True, null=True)  # Field name made lowercase.
    workbenchtemplatemappingitemid = models.ForeignKey('Workbenchtemplatemappingitem', models.DO_NOTHING, db_column='WorkbenchTemplateMappingItemID')  # Field name made lowercase.
    workbenchrowid = models.ForeignKey('Workbenchrow', models.DO_NOTHING, db_column='WorkbenchRowID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workbenchdataitem'


class Workbenchrow(models.Model):
    workbenchrowid = models.AutoField(db_column='WorkbenchRowID', primary_key=True)  # Field name made lowercase.
    biogeomancerresults = models.TextField(db_column='BioGeomancerResults', blank=True, null=True)  # Field name made lowercase.
    cardimagedata = models.TextField(db_column='CardImageData', blank=True, null=True)  # Field name made lowercase.
    cardimagefullpath = models.CharField(db_column='CardImageFullPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lat1text = models.CharField(db_column='Lat1Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lat2text = models.CharField(db_column='Lat2Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    long1text = models.CharField(db_column='Long1Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    long2text = models.CharField(db_column='Long2Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recordid = models.IntegerField(db_column='RecordID', blank=True, null=True)  # Field name made lowercase.
    rownumber = models.SmallIntegerField(db_column='RowNumber', blank=True, null=True)  # Field name made lowercase.
    uploadstatus = models.IntegerField(db_column='UploadStatus', blank=True, null=True)  # Field name made lowercase.
    workbenchid = models.ForeignKey(Workbench, models.DO_NOTHING, db_column='WorkbenchID')  # Field name made lowercase.
    sgrstatus = models.IntegerField(db_column='SGRStatus', blank=True, null=True)  # Field name made lowercase.
    errorestimate = models.DecimalField(db_column='ErrorEstimate', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    errorpolygon = models.TextField(db_column='ErrorPolygon', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workbenchrow'


class Workbenchrowexportedrelationship(models.Model):
    workbenchrowexportedrelationshipid = models.AutoField(db_column='WorkbenchRowExportedRelationshipID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    recordid = models.IntegerField(db_column='RecordID', blank=True, null=True)  # Field name made lowercase.
    relationshipname = models.CharField(db_column='RelationshipName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='workbenchrowexportedrelationship_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.
    workbenchrowid = models.ForeignKey(Workbenchrow, models.DO_NOTHING, db_column='WorkbenchRowID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workbenchrowexportedrelationship'


class Workbenchrowimage(models.Model):
    workbenchrowimageid = models.AutoField(db_column='WorkbenchRowImageID', primary_key=True)  # Field name made lowercase.
    attachtotablename = models.CharField(db_column='AttachToTableName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    cardimagedata = models.TextField(db_column='CardImageData', blank=True, null=True)  # Field name made lowercase.
    cardimagefullpath = models.CharField(db_column='CardImageFullPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imageorder = models.IntegerField(db_column='ImageOrder', blank=True, null=True)  # Field name made lowercase.
    workbenchrowid = models.ForeignKey(Workbenchrow, models.DO_NOTHING, db_column='WorkbenchRowID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workbenchrowimage'


class Workbenchtemplate(models.Model):
    workbenchtemplateid = models.AutoField(db_column='WorkbenchTemplateID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    srcfilepath = models.CharField(db_column='SrcFilePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specifyuserid = models.ForeignKey(Specifyuser, models.DO_NOTHING, db_column='SpecifyUserID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', related_name='workbenchtemplate_modifiedbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workbenchtemplate'


class Workbenchtemplatemappingitem(models.Model):
    workbenchtemplatemappingitemid = models.AutoField(db_column='WorkbenchTemplateMappingItemID', primary_key=True)  # Field name made lowercase.
    timestampcreated = models.DateTimeField(db_column='TimestampCreated')  # Field name made lowercase.
    timestampmodified = models.DateTimeField(db_column='TimestampModified', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    xcoord = models.SmallIntegerField(db_column='XCoord', blank=True, null=True)  # Field name made lowercase.
    ycoord = models.SmallIntegerField(db_column='YCoord', blank=True, null=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=64, blank=True, null=True)  # Field name made lowercase.
    carryforward = models.TextField(db_column='CarryForward', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    datafieldlength = models.SmallIntegerField(db_column='DataFieldLength', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fieldtype = models.SmallIntegerField(db_column='FieldType', blank=True, null=True)  # Field name made lowercase.
    importedcolname = models.CharField(db_column='ImportedColName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iseditable = models.TextField(db_column='IsEditable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isexportabletocontent = models.TextField(db_column='IsExportableToContent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isincludedintitle = models.TextField(db_column='IsIncludedInTitle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isrequired = models.TextField(db_column='IsRequired', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    metadata = models.CharField(db_column='MetaData', max_length=128, blank=True, null=True)  # Field name made lowercase.
    datacolumnindex = models.SmallIntegerField(db_column='DataColumnIndex', blank=True, null=True)  # Field name made lowercase.
    tableid = models.IntegerField(db_column='TableId', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    vieworder = models.SmallIntegerField(db_column='ViewOrder', blank=True, null=True)  # Field name made lowercase.
    modifiedbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='ModifiedByAgentID', blank=True, null=True)  # Field name made lowercase.
    workbenchtemplateid = models.ForeignKey(Workbenchtemplate, models.DO_NOTHING, db_column='WorkbenchTemplateID')  # Field name made lowercase.
    createdbyagentid = models.ForeignKey(Agent, models.DO_NOTHING, db_column='CreatedByAgentID', related_name='workbenchtemplatemappingitem_createdbyagentid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workbenchtemplatemappingitem'
