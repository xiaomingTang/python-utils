from tangUtils.main import Base
import os, sys

def showDetail(b: Base):
  print("\n--- test start ---")
  print("path".ljust(10, " "), " -> ", b.path)
  print("dirname".ljust(10, " "), " -> ", b.dirname)
  print("basename".ljust(10, " "), " -> ", b.basename)
  print("name".ljust(10, " "), " -> ", b.name)
  print("suffix".ljust(10, " "), " -> ", b.suffix)
  print("fakeName".ljust(10, " "), " -> ", b.fakeName)
  print("fakeSuffix".ljust(10, " "), " -> ", b.fakeSuffix)
  print("isFile".ljust(10, " "), " -> ", b.isFile)
  print("isDir".ljust(10, " "), " -> ", b.isDir)
  print("--- test end ---\n")

testFilePath = __file__

fBase = Base(testFilePath).toAbsPath().parent

showDetail(fBase.childOf("dist").siblingOf("README.md"))
