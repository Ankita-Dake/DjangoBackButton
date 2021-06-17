from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1 style="color:orange;">Home Page <br> <a href="/page1">Page 1</a>|<a '
                        'href="/page2">Page '
                        '2</a>|<a '
                        'href="/page3">Page 3</a>|<a href="/page4">Page 4</a>|<a href="/page5">Page 5</a></h1>')


def page1(request):
    return HttpResponse('Page 1 <a style="color:green; border-radius:4px; font-size:23px" '
                        'href="/">Back</a>')


def page2(request):
    return HttpResponse('Page 2 <a style="color:blue; font-size:20px;" href="/">Back</a>')


def page3(request):
    return HttpResponse('Page 3 <a style="color:pink; font-size:20px;" href="/">Back</a>')


def page4(request):
    return HttpResponse('Page 4 <a style="color:red; font-size:20px;" href="/">Back</a>')


def page5(request):
    return HttpResponse('Page 5 <a style="color:brown; font-size:20px;" href="/">Back</a>')
