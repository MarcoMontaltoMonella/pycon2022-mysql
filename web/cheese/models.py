from django.db import models


class Cheese(models.Model):
    name = models.CharField(max_length=100)
    CHEESE_SIZES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    )
    size = models.CharField(max_length=1, choices=CHEESE_SIZES, default="M")
    stored_since = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "cheeses"

    def __str__(self):
        return f"{self.name} ({self.size})"

    def get_absolute_url(self):
        return reverse("Cheese_detail", kwargs={"pk": self.pk})
