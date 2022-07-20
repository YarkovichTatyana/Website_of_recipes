from .models import *

menu=[
    {'title': 'Войти', 'url_name': 'login'}
]
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats=User.objects.all()
        context['menu']= menu
        context ['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected']=0
        return context