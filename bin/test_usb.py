"""Test usb file
"""
from usb import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-10-2"

def test():
	"""Tests the usb function in the usb class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert usb.usb() == "usb", "test failed"
	#assert usb.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
