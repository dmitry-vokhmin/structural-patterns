class ExternalSmsNotificationService:
    def send_sms(self, phone, message):
        print(f"Sending SMS to {phone} with message {message}")
