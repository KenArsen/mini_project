from django.shortcuts import render, get_object_or_404

from blog.models import Category


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category_posts = category.posts.all()
    context = {
        'category': category,
        'category_posts': category_posts,
    }
    return render(request, 'blog/category_detail.html', context)
