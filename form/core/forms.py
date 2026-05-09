from django import forms 
from core.models import Profile

GENDER_CHOICES = (
    ('M','Male'),
    ('F',"Female"),
    ('O',"Other")
)

JOB_CITY_CHOICE = [
    ("Dhaka","Dhaka"),
    ("Gajipur", "Gajipur"),
    ("Rajshahi","Rajshahi"),
    ("Khulna","Khulna"),
    ("Chitagong","Chitagong"),
    ("Tangail","Tangail"),
]

class profileForm(forms.ModelForm):
    
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, 
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    
    job_city = forms.MultipleChoiceField(
        choices=JOB_CITY_CHOICE,
        error_messages={"required": "This field is required, you cannot skip it."},
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        label="Preferred Job cities",
        help_text="Select one or more cities where you are perfect to work"
    )

    class Meta:
        model = Profile
        fields = [
            "name","dob","gender","locality","city","pin",
            "division","mobile","email","job_city","profile_image","my_file"
        ]

       
        labels = {
            "name": "Full Name",
            "dob": "Date of Birth",
            "pin" : "Pin Code",
            "mobile": "Mobile Number",
        }

        help_texts = {
            "profile_image" : "Optional: Upload a profile image",
            'my_file' : "Optional: Attach any additional document (PDF, DOCX, etc.)"
        }

        error_messages = {
            "profile_image": {
                "required": "Profile image is mandatory for the candidate",
            }
        }

        widgets = {
            "name" : forms.TextInput(attrs={"class" : "form-control"}),
            "dob" : forms.DateInput(attrs={"class" : "form-control", "type" :"date"}), 
            "locality": forms.TextInput(attrs={"class" : "form-control","placeholder": "Locality"}),
            "city" : forms.TextInput(attrs={"class":"form-control","placeholder":"City"}),
            "pin" : forms.NumberInput(attrs={"class":"form-control","placeholder" : "Enter 7 digit pin"}),
            "division": forms.Select(attrs={"class": "form-select"}),
            "mobile" : forms.TextInput(attrs={"class" : "form-control","placeholder": "Enter 11 digit mobile number"}),
            "email" : forms.EmailInput(attrs={"class":"form-control","placeholder" : "Enter your email address"}),
        }

   
    def save(self, commit=True):
        instance = super().save(commit=False)
        job_cities = self.cleaned_data.get("job_city")

        if job_cities:
            
            instance.job_city = ",".join(job_cities)

        if commit:
            instance.save()
        return instance