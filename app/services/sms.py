from twilio.rest import Client
from app.config.config import settings




class TwilioClient:
    def __init__(self, account_sid, auth_token) -> None:
        self.account_sid = account_sid
        self.auth_token = auth_token
    

    def send_sms(self, reciever_phone_no:str, txt_message:str):
        '''
        send the message via twilio

        '''
        twilio_client = Client(self.account_sid, self.auth_token)
        sender_phone_no = '+12569603620'
        message = twilio_client.messages.create(
            from_ = sender_phone_no,
            body = txt_message,
            to = reciever_phone_no
        )
        return message.sid


    
sms_client =  TwilioClient(
    account_sid = settings.twilio_account_sid,
    auth_token = settings.twilio_auth_token
)
