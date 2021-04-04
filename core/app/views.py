from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm
from .models import User


class Index(TemplateView):
    """
    Главная страница, отображает текущего пользователя и его сохраненную дополнительную информацию
    """
    template_name = 'index.html'


class UserUpdate(LoginRequiredMixin, UpdateView):
    """
    Контроллер изменения имени и дополнительных данных пользователя
    """
    template_name="user_create_update.html"
    model=User
    form_class=UserUpdateForm
    success_url=reverse_lazy("app:index")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить данные пользователя"
        return context
