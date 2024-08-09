from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser
#az in be bad ,az in model ya bar hasb in model kar ro jolo mibarim

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email' ,'age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields