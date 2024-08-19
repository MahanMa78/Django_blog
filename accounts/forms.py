from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import CustomUser
#az in be bad ,az in model ya bar hasb in model kar ro jolo mibarim

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email' ,'birth_date',)
        widgets = {
            'birth_date': DatePickerInput(),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        widgets = {
            'birth_date': DatePickerInput(),
        }