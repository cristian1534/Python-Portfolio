from django.db import models
from bson import ObjectId


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    technology = models.CharField(max_length=200, default="")
    image = models.CharField(max_length=200)
    url = models.URLField(blank=True)

    @property
    def technologies(self):
        return [tech.strip() for tech in self.technology.split(',')]

    def __str__(self):
        return self.title


class Contact(models.Model):
    _id = models.CharField(max_length=24, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self._id:
            self._id = str(ObjectId())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']
        db_table = 'portfolio_contact'
        managed = False
