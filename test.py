from tangUtils.main import Base
import os, sys

def showDetail(b: Base):
  print("\n--- test ---")
  print("path ->".rjust(13, " "), b.path)
  print("dirname ->".rjust(13, " "), b.dirname)
  print("basename ->".rjust(13, " "), b.basename)
  print("name ->".rjust(13, " "), b.name)
  print("suffix ->".rjust(13, " "), b.suffix)
  print("fakeName ->".rjust(13, " "), b.fakeName)
  print("fakeSuffix ->".rjust(13, " "), b.fakeSuffix)
  print("isFile ->".rjust(13, " "), b.isFile)
  print("isDir ->".rjust(13, " "), b.isDir)
  print("--- test ---\n")

testFilePath = __file__
testDirPath = "./"

fBase = Base(testFilePath).toAbsPath().parent

showDetail(fBase.childOf("dist").siblingOf("test.py"))
