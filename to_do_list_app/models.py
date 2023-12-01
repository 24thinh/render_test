from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Work(models.Model):
    """A work that user working on."""
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    due_date = models.DateField('due_date')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def remaining_days(self):
        remaining = (self.due_date - date.today()).days
        return remaining

    def __str__(self):
        """Return a string representation of a model."""
        return self.text

class Description(models.Model):
    """A description for each work."""
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    describe = models.TextField()
    resource = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.describe

class Entry(models.Model):
    """Entries that show the progress of the work."""
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text