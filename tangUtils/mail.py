from typing import Union, List, Tuple
from smtplib import SMTP
from email import encoders
from email.header import Header
from email.utils import formataddr

from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

Addr = Union[str, Tuple[str, str]]

def _decodeAddr(_addr: Addr) -> Tuple[str, str]:
  """
    _addr:
      str: 表示昵称和地址均为该值
      Tuple[str, str]: 等价于(name, str)
    return (name, str)
  """
  _type = type(_addr)
  if _type == str:
    name = _addr
    addr = _addr
  elif _type == tuple:
    name, addr = _addr
  else:
    raise Exception("arguments type error, accept str or Tuple[str, str], but got", _addr)
  return (name, addr)


def _formatAddr(_addr: Addr):
  name, addr = _decodeAddr(_addr)
  encodedName = Header(name, "utf-8").encode()
  return formataddr((encodedName, addr))


class Email(object):
  # 发件人昵称
  fromName: str
  # 发件人邮箱地址
  fromAddr: str
  # 发件人邮箱密码
  password: str
  # SMTP服务器地址
  smtpServer: str

  __server: SMTP

  def __init__(self, fromAddr: Addr, password: str, smtpServer: str):
    super().__init__()
    self.fromName, self.fromAddr = _decodeAddr(fromAddr)
    self.password = password
    self.smtpServer = smtpServer

  def login(self):
    self.quit()
    # SMTP协议默认端口是25
    __server = SMTP(self.smtpServer, 25)
    __server.set_debuglevel(1)
    __server.login(self.fromAddr, self.password)
    self.__server = __server
    return self

  def quit(self):
    if self.__server:
      self.__server.quit()
    return self

  def sendTo(self, toAddr: List[Addr], subject="", content=""):
    msg = MIMEMultipart("alternative")
    msg["From"] = _formatAddr((self.fromName, self.fromAddr))
    msg["To"] = ",".join([_formatAddr(item) for item in toAddr])
    msg["Subject"] = Header(subject, "utf-8").encode()

    msg.attach(MIMEText("hello", "plain", "utf-8"))
    msg.attach(MIMEText("<html><body><h1>Hello</h1></body></html>", "html", "utf-8"))

    # self.__server.sendmail(self.fromAddr, [
    #   _decodeAddr(item)[1] for item in toAddr
    # ], msg.as_string())

    print(msg.as_string())
