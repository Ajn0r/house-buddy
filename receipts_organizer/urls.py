from . import views
from django.urls import path

urlpatterns = [
    path('categories', views.CategoryList.as_view(), name='categories'),
    path(
        'category_detail/<int:pk>', views.CategoryDetails.as_view(),
        name='detail_category'
        ),
    path('new', views.NewCategory.as_view(), name='new_category'),
    path(
        "edit_category/<int:pk>", views.EditCategory.as_view(),
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
        'entry/<int:pk>', views.EntryDetail.as_view(),
        name='entry_detail'
    ),
    path(
        'edit_entry/<int:pk>', views.EditEntry.as_view(),
        name='edit_entry'
    ),
    path(
        'delete_entry/<int:pk>', views.DeleteEntry.as_view(),
        name='delete_entry'
    ),
    path(
        'mypage', views.MyPage.as_view(), name='mypage'
    )
]