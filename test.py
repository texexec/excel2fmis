# -*- coding: utf-8 -*-
import os, time
import win32com.client as win32
import datetime
import getpass
import shutil
import pyperclip
import pandas as pd
import numpy as np

data = pd.read_excel('item.xlsx', skiprows=[0], skipfooter=1, index_col=[0], engine='openpyxl')
df0 = pd.read_excel('apt_code.xlsx', index_col=[0], engine='openpyxl')
data = df0.merge(data, on='단지코드', how='left').dropna(subset=['동-호']).reset_index(drop=True)
data.columns = data.columns.str.strip()
data['단지동호'] = data['단지구분'] + ' ' + data['동-호']
data = data[['단지동호', '처리내용', '계']]
print(data)