from django import forms
from allauth.account.forms import SignupForm
from home.models import User, Woman, Mentor


class CustomSignupForm(SignupForm):
    """
    Creating the user model instance based on the selected type
    """
    user_type = forms.ChoiceField(
        choices=User.Type.choices, widget=forms.Select)

    def save(self, request):
        user_type = self.cleaned_data.pop('user_type')
        if user_type == User.Type.WOMAN:
            user = Woman()
        else:
            user = Mentor()

        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user
