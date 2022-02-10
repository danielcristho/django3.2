from django.http import HttpResponse

def tentang(request):
    return HttpResponse('Halaman tentang')

def index(request):
    return HttpResponse('Halaman index')
