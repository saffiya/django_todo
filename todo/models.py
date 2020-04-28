from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    # Return the name of the object or instance of that object instead of the type
    # Which will give us a more readable freindly representation when reviewed in the admin panel.
    def __str__(self):
        return self.name
        