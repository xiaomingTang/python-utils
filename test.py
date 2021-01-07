from tangUtils.main import Base, File
import os, sys
from tangUtils.mail import Email

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

# fBase = Base(testFilePath).toAbsPath().parent

# showDetail(fBase.childOf("dist").siblingOf("README.md"))

em = Email(fromAddr=("王小明", "10086@qq.com"), password="your auth code", debugLevel=0)
em.sendTo([
  ("联通", "10010@qq.com"),
  ("电信", "10000@qq.com"),
], subject="来自王小明的提醒", fallbackText="你已经接收到了来自王小明的提醒", html="""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div>您已接收到来自<strong>王小明</strong>的提示</div>
  <img src="cid:1" alt="一张图片">
</body>
</html>
""", attachment=[
  File("./README.md").toAbsPath(),
  File("/path/to/image.jpg").toAbsPath(),
])
