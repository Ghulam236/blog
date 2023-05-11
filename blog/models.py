from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField() # that can store an unlimited amount of text. so we dont defin max_length
    date_posted=models.DateTimeField(default=timezone.now)
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    #  Define an auther field for the post model, 
    # which is a ForeignKey that references the User model. 
    # This establishes a many-to-one relationship between post and User models,
    #  meaning that a user can create multiple posts, but each post can only have one author.
    #  The on_delete argument specifies what happens when the referenced User object is deleted. 
    # In this case, we specify models.CASCADE, which means that if a User object is deleted, 
    # all the post objects that reference it will be deleted as well.