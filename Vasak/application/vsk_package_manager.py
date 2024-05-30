import os

class VSKPackageManager():
  def __init__(self):
    pass

  @staticmethod
  def locked():
    return os.path.exists('/var/lib/pacman/db.lck')