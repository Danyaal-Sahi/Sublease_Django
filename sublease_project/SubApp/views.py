from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'Welcome to My Page'})
# Create your views here.
