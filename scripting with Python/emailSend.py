import smtplib as smtp
# import smtplib as smtp
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path 

#html = Template(Path('index.html').read_text())
# email = EmailMessage()
# email['from'] = 'Anna Dmitrienko'
# email['to'] = 'anna.racovic@yahoo.com'
# email['subject'] = 'You won 1,000,000 dollars!'




connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'annadmittest@gmail.com'
email_passwd = 'sEBA00212015@test'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='anna.racovic@yahoo.com', msg="Sent from my IDE. Hehe")
connection.close()


#email.set_content(html.substitute({'name': 'TinTin'}), 'html')
# email.set_content('first email sent with Python')

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#   smtp.ehlo() #part of the SMTP protocol
#   smtp.starttls() #connect securely to the server
#   smtp.login('<your email address>', '<your password>')
#   smtp.send_message(email)
print('all good boss!')