from botocore.client import BaseClient

class MessageSender:

    def __init__(self, sns_client: BaseClient) -> None:
        self.sns_client = sns_client

    def send(phone: int, message: str) -> None:
        self.sns_client.publish(
            PhoneNumber=f'+1{phone}',
            Message=message
        )
