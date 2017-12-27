from botocore.client import BaseClient

class SNS:

    def __init__(self, sns_client: BaseClient) -> None:
        self.sns_client = sns_client

    def send(self, phone: int, message: str) -> None:
        self.sns_client.publish(
            PhoneNumber=f'+1{phone}',
            Message=message
        )
