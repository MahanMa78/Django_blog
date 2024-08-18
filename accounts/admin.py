from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm , CustomUserCreationForm
from .models import CustomUser
from blog.models import Post

class PostInLine(admin.StackedInline):
    model = Post
    fields = ['id' , 'title' , 'excerpt' , 'body', 'active' , 'photo']
    extra = 0

class CustomUserAdmin(UserAdmin):
    add_from = CustomUserCreationForm #formi ke bahash mikhahim yek user besazim dakhel panel asdmin
    form = CustomUserChangeForm #formii ke baraye taghir karbar dar dakhel panel admin azash estefade mikonim
    model = CustomUser #mige in ke neveshtim modelsh az in model ma miad
    list_display = ['id', 'email' , 'username' , 'age' , 'is_staff','about']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('age' , 'about' , 'photo')}),) #dar inja dar dakhel panel admin zamani ke darim yek user misazim ya update mikonim  field haye 'about' va 'photo' ham ezafe mishan
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('age' , 'about' , 'photo' )}),)
    inlines = [PostInLine]

admin.site.register(CustomUser , CustomUserAdmin)