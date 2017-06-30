# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Results
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.conf import settings
import sqlite3

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
def temp(request):
    project_path = settings.BASE_DIR
    id = int(request.GET.get('id', -1))
    conn = sqlite3.connect(project_path+"/db.sqlite3")
    cursor = conn.cursor()
    results = cursor.execute('select * from polling_results where id=%s'% id)
    final_dict = {}
    for each in results:
        id = each[0]
        name = each[3]
        final_dict[id] = name
    if conn:
        conn.close()
    return HttpResponse(json.dumps(final_dict), content_type="application/json")
# Create your views here.
