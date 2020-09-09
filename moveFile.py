import os
import time
from directories import folderDestination as fD, folderSource as fS

def move():
  for filename in os.listdir(fS): #for every data in source folder
    src = fS + "/" + filename #select the source file
    des = fD + "/" + filename #select the destination file
    os.rename(src, des) #copy from source to destination

def main():
  for filename in os.listdir(fS): #for every data in source folder
    src = fS + "/" + filename #select the source file
    des = fD + "/" + filename #select the destination file
    os.rename(src, des) #copy from source to destination

if __name__ == "__main__":
  try:
    while True:
      main()
      time.sleep(3)
  except KeyboardInterrupt:
    pass