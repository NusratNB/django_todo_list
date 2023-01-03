from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from django.views import View
from .models import TodoItem
from .forms import TodoItemForm

# def index(request):
#     return render(request, "main/main.html")


class MainPageView(ListView):
    template_name = "main/main.html"
    model = TodoItem
    all_tasks = model.objects.all()
    if len(all_tasks)>0:
        context_object_name = "tasks"
    
    def post(self, request):
        task_form = TodoItemForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.save()
            


        


