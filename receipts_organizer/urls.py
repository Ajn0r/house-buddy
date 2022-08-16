from . import views
from django.urls import path

urlpatterns = [
    path('categories', views.CategoryList.as_view(), name='categories'),
    path(
        '<int:pk>/category_detail', views.CategoryDetails.as_view(),
        name='detail_category'
        ),
    path('new', views.NewCategory.as_view(), name='new_category'),
    path(
        "<int:pk>/edit_category", views.EditCategory.as_view(),
        name='edit_category'
        ),
    path(
        'delete_category/<int:pk>', views.DeleteCategory.as_view(),
        name='delete_category'
        ),
    path(
        'detail', views.CategoryList.as_view(),
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
    ),
    path(
        '<int:pk>/edit_entry', views.EditEntry.as_view(),
        name='edit_entry'
    ),
    path(
        '<int:pk>/delete_entry', views.DeleteEntry.as_view(),
        name='delete_entry'
    ),
    path(
        'mypage', views.MyPage.as_view(), name='mypage'
    )
]