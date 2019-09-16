from django.db import models

STATUS_CHOICES = (
    ('new', 'New'),
    ('in_progress', 'In the process'),
    ('done', 'Completed'),
)


class Plan(models.Model):
    title = models.CharField(max_length=200, verbose_name='Plan name')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    status = models.CharField(max_length=20, null=False, blank=False, verbose_name='Status', default=STATUS_CHOICES[0][0],
                              choices=STATUS_CHOICES)
    deadline = models.DateField(max_length=10, null=True, blank=True, default='', verbose_name='Deadline')

    def __str__(self):
        return self.title

# Create your models here.