from django.contrib.auth import get_user_model

from testcms.celery_config import app
from .models import Comment

@app.task
def create_first_comment(post_id):
    author = get_user_model().objects.all().first()
    Comment.objects.create(comment='First one!', author=author, tournament_post_id=post_id)
