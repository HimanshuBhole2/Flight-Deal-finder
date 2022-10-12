from twilio.rest import Client
class NotificationManager:

    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self,text):
        account_id = "YOUR TWILO ID"
        auth_token = "YOUR TWILIO TOKEN"
        client = Client(account_id, auth_token)

        message = client.messages \
            .create(
            body=text,
            from_='YOUR TWILIO NUMBER',
            to='YOUR TWILIO VERIFIED PHONE NUMBER'
        )

        print(message.sid)
