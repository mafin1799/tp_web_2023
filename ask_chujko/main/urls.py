from django.urls import path

from . import views

urlpatterns = [
    path('base', views.base_view, name='base'),
    path('', views.index_view, name='index'),                                       #Главная
    path('main/<int:question_id>', views.question_view, name='main'),               #Страница одного вопроса
    path('ask', views.ask_view, name='ask'),                                        #Страница создания вопроса
    path('login<path:next>', views.login_view, name='login'),                       #Авторизация
    path('signup', views.signup_view, name='signup'),                               #Регистрация
    path('settings', views.settings_view, name='settings'),                         #Настройки
    path('hot', views.hot_view, name='hot'),                                        #Горячие вопросы
    path('tag', views.tag_view, name='tag'),
    path('logout<path:next>', views.logout, name='logout')
    #Вопросы по тэгу
]