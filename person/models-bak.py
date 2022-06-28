import uuid as uuid
from django.db import models

# Create your models here.


class CofkCollectPerson(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_person'

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    upload_id = models.ForeignKey("uploader.CofkCollectUpload", null=False, on_delete=models.CASCADE)
    # upload_id = models.OneToOneField("uploader.CofkCollectUpload", null=False, on_delete=models.DO_NOTHING)
    iperson_id = models.AutoField(primary_key=True)
    # union_iperson_id = Column(ForeignKey('cofk_union_person.iperson_id', ondelete='SET NULL'))
    # TODO
    # Union iperson id necessary?
    # union_iperson_id = models.ForeignKey(CofkUnionPerson.i)
    # person_id = Column(ForeignKey('cofk_union_person.person_id', ondelete='SET NULL'))
    person_id = models.OneToOneField("CofkUnionPerson", on_delete=models.DO_NOTHING, null=True)
    primary_name = models.CharField(max_length=200, null=False)
    alternative_names = models.TextField()
    roles_or_titles = models.TextField()
    # TODO
    # Enumerate type?
    gender = models.CharField(max_length=1, null=False, default='')
    # TODO
    # Boolean field
    is_organisation = models.CharField(max_length=1, null=False, default='')
    # TODO
    # Enumerate type?
    organisation_type = models.IntegerField(null=True)
    date_of_birth_year = models.IntegerField(null=True)
    date_of_birth_month = models.IntegerField(null=True)
    date_of_birth_day = models.IntegerField(null=True)
    # TODO
    # Boolean types below?
    date_of_birth_is_range = models.SmallIntegerField(null=True, default=0)
    date_of_birth2_year = models.IntegerField(null=True)
    date_of_birth2_month = models.IntegerField(null=True)
    date_of_birth2_day = models.IntegerField(null=True)
    date_of_birth_inferred = models.SmallIntegerField(null=True, default=0)
    date_of_birth_uncertain = models.SmallIntegerField(null=True, default=0)
    date_of_birth_approx = models.SmallIntegerField(null=True, default=0)
    date_of_death_year = models.IntegerField(null=True)
    date_of_death_month = models.IntegerField(null=True)
    date_of_death_day = models.IntegerField(null=True)
    date_of_death_is_range = models.SmallIntegerField(null=True, default=0)
    date_of_death2_year = models.IntegerField(null=True)
    date_of_death2_month = models.IntegerField(null=True)
    date_of_death2_day = models.IntegerField(null=True)
    date_of_death_inferred = models.SmallIntegerField(null=True, default=0)
    date_of_death_uncertain = models.SmallIntegerField(null=True, default=0)
    date_of_death_approx = models.SmallIntegerField(null=True, default=0)
    flourished_year = models.IntegerField(null=True)
    flourished_month = models.IntegerField(null=True)
    flourished_day = models.IntegerField(null=True)
    flourished_is_range = models.SmallIntegerField(null=True, default=0)
    flourished2_year = models.IntegerField(null=True)
    flourished2_month = models.IntegerField(null=True)
    flourished2_day = models.IntegerField(null=True)
    notes_on_person = models.TextField(null=True)
    editors_notes = models.TextField(null=True)
    # TODO
    # What does upload name refer to here?
    upload_name = models.CharField(max_length=254)
    _id = models.CharField(max_length=32)

    # person = relationship('CofkUnionPerson', primaryjoin='CofkCollectPerson.person_id == CofkUnionPerson.person_id')
    # union_iperson = relationship('CofkUnionPerson', primaryjoin='CofkCollectPerson.union_iperson_id == CofkUnionPerson.iperson_id')
    # upload = relationship('CofkCollectUpload')


class CofkUnionPerson(models.Model):
    #class Meta:
    #    db_table = 'cofk_union_person'

    # __table_args__ = (
    #    CheckConstraint('(date_of_birth_approx = 0) OR (date_of_birth_approx = 1)'),
    #    CheckConstraint('(date_of_birth_inferred = 0) OR (date_of_birth_inferred = 1)'),
    #    CheckConstraint('(date_of_birth_is_range = 0) OR (date_of_birth_is_range = 1)'),
    #    CheckConstraint('(date_of_birth_uncertain = 0) OR (date_of_birth_uncertain = 1)'),
    #    CheckConstraint('(date_of_death_approx = 0) OR (date_of_death_approx = 1)'),
    #    CheckConstraint('(date_of_death_inferred = 0) OR (date_of_death_inferred = 1)'),
    #    CheckConstraint('(date_of_death_is_range = 0) OR (date_of_death_is_range = 1)'),
    #    CheckConstraint('(date_of_death_uncertain = 0) OR (date_of_death_uncertain = 1)'),
    #    CheckConstraint('(flourished_is_range = 0) OR (flourished_is_range = 1)')
    # )

    # TODO
    # Switch above to boolean fields

    person_id = models.CharField(max_length=100, primary_key=True)
    foaf_name = models.CharField(max_length=200, null=False)
    skos_altlabel = models.TextField()
    skos_hiddenlabel = models.TextField()
    person_aliases = models.TextField()
    date_of_birth_year = models.IntegerField()
    date_of_birth_month = models.IntegerField()
    date_of_birth_day = models.IntegerField()
    date_of_birth = models.DateField()
    date_of_birth_inferred = models.SmallIntegerField(null=False, default=0)
    date_of_birth_uncertain = models.SmallIntegerField(null=False, default=0)
    date_of_birth_approx = models.SmallIntegerField(null=False, default=0)
    date_of_death_year = models.IntegerField()
    date_of_death_month = models.IntegerField()
    date_of_death_day = models.IntegerField()
    date_of_death = models.DateField()
    date_of_death_inferred = models.SmallIntegerField(null=False, default=0)
    date_of_death_uncertain = models.SmallIntegerField(null=False, default=0)
    date_of_death_approx = models.SmallIntegerField(null=False, default=0)
    # TODO
    # Enumerated value?
    gender = models.CharField(max_length=1, null=False, default='')
    # TODO
    # Boolean field
    is_organisation = models.CharField(max_length=1, null=False, default='')
    # iperson_id = models.IntegerField(null=False, unique=True, default=text("nextval('cofk_union_person_iperson_id_seq'::regclass)"))
    creation_timestamp = models.DateTimeField(auto_now=True)
    # creation_user = models.CharField(max_length=50, null=False, default=current_user)
    change_timestamp = models.DateTimeField(auto_now=True)
    # change_user = models.CharField(max_length=50, null=False, default=current_user)
    editors_notes = models.TextField()
    further_reading = models.TextField()
    # organisation_type = Column(ForeignKey('cofk_union_org_type.org_type_id'))
    organisation_type = models.ForeignKey("uploader.CofkUnionOrgType", on_delete=models.DO_NOTHING)
    date_of_birth_calendar = models.CharField(max_length=2, null=False, default='')
    date_of_birth_is_range = models.SmallIntegerField(null=False, default=0)
    date_of_birth2_year = models.IntegerField()
    date_of_birth2_month = models.IntegerField()
    date_of_birth2_day = models.IntegerField()
    date_of_death_calendar = models.CharField(max_length=2, null=False, default='')
    date_of_death_is_range = models.SmallIntegerField(null=False, default=0)
    date_of_death2_year = models.IntegerField()
    date_of_death2_month = models.IntegerField()
    date_of_death2_day = models.IntegerField()
    flourished = models.DateField()
    flourished_calendar = models.CharField(max_length=2, null=False, default='')
    flourished_is_range = models.SmallIntegerField(null=False, default=0)
    flourished_year = models.IntegerField()
    flourished_month = models.IntegerField()
    flourished_day = models.IntegerField()
    flourished2_year = models.IntegerField()
    flourished2_month = models.IntegerField()
    flourished2_day = models.IntegerField()
    uuid = models.UUIDField(default=uuid.uuid4)
    # TODO
    # Boolean fields below
    flourished_inferred = models.SmallIntegerField(null=False, default=0)
    flourished_uncertain = models.SmallIntegerField(null=False, default=0)
    flourished_approx = models.SmallIntegerField(null=False, default=0)

    # cofk_union_org_type = relationship('CofkUnionOrgType')


class CofkCollectOccupationOfPerson(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_occupation_of_person'

    # __table_args__ = (
    #    ForeignKeyConstraint(['upload_id', 'iperson_id'], ['cofk_collect_person.upload_id', 'cofk_collect_person.iperson_id']),
    # )

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    # upload_id = models.ForeignKey("uploader.CofkCollectUpload", primary_key=True, null=False, on_delete=models.DO_NOTHING)
    upload_id = models.OneToOneField("uploader.CofkCollectUpload", null=False, on_delete=models.DO_NOTHING)
    occupation_of_person_id = models.AutoField(primary_key=True)
    iperson_id = models.IntegerField(null=False)
    occupation_id = models.ForeignKey("uploader.CofkUnionRoleCategory", on_delete=models.CASCADE, null=False)
    # occupation_id = Column(ForeignKey('cofk_union_role_category.role_category_id', ondelete='CASCADE'), null=False)

    # occupation = relationship('CofkUnionRoleCategory')
    # upload = relationship('CofkCollectPerson')
    # upload1 = relationship('CofkCollectUpload')


class CofkCollectPersonResource(models.Model):
    #class Meta:
    #    db_table = 'cofk_collect_person_resource'

    # __table_args__ = (
    #    ForeignKeyConstraint(['upload_id', 'iperson_id'], ['cofk_collect_person.upload_id', 'cofk_collect_person.iperson_id']),
    # )

    # upload_id = Column(ForeignKey('cofk_collect_upload.upload_id'), primary_key=True, null=False)
    # upload_id = models.ForeignKey("uploader.CofkCollectUpload", primary_key=True, null=False, on_delete=models.DO_NOTHING)
    upload_id = models.OneToOneField("uploader.CofkCollectUpload", null=False, on_delete=models.DO_NOTHING)
    resource_id = models.AutoField(primary_key=True, null=False)
    iperson_id = models.IntegerField(null=False)
    resource_name = models.TextField(null=False, default='')
    resource_details = models.TextField(null=False, default='')
    resource_url = models.TextField(null=False, default='')

    # upload = relationship('CofkCollectPerson')
    # upload1 = relationship('CofkCollectUpload')