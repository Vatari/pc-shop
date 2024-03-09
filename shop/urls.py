from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
 #   path("404/", views.error404, name="error"),
    path("add/", views.add_offer, name="add"),
    path("offer/<int:id>", views.view, name="offer"),
    path("offer/<int:id>/edit", views.edit_offer, name="edit_offer"),
    path("category/choose", views.category_list, name="category_list"),
    path(
        "category/laptops/",
        views.category,
        {"category": "laptops"},
        name="laptops",
    ),
    path("category/servers/", views.category, {"category": "servers"}, name="servers"),
    path(
        "category/desktop_computers/",
        views.category,
        {"category": "desktop_computers"},
        name="desktop_computers",
    ),
    path(
        "category/parts/",
        views.category,
        {"category": "parts"},
        name="parts",
    ),
    path("cart/", views.cart, name="cart"),
    path("user/<int:id>", views.user_view, name="user_view"),
    path("search/results", views.search_results, name="search_results"),
]
