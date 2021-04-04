from django.urls import path
from allauth.account.views import LoginView, LogoutView, SignupView
from .views import Index, UserUpdate
from .forms import UserCreateForm

app_name = 'app'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", SignupView.as_view(template_name="user_create_update.html", form_class=UserCreateForm), name="register"),
    path("user_update/<int:pk>/", UserUpdate.as_view(), name="user_update"),
]