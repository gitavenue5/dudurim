from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'djangoapp/post_list.html', {"name":"허경영"})