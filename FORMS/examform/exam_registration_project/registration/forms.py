from django import forms

class ExmRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100 , label= "name")
    email = forms.CharField(max_length=100 , label= "email")
    father_name = forms.CharField(max_length=100 , label="Father_NAME")
    mother_name = forms.CharField(max_length=100 , label="mother name")
    date_of_birth = forms.DateField(label="Date of Birth")
    gender=forms.ChoiceField(label="Gender")
    address = forms.CharField(max_length = 100 ,label="Address")
    city = forms.CharField(max_length = 100 , label="city")
    state = forms.CharField(max_length = 100 , label="state")
    country = forms.CharField(max_length = 100 , label="country")
    phone_number = forms.IntegerField(  label="Phone Number")
    qualification = forms.CharField(label="Qualification")
    photo = forms.ImageField(label="photo")
    signature = forms.CharField(label="Signature")
    declaration = forms.BooleanField(label="I agree to term & conditions")