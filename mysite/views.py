from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name = "index.html"


class UserCreationView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreationDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class GameTips_Elemental_Battleground_View(TemplateView):
    template_name = "Game_Tips/Elemental_Battleground.html"

class GameTips_Factory_Town_Tycoon_View(TemplateView):
    template_name = "Game_Tips/Factory_Town_Tycoon.html"

class GameTips_Resource_Factory_Tycoon_View(TemplateView):
    template_name = "Game_Tips/Resource_Factory_Tycoon.html"

class GameTips_Restaurant_Tycoon_2_View(TemplateView):
    template_name = "Game_Tips/Restaurant_Tycoon_2.html"

class GameTips_Critical_Strike_View(TemplateView):
    template_name = "Game_Tips/Critical_Strike.html"

class Lua_Coding_On_Roblox_View(TemplateView):
    template_name = "Lua_Coding_On_Roblox.html"
