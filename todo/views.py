from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm, TodoUpdateForm




def home(request):

    contxt = {
        "title" : "home"
    }
    return render(request, 'todo/index.html', contxt)


def list_todos(request):

    todos = Todo.objects.all()


    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            print("data is valid and  it is ", form)
            form.save()
            form = TodoForm()   
    else :
        form = TodoForm()    

    context = {
        'form' : form,
        'todos' : todos
    }

    return render(request, 'todo/all_todos.html', context)


def delete_item(request, id):

    todo_item = Todo.objects.get(id=id)
    # todo_item.delete()
    todo_item.completed = True
    todo_item.save()

    print("our item status ", todo_item.completed)
    return redirect("/all-todos/")
   




def update_item(request, id):

    todo_item = Todo.objects.get(id=id)

    print("requst object", request.body)

    if request.method == 'POST':
        todo_form = TodoUpdateForm(request.POST, instance=todo_item)
        if todo_form.is_valid():
            todo_form.save()

            return redirect('all_todos')

    else:
        todo_form = TodoUpdateForm(instance=todo_item)

    context = {
        'form' : todo_form
    }
  
    return render(request, 'todo/update_item.html', context)


def aboutUs(request):

    context = {
        'title' : 'about us',
    }


    return render(request, "todo/aboutUs.html", context)