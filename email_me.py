import yagmail

# Email credentials

EMAIL_USER = 'paresh581345@gmail.com'
EMAIL_PASS = '4SU16EE416'


def send_email(email_user, email_pass, email_to, email_subject, email_body):
    yag = yagmail.SMTP(email_user, email_pass)
    yag.send(email_to, email_subject, email_body)
    print(f"Email sent to {email_to} ")

# send email with attachment


def send_email_with_attachment(email_user, email_pass, email_to, email_subject, email_body, attachment):
    yag = yagmail.SMTP(email_user, email_pass)
    yag.send(email_to, email_subject, email_body, attachments=attachment)
    print(f"Email sent to {email_to} ")

# send email with multiple attachments


def send_email_with_multiple_attachments(email_user, email_pass, email_to, email_subject, email_body, attachments):
    yag = yagmail.SMTP(email_user, email_pass)
    yag.send(email_to, email_subject, email_body, attachments=attachments)
    print(f"Email sent to {email_to} ")


# send_email(EMAIL_USER, EMAIL_PASS,
#            'parhusail416@gmail.com', 'paresh', 'hello world')
send_email_with_attachment(EMAIL_USER, EMAIL_PASS,
                           'parhusail416@gmail.com', 'paresh', 'hello world', 'blog.png')
