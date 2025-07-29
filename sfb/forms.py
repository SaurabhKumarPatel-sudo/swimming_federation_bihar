from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    email2 = forms.EmailField(label="Re-enter Email")
    mobile_number2 = forms.CharField(label="Re-enter Mobile Number")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        email2 = cleaned_data.get("email2")
        mobile2 = cleaned_data.get("mobile_number2")
        # mobile_number is in ProfileForm, so only check mobile2 here

        if email and email2 and email != email2:
            raise forms.ValidationError("Emails do not match.")
        # mobile_number2 will be checked in ProfileForm
        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'middle_name', 'gender', 'dob', 'mobile_number', 'father_name', 
            'mother_name', 'address', 'home_association', 'photograph', 
            'id_proof', 'dob_proof', 'address_proof'
        )
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        mobile1 = cleaned_data.get('mobile_number')
        mobile2 = self.data.get('mobile_number2')
        if mobile1 and mobile2 and mobile1 != mobile2:
            raise forms.ValidationError("Mobile numbers do not match.")
        return cleaned_data

class CoachProfileForm(ProfileForm):
    class Meta(ProfileForm.Meta):
        fields = ProfileForm.Meta.fields + ('coaching_certificate',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coaching_certificate'].required = True 