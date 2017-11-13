from django.contrib.auth.models import User
from .models import *
from datetime import datetime



class NotificationUtil(object):

    def createNotification(self,user,source,subject,body,action_generic='',action_yes='',action_no=''):
        usernotifiction = UserNotification()
        usernotification.user = user
        usernotification.source = source
        usernotification.subject = subjecct
        usernotification.body = body
        if action_generic != '':
            usernotification.action_generic = action_generic
        if action_yes != '':
            usernotification.action_yes = action_yes
        if action_no != '':
            usernotification.action_no = action_no

        usernotification.receive_timestamp = datetime.now()
        usernotification.save()

    def markNotificationAsRead(self,usernotification):
        if usernotification.is_read == 'N':
            usernotification.is_read = 'Y'
            usernotification.read_timestamp = datetime.now()
            usernotification.save()

    def archiveNotification(self,usernotification):
        if usernotification.is_archived == 'N':
            usernotification.is_archived = 'Y'
            usernotification.archived_timestamp = datetime.now()
            usernotification.save()
