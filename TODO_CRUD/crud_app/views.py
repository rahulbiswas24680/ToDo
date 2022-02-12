import os, asana
from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string

# variables needed in functions

project_gid = str(1201798829042385)
asana_token = str(os.environ.get('PERSONAL_ACCESS_TOKEN'))



def middle(request):
    client = asana.Client.access_token(asana_token)
    result = client.tasks.get_tasks_for_project(project_gid, {'created_at': '22', 'completed': 'true'}, opt_pretty=True)
    
    list = []
    for task in result:
        list.append(task)


    context = {
        'list': list
    }

    return render(request, 'crud_app/middle.html', context)


def task_detail(request, task_id):
    client = asana.Client.access_token(asana_token)
    task_id = str(task_id)
    detail_task = client.tasks.get_task(task_id, {'param': 'value', 'param': 'value'}, opt_pretty=True)
    result = client.tasks.get_tasks_for_project(project_gid, {'param': 'value', 'param': 'value'}, opt_pretty=True)
    list = []
    for task in result:
        list.append(task)

    context = {
        'task': detail_task,
        'list': list
    }

    return render(request, 'crud_app/task_detail.html', context)


def create_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        notes = request.POST.get('notes')

        client = asana.Client.access_token(asana_token)
        result = client.tasks.create_task({'name': name, 'notes': notes, 'projects': project_gid}, opt_pretty=True)
        print(result)
        return redirect('middle')

        
    return render(request, 'crud_app/form.html')


def update_task(request, task_id):
    task_id = str(task_id)
    update = True

    if request.method == 'POST':
        name = request.POST.get('name')
        notes = request.POST.get('notes')

        client = asana.Client.access_token(asana_token)
        result = client.tasks.update_task(task_id, {'name': name, 'notes': notes}, opt_pretty=True)

        return redirect('middle')

    return render(request, 'crud_app/form.html', {'update': update})


def delete_task(request, task_id):
    task_id = str(task_id)
    client = asana.Client.access_token(asana_token)
    result = client.tasks.delete_task(task_id, opt_pretty=True)

    return redirect(middle)