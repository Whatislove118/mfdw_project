from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = (
    ('NEW', 'New Site'),
    ('EX', 'Existing site'),
)

PRIORITY_CHOICES = (
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 to 4 weeks'),
    ('L', 'Low - Still Researching'),
)

class Quote(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=60, blank=True)
    company = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)
    web = models.URLField(blank=True)
    description = models.TextField()
    site_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES)
    job_file = models.FileField(upload_to='uploads/', blank=True)
    submitted = models.DateField(auto_now_add=True)
    quote_date = models.DateField(blank=True, null=True)
    quote_price = models.DecimalField(decimal_places=2,
                                      max_digits=7,
                                      blank=True,
                                      default=0)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



