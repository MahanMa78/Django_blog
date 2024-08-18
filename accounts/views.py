from django.urls import reverse_lazy
from django.views.generic import CreateView , TemplateView , View ,UpdateView
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm #migim baraye sakhtan form az in estefade bokon
    success_url = reverse_lazy('login') #mige baad az inke signup anjam shod loja bere?bere be safhe login
    template_name = 'registration/signup.html'

class ProfileView(TemplateView):
    model = CustomUser
    template_name = 'profile.html'


class ProfileUpdateView(UpdateView):
    model = CustomUser
    fields = ['first_name' , 'last_name' , 'email' , 'photo' ,'age' , 'about' , 'description']
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
