from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse("Hello world!")


def my_homepage_view(request):
    return HttpResponse("This is Home page!")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now {0}".format(now)
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In {0} hour(s), it will be {1}".format(offset, dt)
    return HttpResponse(html)
