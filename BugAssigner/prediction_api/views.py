from django.shortcuts import render
from rest_framework import generics
from .models import Result, Request
from .serializers import RequestSerializer, ResultSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import nltk
import string
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import Model, load_model


# Create your views here.
class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class ResultList(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class RequestDetail(generics.RetrieveAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class ResultDetail(generics.RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

@api_view(["POST"])
def prediction(request):
    try:
        rankK = 10
        myrequest = request.data
        #tokenize
        userinput = myrequest.get('description')
        print(userinput)
        data = nltk.word_tokenize(userinput)

        clean_data = []
        for item in data:
            #Change to lower case
            desc = item.lower()

            #remove trailing punctuation
            stripped_desc = desc.strip(string.punctuation)

            #remove whitespaces
            stripped_desc = stripped_desc.strip()

            #filter  and append to new list
            clean_data.append(stripped_desc)
            clean_data = list(filter(None, clean_data))

        unit = np.array(clean_data)
        X_test = np.empty(shape=[len(unit), 30,200], dtype='float32')
        model = load_model('/home/athman/Documents/django/BugAssigner/prediction_api/dbbrna3.h5')
        predict = model.predict(X_test)
        sortedIndices = []
        pred_classes = []
        labels = pd.read_csv('/home/athman/Documents/django/BugAssigner/prediction_api/labels.csv')
        classes = np.array(labels)
        for ll in predict:
            sortedIndices.append(sorted(range(len(ll)), key=lambda ii: ll[ii], reverse=True))
        for k in range(1, rankK+1):
            for sortedInd in sortedIndices:
                pred_classes.append(classes[sortedInd[:k]])

        array1_length = len(pred_classes)
        useremail_array = pred_classes[0:1]
        user = useremail_array[0]
        result=user[0][0]
        return JsonResponse('Your result is {}'.format(result), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)






