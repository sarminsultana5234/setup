from django.db import models

# Create your models here.
class user_info(models.Model):
    username=models . CharField(max_length=50)
    password=models . CharField(max_length=50)

    def _str_ (self):
        return self.username

class userpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def _str_ (self):
        return self.user_name +" "+ self.post



    