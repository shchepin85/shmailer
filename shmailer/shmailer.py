# ================================ LIBRARIES ================================ #


import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
from jinja2 import Template, Environment, meta


# ================================ FUNCTIONS ================================ #


def sh_template_select():
    """Select template from the directory"""

    template_files_directory = os.path.join(os.getcwd(), 'templates')
    template_files_list = os.listdir(template_files_directory)
    print('List of templates:')
    for template_file_name in template_files_list:
        print(template_files_list.index(template_file_name), ':',
              template_file_name)
    template_selected_file_id = int(input(
            'Input number of selected template: '))
    template_selected_file_path = os.path.join(
            template_files_directory,
            template_files_list[template_selected_file_id])
    return template_selected_file_path


def sh_template_modify(file_path):
    """Modify template"""

    file_object = open(file_path, encoding='utf-8').read()
    template_enviroment = Environment()
    template_ast = template_enviroment.parse(file_object)
    template_variables = dict.fromkeys(
            meta.find_undeclared_variables(template_ast), None)

    for key in template_variables.keys():
        template_variables[key] = input("Input '" + key + "': ")
        template_modified = Template(
                file_object).render(template_variables.items())
    file_object.close()

    return template_modified


def sh_email_send(email_body):
    """Send email"""

    print('Input additional information to send email!')
    email_from = input('From: ')
    email_to = input('To: ')
    email_subject = input('Email subject: ')

    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_body, 'html'))

    server_smtp = ''
    server_port = 0
    server_login = ''
    server_password = ''

    server = smtplib.SMTP(server_smtp, server_port)
    server.starttls()
    server.login(server_login, server_password)
    server.send_message(msg)
    server.quit()

    print('Email sent succesfully!')
    return True


# ================================ MAIN CYCLE =============================== #


print('Hello, welcome to shmailer!')

while(True):
    template_select = sh_template_select()
    template_modify = sh_template_modify(template_select)
    email_send = sh_email_send(template_modify)
    shmailer_exit = input('press Enter')
    # if shmailer_exit == 'exit': break

# print('Bye-bye!')


# ================================ END ====================================== #
