from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from . import models


def base_view(request):
    return render(request, 'base.html', {
        'user': request.user,
    })


def index_view(request):
    questions_list = []
    for i in range(1, 30):
        questions_list.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    item = {
        'tags': ['snakes', 'milk', "furry", "love", "milking", "scalie", "milk",
                 "furry", "love", "milking", "scalie", "milk", "furry", "love", "milking", "scalie"]
    }
    questions = paginate(questions_list, request)
    return render(request, 'index.html', {
        'objects': questions,
        'item' : item
    })


def hot_view(request):
    questions_list = []
    for i in range(1, 30):
        questions_list.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    questions = paginate(questions_list, request)
    return render(request, 'hot.html', {
        'objects': questions
    })


def question_view(request, question_id):
    question = [{
        'title': 'Заголовок вопроса' + str(4),
        'id': question_id,
        'text': 'Подробнейшее описание волнующей темы' + str(4)
    }]
    answer_list = []
    for i in range(1, 10):
        answer_list.append({
            'title': 'ANSWER' + str(i),
            'id': i,
            'text': 'answer text' + str(i)
        })
    answers = paginate(answer_list, request)
    return render(request, 'question.html', {
        'question': question,
        'objects': answers,

    })


def tag_view(request, tag_text):
    questions_list = []
    for i in range(1, 6):
        questions_list.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    questions = paginate(questions_list, request)
    return render(request, 'tag.html', {
        'objects': questions,
        'tag' : tag_text
    })


def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')


def settings_view(request):
    return render(request, 'settings.html')


def ask_view(request):
    return render(request, 'ask.html')


def logout(request):
    return render(request, 'login.html')


def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)
    return objects_page
