from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Entry

def dummy_view(request):
    return render(request, "posts/post_list.html", {})


def status_code_view(request):
    return render(request, "posts/post_list.html", {})

def entry_list(request):
    return render(request, "posts/post_list.html", {})

def redirect_back_home(request):
    return redirect('entries:entry_detail', id=1)

class MyClassView(View):
    def get(self, request):
        print("corremos codigo")
        return HttpResponse("Response basado en clases")

class MyListView(ListView):
    model = Entry