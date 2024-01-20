from django.shortcuts import render

# Create your views here.


def starting_page(request):  # request will pass dynamically by django
    return render(request, "blog/starting_page.html")     # point to html file, to instruct django look for this html


def posts(request):         # for the post/ page
    pass



def single_detail(request):
    pass