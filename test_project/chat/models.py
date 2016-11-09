import json
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import linebreaks_filter
from django.utils.six import python_2_unicode_compatible
from channels import Group


class Chat(models.Model):
    from_user = models.ForeignKey(User, related_name='%(class)s_from')
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    has_seen = models.BooleanField(default=False)

    def send_notification(self):
        print("send notification")
        notification = {
            "from_user": self.from_user.username,
            "message": self.message,
        }
        print("hii")
        Group("new_chat").send({
            "text": json.dumps(notification),
        })

    def save(self, *args, **kwargs):
        result = super(Chat, self).save(*args, **kwargs)
        self.send_notification()
        return result


