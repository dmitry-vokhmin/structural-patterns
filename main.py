from bridge import UserNotification
from factory import NotificationType, NotificationFactory
from notification import AttachmentNotification
from user import User, UserGroup

if __name__ == '__main__':
    recipient = User('John', 'email', 'phone')
    recipient2 = User('Jane', 'email', 'phone')
    group_recipient = UserGroup('Team', [recipient, recipient2])
    notification = AttachmentNotification('Hello', [recipient, group_recipient], 'attachment')
    notification_service = NotificationFactory.create_notification_service(
        NotificationType.SMS, attachment=True
    )
    user_notification = UserNotification(notification_service)
    user_notification.send_notification(notification)

