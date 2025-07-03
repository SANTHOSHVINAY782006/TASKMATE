from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('study', 'Study'),
        ('personal', 'Personal'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    deadline = models.DateField(null=True, blank=True)
    is_complete = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

