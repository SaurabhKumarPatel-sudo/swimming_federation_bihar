# sfb/models.py
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Record(models.Model):
    event = models.CharField(max_length=100)
    athlete = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    date = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.event} - {self.athlete}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# NEW: Profile model to extend the built-in User model
class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('athlete', 'Athlete'),
        ('coach', 'Coach'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    # Link to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    # Personal Information
    middle_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField(verbose_name="Date of Birth")
    mobile_number = models.CharField(max_length=15)
    
    # Parent Information
    father_name = models.CharField(max_length=200, blank=True)
    mother_name = models.CharField(max_length=200, blank=True)
    
    # Address Information
    address = models.TextField()
    
    # Home Association
    home_association = models.CharField(max_length=200, blank=True)

    # File Uploads
    photograph = models.ImageField(upload_to='documents/photos/')
    id_proof = models.FileField(upload_to='documents/id_proofs/')
    dob_proof = models.FileField(upload_to='documents/dob_proofs/')
    address_proof = models.FileField(upload_to='documents/address_proofs/')
    
    # Coach-specific field
    coaching_certificate = models.FileField(upload_to='documents/coaching_certs/', blank=True, null=True, help_text="Required for coaches only.")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

