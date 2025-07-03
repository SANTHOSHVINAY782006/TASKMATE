from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .models import Task 

def index(request):
    form = TaskForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')  # Important! Redirect after POST
        else:
            # Form invalid: render the page with form errors
            tasks = Task.objects.all().order_by('-id')
            return render(request, 'taskmanager/index.html', {
                'form': form,
                'tasks': tasks,
                'completed': tasks.filter(is_complete=True).count(),
                'pending': tasks.filter(is_complete=False).count(),
                'work_count': tasks.filter(category='work').count(),
                'study_count': tasks.filter(category='study').count(),
                'personal_count': tasks.filter(category='personal').count(),
            }) 

    # GET method: just render the page
    tasks = Task.objects.all().order_by('-id')
    context = {
        'form': form,
        'tasks': tasks,
        'completed': tasks.filter(is_complete=True).count(),
        'pending': tasks.filter(is_complete=False).count(),
        'work_count': tasks.filter(category='work').count(),
        'study_count': tasks.filter(category='study').count(),
        'personal_count': tasks.filter(category='personal').count(),
    }
    return render(request, 'taskmanager/index.html', context)  

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_complete = not task.is_complete
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index') 
