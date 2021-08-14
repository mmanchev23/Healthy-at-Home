import uuid
from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class Customer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_picture = models.ImageField(null=True, blank=True, default='default_profile_picture.png')
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    mobile_number = models.CharField(max_length=100, null=True, blank=True)
    website_link = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    pass

    def __str__(self):
        return self.username


class Workout(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    workout_image = models.ImageField(null=True, blank=True, default='default_workout_image.png')
    video_url = models.CharField(max_length=200, default='https://www.youtube.com/embed/oAPCPjnU1wA')
    description = models.TextField()
    exercises = models.TextField()
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.title}"

    @property
    def imageURL(self):

        try:
            url = self.image.url
        except:
            url = ''

        return url

    def save(self, *args, **kwargs):
        url = self.video_url
        url = url.replace("watch?v=", "embed/")
        self.video_url = url
        super().save(*args,**kwargs)


class Task(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.title}"


class BMICalculator(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    height = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    weight = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    result = models.DecimalField(max_digits=10, decimal_places=2, editable=False, validators=[MinValueValidator(Decimal('0.00'))])
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.customer}"

    def save(self,*args,**kwargs):
        self.result = self.weight / (self.height / 100) ** 2
        super().save(*args,**kwargs)


class Food(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    calories = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    fat = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    protein = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    carbs = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    date_eaten = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.name}"