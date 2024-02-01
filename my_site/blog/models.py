from django.db import models

# Create your models here.


from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):  # this func overrides what we want to return
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):  # adding a helper to return full name in admin ui
        return f"{self.first_name} {self.last_name}"

    def __str__(self):  # this func overrides what we want to return
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=80)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)


# class TestTableBook(models.Model):
#     title = models.CharField(max_length=50)
#     rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])    # set boundaries , validator
#     author = models.CharField(null=True, max_length=30)
#     is_bestSelling = models.BooleanField(default=False)
#
#     def __str__(self):   # if TestTableBook was requested in the console give me the output in this format
#         return f'{self.title} ({self.rating})'
