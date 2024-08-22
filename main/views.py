from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DiAlTi - Главная'
        context['content'] = 'Супермаркет DiAlTi'
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DiAlTi - О нас'
        context['content'] = 'О нас'
        context['text_on_page'] = (
            "<p>Добро пожаловать на наш сайт — место, где вы найдёте всё необходимое для комфортной и активной жизни! "
            "Мы предлагаем широкий ассортимент товаров, которые сделают ваш дом уютнее, улицу ярче, а путешествия и спорт — ещё увлекательнее.</p>"
            "<p>У нас вы найдёте:</p>"
            "<ul>"
            "<li><strong>Товары для дома:</strong> Удобные и стильные решения для обустройства вашего жилища.</li>"
            "<li><strong>Товары для улицы:</strong> Всё, что нужно для активного отдыха и незабываемого времяпрепровождения на свежем воздухе.</li>"
            "<li><strong>Детские товары:</strong> Надёжные и безопасные вещи для ваших малышей.</li>"
            "<li><strong>Спорт:</strong> Экипировка и аксессуары для спорта, чтобы поддерживать форму и достигать новых вершин.</li>"
            "<li><strong>Путешествия:</strong> Необходимые вещи для комфортных и ярких путешествий.</li>"
            "<li><strong>Гарнитура:</strong> Современные и качественные наушники и гарнитуры для работы и развлечений.</li>"
            "<li><strong>Канцелярия:</strong> Всё для работы и творчества — от ручек до органайзеров.</li>"
            "</ul>"
            "<p>Мы стремимся предлагать только лучшие товары, которые будут радовать вас каждый день. Спасибо, что выбрали нас!</p>"
        )
        return context


