from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from ..models import Watchlist,StreamPlatform
from .serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def watch_list(request):
    try:
        if request.method == 'GET':
            movies = Watchlist.objects.all()
            serializer = WatchListSerializer(movies, many=True)  # Note the `many=True` argument
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer =WatchListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','PUT','DELETE'])
def watchlist_detail(request,pk):
    movie = None
    try:
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = WatchListSerializer(movie,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        elif request.method == 'DELETE':
            movie.delete()
            return Response({"message": "Movie deleted successfully"},status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
    
@api_view(['GET','POST'])
def stream_platform(request):
    try:
        if request.method == 'GET':
            platforms = StreamPlatform.objects.all()
            serializer = StreamPlatformSerializer(platforms, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = StreamPlatformSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET','PUT','DELETE'])
def  stream_platform_detail(request,pk):
    stream_platform = None
    try:
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"error": "Stream Platform not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = StreamPlatformSerializer(stream_platform)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = StreamPlatformSerializer(stream_platform,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            stream_platform.delete()
            return Response({"message": "Stream Platform deleted successfully"},status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
