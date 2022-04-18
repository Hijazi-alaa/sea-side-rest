from django.views import generic
from .models import MenuItems


class MenuList(generic.ListView):
    """
    View class defines the view of the menu model
    """
    model = MenuItems

    def get_context_data(self, **kwargs):
        context = super(MenuList, self).get_context_data(**kwargs)
        context['starters'] = MenuItems.objects.filter(category='Starters')
        context['mains'] = MenuItems.objects.filter(category='Main Courses')
        context['sides'] = MenuItems.objects.filter(category='Side Orders')
        context['deserts'] = MenuItems.objects.filter(category='Desserts')
        return context

    template_name = 'menu.html'
