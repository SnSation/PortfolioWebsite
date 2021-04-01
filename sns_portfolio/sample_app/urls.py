from django.urls import path

from . import views

app_name = 'sample_app'

urlpatterns = [
    # path(route='url_path', view=view_function, kwargs={}, name='route_name', Pattern=None)
    # sample path = path('profile/<int:profile_id>/summary/', blog.views.profile.summary, {}, 'profile_summary')
    path('', view=views.IndexView.as_view(), name='index'),
    path(route='<int:pk>/', view=views.DetailView.as_view(), name='detail'),
    path(route='<int:pk>/results/', view=views.ResultsView.as_view(), name='results'),
    path(route='<int:question_id>/vote/', view=views.vote, name='vote')
]