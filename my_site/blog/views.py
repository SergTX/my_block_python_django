from django.shortcuts import render
from datetime import date

# creating posts dummy for now
all_posts = [
    {
    "slug": "post-about-me-and-human",
    "image": "bars_coding.jpg",
    "author": "My human",
    "date": date(2023, 12, 21),
    "title": "My cat Bars",
    "excerpt": "This post will be about me - cat and my human , and how I like him",
    "content": """
          This is a fake text which I have to include to provide more text data 
          on my dummy post , so if you read this to this point  I would say there is nothing would 
          be interesting under this post , just My thoughts about my super cat
                     """},

{
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Bars",
    "date": date(2021, 7, 21),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
},
{
    "slug": "programming-is-fun",
    "image": "coding.png",
    "author": "Barsik",
    "date": date(2022, 3, 10),
    "title": "Programming Is Great!",
    "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
},
{
    "slug": "into-the-woods",
    "image": "woods.jpg",
    "author": "Barsik",
    "date": date(2020, 8, 5),
    "title": "Nature At Its Best",
    "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
}
]

def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):  # request will pass dynamically by django
    sorted_posts = sorted(all_posts, key=get_date)  # func get_date will go to every post and return date
    latest_post = sorted_posts[-3:]   # getting the last 3 positions from the list of sorted dates
    return render(request, "blog/starting_page.html", {
        "posts": latest_post     # using posts varibale to display 3 latest post
    })     # point to html file, to instruct django look for this html


def posts(request):         # for the post/ page
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })



def single_detail(request, slug): # taking a slug , then we loop trough all posts and finding that post by provided slug, returning a post
    # where next() function finds a first element when condition met
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })