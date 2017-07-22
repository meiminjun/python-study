#!/usr/bin/env python3

i =  input('请输入你的出生年:')
age = int(i)
if age >= 1990:
  print('你是个90后')
elif age >= 1980:
  print('你是个80后')
elif age >= 1970:
  print('你是个70后的青年人')
elif age >= 1960:
  print('你是个60后的大叔')
else:
  print('你是个古人')
