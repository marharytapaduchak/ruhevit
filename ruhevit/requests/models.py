from django.db import models
from django.conf import settings


class Request(models.Model):
    TYPE_CHOICES = [
        ('medicine', 'Медицина'),
        ('ammo', 'Амуніція'),
        ('drones', 'Дрони'),
        ('transport', 'Транспорт'),
        ('repair', 'Ремонт'),
    ]

    PRIORITY_CHOICES = [
        ('high', 'Високий'),
        ('medium', 'Середній'),
        ('low', 'Низький'),
    ]

    LOCATION_CHOICES = [
        ('front', 'Фронт'),
        ('near_rear', 'Близький тил'),
        ('far_rear', 'Далекий тил'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Очікує'),
        ('in_progress', 'Виконується'),
        ('done', 'Виконано'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='requests_made'
    )
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='requests_taken'
    )

    name = models.CharField(max_length=255)
    description = models.TextField()

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    location = models.CharField(max_length=15, choices=LOCATION_CHOICES)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RequestHistory(models.Model):
    request = models.ForeignKey(
        Request, on_delete=models.CASCADE, related_name='history')
    status = models.CharField(max_length=20, choices=Request.STATUS_CHOICES)
    comment = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to='report_photos/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.request.name} – {self.status}'


class Review(models.Model):
    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1–5
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.executor.username} – {self.rating}⭐'
