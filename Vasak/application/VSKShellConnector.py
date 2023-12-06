import subprocess

class VSKShellConnector():
  def __init__(self):
    pass

  @staticmethod
  def run(command, shell=False):
    proc = subprocess.Popen(command, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.communicate()