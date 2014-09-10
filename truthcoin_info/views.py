import logging, hashlib, random
import re, sys, os
import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.http import urlquote

import numpy
from numpy import ma
from consensus import Factory

def home(request):

    return render(request, 'home.html')


def voting(request):

    return render(request, 'voting.html')


def faq(request):

    return render(request, 'faq.html')


class NumpyEncoder(json.JSONEncoder):

    def default(self, obj):

        if isinstance(obj, numpy.ndarray):

            return obj.tolist();

        return json.JSONEncoder.default(self, obj)


@csrf_exempt
def vote(request):

    if request.method == 'POST':

        user_ballot = [
            float(request.POST.get('d1', 0.5)),
            float(request.POST.get('d2', 0.5)),
            float(request.POST.get('d3', 0.5)),
            float(request.POST.get('d4', 0.5)),
            float(request.POST.get('d5', 0.5))
        ]

        votes = ma.masked_array([
            ma.masked_array([0, 0, 0.5, 0, 0]),   # jack
            ma.masked_array([0, 0, 0.5, 0, 0]),   # jill
            ma.masked_array([0, 0, 0.5, 0, 0]),   # hansel
            ma.masked_array([0, 0, 0.5, 0, 0]),   # gretel
            ma.masked_array([0, 0, 0.5, 0, 0]),   # mary mary
            ma.masked_array(user_ballot),      # user
        ])

        logging.error(votes)
        results = json.dumps(Factory(votes), cls=NumpyEncoder)

    else:

        results = {}

    return HttpResponse(results, content_type='application/json')

