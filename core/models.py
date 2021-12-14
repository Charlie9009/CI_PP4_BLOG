from django.db import models
from django.contrib.auth.models import User

# Create a constant tuple to make sure if a post is in draft or published
STATUS = ((0, 'Draft'), (1, 'Published'))
