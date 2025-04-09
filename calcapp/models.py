from django.db import models

# Create your models here.

class Item(models.Model):
    number1 = models.FloatField()  # Stores the first number
    number2 = models.FloatField()  # Stores the second number
    operator = models.CharField(max_length=10)  # Stores the operator (+, -, *, /)
    output = models.FloatField(null=True, blank=True)  # Stores the result, can be empty initially

    def __str__(self):
        return f"{self.number1} {self.operator} {self.number2} = {self.output}"
