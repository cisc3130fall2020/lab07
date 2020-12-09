from django.db import models

# Create your models here.
class Lab(models.Model):
    number = models.IntegerField(
        primary_key=True,
    )
    description = models.TextField(
        help_text = "Brief description of the lab."
    )
    lab_url = models.CharField(
        max_length=200,
        help_text = "The url of the repository where I uploaded my solution."
    )

    def __str__(self):
        """
        Specify the String represtation of each Lab object. This is equivalent
        to the java as_string() funtion.
        """
        return "Lab {}".format(self.number)
