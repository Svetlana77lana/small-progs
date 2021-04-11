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
            Настройка
        View - Identation(отступ) - Convert Identation To Spaces
'''
#-----------------------------------------------------------------------------------------#
#---------                                                                       ---------#
# ---                  Работа со строками                                            -----#  
#---------                                                                           -----# 
#-----------------------------------------------------------------------------------------#

# Проверка введено ли что-то в поле e_analog (из виджета Entry библиотек tkinter)
if e_analog.get() in '<string>':

# And when looking for subsrings
any(i in '<string>' for i in ('11','22','33'))

#-----------------------------------------------------------------------------------------#
#---------                                                                       ---------#
# ---                  парсинг введеной строки - номеров в список
#---                           Например:1-3 , 5 -  6,20                               -----#  
#---------                                                                           -----# 
#-----------------------------------------------------------------------------------------#
string = "1,   4   -5,   7,   8, 10   - 22, 18"

def conv_to_list(date):  # преобразование строки в массив - убраны пробелы и разбита строка в список по ,
    conv_list = []
    date = date.replace(' ', '')  # Можно добавить спец символы, которые следует удалять
    date = date.split(',')
    for x in date:
        print(x)
        if("-" in x):  # учитывается промежуток типа: 3-8 - несколько элементов
            date_ = x.split('-')
            date_list_ = [num for num in range(int(date_[0]), int(date_[-1])+1)]
            conv_list = conv_list + date_list_
        else:
            conv_list.append(int(x))
            conv_list = list(set(conv_list))   # set - убирет повторы в списке
    return(conv_list)

print(conv_to_list(string))

#-----------------------------------------------------------------------------------------#
if len(e_analog.get()) == 0:    # e_analog.get() -  введенная строка
            l_exit_analog['text'] = "Пустой ввод" + e_analog.get() + "\nПовторите ввод!!!"
            l_exit_analog['bg'] = bg_title_blue
        else:
            exit_list = conv_to_list(e_analog.get())
            print("exit-list", exit_list)

#-----------------------------------------------------------------------------------------#
#---------                                                                       ---------#
# ---                  Работа со списками                                            -----#  
#---------                                                                           -----# 
#-----------------------------------------------------------------------------------------#
#       ф-ции   sort()   и  sorted()
lst.sort()          # lst отсортирован уже 
lst = sorted(lst)   # можно переопределять


#-----------------------------------------------------------------------------------------#
#---------                                                                       ---------#
# ---                  Работа с файлами Excel                                        -----#  
#---------                                                                           -----# 
#-----------------------------------------------------------------------------------------#

res_val_chan = pd.read_excel('leak_current.xls', sheetname = module_type)
        # print res_val_chan
        # print res_val_chan.head(5), '\n'
        # print res_val_chan.tail(12)
        # print res_val_chan.columns
        # print res_val_chan.channels_module
        # print res_val_chan[5:8]       # строки таблицы
        print res_val_chan.iloc[0,2]    # take exectly this element from 0 row and column 2
        # # print res_val_chan.describe()       # good for 64int type
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
        #   channels_sheets.append(xlsx.parse(sheet))
        #   channels = pd.concat(channels_sheets)
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
#-----------------------------------------------------------------------------------------#
#---------                                                                       ---------#
# ---                  Работа с xls и формирование из них списков                                            -----#  
#---------                                                                           -----# 
#-----------------------------------------------------------------------------------------#

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
#--------------
changes = pd.read_excel('Changes.xlsx', encoding='utf-8')
initial_list = []
final_list = []
initial_list_start = changes['initial'].tolist()
final_list_start = changes['should_be'].tolist()

for elem in initial_list_start:
    initial_list.append(elem.encode('utf-8'))
for elem in final_list_start:
    final_list.append(elem.encode('utf-8'))

#       read csv
df2 = pd.read_csv('megapolis_print.csv', sep=';') #, encoding='utf-8'
elem_name = df2['column'].tolist()

'''          запись dataframe в файл
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

#       запись списка в data frame и в excel файл
df = pd.DataFrame(output_list)
print df
file_output = 'output_' + str(random.randint(1,1000)) + '.xlsx'
df.to_excel(file_output, 'Sheet1')

    # ф-ция тестирования работы с файлами xls
def TestExcel(self, module_type='MDD'):
    res_val_chan = pd.read_excel('leak_current.xls', sheetname = module_type)
    print res_val_chan.iloc[0,2]    # take exectly this element from 0 row and column 2

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
                    #          короткие штуки
x = [i for i in xrange(10)]
y = [i*i for i in xrange(10)]
print x,y
plt.plot(x,y)
plt.show()

a = [1, 2, 3]
b = [1, 1, 1]
b = a.copy()

import pandas as pd
d = {"price":[1, 2, 3], "count": [10, 20, 30], "percent": [24, 51, 71]}

df = pd.DataFrame(d, index=['a', 'b', 'c'])
print df[df['price'] >= 2]

for i in [1, 2, 3]:
    print i

'''
            Строки
'''
for i in input_str.upper():
    if ord(i) in [35, 60, 37, 38]:      # ord - Возвращает числовое представление для указанного символа
        print "Нельзя использовтаь спец символы"
    if i == 'G' or i == 'C':
        count += 1

#-----------------------------------------------------------------------------------------#
#---------                                                                       ---------#
# ---                  Словрь - тип данных: генерация, работа с ним                  -----#  
#---------                                                                           -----# 
#-----------------------------------------------------------------------------------------#

# Вы быстро заметите, что здесь нет индекса. Что делать, если вы захотите оперировать индексом?
#  В Python вы можете воспользоваться enumerate. Это отличный способ получить доступ ко всему, что вам нужно!
for index, name in enumerate(greek_gods):
    print (f'at index {index} , we have : {name}')

#-----------------------------------------------------------------------------------------#
# dict_ex = {'1': 3, '2': 4}
# print(dict_ex.__sizeof__())
#---------------                      ГЕНЕАРЦИЯ словаря                      -------------#
dict_ex={x: 'Null'  for x in range(1, 65)}

print(dict_ex.get(1))
#               get(1) и get('1') - разные ключи!!!
print(dict_ex.get('1'))

print(dict_ex)
print(dict_ex.__sizeof__())

#   сделать два списка keyslist, valueslist - сложить их в словарь
print dict_Channel_DATA_IN_SEL.get('CH_B14')

dict_ex = {x: x*2 for x in range(100)}
print(dict_ex.get(1))
print(dict_ex.__sizeof__())

#------------------------------------------------------------------------------------------------#
#---------                                                                              ---------#
# ---               создание словаря из двух списков,    -----#  
#---------          normal_range_dict - словарь, элементами которого являются слвоари       -----# 
#------------------------------------------------------------------------------------------------#

# normal_range_dict - словарь данных по допустимым значениям поля Диапазон нормализации 
    # normal_range_dict = {analog: {'16.68':0, '' }, param: {'6':0 } }
    digit_list = [hex(i)for i in range(15)]
    
    digit_dict_analog = {}
    digit_dict_param = {}
    
    analog_list = ['16.68', '33.36' ]
    param_list = ['6', '12', '18', '24', '30', '36', '48', '60', '78', '96', '160', '300', '500', '1200', '2000']

    digit_dict_analog = dict(zip(digit_list, analog_list))  # создание словаря из двух списков
    digit_dict_param = dict(zip(digit_list, param_list))
    # print(digit_list)
    print(digit_dict_analog)
    print(digit_dict_param)
    normal_range_dict = {'analog': digit_dict_analog, 'param': digit_dict_param}
    # print(normal_range_dict)

#------------------------------------------------------------------------------------------------#
#---------                                                                              ---------#
# ---               пример структыры СЛОВАРЯ словаря - элементом словоря является словарь   -----#  
#---------                                                                                  -----# 
#------------------------------------------------------------------------------------------------#

type_and_shift = {x: {'sensor_type_val': 'Null', 'sensor_type_check': 'Null',\
              'sensor_shift_val': 'Null', 'sensor_shift_text_dimention': 'Null'}  for x in range(1, 65)}

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
temp |= 0x10    # 
ch_adc = 0b010
dev_adc = 0x10

print bin(temp), "\n"   
temp &= 0xFFFFFF8F  # принудительное обнуление бит, где 0 справа
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

        # дробное деление
Python2: 4 / 20 # = 0 или  20 / 3 = 6 
Python3: 
print float(4) / 20 # = 0.2 исправление для Python2


print '4',
print 'vot' # 4 vot

'''
        

            Кооментраии - фурмулирровка  


'''

 voltage_type - тип подаваемого напряжения
filt - включение, выключение медианного фильтра. При включении фильтра повышается точность измерения, но увеличивается время измерения канала.

        'on'  --- включение фильтра

        'off' --- выключение фильтра


channel_name_list - список измеряемых каналов, задается в виде ['CH_A1', 'CH_D1'.......]. Будут измерены токи утечек каналов находящихся в списке.
 
                Параметр активируется только при ch_sel = 'same'.
 
    channel_name - выбор типа подключенного модуля для измерения тока утечки.
 
            'mdd' --- проверка каналов модуля МДД
#------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------#
#---------                                                                       ---------#
#---                    ФУНКЦИИ, СВЯЗАННЫЕ С АНАЛИЗОМ БУФЕРА КИИМ                      ---#
#---------
#-------------------------------------               -------------------------------------#
#-----------------------------------------------------------------------------------------#
