"""Forms for use cases modelations"""
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    """Form for user creation use case"""
    class Meta:
        """CreateUserForm metadata"""
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
