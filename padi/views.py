from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import os

from helper.create_data import create_data
from helper.identify import cnn_predict, lvq_predict

# Create your views here.
def index(request):
    response = {}
    if request.method == 'POST':
        response = upload(request).data
    response['path'] = request.get_full_path()
    return render(request, 'index.html', response);

def info(request):
    return render(request, 'info.html', { 'path': request.get_full_path() })

def about(request):
    return render(request, 'about.html', { 'path': request.get_full_path() });

@api_view(['POST'])
def upload(request):
    if request.method == 'POST':

        userFile = request.data.get('gambar')
        fs = FileSystemStorage()
        filename = fs.save(userFile.name, userFile)
        file_to_test = os.path.join(settings.BASE_DIR, ('media/' + userFile.name))

        data = create_data(file_to_test)

        cnn_result = cnn_predict(data['cnn'])
        lvq_result = lvq_predict(data['lvq'])
    
        return Response({
            'message': 'ok', 
            'url': 'http://'+ request.META['HTTP_HOST'] + fs.url(filename), 
            'label': {'cnn': cnn_result, 'lvq': lvq_result}, 
            'prob': 100
        })
    
    return Response({'message': 'not ok'})