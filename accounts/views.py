from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm #migim baraye sakhtan form az in estefade bokon
    success_url = reverse_lazy('login') #mige baad az inke signup anjam shod loja bere?bere be safhe login
    template_name = 'registration/signup.html'