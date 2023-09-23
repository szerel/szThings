from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
# from add_content.models import Media_models
# from main.forms_main import Comments_form, RegisterForm, Login_form
from main.models import RegisterForm, Login_form, Media_models, Comments
from main.forms import addTasks, editTasks, Comments_form, Comments_form_EDITtask
from main.editTask import delete, get_mod, deleteTask, get_mod_to_tasks
import requests
from main.greeting_message import message


def index(request):
    if request.user.is_authenticated is True:
        if request.user.has_perm('main.add_media_models'):
            # data = Media_models.objects.filter(name=request.user.username)
            if request.method == 'POST':

                if 'hideTask' in request.POST:
                    # print(request.POST)
                    numbers_string = request.POST['hideTask']
                    numbers_list = []
                    numbers = numbers_string.split()
                    for number in numbers:
                        numbers_list.append(int(number))
                    deleteTask({'hideTask': numbers_list[0]})
                    return redirect(f'/?NameGroup={numbers_list[1]}')

                # elif 'addTask' in request.POST:
                #     # print(request.POST)
                #     form = addTasks(request.POST)
                #     # post = get_object_or_404(Media_models, slug=post_slug)
                #     # print(post)
                #     if form.is_valid():
                #         if len(request.POST['title']) >= 1:
                #             form = form.save(commit=False)
                #             form.name = request.user.username
                #             form.geeks_field = True
                #             form.save()
                #             return redirect('home')
                #         else:
                #             return redirect('home')

                elif 'editTask' in request.POST:
                    # print(request.POST)
                    numbers_string = request.POST['editTask']
                    numbers_list = []
                    numbers = numbers_string.split()
                    for number in numbers:
                        numbers_list.append(int(number))
                    colection = {}
                    x = get_mod_to_tasks(numbers_list[0])
                    # print(x)
                    colection['id'] = x.values_list()[0][0]
                    form = Comments_form_EDITtask(initial={'title': x.values_list()[0][2]})
                    colection['form'] = form
                    data = Media_models.objects.filter(name=request.user.username, geeks_field=True)[::-1]  # забираю свои группы,
                    colection['data'] = data
                    task = Comments.objects.filter(name=request.user.username, geeks_field = True, user_comment=numbers_list[1])
                    colection['task'] = task
                    # print(colection)
                    return render(request, 'main/home.html', colection)
                    # return redirect('home')

                elif 'saveTask' in request.POST:

                    x = get_mod_to_tasks(request.POST['saveTask'])
                    # print(x.values_list())
                    form = Comments.objects.filter(id=request.POST['saveTask'])
                    # print(form)
                    form.update(title=request.POST['title'])
                    return redirect(f'/?NameGroup={x.values_list()[0][4]}')

                elif 'addTaskInGroup' in request.POST:
                    # print(request.POST)
                    if request.POST['addTaskInGroup'] == '':
                        pass
                        # form_comment = Comments_form(request.POST)
                        # # if form_comment.is_valid():
                        # form = form_comment.save(commit=False)
                        # form.user_comment = Media_models(request.POST['addTaskInGroup'])
                        # print(form.user_comment)
                        # form.slug = 'test_post_slug'
                        # form.name = request.user.username
                        # form.geeks_field = True
                        # form.save()
                        # return redirect('home')
                    else:
                        # print(request.POST)
                        form_comment = Comments_form(request.POST)
                        form = form_comment.save(commit=False)
                        form.user_comment = Media_models(request.POST['addTaskInGroup'])
                        # print(form.user_comment.id)
                        # print(form.user_comment)
                        form.slug = 'test_post_slug'
                        form.name = request.user.username
                        form.geeks_field = True
                        form.save()
                        # return redirect('home')
                        # return redirect('home')+f'?NameGroup={form.user_comment.id}'
                        return redirect(f'/?NameGroup={form.user_comment.id}')




        if request.method == 'GET':

            # print(request.GET)
            logo = Media_models.objects.filter(name=request.user.username, geeks_field=True)
            listGroup = []
            for i in logo:
                listGroup.append(i.id)
            # print(listGroup)
            if 'NameGroup' in request.GET:
                # print(request.GET['NameGroup'])
                if int(request.GET['NameGroup']) in listGroup:
                    data = Media_models.objects.filter(name=request.user.username, geeks_field=True)[::-1] #забираю свои группы,
                    # print(data)
                    task = Comments.objects.filter(name=request.user.username, geeks_field=True, user_comment=Media_models(request.GET['NameGroup'])) # Забираю таски из группы
                    form = Comments_form()
                    marker = request.GET['NameGroup']
                    # print(repr(data[2].id), repr(marker))

                    context = {
                        'ide': request.GET['NameGroup'],
                        'form': form,
                        'data': data,
                        'task': task,
                        'marker': int(marker),
                    }
                    return render(request, 'main/home.html', context)



            else:
                logo = Media_models.objects.filter(name=request.user.username, geeks_field = True)[::-1][0] #забираю айдишник моего inbox
                # print(logo.id)
                data = Media_models.objects.filter(name=request.user.username, geeks_field = True)[::-1]
                task = Comments.objects.filter(name=request.user.username, geeks_field=True, user_comment=Media_models(logo.id))
                form = Comments_form()

                context = {
                    'logo': logo,
                    'ide': logo.id,
                    'form': form,
                    'data': data,
                    'task': task,
                    'marker': int(logo.id),
                }
                return render(request, 'main/home.html', context)
    return render(request, 'main/home.html')


def about(request):
    if request.user.is_authenticated is True:
        if request.method == 'GET':
            data = Comments.objects.filter(name=request.user.username, geeks_field = False)
            context = {
                'data': data
            }
            return render(request, 'main/about.html', context)

        if request.method == 'POST':

            if 'deleteTask' in request.POST:
                deleteTask(request.POST)
                data = Comments.objects.filter(name=request.user.username, geeks_field=False)
                context = {
                    'data': data
                }
                return render(request, 'main/about.html', context)

            if 'restoreTask' in request.POST:
                deleteTask(request.POST)
                data = Comments.objects.filter(name=request.user.username, geeks_field=False)
                context = {
                    'data': data
                }
                return render(request, 'main/about.html', context)

    return render(request, 'main/about.html')



def register(request):
    if request.user.is_authenticated is True:
        return redirect('home')
    global form_reg
    error = ''
    if request.method == 'POST':
        form_reg = RegisterForm(request.POST)
        if form_reg.is_valid():
            upper = False
            digit = False
            # print(request.POST)
            for x in request.POST['password1']:
                if x.isupper():
                    upper = True
                if x.isdigit():
                    digit = True
            if upper and digit:
                user = form_reg.save(commit=False)
                user.is_staff = False
                user.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)     #////////
                g = Group.objects.get(name='view_add_task')
                # GroupTask.objects.create(name=user.username, association='InBox')
                user.groups.add(g)
                form = addTasks()
                form = form.save(commit=False)
                form.title = 'Inbox'
                form.name = request.user.username
                form.geeks_field = True
                form.save()

                # ------ ADD first message "hi bro"
                logo = Media_models.objects.filter(name=request.user.username, geeks_field=True)[::-1][0]
                print(logo.id)
                test = Comments_form()
                test = test.save(commit=False)
                test.title = message
                test.name = request.user.username
                test.geeks_field = True
                test.user_comment = logo
                test.save()

                # ======

                return redirect('home')
            else:
                form = RegisterForm(request.POST)
                return render(request, 'main/register.html',
                              {'name': request.POST['username'], 'email': request.POST['email'],
                               'register': form, 'errorPass1': 'Condition not met ↓'})

        else:
            response = {}
            errorForm = ['username', 'email', 'password1', 'password2']
            form = RegisterForm(request.POST)
            for k in form.errors:
                response[k] = form.errors[k][0]
            error = response.keys()
            missing_error = [num for num in errorForm if num not in error]
            for x in missing_error:
                response[x] = ''
            # print(response)
            return render(request, 'main/register.html',
                          {'name': request.POST['username'], 'email': request.POST['email'],
                           'register': form, 'errorName': response['username'],
                           'errorMail': response['email'], 'errorPass1': response['password1']
                           })
            # error = 'There was an error during registration, check the data is correct and try again'
    else:
        form_reg = RegisterForm()
    return render(request, 'main/register.html', {'register': form_reg, 'error': error})


def login_user(request):
    global met
    error = ''
    form_login = Login_form()
    if request.method == 'GET':
        met = request.GET['next']

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'The username or password is not valid.'

    return render(request,'main/login.html',{'login':form_login,'error':error})


#log OUT for user and redirect to home page str404 'not Found'
def logout_user(request):
    logout(request)
    return redirect('home')


#create str404 'not Found'
def page_not_found_view(request, exception):
    return render(request, 'main/404.html', status=404)


def profile(request):
    if request.user.is_authenticated is True:

        if request.method == 'POST':
            if 'addGroup' in request.POST:
                # print(request.POST)
                form = addTasks(request.POST)
                if form.is_valid():
                    if len(request.POST['title']) >= 1:
                        # print('len- good')
                        form = form.save(commit=False)
                        form.name = request.user.username
                        form.geeks_field = True
                        form.save()
                        return redirect('profile')
                    else:
                        return redirect('profile')
            if 'hideGroup' in request.POST:
                # print(request.POST)
                delete(request.POST)
                return redirect('profile')
            elif 'editGroup' in request.POST:
                colection = {}
                x = get_mod(request.POST)
                # print('x== ', x)
                colection['id'] = x.values_list()[0][0]
                # print(x.values_list()[0][0])
                form = editTasks(initial={'title': x.values_list()[0][2]})
                # print(x.values_list()[0][2])
                colection['form'] = form
                data = Media_models.objects.filter(name=request.user.username, geeks_field=True)[::-1][1::]
                colection['data'] = data
                return render(request, 'main/profile.html', colection)
            elif 'saveGroup' in request.POST:
                # print(request.POST['saveGroup'])
                form = Media_models.objects.filter(id=request.POST['saveGroup'])
                form.update(title=request.POST['title'])
                return redirect('profile')
        if request.method == 'GET':

            data = Media_models.objects.filter(name=request.user.username, geeks_field=True)[::-1][1::]
            # print(data)
            form = addTasks()
            context = {
                'form': form,
                'data': data
            }
            return render(request,'main/profile.html', context)
        #