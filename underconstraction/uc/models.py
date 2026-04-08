from django.db import models

# Create your models here.
class UnderConstraction(models.Model):
    is_underconstraction = models.BooleanField(default=False)
    uc_note = models.TextField(max_length=255)
    uc_duration = models.DateTimeField(blank=True,null=True,help_text="Enter the duration time")
    uc_update = models.DateTimeField( auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"Under consstraction {self.is_underconstraction}"