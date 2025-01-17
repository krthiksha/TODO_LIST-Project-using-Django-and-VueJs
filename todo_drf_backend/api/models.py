from django.db import models
import uuid
# Create your models here.
#model for to-do app


#  Category table
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescripition = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.categoryName
    

# task table
class Task(models.Model):
    
    PRIORITY_CHOICES = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_process', 'In Process'),
        ('completed', 'Completed'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(default='', blank=True, null=True)    
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default='medium',blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', blank=True,null=True)
     
    
    # models.CASCADE -> used to del all tasks when its category is deleted

    
    def __str__(self):
        return self.name
    
    
    
    
    
