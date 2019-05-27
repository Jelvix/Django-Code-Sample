from .models import User
from .serializers import UserSerializer, GetUserSerializer
from .forms import RegisterForm
from django.views.generic import CreateView
from rest_framework import viewsets


class RegisterUserView(CreateView):
    """
    Class for user registration view
    """
    form_class = RegisterForm
    template_name = "registration/user_form.html"
    success_url = "/login/"
    active_url = 'registration'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to create(register) new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GetUserSerializer
        return self.serializer_class

