from django.shortcuts import render
from django.http import JsonResponse
from.models import *
import json

def serialize_data(qs, fields):
    data = {}
    obj_dict = {}
    for obj in qs:
        key = data[int(obj.id)]
        for field in fields:
            obj_dict[field] = qs.field
        data[key] = obj_dict
        obj_dict = {}
    return data

# Create your views here.
def search_endpoint(request):
    query = request.GET.get('q')
    data = Blog.objects.filter(tagline__search=query)
    response = {"data": serialize_data(query, ['name', 'tagline', 'id'])}
    return JsonResponse(response)