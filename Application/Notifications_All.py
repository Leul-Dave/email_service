import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from dotenv import load_dotenv
load_dotenv()


class Notify:

    def __init__(self):
        self.my_email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
        # self.people_c = []
        self.response_c = requests.get(os.getenv('C_SHEETY_URL'))
        self.response_j = requests.get(os.getenv('J_SHEETY_URL'))
        self.response_k = requests.get(os.getenv('K_SHEETY_URL'))

    # retrieves emails from your sheety api
    def peoples_email_c(self):
        if self.response_c.status_code != 200:
            print(f"Failed to retrieve data: {self.response_c.status_code}")
        else:
            data = self.response_c.json()
            information = data.get('cEmail', [])
            persons_email = [info['email'] for info in information]
            # self.people_c = [info['first'] for info in information]
            return persons_email

    def peoples_email_j(self):
        if self.response_j.status_code != 200:
            print(f"Failed to retrieve data: {self.response_j.status_code}")
        else:
            data = self.response_j.json()
            information = data.get('jEmail', [])
            persons_email = [info['email'] for info in information]
            # self.people_c = [info['first'] for info in information]
            return persons_email


    def peoples_email_k(self):
        if self.response_k.status_code != 200:
            print(f"Failed to retrieve data: {self.response_k.status_code}")
        else:
            data = self.response_k.json()
            information = data.get('kEmail', [])
            persons_email = [info['email'] for info in information]
            # self.people_c = [info['first'] for info in information]
            return persons_email

    # sends the email (can be reused for both Korean and Chinese)
    def send_email(self, recipients, subject, text_content, html_content):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.my_email
        msg['To'] = ','.join(recipients)

        part1 = MIMEText(text_content, 'plain')
        part2 = MIMEText(html_content, 'html')

        msg.attach(part1)
        msg.attach(part2)

        with smtplib.SMTP(os.getenv('SMTP'), 587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.ehlo()
            connection.login(user=self.my_email, password=self.password)
            connection.send_message(msg)
        print(f'Email sent successfully for "{subject}"')

    # send email for Korean word
    def send_mail_k(self, korean, english):
        recipients = self.peoples_email_k()
        subject = "Korean Word of the Day"
        text_content = f"Word of the Day:\nKorean: {korean}\nMeaning: {english}"
        html_content = f"""
        <html>
          <head>
          </head>
          <body style="font-family: Arial, sans-serif; background-color: #f5f5f5; color: #333; padding: 20px;">
            <div style="background-color: #fff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 20px; max-width: 600px; margin: 0 auto;">
              <h1 style="color: #666; text-align: center;" class="flag-wave">Korean Word of the Day</h1>
              <div style="background-color: #DC5F00; border-radius: 10px; padding: 20px; margin: 20px 0; text-align: center;" class="glowing-border">
                <h2 style="color: #fff; font-size: 2.5em;">{korean}</h2>
              </div>
              <p style="font-size: 1.2em; line-height: 1.5;"><strong>Meaning: </strong> {english}</p>
              <hr style="border-top: 1px solid #DC5F00; margin: 20px 0;">
              <p style="font-size: 0.8em; color: #666; text-align: center;">
                Korean can be difficult to learn, but you're doing great! Keep going!!
              </p>
            </div>
          </body>
        </html>
        """
        self.send_email(recipients, subject, text_content, html_content)

    # send email for Chinese word
    def send_mail_c(self, chinese, pinyin, meaning):
        recipients = self.peoples_email_c()
        subject = "Chinese Word of the Day"
        text_content = f"Word of the Day:\nChinese: {chinese}\nPinyin: {pinyin}\nMeaning: {meaning}"
        html_content = f"""
        <html>
          <head>
          </head>
          <body style="font-family: Arial, sans-serif; background-color: #f5f5f5; color: #333; padding: 20px;">
            <div style="background-color: #fff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 20px; max-width: 600px; margin: 0 auto;">
              <h1 style="color: #666; text-align: center;" class="flag-wave">Chinese Word of the Day</h1>
              <div style="background-color: #DC5F00; border-radius: 10px; padding: 20px; margin: 20px 0; text-align: center;" class="glowing-border">
                <h2 style="color: #fff; font-size: 2.5em;">{chinese}</h2>
              </div>
              <p style="font-size: 1.2em; line-height: 1.5;"><strong>Pinyin: </strong> {pinyin}</p>
              <p style="font-size: 1.2em; line-height: 1.5;"><strong>Meaning: </strong> {meaning}</p>
              <hr style="border-top: 1px solid #DC5F00; margin: 20px 0;">
              <p style="font-size: 0.8em; color: #666; text-align: center;">
                Chinese can be difficult to learn, but you're doing great! Keep going!!
              </p>
            </div>
          </body>
        </html>
        """
        self.send_email(recipients, subject, text_content, html_content)

    def send_mail_j(self, hiragana, kanji, english):
        recipients = self.peoples_email_j()
        subject = "Japanese Word of the Day"

        # Create the text content, checking if Kanji exists
        text_content = f"Word of the Day:\nHiragana: {hiragana}"
        if kanji:
            text_content += f"\nKanji: {kanji}"
        text_content += f"\nMeaning: {english}"

        # Create the HTML content
        kanji_html = f"<h2 style='color: #fff; font-size: 2.5em;'>Kanji: {kanji}</h2>" if kanji else ""
        html_content = f"""
        <html>
          <head>
          </head>
          <body style="font-family: Arial, sans-serif; background-color: #f5f5f5; color: #333; padding: 20px;">
            <div style="background-color: #fff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 20px; max-width: 600px; margin: 0 auto;">
              <h1 style="color: #666; text-align: center;" class="flag-wave">Japanese Word of the Day</h1>
              <div style="background-color: #DC5F00; border-radius: 10px; padding: 20px; margin: 20px 0; text-align: center;" class="glowing-border">
                <h2 style="color: #fff; font-size: 2.5em;">{hiragana}</h2>
              </div>
              {kanji_html}
              <p style="font-size: 1.2em; line-height: 1.5;"><strong>Meaning: </strong> {english}</p>
              <hr style="border-top: 1px solid #DC5F00; margin: 20px 0;">
              <p style="font-size: 0.8em; color: #666; text-align: center;">
                Japanese can be difficult to learn, but you're doing great! Keep going!!
              </p>
            </div>
          </body>
        </html>
        """
        self.send_email(recipients, subject, text_content, html_content)