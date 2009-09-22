"""
SMTP Server for development:
* stories receiving emails in root directory of project
"""
from datetime import datetime
import asyncore
from smtpd import SMTPServer


class EmailServer(SMTPServer):
    """  SMTP Server for development  """

    def __init__(self, localaddr, remoteaddr):
        SMTPServer.__init__(self, localaddr, remoteaddr)
        self.number = 0

    def process_message(self, peer, mailfrom, rcpttos, data):
        """
        Saves received message to file
        """
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = '%s-%d.eml' % (now, self.number)
        email_file = open(filename, 'w')
        email_file.write(data)
        email_file.close()
        print '%s saved.' % filename
        self.number += 1


def run():
    """
    Starts SMTP development server
    """
    EmailServer(('localhost', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
