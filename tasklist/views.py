from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView

from tasklist.models import Task, User
from tasklist.forms import TaskForm, UserForm


def user_list(request):
    users = User.objects.all().order_by('id')
    return render(request, 
                'tasklist/user_list.html',
                {'users': users})


def user_edit(request, user_id=None):
    """ユーザーの編集追加"""
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user = User()


    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'tasklist/user_edit.html', dict(form=form, user_id=user_id))


def user_del(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return redirect('user_list')



class TaskList(ListView):
    """タスクの一覧"""
    context_object_name = 'tasks'
    templates_name = 'tasklist/task_list.html'
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        tasks = user.tasks.all().order_by('id')
        self.object_list = tasks

        context = self.get_context_data(object_list=self.object_list, user=user)
        return self.render_to_response(context)


def task_edit(request, user_id, task_id=None):
    """タスクの編集"""
    user = get_object_or_404(User, pk=user_id)
    if task_id:
        task = get_object_or_404(Task, pk=task_id)
    else:
        task = Task()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('task_list', user_id=user_id)
    else:
        form = TaskForm(instance=task)
        
        return render(request,
                    'tasklist/task_edit.html',
                    dict(form=form, user_id=user_id, task_id=task_id, user=user))



def task_del(request, user_id, task_id):
    """タスクの削除"""
    task = get_object_or_404(Task, pk=task_id)
    task.delte()
    return redirect('task_list', user_id=user_id)
