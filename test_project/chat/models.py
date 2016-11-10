import json
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import linebreaks_filter
from django.utils.six import python_2_unicode_compatible
from channels import Group

import json
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
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
            'group': "new_chat",
        }
        print("hii")
        Group("new_chat").send({
            "text": json.dumps(notification),
        })

    def save(self, *args, **kwargs):
        result = super(Chat, self).save(*args, **kwargs)
        self.send_notification()
        return result


def new_user_send_notification(notification):
    Group("new_user").send({'text': json.dumps(notification)})



def user_post_save(sender, **kwargs):
    print("signals...")
    user = kwargs.get('instance')
    print(user)
    new_user_send_notification({
        'user': user.username,
        'group': "new_user",
    })

post_save.connect(user_post_save, sender=User)

