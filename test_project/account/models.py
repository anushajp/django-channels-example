from django.db import models
import json
from django.contrib.auth.models import User
from channels import Group

class CustomUser(User):

    def send_notification(self):
        print(self)
        print("send noti")
        notification = {
            "username": self.username,
            "text":"hello"
        }
        # Group("new_user").send({
        #     "text": json.dumps(notification),
        # })

    def save(self, *args, **kwargs):

        print("saving something.... in user table")
        print(self)
        result = super(User, self).save(*args, **kwargs)
        # if not User.objects.get(username=self.username):
        self.send_notification()
        return result
