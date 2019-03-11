from django.core.mail import send_mail
from django.db import models


class MySite(models.Model):

    @staticmethod
    def send_mail(name, subject, email_address, message):
        # 送った人に確認用として送信
        # confirm_message = f"{name} さん \n\n サイトへの訪問とご連絡ありがとうございます！！\n\n*このメールは確認用です。\n\n================================================\n{message}\n\n================================================"
        # my_address = [email_address]
        # send_mail("ご連絡ありがとうございます", confirm_message, email_address, my_address)

        # 自分用に送信
        message = f"from:{email_address}\n{name} さんから送られたメールです。 \n================================================\n{message}\n================================================\n from django project"
        my_address = ['kyou9712@gmail.com']
        send_mail(subject, message, email_address, my_address)
