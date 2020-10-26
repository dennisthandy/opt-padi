from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.conf import settings

import os

from helper.create_data import create_data
from helper.test_data import predict

# Create your views here.
def index(request):
    response = {}
    if request.method == 'POST':
        response = upload(request).data
    return render(request, 'index.html', response);

@api_view(['POST'])
def upload(request):
    if request.method == 'POST':

        userFile = request.data.get('gambar')
        fs = FileSystemStorage()
        filename = fs.save(userFile.name, userFile)
        file_to_test = os.path.join(settings.BASE_DIR, ('media/' + userFile.name))

        data = create_data(file_to_test)

        result = predict(data)
    
        return Response({
            'message': 'ok', 
            'url': 'http://'+ request.META['HTTP_HOST'] + fs.url(filename), 
            'label': result, 
            'prob': 100
        })
    
    return Response({'message': 'not ok'})