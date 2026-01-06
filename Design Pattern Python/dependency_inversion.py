from abc import ABC, abstractmethod

# interface
class Notification(ABC):
  @abstractmethod
  def send(self, to: str, msg: str):
    pass
  
class EmailNotification(Notification):
  def send(self, to: str, msg: str):
    print(f"Sending the notification using email to {to}: {msg}")
    
class SMSNotification(Notification):
  def send(self, to: str, msg: str):
    print(f"Sending the notification using the sms {to} and message data {msg}")
    
email_notification = EmailNotification()
sms_notification = SMSNotification()

class NotificationClient:
  def __init__(self, notification_service: Notification):
    self.notification_service = notification_service
    
  def send_notification(self, to: str, msg: str):
    self.notification_service.send(to, str)
    
notification_service_email = NotificationClient(email_notification)
notification_service_email.send_notification("test@test.com", "Hi")

notification_service_sms = NotificationClient(sms_notification)
notification_service_sms.send_notification("1234567890", "Hi from the sms notification data")
    
    