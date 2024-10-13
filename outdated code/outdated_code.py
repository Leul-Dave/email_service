import pandas as pd

# emails = pd.read_csv('emails/emails.csv')
# emails.columns = emails.columns.str.strip()
# email_dictionary = {row['name']: row['email'] for _, row in emails.iterrows()}
# persons_email = list(email_dictionary.values())
# print(persons_email)


# This was from me trying to read the file from the csv file then change it to a dictionary so i can hash through it

# letters = pd.read_csv('Chinese words/1- 1000 - Sheet1.csv')
# Simplified = {(letters_row.Simplified, letters_row.Pinyin): letters_row.Meaning for (index, letters_row) in
#               letters.iterrows()}
# Traditional = {(letters_row.Traditional, letters_row.Pinyin): letters_row.Meaning for (index_, letters_row) in
#                letters.iterrows()}
# Simplified_Keys = list(Simplified)
# Traditional_Keys = list(Traditional)
# random_num = r.randint(1, len(Simplified_Keys) - 1)
# key = Simplified_Keys[random_num]
# chinese, pinyin = key
# meaning = Simplified[key]



# I realized i could change my csv to a json file to cut processing time of the data and have it already hashed(in a dict)

# import json
# with open('../Chinese words/chinese_words.json', 'r', encoding='utf-8') as f:
#     words = json.load(f)
#
# random_word = r.choice(words)
# chinese = random_word['Simplified']
# pinyin = random_word['Pinyin']
# meaning = random_word['Meaning']


# just put this in another file using OOP

# def send_mail():
#     # the email is still kind of bland and boring, so I want to make it seem more lively and try and figure out a way if
#     # I can make the email more interactive and fun to look at so people would want to actually study the language and would
#     # wait for the email
#
#     # if I can make the NLPM fit in here I want there to be a circular thing that shows there progress over the words and
#     # over the sentences they can make from the words, if we can make the randomizer also pick the words in the new database
#     # less than the new ones every time
#     try:
#         msg = MIMEMultipart('alternative')
#         msg['Subject'] = Header("Chinese Word of the Day", 'utf-8')
#         msg['From'] = my_email
#         msg['To'] = ','.join(persons_email)
#
#         text = f"Word of the Day:\nChinese: {chinese}\nPinyin: {pinyin}\nMeaning: {meaning}"
#
#         html = f"""
#         <html>
#           <head>
#           </head>
#           <body style="font-family: Arial, sans-serif; background-color: #f5f5f5; color: #333; padding: 20px;">
#             <div style="background-color: #fff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); padding: 20px; max-width: 600px; margin: 0 auto;">
#               <h1 style="color: #666; text-align: center;" class="flag-wave">Chinese Word of the Day</h1>
#               <div style="background-color: #DC5F00; border-radius: 10px; padding: 20px; margin: 20px 0; text-align: center;" class="glowing-border">
#                 <h2 style="color: #fff; font-size: 2.5em;">{chinese}</h2>
#               </div>
#               <p style="font-size: 1.2em; line-height: 1.5;"><strong>Pinyin: </strong> {pinyin}</p>
#               <p style="font-size: 1.2em; line-height: 1.5;"><strong>Meaning: </strong> {meaning}</p>
#               <hr style="border-top: 1px solid #DC5F00; margin: 20px 0;">
#               <p style="font-size: 0.8em; color: #666; text-align: center;">
#                 Chinese can be difficult to learn, but you're doing great! Keep going!!
#               </p>
#             </div>
#           </body>
#         </html>
#         """
#
#         part1 = MIMEText(text, 'plain')
#         part2 = MIMEText(html, 'html')
#
#         msg.attach(part1)
#         msg.attach(part2)
#
#         with smtplib.SMTP(os.getenv('SMTP'), 587) as connection:
#             connection.ehlo()
#             connection.starttls()
#             connection.ehlo()
#             connection.login(user=my_email, password=password)
#             connection.send_message(msg)
#         print('Emails sent successfully')
#
#         # notification.email(msg)
#
#     except Exception as e:
#         print(f'Error found {e}')



# just put this in the notifications file ()

# response = requests.get(os.getenv('SHEETY_URL'))
# if response.status_code == 200:
#     information = response.json()['email']
#     # Do something with the data
#     persons_email = [info['email'] for info in information]
#     print(persons_email)
# else:
#     print(f"Failed to retrieve data: {response.status_code}")



# made it into a function

# with smtplib.SMTP(os.getenv('SMTP'), 587) as connection:
#     connection.ehlo()
#     connection.starttls()
#     connection.ehlo()
#     connection.login(user=self.my_email, password=self.password)
#     connection.send_message(msg)
# print('Emails sent successfully')