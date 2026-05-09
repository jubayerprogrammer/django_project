from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.

def validate_pin_length(value):
    try:
      if str(len(value)) <6 :
         raise ValidationError("The pin must be grather than 6 charcter")
      
    except:
        pass

DIVISION_CHOICE = (
    ("Dhaka", "Dhaka"),
    ("Chattogram", "Chattogram"),
    ("Rajshahi", "Rajshahi"),
    ("Khulna", "Khulna"),
    ("Barisal", "Barisal"),
    ("Sylhet", "Sylhet"),
    ("Rangpur", "Rangpur"),
    ("Mymensingh", "Mymensingh"),
)

class Profile(models.Model):
   name= models.CharField(max_length=244)
   dob = models.DateField(auto_now=False,auto_now_add=False)
   gender = models.CharField(max_length=1)
   locality = models.CharField(max_length=255)
   city = models.CharField(max_length=255)
   pin = models.PositiveBigIntegerField(validators=[validate_pin_length],help_text="The pin length mimimum 7 charecter")

   division = models.CharField(choices=DIVISION_CHOICE,max_length=60)

   mobile = models.CharField(max_length=11,
                             validators=[

                                RegexValidator(regex=r'^\d{11}$',message="Enter a valid 11 digit number")
                             ],
                             help_text="Enter a 11 digit mobile_number ",
                             
                             
                             )
   email = models.EmailField(max_length=89)
   job_city = models.CharField(max_length=78)
   profile_image = models.ImageField(upload_to="profile_image",blank=True)
   
   my_file = models.FileField(upload_to = "doc",blank= True)

