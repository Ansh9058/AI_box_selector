from django.db import models
class Box(models.Model):
    name=models.CharField(max_length=255)
    inner_length=models.FloatField()
    inner_width=models.FloatField()
    inner_height=models.FloatField()
    max_weight=models.FloatField()
    cost=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.name
