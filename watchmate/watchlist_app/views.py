# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from .models import Movie
# # Create your views here.

# def movie_list(request):
#     try:
#         movies = Movie.objects.all()
#         data = {'movies':list(movies.values())}
#         return JsonResponse(data)
#     except Exception as e:
#         return HttpResponse(f"An error occurred: {e}")

# def movie_detail(request,pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#         data = {
#             'name':movie.name,
#             'description':movie.description,
#              'active':movie.active
#         }
#         print(data)
#         return JsonResponse(data)
#     except Exception as e:
#         return HttpResponse(f"An error occurred: {e}")
