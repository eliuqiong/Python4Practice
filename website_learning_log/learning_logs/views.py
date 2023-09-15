from django.shortcuts import render

# Create your views here.
def index(request):
    """homepage for learning logs"""
    return render(request, 'learning_logs/index.html')