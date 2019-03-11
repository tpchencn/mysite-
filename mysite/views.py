from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime


def hello(request):
    ua = request.is_secure()
    return HttpResponse("Hello world! your add is :{0} ".format(ua))


def my_homepage_view(request):
    return HttpResponse("This is Home page!")


def current_datetime(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now {0} </body></html>".format(now)
    # t = get_template('current_datetime.html')
    # t = Template("<html><body>It is now {{ current_date }} </body></html>")
    context = {'current_date': now}
    # html = t.render(context)
    # return HttpResponse(html)
    return render(request, 'current_datetime.html', context)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    context = {"hour_offset": offset, "next_time": dt}
    html = "In {0} hour(s), it will be {1}".format(offset, dt)
    # return HttpResponse(html)
    return render(request, "hours_ahead.html", context)


