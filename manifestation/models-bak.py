import uuid as uuid
from django.db import models

# Create your models here.


class CofkUnionManifestation(models.Model):
    #class Meta:
    #    db_table = 'cofk_union_manifestation'

    # __table_args__ = (
    #    CheckConstraint('(manifestation_creation_date_approx = 0) OR (manifestation_creation_date_approx = 1)'),
    #    CheckConstraint('(manifestation_creation_date_inferred = 0) OR (manifestation_creation_date_inferred = 1)'),
    #    CheckConstraint('(manifestation_creation_date_uncertain = 0) OR (manifestation_creation_date_uncertain = 1)')
    # )

    # TODO
    # Above fields should be boolean fields

    manifestation_id = models.CharField(max_length=100, primary_key=True)
    manifestation_type = models.CharField(max_length=3, null=False, default='')
    id_number_or_shelfmark = models.CharField(max_length=500)
    printed_edition_details = models.TextField()
    paper_size = models.CharField(max_length=500)
    paper_type_or_watermark = models.CharField(max_length=500)
    number_of_pages_of_document = models.IntegerField()
    number_of_pages_of_text = models.IntegerField()
    seal = models.CharField(max_length=500)
    postage_marks = models.CharField(max_length=500)
    endorsements = models.TextField()
    non_letter_enclosures = models.TextField()
    manifestation_creation_calendar = models.CharField(max_length=2, null=False, default='U')
    manifestation_creation_date = models.DateField()
    manifestation_creation_date_gregorian = models.DateField()
    manifestation_creation_date_year = models.IntegerField()
    manifestation_creation_date_month = models.IntegerField()
    manifestation_creation_date_day = models.IntegerField()
    manifestation_creation_date_inferred = models.SmallIntegerField(null=False, default=0)
    manifestation_creation_date_uncertain = models.SmallIntegerField(null=False, default=0)
    manifestation_creation_date_approx = models.SmallIntegerField(null=False, default=0)
    manifestation_is_translation = models.SmallIntegerField(null=False, default=0)
    language_of_manifestation = models.CharField(max_length=255)
    address = models.TextField()
    manifestation_incipit = models.TextField()
    manifestation_excipit = models.TextField()
    manifestation_ps = models.TextField()
    creation_timestamp = models.DateTimeField(auto_now=True)
    # TODO
    # All user references in tables seem to refer to database user and NOT
    # system users. This has to be fixed
    # creation_user = models.CharField(max_length=50, null=False, default=current_user)
    change_timestamp = models.DateTimeField(auto_now=True)
    # change_user = models.CharField(max_length=50, null=False, default=current_user)
    manifestation_creation_date2_year = models.IntegerField()
    manifestation_creation_date2_month = models.IntegerField()
    manifestation_creation_date2_day = models.IntegerField()
    manifestation_creation_date_is_range = models.SmallIntegerField(null=False, default=0)
    manifestation_creation_date_as_marked = models.CharField(max_length=250)
    # Enumerated values?
    # TODO
    opened = models.CharField(max_length=3, null=False, default='o')
    uuid = models.UUIDField(default=uuid.uuid4)
    routing_mark_stamp = models.TextField()
    routing_mark_ms = models.TextField()
    handling_instructions = models.TextField()
    stored_folded = models.CharField(max_length=20)
    postage_costs_as_marked = models.CharField(max_length=500)
    postage_costs = models.CharField(max_length=500)
    non_delivery_reason = models.CharField(max_length=500)
    date_of_receipt_as_marked = models.CharField(max_length=500)
    # Enumerated values?
    # TODO
    manifestation_receipt_calendar = models.CharField(max_length=2, null=False, default='U')
    manifestation_receipt_date = models.DateField()
    manifestation_receipt_date_gregorian = models.DateField()
    manifestation_receipt_date_year = models.IntegerField()
    manifestation_receipt_date_month = models.IntegerField()
    manifestation_receipt_date_day = models.IntegerField()
    manifestation_receipt_date_inferred = models.SmallIntegerField(null=False, default=0)
    manifestation_receipt_date_uncertain = models.SmallIntegerField(null=False, default=0)
    manifestation_receipt_date_approx = models.SmallIntegerField(null=False, default=0)
    manifestation_receipt_date2_year = models.IntegerField()
    manifestation_receipt_date2_month = models.IntegerField()
    manifestation_receipt_date2_day = models.IntegerField()
    manifestation_receipt_date_is_range = models.SmallIntegerField(null=False, default=0)
    accompaniments = models.TextField()


class CofkCollectManifestation(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_manifestation'

    #__table_args__ = (
        # ForeignKeyConstraint(['upload_id', 'iwork_id'], ['cofk_collect_work.upload_id', 'cofk_collect_work.iwork_id']),
        # ForeignKeyConstraint(['upload_id', 'repository_id'], ['cofk_collect_institution.upload_id', 'cofk_collect_institution.institution_id'])
    #)

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    upload_id = models.ForeignKey("uploader.CofkCollectUpload", null=False, on_delete=models.CASCADE)
    # upload_id = models.OneToOneField("uploader.CofkCollectUpload", on_delete=models.DO_NOTHING)
    manifestation_id = models.AutoField(primary_key=True)
    # TODO
    # missing iwork_id
    # iwork_id = models.AutoField(primary_key=True)
    # union_manifestation_id = Column(ForeignKey('cofk_union_manifestation.manifestation_id', ondelete='SET NULL'))
    # union_manifestation_id = models.ForeignKey("uploader.CofkUnionManifestation", on_delete=models.SET_NULL)
    union_manifestation_id = models.OneToOneField("CofkUnionManifestation", null=True, on_delete=models.CASCADE)
    # TODO
    # Enumerate field?
    manifestation_type = models.CharField(max_length=3, null=False, default='')
    repository_id = models.IntegerField()
    id_number_or_shelfmark = models.CharField(max_length=500)
    printed_edition_details = models.TextField()
    manifestation_notes = models.TextField()
    # TODO
    # Appropriate free text fields below?
    image_filenames = models.TextField()
    upload_name = models.CharField(max_length=254)
    _id = models.CharField(max_length=32)

    # union_manifestation = relationship('CofkUnionManifestation')
    # upload = relationship('CofkCollectWork')
    # upload1 = relationship('CofkCollectInstitution')
    # upload2 = relationship('CofkCollectUpload')


# TODO
# Composite primary keys

class CofkUnionLanguageOfManifestation(models.Model):
    #class Meta:
    #    db_table = 'cofk_union_language_of_manifestation'

    # manifestation_id = Column(ForeignKey('cofk_union_manifestation.manifestation_id', ondelete='CASCADE'), primary_key=True, null=False)
    # manifestation_id = models.ForeignKey("uploader.CofkUnionManifestation", on_delete=models.CASCADE, primary_key=True)
    manifestation_id = models.OneToOneField("CofkUnionManifestation", on_delete=models.CASCADE)
    # language_code = Column(ForeignKey('iso_639_language_codes.code_639_3', ondelete='CASCADE'), primary_key=True, null=False)
    # both primary keys?
    language_code = models.ForeignKey("uploader.Iso639LanguageCode", on_delete=models.CASCADE, null=False)
    notes = models.CharField(max_length=100)

    # iso_639_language_code = relationship('Iso639LanguageCode')
    # manifestation = relationship('CofkUnionManifestation')
