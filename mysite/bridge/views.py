from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_index(request):
    return render(request, 'templates/index1.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')
