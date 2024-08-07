from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm , CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_from = CustomUserCreationForm #formi ke bahash mikhahim yek user besazim dakhel panel asdmin
    form = CustomUserChangeForm #formii ke baraye taghir karbar dar dakhel panel admin azash estefade mikonim
    model = CustomUser #mige in ke neveshtim modelsh az in model ma miad
    list_display = ['id', 'email' , 'username' , 'age' , 'is_staff']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('age' , )}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('age' , )}),)

admin.site.register(CustomUser , CustomUserAdmin)