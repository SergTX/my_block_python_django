from django.shortcuts import render, get_object_or_404
# from datetime import date
from .models import Post


# creating posts dummy for now
# all_posts = []


# def get_date(post):
#     return post['date']

# Create your views here.


def starting_page(request):  # request will pass dynamically by django
    latest_post = Post.objects.all().order_by("-date")[:3]    # query in desc order lasts posts by date,not support [-3:]
    # sorted_posts = sorted(all_posts, key=get_date)  # func get_date will go to every post and return date
    # latest_post = sorted_posts[-3:]   # getting the last 3 positions from the list of sorted dates
    return render(request, "blog/starting_page.html", {
        "posts": latest_post     # using posts varibale to display 3 latest post
    })     # point to html file, to instruct django look for this html


def posts(request):         # for the post/ page
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts     # getting all post from the list
        # now getting all posts from database
    })



def single_detail(request, slug): # taking a slug , then we loop trough all posts and finding that post by provided slug, returning a post
    # where next() function finds a first element when condition met
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    identified_post = get_object_or_404(Post, slug=slug)  # if slug was not there it will return error
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })