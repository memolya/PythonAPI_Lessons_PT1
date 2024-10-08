# Режимы доступа, доступные для open() функции, следующие:
#
# r: Открывает файл в режиме только для чтения. Начинает чтение с начала файла и является режимом по умолчанию для open() функции.
# rb: Открывает файл как доступный только для чтения в двоичном формате и начинает чтение с начала файла. Хотя двоичный формат может использоваться для разных целей, он обычно используется при работе с такими вещами, как изображения, видео и т.д.
# r+: Открывает файл для чтения и записи, помещая указатель в начало файла.
# w: Открывается в режиме только для записи. Указатель помещается в начало файла, и это перезапишет любой существующий файл с тем же именем. Он создаст новый файл, если файл с таким же именем не существует.
# wb: Открывает файл, доступный только для записи, в двоичном режиме.
# w+: Открывает файл для записи и чтения.
# wb+: Открывает файл для записи и чтения в двоичном режиме.
# a: Открывает файл для добавления в него новой информации. Указатель размещается в конце файла. Новый файл создается, если файл с таким же именем не существует.
# ab: Открывает файл для добавления в двоичном режиме.
# a+: Открывает файл как для добавления, так и для чтения.
# ab+: Открывает файл как для добавления, так и для чтения в двоичном режиме.

# a - add, запись новых данных в конец файла
# w - write, запись новых данных с удалением старых
# r - read

# add

# var = input('Enter something: ')
# fw = open('doc/file.txt', 'a') #a - (add) - открытие файла и дозапись в его конец
# fw.write(var+'\n')
# # fw.write('\n') #new line
# fw.close()


#write

# # var = input('Enter something: ')
# fw = open('doc/file_2.txt', 'w')
# fw.write('meow')
# fw.close()

#read

fr = open('doc/file.txt', 'r')
text = fr.read()
print(text)