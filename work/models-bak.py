import uuid as uuid
from django.db import models

# Create your models here.


class CofkUnionWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_union_work'

    '''__table_args__ = (
        CheckConstraint('(addressees_inferred = 0) OR (addressees_inferred = 1)'),
        CheckConstraint('(addressees_uncertain = 0) OR (addressees_uncertain = 1)'),
        CheckConstraint('(authors_inferred = 0) OR (authors_inferred = 1)'),
        CheckConstraint('(authors_uncertain = 0) OR (authors_uncertain = 1)'),
        CheckConstraint('(date_of_work_approx = 0) OR (date_of_work_approx = 1)'),
        CheckConstraint('(date_of_work_inferred = 0) OR (date_of_work_inferred = 1)'),
        CheckConstraint('(date_of_work_std_is_range = 0) OR (date_of_work_std_is_range = 1)'),
        CheckConstraint('(date_of_work_uncertain = 0) OR (date_of_work_uncertain = 1)'),
        CheckConstraint('(destination_inferred = 0) OR (destination_inferred = 1)'),
        CheckConstraint('(destination_uncertain = 0) OR (destination_uncertain = 1)'),
        CheckConstraint('(origin_inferred = 0) OR (origin_inferred = 1)'),
        CheckConstraint('(origin_uncertain = 0) OR (origin_uncertain = 1)'),
        CheckConstraint('(work_is_translation = 0) OR (work_is_translation = 1)'),
        CheckConstraint('(work_to_be_deleted = 0) OR (work_to_be_deleted = 1)')
    )'''

    work_id = models.CharField(max_length=100)  # , primary_key=True)
    description = models.TextField()
    date_of_work_as_marked = models.CharField(max_length=250)
    original_calendar = models.CharField(max_length=2, null=False, default='')
    date_of_work_std = models.CharField(max_length=12)  # , default=text("'9999-12-31'::character varying"))
    date_of_work_std_gregorian = models.CharField(max_length=12)  # , default=text("'9999-12-31'::character varying"))
    date_of_work_std_year = models.IntegerField()
    date_of_work_std_month = models.IntegerField()
    date_of_work_std_day = models.IntegerField()
    date_of_work2_std_year = models.IntegerField()
    date_of_work2_std_month = models.IntegerField()
    date_of_work2_std_day = models.IntegerField()
    # TODO
    # A lot of boolean field below
    date_of_work_std_is_range = models.SmallIntegerField(null=False, default=0)
    date_of_work_inferred = models.SmallIntegerField(null=False, default=0)
    date_of_work_uncertain = models.SmallIntegerField(null=False, default=0)
    date_of_work_approx = models.SmallIntegerField(null=False, default=0)
    authors_as_marked = models.TextField()
    addressees_as_marked = models.TextField()
    authors_inferred = models.SmallIntegerField(null=False, default=0)
    authors_uncertain = models.SmallIntegerField(null=False, default=0)
    addressees_inferred = models.SmallIntegerField(null=False, default=0)
    addressees_uncertain = models.SmallIntegerField(null=False, default=0)
    destination_as_marked = models.TextField()
    origin_as_marked = models.TextField()
    destination_inferred = models.SmallIntegerField(null=False, default=0)
    destination_uncertain = models.SmallIntegerField(null=False, default=0)
    origin_inferred = models.SmallIntegerField(null=False, default=0)
    origin_uncertain = models.SmallIntegerField(null=False, default=0)
    abstract = models.TextField()
    keywords = models.TextField()
    language_of_work = models.CharField(max_length=255)
    work_is_translation = models.SmallIntegerField(null=False, default=0)
    incipit = models.TextField()
    explicit = models.TextField()
    ps = models.TextField()
    # TODO on update
    # original_catalogue = Column(ForeignKey('cofk_lookup_catalogue.catalogue_code', onupdate='CASCADE'), null=False, default='')
    # missing onupdate
    original_catalogue = models.ForeignKey("uploader.CofkLookupCatalogue", null=False, default='',
                                           on_delete=models.DO_NOTHING)
    accession_code = models.CharField(max_length=1000)
    work_to_be_deleted = models.SmallIntegerField(null=False, default=0)
    iwork_id = models.AutoField(primary_key=True, null=False, unique=True)
    editors_notes = models.TextField()
    # TODO
    # Enumarated field?
    edit_status = models.CharField(max_length=3, null=False, default='')
    # TODO
    # Boolean field
    relevant_to_cofk = models.CharField(max_length=3, null=False, default='Y')
    creation_timestamp = models.DateTimeField(auto_now=True)
    # creation_user = models.CharField(max_length=50, null=False, default=current_user)
    change_timestamp = models.DateTimeField(auto_now=True)
    # change_user = models.CharField(max_length=50, null=False, default=current_user)
    uuid = models.UUIDField(default=uuid.uuid4)

    # cofk_lookup_catalogue = relationship('CofkLookupCatalogue')


class CofkCollectWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_work'

    #__table_args__ = (
        #    ForeignKeyConstraint(['upload_id', 'destination_id'], ['cofk_collect_location.upload_id', 'cofk_collect_location.location_id']),
        #    ForeignKeyConstraint(['upload_id', 'origin_id'], ['cofk_collect_location.upload_id', 'cofk_collect_location.location_id'])
    #)

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    upload_id = models.ForeignKey("uploader.CofkCollectUpload", null=False, on_delete=models.CASCADE)
    # upload_id = models.OneToOneField("uploader.CofkCollectUpload", null=False, on_delete=models.DO_NOTHING)
    iwork_id = models.AutoField(primary_key=True)
    union_iwork_id = models.ForeignKey("CofkUnionWork", null=True, on_delete=models.DO_NOTHING)
    # union_iwork_id = Column(ForeignKey('cofk_union_work.iwork_id', ondelete='SET NULL'))
    # work_id = Column(ForeignKey('cofk_union_work.work_id', ondelete='SET NULL'))
    # work_id = models.ForeignKey("uploader.CofkUnionWork", on_delete=models.SET_NULL)
    # TODO
    # Missing work_id
    date_of_work_as_marked = models.CharField(max_length=250)
    original_calendar = models.CharField(max_length=2, null=False, default='')
    date_of_work_std_year = models.IntegerField()
    date_of_work_std_month = models.IntegerField()
    date_of_work_std_day = models.IntegerField()
    date_of_work2_std_year = models.IntegerField()
    date_of_work2_std_month = models.IntegerField()
    date_of_work2_std_day = models.IntegerField()
    # TODO
    # Booleans below
    date_of_work_std_is_range = models.SmallIntegerField(null=False, default=0)
    date_of_work_inferred = models.SmallIntegerField(null=False, default=0)
    date_of_work_uncertain = models.SmallIntegerField(null=False, default=0)
    date_of_work_approx = models.SmallIntegerField(null=False, default=0)
    notes_on_date_of_work = models.TextField()
    authors_as_marked = models.TextField()
    authors_inferred = models.SmallIntegerField(null=False, default=0)
    authors_uncertain = models.SmallIntegerField(null=False, default=0)
    notes_on_authors = models.TextField()
    addressees_as_marked = models.TextField()
    addressees_inferred = models.SmallIntegerField(null=False, default=0)
    addressees_uncertain = models.SmallIntegerField(null=False, default=0)
    notes_on_addressees = models.TextField()
    destination_id = models.IntegerField()
    destination_as_marked = models.TextField()
    destination_inferred = models.SmallIntegerField(null=False, default=0)
    destination_uncertain = models.SmallIntegerField(null=False, default=0)
    origin_id = models.IntegerField()
    origin_as_marked = models.TextField()
    origin_inferred = models.SmallIntegerField(null=False, default=0)
    origin_uncertain = models.SmallIntegerField(null=False, default=0)
    abstract = models.TextField()
    keywords = models.TextField()
    language_of_work = models.CharField(max_length=255)
    incipit = models.TextField()
    excipit = models.TextField()
    accession_code = models.CharField(max_length=250)
    notes_on_letter = models.TextField()
    notes_on_people_mentioned = models.TextField()
    # upload_status = Column(ForeignKey('cofk_collect_status.status_id'), null=False, default=text("1"))
    upload_status = models.ForeignKey("uploader.CofkCollectStatus", null=False, default="1",
                                      on_delete=models.DO_NOTHING)
    editors_notes = models.TextField()
    _id = models.CharField(max_length=32)
    date_of_work2_approx = models.SmallIntegerField(null=False, default=0)
    date_of_work2_inferred = models.SmallIntegerField(null=False, default=0)
    date_of_work2_uncertain = models.SmallIntegerField(null=False, default=0)
    mentioned_as_marked = models.TextField()
    mentioned_inferred = models.SmallIntegerField(null=False, default=0)
    mentioned_uncertain = models.SmallIntegerField(null=False, default=0)
    notes_on_destination = models.TextField()
    notes_on_origin = models.TextField()
    notes_on_place_mentioned = models.TextField()
    place_mentioned_as_marked = models.TextField()
    place_mentioned_inferred = models.SmallIntegerField(null=False, default=0)
    place_mentioned_uncertain = models.SmallIntegerField(null=False, default=0)
    upload_name = models.CharField(max_length=254)
    explicit = models.TextField()

    # union_iwork = relationship('CofkUnionWork', primaryjoin='CofkCollectWork.union_iwork_id == CofkUnionWork.iwork_id')
    # upload = relationship('CofkCollectLocation', primaryjoin='CofkCollectWork.upload_id == CofkCollectLocation.upload_id')
    # upload1 = relationship('CofkCollectLocation', primaryjoin='CofkCollectWork.upload_id == CofkCollectLocation.upload_id')
    # upload2 = relationship('CofkCollectUpload')
    # cofk_collect_statu = relationship('CofkCollectStatus')
    # work = relationship('CofkUnionWork', primaryjoin='CofkCollectWork.work_id == CofkUnionWork.work_id')

'''
class CofkCollectWorkSummary(CofkCollectWork):
    class Meta:
        db_table = 'cofk_collect_work_summary'

    __table_args__ = (
        #    ForeignKeyConstraint(['upload_id', 'work_id_in_tool'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id']),
    )

    # upload_id = models.AutoField(primary_key=True)
    # work_id_in_tool = models.AutoField(primary_key=True)
    source_of_data = models.CharField(max_length=250)
    # notes_on_letter = models.TextField()
    date_of_work = models.CharField(max_length=32)
    # date_of_work_as_marked = models.CharField(max_length=250)
    # original_calendar = models.CharField(max_length=30)
    date_of_work_is_range = models.CharField(max_length=30)
    # date_of_work_inferred = models.CharField(max_length=30)
    # date_of_work_uncertain = models.CharField(max_length=30)
    # date_of_work_approx = models.CharField(max_length=30)
    # notes_on_date_of_work = models.TextField()
    authors = models.TextField()
    # authors_as_marked = models.TextField()
    # authors_inferred = models.CharField(max_length=30)
    # authors_uncertain = models.CharField(max_length=30)
    # notes_on_authors = models.TextField()
    addressees = models.TextField()
    # addressees_as_marked = models.TextField()
    # addressees_inferred = models.CharField(max_length=30)
    # addressees_uncertain = models.CharField(max_length=30)
    # notes_on_addressees = models.TextField()
    destination = models.TextField()
    # destination_as_marked = models.TextField()
    # destination_inferred = models.CharField(max_length=30)
    # destination_uncertain = models.CharField(max_length=30)
    origin = models.TextField()
    # origin_as_marked = models.TextField()
    # origin_inferred = models.CharField(max_length=30)
    # origin_uncertain = models.CharField(max_length=30)
    # abstract = models.TextField()
    # keywords = models.TextField()
    languages_of_work = models.TextField()
    subjects_of_work = models.TextField()
    # incipit = models.TextField()
    # excipit = models.TextField()
    people_mentioned = models.TextField()
    # notes_on_people_mentioned = models.TextField()
    places_mentioned = models.TextField()
    manifestations = models.TextField()
    related_resources = models.TextField()
    # editors_notes = models.TextField()
'''


class CofkCollectAddresseeOfWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_addressee_of_work'

    # __table_args__ = (
    # ForeignKeyConstraint(['upload_id', 'iperson_id'], ['cofk_collect_person.upload_id', 'cofk_collect_person.iperson_id']),
    # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id'])
    # )

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    # upload_id = models.ForeignKey("uploader.CofkCollectUpload", primary_key=True, null=False, on_delete=models.DO_NOTHING)
    upload_id = models.OneToOneField("uploader.CofkCollectUpload", on_delete=models.DO_NOTHING)
    addressee_id = models.AutoField(primary_key=True)
    # TODO
    # Fix missing columns below
    iperson_id = models.IntegerField(null=False)
    # iwork_id = models.AutoField(primary_key=True)
    notes_on_addressee = models.TextField()
    _id = models.CharField(max_length=32)

    # upload = relationship('CofkCollectPerson')
    # upload1 = relationship('CofkCollectWork')
    # upload2 = relationship('CofkCollectUpload')


class CofkCollectAuthorOfWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_author_of_work'

    # __table_args__ = (
    # ForeignKeyConstraint(['upload_id', 'iperson_id'], ['cofk_collect_person.upload_id', 'cofk_collect_person.iperson_id']),
    # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id'])
    # )

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    upload_id = models.ForeignKey("uploader.CofkCollectUpload", null=False, on_delete=models.CASCADE)
    #upload_id = models.OneToOneField("uploader.CofkCollectUpload", on_delete=models.DO_NOTHING)
    author_id = models.AutoField(primary_key=True)
    iperson_id = models.IntegerField(null=False)
    # TODO
    # missing iwork_id
    # iwork_id = models.AutoField(primary_key=True)
    notes_on_author = models.TextField()
    _id = models.CharField(max_length=32)

    # upload = relationship('CofkCollectPerson')
    # upload1 = relationship('CofkCollectWork')
    # upload2 = relationship('CofkCollectUpload')


class CofkCollectDestinationOfWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_destination_of_work'

    #__table_args__ = (
        # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id']),
        # ForeignKeyConstraint(['upload_id', 'location_id'], ['cofk_collect_location.upload_id', 'cofk_collect_location.location_id'])
    #)

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    # upload_id = models.ForeignKey("uploader.CofkCollectUpload", primary_key=True, null=False, on_delete=models.DO_NOTHING)
    upload_id = models.OneToOneField("uploader.CofkCollectUpload", on_delete=models.DO_NOTHING)
    destination_id = models.AutoField(primary_key=True)
    location_id = models.IntegerField(null=False)
    # TODO
    # missing iwork_id
    # iwork_id = models.AutoField(primary_key=True)
    notes_on_destination = models.TextField()
    _id = models.CharField(max_length=32)

    # upload = relationship('CofkCollectWork')
    # upload1 = relationship('CofkCollectLocation')
    # upload2 = relationship('CofkCollectUpload')


class CofkCollectLanguageOfWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_language_of_work'

    #__table_args__ = (
        # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id']),
    #)

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    upload_id = models.ForeignKey("uploader.CofkCollectUpload", null=False, on_delete=models.CASCADE)
    # upload_id = models.OneToOneField("uploader.CofkCollectUpload", on_delete=models.CASCADE)
    language_of_work_id = models.AutoField(primary_key=True)
    # TODO
    # missing iwork_id
    # iwork_id = models.AutoField(primary_key=True)
    # language_code = Column(ForeignKey('iso_639_language_codes.code_639_3'), null=False)
    language_code = models.ForeignKey("uploader.Iso639LanguageCode", null=False, on_delete=models.DO_NOTHING)
    _id = models.CharField(max_length=32)

    # iso_639_language_code = relationship('Iso639LanguageCode')
    # upload = relationship('CofkCollectWork')
    # upload1 = relationship('CofkCollectUpload')


class CofkCollectOriginOfWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_origin_of_work'

    #__table_args__ = (
        # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id']),
        # ForeignKeyConstraint(['upload_id', 'location_id'], ['cofk_collect_location.upload_id', 'cofk_collect_location.location_id'])
    #)

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    # upload_id = models.ForeignKey("uploader.CofkCollectUpload", primary_key=True, null=False, on_delete=models.DO_NOTHING)
    upload_id = models.OneToOneField("uploader.CofkCollectUpload", on_delete=models.DO_NOTHING)
    origin_id = models.AutoField(primary_key=True)
    location_id = models.IntegerField(null=False)
    # TODO
    # missing iwork_id
    # iwork_id = models.AutoField(primary_key=True)
    notes_on_origin = models.TextField()
    _id = models.CharField(max_length=32)

    # upload = relationship('CofkCollectWork')
    # upload1 = relationship('CofkCollectLocation')
    # upload2 = relationship('CofkCollectUpload')


class CofkCollectPersonMentionedInWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_person_mentioned_in_work'

    #__table_args__ = (
        # ForeignKeyConstraint(['upload_id', 'iperson_id'], ['cofk_collect_person.upload_id', 'cofk_collect_person.iperson_id']),
        # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id'])
    #)

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    # upload_id = models.ForeignKey("uploader.CofkCollectUpload", primary_key=True, null=False, on_delete=models.DO_NOTHING)
    upload_id = models.OneToOneField("uploader.CofkCollectUpload", null=False, on_delete=models.DO_NOTHING)
    # mention_id = models.AutoField(primary_key=True)
    iperson_id = models.IntegerField(null=False)
    # TODO
    # missing iwork_id
    # iwork_id = models.AutoField(primary_key=True)
    notes_on_person_mentioned = models.TextField()
    _id = models.CharField(max_length=32)

    # upload = relationship('CofkCollectPerson')
    # upload1 = relationship('CofkCollectWork')
    # upload2 = relationship('CofkCollectUpload')


class CofkCollectPlaceMentionedInWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_place_mentioned_in_work'

    #__table_args__ = (
        # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id',
        # 'cofk_collect_work.iwork_id']), ForeignKeyConstraint(['upload_id', 'location_id'],
        # ['cofk_collect_location.upload_id', 'cofk_collect_location.location_id'])
    #)

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False) upload_id =
    # models.ForeignKey("uploader.CofkCollectUpload", primary_key=True, null=False, on_delete=models.DO_NOTHING)
    upload_id = models.OneToOneField("uploader.CofkCollectUpload", null=False, on_delete=models.DO_NOTHING)
    # mention_id = models.AutoField(primary_key=True)
    location_id = models.IntegerField(null=False)
    # iwork_id = models.AutoField(primary_key=True)
    notes_on_place_mentioned = models.TextField()
    _id = models.CharField(max_length=32)

    # upload = relationship('CofkCollectWork')
    # upload1 = relationship('CofkCollectLocation')
    # upload2 = relationship('CofkCollectUpload')


class CofkCollectSubjectOfWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_subject_of_work'

    #__table_args__ = (
        # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id']),
    #)

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    # upload_id = models.ForeignKey("uploader.CofkCollectUpload", primary_key=True, null=False, on_delete=models.DO_NOTHING)
    upload_id = models.OneToOneField("uploader.CofkCollectUpload", null=False, on_delete=models.DO_NOTHING)
    subject_of_work_id = models.AutoField(primary_key=True)
    # iwork_id = models.AutoField(primary_key=True)
    # subject_id = Column(ForeignKey('cofk_union_subject.subject_id', ondelete='CASCADE'), null=False)
    subject_id = models.ForeignKey("uploader.CofkUnionSubject", on_delete=models.CASCADE, null=False)

    # subject = relationship('CofkUnionSubject')
    # upload = relationship('CofkCollectWork')
    # upload1 = relationship('CofkCollectUpload')


class CofkCollectWorkResource(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_work_resource'

    #__table_args__ = (
        # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id']),
    #)

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    upload_id = models.ForeignKey("uploader.CofkCollectUpload", null=False, on_delete=models.CASCADE)
    # upload_id = models.OneToOneField("uploader.CofkCollectUpload", null=False, on_delete=models.DO_NOTHING)
    # resource_id = models.AutoField(primary_key=True)
    # iwork_id = models.AutoField(primary_key=True)
    resource_name = models.TextField(null=False, default='')
    resource_details = models.TextField(null=False, default='')
    resource_url = models.TextField(null=False, default='')
    _id = models.CharField(max_length=32)

    # upload = relationship('CofkCollectWork')
    # upload1 = relationship('CofkCollectUpload')


class CofkUnionLanguageOfWork(models.Model):
    #class Meta:
    #    db_table = 'cofk_union_language_of_work'

    # TODO
    # Composite primary keys

    # work_id = Column(ForeignKey('cofk_union_work.work_id', ondelete='CASCADE'), primary_key=True, null=False)
    # work_id = models.ForeignKey("uploader.CofkUnionWork", on_delete=models.CASCADE, primary_key=True, null=False)
    work_id = models.OneToOneField("CofkUnionWork", on_delete=models.CASCADE, null=False)
    # language_code = Column(ForeignKey('iso_639_language_codes.code_639_3', ondelete='CASCADE'), primary_key=True, null=False)
    # missing 2x primary key
    language_code = models.ForeignKey("uploader.Iso639LanguageCode", on_delete=models.CASCADE, null=False)
    notes = models.CharField(max_length=100)

    # iso_639_language_code = relationship('Iso639LanguageCode')
    # work = relationship('CofkUnionWork')