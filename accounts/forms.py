from django import forms
from accounts.models import UserProfile

class SignupForm(forms.ModelForm):
    """
    SignupForm Class
    """

    class Meta:
        model = UserProfile

        fields = (
            "first_name",
            "last_name",
            "phone_no",
        )
    
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.save()

        profile = UserProfile()
        profile.user = user
        profile.user = user 
        profile.phone_no = self.cleaned_data['phone_no']
        profile.save()