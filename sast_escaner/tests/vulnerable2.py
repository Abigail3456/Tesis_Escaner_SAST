import os
import subprocess

os.system("dir")

subprocess.run("dir", shell=True)

subprocess.call("dir", shell=True)

subprocess.Popen("dir", shell=True)