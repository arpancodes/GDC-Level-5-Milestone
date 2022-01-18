# Add all your views here
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Task


def view_tasks(requests):
		tasks = Task.objects.filter(deleted=False).filter(completed=False)
		search_term = requests.GET.get("search_term")
		if(search_term):
				tasks = tasks.filter(title__icontains=search_term)
		return render(requests, "tasks.html", {"tasks": tasks})

def add_task(requests):
		task = requests.GET.get("task")
		Task(title=task).save()
		return HttpResponseRedirect("/tasks")

def delete_task(requests, id):
		Task.objects.filter(id=id).update(deleted=True)
		return HttpResponseRedirect("/tasks")

def complete_task(requests, id):
		Task.objects.filter(id=id).update(completed=True)
		return HttpResponseRedirect("/tasks")

def list_complete_task(requests):
		completed_tasks = Task.objects.filter(deleted=False).filter(completed=True)
		return render(requests, "completed_tasks.html", {"tasks": completed_tasks})
