import uuid
from django.db import models

# KTODO Researchers' notes for front-end display
# KTODO Related resources

class CofkCollectLocation(models.Model):
    upload = models.ForeignKey("uploader.CofkCollectUpload", null=True, on_delete=models.CASCADE)
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=500, null=False, default='')
    element_1_eg_room = models.CharField(max_length=100, null=False, default='')
    element_2_eg_building = models.CharField(max_length=100, null=False, default='')
    element_3_eg_parish = models.CharField(max_length=100, null=False, default='')
    element_4_eg_city = models.CharField(max_length=100, null=False, default='')
    element_5_eg_county = models.CharField(max_length=100, null=False, default='')
    element_6_eg_country = models.CharField(max_length=100, null=False, default='')
    element_7_eg_empire = models.CharField(max_length=100, null=False, default='')
    notes_on_place = models.TextField()
    editors_notes = models.TextField()
    upload_name = models.CharField(max_length=254)
    _id = models.CharField(max_length=32)  # KTODO what is this _id, should be remove??
    location_synonyms = models.TextField()
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)


class CofkUnionLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=500, null=False, default='')
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    creation_timestamp = models.DateTimeField(auto_now=True)
    change_timestamp = models.DateTimeField(auto_now=True)
    location_synonyms = models.TextField()
    editors_notes = models.TextField()
    element_1_eg_room = models.CharField(max_length=100, null=False, default='')
    element_2_eg_building = models.CharField(max_length=100, null=False, default='')
    element_3_eg_parish = models.CharField(max_length=100, null=False, default='')
    element_4_eg_city = models.CharField(max_length=100, null=False, default='')
    element_5_eg_county = models.CharField(max_length=100, null=False, default='')
    element_6_eg_country = models.CharField(max_length=100, null=False, default='')
    element_7_eg_empire = models.CharField(max_length=100, null=False, default='')
    uuid = models.UUIDField(default=uuid.uuid4)


class CofkCollectLocationResource(models.Model):
    upload_id = models.OneToOneField("uploader.CofkCollectUpload", null=False, on_delete=models.DO_NOTHING)
    resource_id = models.AutoField(primary_key=True)
    location_id = models.IntegerField(null=False)
    resource_name = models.TextField(null=False, default='')
    resource_details = models.TextField(null=False, default='')
    resource_url = models.TextField(null=False, default='')
