# -- coding:utf-8
import smtplib
import time
from email.mime.text import MIMEText

class BeaverBotSender(object):
    """
    BeaverBotSender. It sends mails to me.
    bbs = BeaverBotSender()
    bbs.send(title, content)
    """
    def __init__(self):
        self.sender = 'beaver4276@daum.net'
        self.receivers = ['sunkyu4276@gmail.com']

    def send(self, subject, message):
        try_count = 0
        while(True):
            try:
                self.__send(subject, message)
                break
            except Exception as e:
                if try_count == 3:
                    print(str(e))
                    break

                time.sleep(10)
                try_count += 1
                continue

    def __send(self, subject, message):
        server = smtplib.SMTP_SSL('smtp.daum.net', port=465)
        server.ehlo()
        server.login('beaver4276',"daum_tjsrb")
        subject = "[BeaverBot] " + subject
        msg = MIMEText(message)
        msg['Subject'] = subject
        server.sendmail(self.sender, self.receivers, msg.as_string())
        server.quit()
        print("Successfully sent email")

    def test(self):
        subject = "[BeaverBot] SMTP TEST"
        message = """
        SMTP TEST 테스트 입니다.
        """
        msg = MIMEText(message)
        msg['Subject'] = subject
        self.server.sendmail(self.sender, self.receivers, msg.as_string())
        self.server.quit()
        print("Successfully sent email")

def setlogger(logname):
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
    fileHandler = logging.FileHandler("logs/{}.log".format(logname))
    streamHandler = logging.StreamHandler()

    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    return logger


if __name__== '__main__':
    bbs = BeaverBotSender()
    bbs.send("go2", "gogo~")
