from django import forms
from tasklist.models import Task, User

class TaskForm(forms.ModelForm):
    """タスクのフォーム"""
    class Meta:
      model = Task
      fields = ('name', )


class UserForm(forms.ModelForm):
  """ユーザーのフォーム"""
  class Meta:
    model = User
    fields = ('name', )