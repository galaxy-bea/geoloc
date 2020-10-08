from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models as gis_model



class BaseModel(models.Model):
    """Base model for each models with common fields."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Abstract true."""

        abstract = True
class Category(BaseModel):
    category = models.CharField(max_length=255)
    def __str__(self):
     return format(self.category)

class SubCategory(BaseModel):
  sub_category = models.CharField(max_length=255)
  category = models.ForeignKey(Category, on_delete = models.CASCADE)
  def __str__(self):
     return format(self.sub_category)


class Marker(BaseModel):
    """Marker model to manage map markers."""

    email = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(default="")
    is_active = models.BooleanField(default=False)

    location_name = models.CharField(max_length=255, blank=True, null=True)
    location = gis_model.PointField(srid=4326, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default='', null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE, default='', null=True, blank=True)
    def wrap_location(self):
        """Save location."""

        print("coordinates:",self.longitude, self.latitude)
        self.location = Point(self.longitude, self.latitude)