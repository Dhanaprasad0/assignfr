from django.urls import path, include
from .views import home, ask_question, question_detail, signup_view, login_view, logout_view, like_answer, dislike_answer


urlpatterns = [
    path('', home, name='home'),
    path('ask/', ask_question, name='ask'),
    path('question/<int:question_id>/', question_detail, name='question_detail'),
    path('like/<int:answer_id>/', like_answer, name='like_answer'),
    path('dislike/<int:answer_id>/', dislike_answer, name='dislike_answer'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]