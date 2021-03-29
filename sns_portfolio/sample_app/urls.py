from django.urls import path

from . import views

urlpatterns = [
    # path(route='url_path', view=view_function, kwargs={}, name='route_name', Pattern=None)
    # sample path = path('profile/<int:profile_id>/summary/', blog.views.profile.summary, {}, 'profile_summary')
    path('', view=views.index, name='index'),
    path(route='<int:question_id>/', view=views.detail, kwargs={}, name='detail'),
    path(route='<int:question_id>/results', view=views.results, kwargs={}, name='results'),
    path(route='<int:question_id/vote', view=views.vote, kwargs={}, name='vote')
]