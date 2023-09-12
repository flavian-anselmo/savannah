from app.services.sms import sms_client
class SmsTaks:
    @staticmethod
    def send_sms_for_orders(phone_no:str, customer_name:str):
        sms_client.send_sms(
            reciever_phone_no=phone_no,
            txt_message=f'Hey  {customer_name}, Your order was created successfully! Continue shoping with us 🛍️'
        )