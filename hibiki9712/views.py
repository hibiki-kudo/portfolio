import threading

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_protect
import requests

from my_site.settings import GAS_LOGGING_URL
from .models import MySite


@csrf_protect
def index(request):
    context = {
        "facebook": "https://www.facebook.com/profile.php?id=100012278737413",
        "twitter": "https://twitter.com/hibikikkk_9712",
        "github": "https://github.com//hibikikkk",
        "mail_url": "/send_mail"
    }
    logging_access_info(request)
    # threading.Thread(target=logging_access_info, args=(request,)).start()
    return render(request, "index.html", context)


@csrf_protect
def send_mail(request):
    if request.method == "POST":
        try:
            if not request.POST.get('name'):
                raise ValueError
            if not request.POST.get('email'):
                raise ValueError
            if not request.POST.get('subject'):
                raise ValueError
            if not request.POST.get('message'):
                raise ValueError

            MySite.send_mail(request.POST.get('name'),
                             request.POST.get('subject'),
                             request.POST.get('email'),
                             request.POST.get('message')
                             )
            return HttpResponse("ok")
        except ValueError:
            raise Http404

    raise Http404


def logging_access_info(request):
    requests.get(GAS_LOGGING_URL, params={"access_log": str(request.headers)})
