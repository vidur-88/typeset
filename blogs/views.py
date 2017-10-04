from django.http import HttpResponse, HttpResponseServerError
from rest_framework.decorators import api_view
import json

from blogs.services import (get_all_blogs, add_blog, add_comment,
                            update_comment, get_blog, get_blog_comment,
                            add_blog_paragraph, update_blog_paragraph)


@api_view(['GET'])
def index(request):
    try:
        resp = {'data': get_all_blogs()}
    except Exception as e:
        return HttpResponseServerError("{'Error': 'Server Error', \
                                       'message': '%s'}" % e.message)
    return HttpResponse(json.dumps(resp))


@api_view(['POST'])
def create_blog(request):
    try:
        params = json.loads(request.body)
        resp = add_blog(params)
    except Exception as e:
        return HttpResponseServerError("{'Error': 'Server Error', \
                                       'message': '%s'}" % e.message)
    return HttpResponse(json.dumps(resp))


@api_view(['GET'])
def blog(request):
    try:
        resp = get_blog(request.GET)
    except Exception as e:
        return HttpResponseServerError("{'Error': 'Server Error', \
                                       'message': '%s'}" % e.message)
    return HttpResponse(json.dumps(resp))


@api_view(['POST'])
def create_blog_paragraph(request):
    try:
        params = json.loads(request.body)
        resp = add_blog_paragraph(params)
    except Exception as e:
        return HttpResponseServerError("{'Error': 'Server Error', \
                                       'message': '%s'}" % e.message)
    return HttpResponse(json.dumps(resp))


@api_view(['POST'])
def edit_blog_paragraph(request):
    try:
        params = json.loads(request.body)
        resp = update_blog_paragraph(params)
    except Exception as e:
        return HttpResponseServerError("{'Error': 'Server Error', \
                                       'message': '%s'}" % e.message)
    return HttpResponse(json.dumps(resp))


@api_view(['POST'])
def create_comment(request):
    try:
        params = json.loads(request.body)
        resp = add_comment(params)
    except Exception as e:
        return HttpResponseServerError("{'Error': 'Server Error', \
                                       'message': '%s'}" % e.message)
    return HttpResponse(json.dumps(resp))


@api_view(['POST'])
def edit_comment(request):
    try:
        params = json.loads(request.body)
        resp = update_comment(params)
    except Exception as e:
        return HttpResponseServerError("{'Error': 'Server Error', \
                                       'message': '%s'}" % e.message)
    return HttpResponse(json.dumps(resp))


@api_view(['GET'])
def blog_comments(request):
    try:
        resp = get_blog_comment(request.GET)
    except Exception as e:
        return HttpResponseServerError("{'Error': 'Server Error', \
                                       'message': '%s'}" % e.message)
    return HttpResponse(json.dumps(resp))
