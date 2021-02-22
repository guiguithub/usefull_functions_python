from subprocess import Popen, PIPE
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from email import encoders

#function sendmail
def sendmail(sender, MailA, MailCC, object, mailHTML, codage, pj=None):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = MailA
    msg['Cc'] = MailCC
    msg['Subject'] = object
    msg['Charset'] = codage
    html = mailHTML
    msg.attach(MIMEText(html,'html',_charset=codage))
    if pj:
       attachment  = open(pj,'rb')
       part = MIMEBase('application','octet-stream')
       part.set_payload((attachment).read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition',"attachment; filename= "+os.path.basename(os.path.normpath(pj)))
       msg.attach(part)

    text = msg.as_string()

    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    p.communicate(text)
