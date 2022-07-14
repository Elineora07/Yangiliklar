from django.contrib import admin
from .models import Category, Carousel, Post



@admin.action(description="Faollashtirish")
def active(self, request, queryset):
    queryset.update(status=Carousel.ACTIVE)


@admin.action(description="Nofaollashtirish")
def inactive(self, request, queryset):
    queryset.update(status=Carousel.INACTIVE)




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name_uz',
        'name_en'
    ]


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    actions = [
        active,
        inactive
    ]
    list_display = [
        'id',
        'header',
        'comment',
        'status'
    ]




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'subject_uz',
        'subject_en'
    ]

    fields = [
        'category',
        'subject_uz',
        'subject_en',
        'content_uz',
        'content_en',
        'image'
    ]