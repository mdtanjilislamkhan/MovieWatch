from django.shortcuts import render 
from django.http import HttpResponse
from MR.models import Movie,Top_Movies
import requests

def index(request):
    '''for i in range(2000,2023):
        url = "https://moviesdatabase.p.rapidapi.com/titles"

        querystring ={"list":"most_pop_movies","limit":"50","year":f"{i}"}

        headers = {
            "X-RapidAPI-Key": "6b32103fa2msh39f193544b02f1fp185db3jsn6623e4eac535",
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        for result in data['results']:
            try:
                T = result['titleText']['text']
                image_url = result['primaryImage']['url']
                id = result['id']
                release_year = result['releaseYear']['year']
                movie = Movie(imdb_id=id,title=T,year=release_year,image=image_url)
                movie.save()
            except:
                continue'''
    return HttpResponse("Done")

def homepage(request):
    from django.db.models import Q
    if request.method=="POST":
        queryset = Movie.objects.filter(Q(title__icontains=request.POST['Search']))
        context={"object_list": queryset,}
        return render(request, 'homepage.html',context)
    else:
        ls=[94, 55, 261, 330, 549, 573, 37, 913, 923, 962, 825, 929, 902, 387, 204, 37, 134, 896, 268, 1033, 133, 435, 545, 1087, 485, 766, 598, 200, 29, 609, 87, 733, 998, 664, 175, 656, 382, 131, 642, 63, 632, 81, 576, 90, 484, 409, 516, 283, 396, 1009]
        queryset = Movie.objects.filter(id__in=ls)
        context={"object_list": queryset,}
        return render(request, 'homepage.html',context)

def Top(request):
        from django.db.models import Q
        if request.method=="POST":
            queryset = Movie.objects.filter(Q(title__icontains=request.POST['Search']))
            context={"object_list": queryset,}
            return render(request, 'Top.html',context)
        else:    
            queryset = Top_Movies.objects.all()
            context={"object_list": queryset,}
            return render(request, 'Top.html',context)
    
def Year(request,id):
        from django.db.models import Q
        if request.method=="POST":
            queryset = Movie.objects.filter(Q(title__icontains=request.POST['Search']))
            context={"object_list": queryset,}
            return render(request, 'Year.html',context)
        else:
            yr=int(id)  
            queryset = Movie.objects.filter(year=yr)
            context={"object_list": queryset,}
            return render(request, 'Year.html',context)
def rating(request,id):
    print(id)
    if(id=='1'):
        queryset=Movie.objects.filter(averageRating__gt=0, averageRating__lte=3.9)
        context={"object_list": queryset,}
        return render(request, 'rating.html',context)
    elif(id=='2'):
        queryset=Movie.objects.filter(averageRating__gt=4, averageRating__lte=4.9)
        context={"object_list": queryset,}
        return render(request, 'rating.html',context)
    elif(id=='3'):
        queryset=Movie.objects.filter(averageRating__gt=5, averageRating__lte=6.9)
        context={"object_list": queryset,}
        return render(request, 'rating.html',context)
    elif(id=='4'):
        queryset=Movie.objects.filter(averageRating__gt=7)
        context={"object_list": queryset,}
        return render(request, 'rating.html',context)