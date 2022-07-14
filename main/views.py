from django.contrib import messages
from django.shortcuts import render, redirect
from .form import PostForm
from .models import Post
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from main.models import Category
from django.core.paginator import Paginator
from .models import Carousel
from django.urls import reverse_lazy


def main_index(request):
    request.page_title = "Bosh sahifa"
    return render(request, "main/index.html", {
        "carousel": Carousel.objects.filter(status=Carousel.ACTIVE).all(),
        'last_posts': Post.objects.order_by('-id')[:4],
        'top_like': Post.objects.order_by('-like')[:4],
        'top_dislike': Post.objects.order_by('-dislike')[:4],
        'top_read': Post.objects.order_by('-read')[:4]
    })


def main_cat(request, id):
    request.page_title = "Mahalliy"
    post_list = Post.objects
    category = Category.objects.get(id=id)
    request.breadcrumb = [
        [category.name]
    ]

    post_list = post_list.filter(category_id=id).all()
    paginator = Paginator(post_list.order_by('-id'), per_page=4)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, "main/cat.html", context={
        "objects_list": page.object_list,
        "page_obj": page,
        'category': category
    })


def main_about(request):
    request.page_title = _("Biz haqimizda")
    request.breadcrumb = [
        ['About']
    ]
    return render(request, "main/about.html", context={
    })


def main_coding(request):
    request.page_title = _("Kodlash")
    request.breadcrumb = [
        ['Coding']
    ]
    return render(request, "main/coding.html", context={
    })


@login_required
def main_add(request):
    request.page_title = _("Qo'shish")
    request.breadcrumb = [
        ['Add'],
    ]
    form = PostForm()
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        messages.success(request, _("Maqola muvaffaqiyatli qo'shildi"))
        return redirect('main:index')

    return render(request, "main/add-post.html", {
        "form": form
    })


def main_view(request, id):
    post = Post.objects.get(id=id)
    request.page_title = post.subject



    post.read += 1
    post.save()
    request.breadcrumb = [
        ['View']
    ]
    return render(request, "main/view.html", {
        "post": post,
        'posts': Post.objects.order_by('?')[:3]
    })


@login_required
def main_delete(request, id):
    Post.objects.filter(id=id).delete()

    messages.success(request, _("Maqola muvaffaqiyatli o'chirildi"))

    return redirect("main:index")


@login_required
def main_edit_post(request, pk):
    request.page_title = request.button_title = _("Tahrirlash")
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            form.save()

        messages.success(request, _("Maqola muvaffaqiyatli tahrirlandi"))
        return redirect('main:index')

    return render(request, "main/edit.html", {
        'form': form,
        'post': post
    })



def like(request, type, id):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('main:index') + '?modal=1')
    post = Post.objects.get(id=id)
    if type == 'like':
        post.like += 1
    elif type == 'dislike':
        post.dislike += 1

    post.save()

    return redirect('main:index')