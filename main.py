from adapter import SmartphoneNotificationAdapter, TabletNotificationAdapter, DesktopNotificationAdapter
from bridge import UserNotification
from notification import Notification, NotificationWithSubject, NotificationWithAttachment
from recipient import Recipient, GroupRecipient

if __name__ == '__main__':
    recipient = Recipient('John')
    recipient2 = Recipient('Jane')
    group_recipient = GroupRecipient('Team', [recipient, recipient2])
    notification = Notification('Hello', [recipient, group_recipient])
    notification.send()

    # Decorator
    notification_with_subject = NotificationWithSubject(notification, 'Important announcement')
    notification_with_attachment = NotificationWithAttachment(
        notification_with_subject, 'product_images.zip'
    )
    notification_with_attachment.send()

    # Adapter
    smartphone_notification = SmartphoneNotificationAdapter(notification)
    tablet_notification = TabletNotificationAdapter(notification)
    desktop_notification = DesktopNotificationAdapter(notification)

    smartphone_notification.send_notification()
    tablet_notification.send_notification()
    desktop_notification.send_notification()

    # Bridge
    user_notification = UserNotification(smartphone_notification)
    user_notification.send()
