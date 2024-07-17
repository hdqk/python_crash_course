from django.shortcuts import render


def index(request):
    """The home page from Learning Log."""
    return render(request, 'learning_logs/index.html')
