from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.
def first_project(request):
    return render(request, 'first_project/first_project.html')