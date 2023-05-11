from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts=[
    {
        'auther':'ghulam rasool',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'april 26, 2023'

    },
    {
        'auther':'shobi abbas',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'april 26, 2023'

    },
]


def home(request):
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html',{'title':'about'})
