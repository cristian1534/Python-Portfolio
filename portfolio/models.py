from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    technology = models.CharField(max_length=200, default="")  # Added default empty string
    image = models.CharField(max_length=200)
    url = models.URLField(blank=True)

    @property
    def technologies(self):
        return [tech.strip() for tech in self.technology.split(',')]

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"