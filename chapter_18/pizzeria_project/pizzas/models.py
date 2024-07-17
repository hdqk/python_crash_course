from django.db import models


class Pizza(models.Model):
    """A pizza."""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Topping(models.Model):
    """A class to hold toppings for the pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Return a simple string representing the toppings."""
        if len(self.name) > 50:
            return f"{self.name[:50]}..."
        else:
            return f"{self.name}"
