from .models import Post, Author, Category
from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        lookup_expr='exact',
        label='Author',
        empty_label='all'
    )


    postConnection = ModelMultipleChoiceFilter(
        field_name='postConnection',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=False,
    )

    time_in = DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        label='Publication date',
        widget=DateTimeInput(format='%Y-%m-%d',
                             attrs={'type': 'date'}
                             )
    )


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'postConnection': ['exact'],
        }


class CategoryFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='',
    )