# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    topic = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Question(models.Model):

    #__Question_FIELDS__
    question_text = models.CharField(max_length=255, null=True, blank=True)
    pub_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Question_FIELDS__END

    class Meta:
        verbose_name        = _("Question")
        verbose_name_plural = _("Question")


class Choise(models.Model):

    #__Choise_FIELDS__
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255, null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True)

    #__Choise_FIELDS__END

    class Meta:
        verbose_name        = _("Choise")
        verbose_name_plural = _("Choise")



#__MODELS__END
