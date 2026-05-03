from django.shortcuts import render
from django.views import View
from datetime import datetime


def home(request):
    context = {
        'title': 'Головна',
        'welcome_message': 'Ласкаво просимо на наш сайт!',
    }
    return render(request, 'main/home.html', context)


def about(request):
    company_info = "Наша компанія була заснована у 2000 році і займається розробкою веб-рішень."
    last_updated = datetime.now()
    context = {
        'title': 'Про нас',
        'company_info': company_info,
        'last_updated': last_updated,
    }
    return render(request, 'main/about.html', context)


class ContactView(View):
    def get(self, request):
        context = {
            'title': 'Контакти',
            'address': 'вул. Прикладна 10, Київ, Україна',
            'phone': '+380 44 123 45 67',
            'email': 'info@example.com',
        }
        return render(request, 'main/contact.html', context)


class ServiceView(View):
    def get(self, request):
        services = [
            {'name': 'Веб-розробка', 'description': 'Створення сучасних веб-сайтів та додатків.'},
            {'name': 'SEO оптимізація', 'description': 'Підвищення видимості вашого сайту в пошукових системах.'},
            {'name': 'Маркетинг', 'description': 'Розробка маркетингових стратегій для бізнесу.'},
            {'name': 'Консалтинг', 'description': 'Професійні консультації для вашого бізнесу.'},
        ]
        last_updated = datetime.now()
        context = {
            'title': 'Послуги',
            'services': services,
            'last_updated': last_updated,
        }
        return render(request, 'main/services.html', context)