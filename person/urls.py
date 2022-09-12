from django.urls import path

from core.helper import url_utils
from . import views

app_name = 'person'
urlpatterns = []
urlpatterns.extend(
    url_utils.create_common_urls_for_section(
        init_view=views.PersonInitView.as_view(),
        edit_view=views.full_form,
        search_view=views.PersonSearchView.as_view(),
        merge_view=views.PersonInitView.as_view(),
        edit_id_name='iperson_id',
        # edit_view=views.full_form,
        # search_view=views.LocationSearchView.as_view(),
        # merge_view=views.LocationMergeView.as_view(),
    )
)

urlpatterns.extend(url_utils.create_urls_for_quick_init(
    views.PersonQuickInitView.as_view(),
    views.return_quick_init,
))

urlpatterns.extend([
    path('debug1', views.return_quick_init, name='debug1'),
])