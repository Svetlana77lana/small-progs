# -*- coding: utf-8 -*-

import cyrtranslit
import csv
import sys

##################### Настройка скрипта под конкретный BOM #################################

translate_colums = [1,2,3] # номера столбцов для перевода через запятую (PREFIX, PE3_NAME,  
                           # DESC, MANUFACTURE и т.д.), нумерация с нуля

pe3name_col = 2 # номер столбца содержащего PE3_NAME
partnum_col = 0 # номер столбца содержащего PART_NUMBER
prefix_col  = 1 # номер столбца содержащего PREFIX
desc_col    = 3 # номер столбца содержащего DESC

join_desc   = 1 # 0 - не объединять столбцы DESC и PE3_NAME(PART_NUMBER)
                # 1 -    объединять столбцы DESC и PE3_NAME(PART_NUMBER)

############################################################################################

# Удаление пустых строк из исходного BOM файла

source_bom_file = open('.\\BOM.rpt', 'r')
temp_bom_file = open('BOM_mod.rpt', 'w')
temp = source_bom_file.readlines()
temp.remove('\n')
temp_bom_file.writelines(temp)
temp_bom_file.close()
source_bom_file.close()

# Открытие файлов

rus_bom_file = open('.\\BOM_rus.csv', 'w')
source_bom_file = open('.\\BOM_mod.rpt', 'r')

csv_str = 0

try:
    reader = csv.reader(source_bom_file, delimiter=';')
    writer = csv.writer(rus_bom_file, delimiter=';')
    row_num = 0
    for row in reader:
        
        csv_str = row
        col_num = 0
        row_num = row_num + 1

        while col_num < len(csv_str):
            if col_num in translate_colums:
                if (col_num == pe3name_col):
                    if (csv_str[col_num] != "-"):
                        csv_str[col_num] = cyrtranslit.to_cyrillic(csv_str[col_num].encode("utf-8"), 'ru')
                    else:
                        csv_str[col_num] = csv_str[partnum_col]
                else:
                    csv_str[col_num] = cyrtranslit.to_cyrillic(csv_str[col_num].encode("utf-8"), 'ru')
            col_num = col_num + 1

        if (len(csv_str[prefix_col])==1): csv_str[prefix_col] = ''
        if (len(csv_str[partnum_col])==1): csv_str[partnum_col] = ''
        if (len(csv_str[desc_col])==1): csv_str[desc_col] = ''

        prefix_value     = csv_str[prefix_col]
        partnumber_value = csv_str[partnum_col]
        pe3name_value    = csv_str[pe3name_col]
        desc_value       = csv_str[desc_col]

        csv_str[pe3name_col] = csv_str[prefix_col] + ' ' + csv_str[pe3name_col]

        if (join_desc==1):
            csv_str[pe3name_col] = csv_str[pe3name_col] + ' ' + csv_str[desc_col]

        csv_str.remove(partnumber_value)
        csv_str.remove(prefix_value)
        csv_str.remove(desc_value)

        writer.writerow(csv_str)

        # print "row_num = ", row_num, "\n"        
        # print (csv_str)
finally:
    source_bom_file.close()
    rus_bom_file.close()
