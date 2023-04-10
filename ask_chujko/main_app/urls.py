from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),                                       #Главная
    path('main_app/<int:question_id>', views.question_view, name='main_app'),               #Страница одного вопроса
    path('ask', views.ask_view, name='ask'),                                        #Страница создания вопроса
    path('login', views.login_view, name='login'),                                  #Авторизация
    path('signup', views.signup_view, name='signup'),                               #Регистрация
    path('settings', views.settings_view, name='settings'),                         #Настройки
    path('hot', views.hot_view, name='hot'),                                        #Горячие вопросы
    path('tag/<tag_text>', views.tag_view, name='tag'),
    path('logout', views.logout, name='logout')

]