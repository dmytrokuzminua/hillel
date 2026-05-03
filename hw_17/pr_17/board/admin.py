from django.contrib import admin
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse

from .models import Ad, Category, Comment, Profile


# === ACTIONS FOR ADMIN ===
def show_last_month_ads(modeladmin, request, queryset):
    ads = Ad.objects.filter(created_at__gte=timezone.now() - timedelta(days=30))
    response = "<h2>Оголошення за останній місяць:</h2><ul>"
    for ad in ads:
        response += f"<li>{ad.title} - {ad.price}</li>"
    response += "</ul>"
    return HttpResponse(response)
show_last_month_ads.short_description = "Показати оголошення за останній місяць"


def show_ads_with_comment_count(modeladmin, request, queryset):
    ads = Ad.objects.annotate(comment_count=Count('comment'))
    response = "<h2>Оголошення з кількістю коментарів:</h2><ul>"
    for ad in ads:
        response += f"<li>{ad.title} - {ad.comment_count} коментарів</li>"
    response += "</ul>"
    return HttpResponse(response)
show_ads_with_comment_count.short_description = "Показати оголошення з кількістю коментарів"


# === AD MODEL REG===
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_active', 'category', 'user')
    list_filter = ('is_active', 'category')
    search_fields = ('title',)
    actions = [show_last_month_ads, show_ads_with_comment_count]


# === OTHER MODEL REG ===
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'ad', 'created_at')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')