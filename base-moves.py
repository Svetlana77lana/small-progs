# -*- coding: utf-8 -*-
import sys
import yaml
import numpy as np
import bitstring
from bitstring import *
from time import strftime,sleep
from datetime import datetime
import matplotlib.pyplot as plt

'''
		Работа с файлами Excel
'''
res_val_chan = pd.read_excel('leak_current.xls', sheetname = module_type)
		# print res_val_chan
		# print res_val_chan.head(5), '\n'
		# print res_val_chan.tail(12)
		# print res_val_chan.columns
		# print res_val_chan.channels_module
		# print res_val_chan[5:8]
		print res_val_chan.iloc[0,2]	# take exectly this element from 0 row and column 2
		# # print res_val_chan.describe()		# good for 64int type
		# list_chan_MPM_first = res_val_chan['channels_MPM'].tolist()
		# print res_val_chan[0:6]
		# df1 = pd.read_excel('leak_current.xls', sheetname = 'MDD', index_col=1)
		# print df1.head(6)
		# df2 = pd.read_excel('leak_current.xls', sheetname = 'MAD')
		# print pd.merge(df1, df2, on='channels_MPM')

# Using the ExcelFile class to read multiple sheets
		# xlsx = pd.ExcelFile('leak_current.xls')
		# channels_sheets = []
		# for sheet in xlsx.sheet_names:
		# 	channels_sheets.append(xlsx.parse(sheet))
		# 	channels = pd.concat(channels_sheets)
		# print channels_sheets

		# res_val_chan = pd.read_excel('leak_current.xls', sheetname = module_type)
		# res_val_chan.iloc[0,2] = 6
		# print res_val_chan.iloc[0,2]
		now_time = datetime.now()
		# file_output = 'output_' + strftime("%d_%b_%Y_%H:%M:%S") + '.xlsx'
		file_output = 'output.xls'
		# writer = pd.ExcelWriter()
		# dict_LeakCurrent = [('CH_A1', None), ('CH_B1', None), ('CH_C1', None)]
		dict_LeakCurrent = {'CH_A8': 1, 'CH_A9': 1, 'CH_A2': 1, 'CH_A3': 1, 'CH_A1': 1}
		df = pd.DataFrame.from_records(dict_LeakCurrent, index=[0]) # , columns=dict_LeakCurrent.keys()
		print type(dict_LeakCurrent)
		print df
		df.to_excel('output.xls', 'Sheet1')
		
		# writer.save()


		'''
		df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])
		print df1
		df1.to_excel(file_output, sheet_name = 'Sheet2')

		with pd.ExcelWriter('output.xls',
                    mode='a') as writer:  
			df1.to_excel(writer, sheet_name='Sheet_name_2')
		'''
'''
		Работа с xls и формирование из них списков
'''
res_val_chan = pd.read_excel('leak_current.xls', sheetname = module_type)
list_chan_MPM = res_val_chan['channels_MPM'].tolist()

new_list = []
for i in range(len(list_chan_module)):
	str = ''.join(list_chan_module[i])
	temp = str.split(', ')
	new_list.extend(temp)
print new_list

# считывание из xls  файла - преобразовывание сбитой кодировки
list_chan_MPM.append(temp.encode('utf-8'))

''' запись dataframe в файл
	data - формирование словаря из списков, формата название 'колонки':список(значения колонки)
	dataframe  - формируется ф-цией pd.DataFrame
	file_output - названее файла, состоящее из даты и времени


'''
data = {'КАНАЛ МПМ':list_chan_MPM, 'Ток утечки, ' + izm_ed: dict_LeakCurrent.values(), 'Канал модуля ' + module_type: self.dict_chan.values()}
print ('-------------------------------------------------------------------------------------------------------------')
all_ch_data = pd.DataFrame(data, columns = ['КАНАЛ МПМ', 'Ток утечки, ' + izm_ed, 'Канал модуля ' + module_type])
pd.set_option('display.max_rows', 160)

file_output = "output_" + strftime("%d_%b_%Y_%H_%M_%S") + ".xlsx"

all_ch_data.to_excel("init/" + file_output, module_type, engine='openpyxl')

	# ф-ция тестирования работы с файлами xls
def TestExcel(self, module_type='MDD'):
	res_val_chan = pd.read_excel('leak_current.xls', sheetname = module_type)
	print res_val_chan.iloc[0,2]	# take exectly this element from 0 row and column 2

	# res_val_chan = pd.read_excel('leak_current.xls', sheetname = module_type)
	# res_val_chan.iloc[0,2] = 6
	# print res_val_chan.iloc[0,2]
	file_output = 'output.xls'
	# writer = pd.ExcelWriter()
	# dict_LeakCurrent = [('CH_A1', None), ('CH_B1', None), ('CH_C1', None)]
	dict_LeakCurrent = {'CH_A8': 1, 'CH_A9': 1, 'C H_A2': 1, 'CH_A3': 1, 'CH_A1': 1}
	df = pd.DataFrame.from_records(dict_LeakCurrent, index=[0]) # , columns=dict_LeakCurrent.keys()
	print type(dict_LeakCurrent)
	print df
	df.to_excel('output.xls', 'Sheet1')

	now_time = datetime.now()
	file_output = 'output_' + strftime("%d_%b_%Y_%H:%M:%S") + '.xlsx'
	
	return True
''' ------------------------------------------------------------------------------------------'''
#	короткие штуки
x = [i for i in xrange(10)]
y = [i*i for i in xrange(10)]
print x,y
plt.plot(x,y)
plt.show()

a = [1, 2, 3]
b = [1, 1, 1]
b = a.copy()

'''
		Решение проблеммы: unindent does not match any outer indentation level
		For Sublime Text users:

Set Sublime Text to use tabs for indentation: View --> Indentation --> Convert Indentation to Tabs

Uncheck the Indent Using Spaces option as well in the same sub-menu above. This will immediately resolve this issue.
'''


'''
	Операции с битовыми числами
'''
temp = 0xFFFFFFFF
temp |= 0x10	# 
ch_adc = 0b010
dev_adc = 0x10

print bin(temp), "\n"	
temp &= 0xFFFFFF8F	# принудительное обнуление бит, где 0 справа
print bin(temp)
temp |= ch_adc
# if dev_adc != 0:
#     temp &= (dev_adc<<20)
print bin(temp)
temp &= 0xE00FFFFF
print bin(temp)
# a = dev_adc<<20
# print bin(a)
temp |= (dev_adc<<20)
print bin(dev_adc)
print bin(temp)

'''
	Различия Python2 и Python3
'''
Python2: print "The answer is", 2*2
Python3: print("The answer is", 2*2)

Python2: print x,           # Запятая в конце подавляет перевод строки
Python3: print(x, end=" ")  # Добавляет пробел вместо перевода строки

Python2: print              # Печатает перевод строки
Python3: print()            # Нужно вызвать функцию!

print '4',
print 'vot'	# 4 vot
