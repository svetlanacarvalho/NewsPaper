from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorRating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.authorUser.username}'

    def update_rating(self):
        postRt = self.post_set.aggregate(postRating=Sum('rating'))
        prt = 0
        prt += postRt.get('postRating')

        commentRt = self.authorUser.comment_set.aggregate(commentRating=Sum('ratingComment'))
        crt = 0
        crt += commentRt.get('commentRating')

        self.authorRating = prt * 3 + crt
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'

    CATEGORIES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    ]

    options = models.CharField(max_length=2, choices=CATEGORIES, default=NEWS)
    time_in = models.DateTimeField(auto_now_add=True)
    postConnection = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} : {self.text}'

    def preview(self):
        return self.text[0:124] + '...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    postComment = models.ForeignKey(Post, on_delete=models.CASCADE)
    userComment = models.ForeignKey(User, on_delete=models.CASCADE)
    textComment = models.TextField()
    dateComment = models.DateTimeField(auto_now_add=True)
    ratingComment = models.IntegerField(default=0)

    def like(self):
        self.ratingComment += 1
        self.save()

    def dislike(self):
        self.ratingComment -= 1
        self.save()
