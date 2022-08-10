from . import views
from django.urls import path

urlpatterns = [
    path("categories", views.CategoryList.as_view(), name="categories"),
    path("new", views.NewCategory.as_view(), name='new_category'),
    path(
        "<slug:slug>/edit", views.EditCategory.as_view(),
        name='edit_category'
        ),
    path(
        "<slug:slug>/delete", views.DeleteCategory.as_view(),
        name='delete_category'
        ),
    path(
        "detail", views.CategoryList.as_view(),
        name='category_index'
    ),
    path(
        'entries', views.EntryList.as_view(),
        name='entries'
    ),
    path(
        'new_entry', views.NewEntry.as_view(),
        name='new_entry'
    ),
    path(
        '<int:pk>/', views.EntryDetail.as_view(),
        name='entry_detail'
    )
]