from .forms import addTasks
from main.models import Media_models, Comments
from django.shortcuts import render, redirect

b = ('back',)
EDIT = []
count = 0


def get_mod(data):
    data = data['editGroup']
    try:
        print(Media_models.objects.filter(id=data))
        return Media_models.objects.filter(id=data)
    except Exception:
        return False

def value():
    return get_mod(EDIT[0])

def filter_mod_to_group(data):
    try:
        # print('test', Media_models.objects.filter(name='admin'))
        return Media_models.objects.filter(id=data)
    except Exception:
        return False

def delete(data: dict):
    global EDIT
    if 'hideGroup' in data:
        slug = data['hideGroup']
        # print('slug==',slug)
        value = filter_mod_to_group(slug)
        # print('testValue',value)
        value.update(geeks_field = False)
    elif 'editGroup' in data:
        slug = data['editGroup']
        value = filter_mod_to_group(slug)
        value.delete()

def get_mod_to_tasks(data):
    data = data
    try:
        # print(Comments.objects.filter(id=data))
        return Comments.objects.filter(id=data)
    except Exception:
        return False
def filter_mod_to_task(data):
    try:
        # print('test', Media_models.objects.filter(name='admin'))
        return Comments.objects.filter(id=data)
    except Exception:
        return False
def deleteTask(data: dict):
    global EDIT
    if 'hideTask' in data:
        slug = data['hideTask']
        value = filter_mod_to_task(slug)
        value.update(geeks_field = False)
    elif 'editTask' in data:
        slug = data['editTask']
        value = filter_mod_to_task(slug)
        value.delete()
    elif 'deleteTask' in data:
        slug = data['deleteTask']
        value = filter_mod_to_task(slug)
        value.delete()
        # print(value)
    elif 'restoreTask' in data:
        slug = data['restoreTask']
        value = filter_mod_to_task(slug)
        value.update(geeks_field=True)