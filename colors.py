class ansi:
  # clear all ansi escape sequences
  def clear(): return "\x1b[0m\033[0m "
  # text-color functions to return ANSI escape codes for text color
  def tblack():  return 30
  def tred():  return 31
  def tgreen():  return 32
  def tyellow():  return 33
  def tblue():  return 34
  def tpurple():   return 35
  def tcyan():   return 36
  def twhite():   return 37
  # text-style functions to return ANSI escape codes for text style
  def bold():  return 1
  def underl():  return 2
  def nostyle():  return 0
  def negative1():  return 3
  def negative2():  return 5
  # background color functions to return ANSI escape codes for background color
  def bblack():  return "40m"
  def bred():  return "41m"
  def bgreen():  return "42m"
  def byellow():  return "43m"
  def bblue():  return "44m"
  def bpurple():  return "45m"
  def bcyan():  return "46m"
  def bwhite():  return "47m"
  
