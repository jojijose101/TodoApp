from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.forms import TodoForm
from todoapp.models import Todo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


#class based views

class Task(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todo'

class TodoDetails(DetailView):
    model = Todo
    template_name = 'details.html'
    context_object_name = 'todo'

class TodoUpdate(UpdateView):
    model = Todo
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('task','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk':self.object.id})


class TodoDelete(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvlist')



# Create your views here.
def index(request):
    obj = Todo.objects.all()
    if request.method == 'POST':
        task = request.POST['task']
        priority = request.POST['priority']
        date = request.POST['date']
        todo = Todo.objects.create(task=task,priority=priority,date=date)
        todo.save()
        return redirect('/')
    return render(request,'index.html',{'todo': obj })
def delete(request,taskid):
    task = Todo.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def edit(request,id):
    task = Todo.objects.get(id=id)
    f = TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'f':f})