from datetime import date
from django.shortcuts import render

all_posts=[

    {
    "slug":"hike-int-the-mountains",
    "image":"mountains.jpg",
    "author":"Leo",
    "date":date(2021,7,21),
    "title":"Mountain Hiking",
    "excerpt":"1 There is nothing like the views you get when hiking in the mountains! and I was not even prepared for what happened whilst I was enjoying the view",
    "content":"lorem ipsum"

    },
    {
    "slug":"hike-int-the-mountains2",
    "image":"leo.png",
    "author":"Leo",
    "date":date(2021,8,21),
    "title":"Mountain Hiking2",
    "excerpt":"2 There is nothing like the views you get when hiking in the mountains! and I was not even prepared for what happened whilst I was enjoying the view",
    "content":"lorem ipsum"

    },
    {
    "slug":"hike-int-the-mountains3",
    "image":"woods.jpg",
    "author":"Leo",
    "date":date(2021,9,21),
    "title":"Mountain Hiking3",
    "excerpt":"3 There is nothing like the views you get when hiking in the mountains! and I was not even prepared for what happened whilst I was enjoying the view",
    "content":"lorem ipsum"

    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/index.html",{

        "posts":latest_posts
    })
    

def posts(request):
    return render(request,"blog/all-posts.html")
    

def post_detail(request,slug):
    return render(request,"blog/post_detail.html")

