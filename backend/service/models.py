from django.db import models


class Service(models.Model):
    """
    Service Object that stores data about a service
    offered by iNethi
    """
    TYPE_ENTERTAINMENT = 'entertainment'
    TYPE_LEARNING = 'learning'
    TYPE_UTILITY = 'utility'
    TYPE_EDUCATION = 'education'

    TYPE_CHOICES = [
        (TYPE_ENTERTAINMENT, 'Entertainment'),
        (TYPE_LEARNING, 'Learning'),
        (TYPE_UTILITY, 'Utility'),
        (TYPE_EDUCATION, 'Education'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(unique=True)
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default=TYPE_UTILITY,
    )
    paid = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
