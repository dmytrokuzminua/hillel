"""Homework 7 task 6"""


class MessageSender:
    """Class interface for message sender"""
    def send_message(self, message: str) -> None:
        """Send a message"""
        pass


class SMSService:
    """Class for SMS service"""
    def send_sms(self, phone_number: str, message: str) -> None:
        """Send SMS message"""
        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    """Class for email service"""
    def send_email(self, email_address: str, message: str) -> None:
        """Send email message"""
        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    """Class for push service"""
    def send_push(self, device_id: str, message: str) -> None:
        """Send push message"""
        print(f"Відправка Push на пристрій {device_id}: {message}")


class SMSAdapter(MessageSender):
    """Class adapter for SMS service"""

    def __init__(self, sms_service, phone_number: str):
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:
        """Sending message by sms service"""
        try:
            self.sms_service.send_sms(self.phone_number, message)
        except Exception as e:
            print(f"Помилка SMS: {e}")

class EmailAdapter(MessageSender):
    """Class adapter for email service"""
    def __init__(self, email_service, email_address):
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str) -> None:
        """Sending message by email service"""
        try:
            self.email_service.send_email(self.email_address, message)
        except Exception as e:
            print(f"Помилка Email: {e}")

class PushAdapter(MessageSender):
    """Class adapter for push service"""
    def __init__(self, push_service, device_id: str):
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str) -> None:
        """Sending message by push service"""
        try:
            self.push_service.send_push(self.device_id, message)
        except Exception as e:
            print(f"Помилка Push: {e}")


def send_bulk_message(adapters: list, message: str) -> None:
    """Send bulk message"""
    for adapter in adapters:
        adapter.send_message(message)


if __name__ == "__main__":
    sms_service = SMSService()
    email_service = EmailService()
    push_service = PushService()

    sms_adapter = SMSAdapter(sms_service, "+380123456789")
    email_adapter = EmailAdapter(email_service, "user@example.com")
    push_adapter = PushAdapter(push_service, "device123")

    adapters = [sms_adapter, email_adapter, push_adapter]
    message = "Привіт! Це тестове повідомлення."

    send_bulk_message(adapters, message)
