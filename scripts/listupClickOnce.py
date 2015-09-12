#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import time

import winreg

if __name__ == '__main__':

	print("ClickOnce でインストールされたパッケージを一覧表示")

	aReg = ConnectRegistry(None, HKEY_CURRENT_USER)
	aKey = OpenKey(aReg, "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\")
	for i in range(1024):
		try:
			asubkey_name = EnumKey(aKey, i)
			asubkey = OpenKey(aKey,asubkey_name)
			val = QueryValueEx(asubkey, "DisplayName")
			print(val)
		except EnvironmentError:
			break
	CloseKey(aKey)
	CloseKey(aReg)



