# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Results
from django.shortcuts import render
from django.http import HttpResponse
import json

def get_value(request):
    key=request.GET.get('id','')
    record=Results.objects.get(id=key)
    final_dict = {}
    final_dict["constituency"] = record.constituency
    final_dict["constituency_code"] = record.constituency_code
    final_dict["leading_party"] = record.leading_party
    final_dict["trailing_candidate"] = record.trailing_candidate
    final_dict["trailing_party"] = record.trailing_party
    return HttpResponse(json.dumps(final_dict), content_type="application/json")

# Create your views here.
