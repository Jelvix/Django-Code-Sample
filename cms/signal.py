

def add_first_comment(sender, instance, created, *args, **kwargs):
    from .tasks import create_first_comment
    if instance and created:
        create_first_comment.delay(instance.id)
