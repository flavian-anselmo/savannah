from app.services.sms import sms_client
class SmsTaks:
    @staticmethod
    def send_sms_for_orders(phone_no:str):
        sms_client.send_sms(
            reciever_phone_no=phone_no,
            txt_message='MSG TEST'
        )