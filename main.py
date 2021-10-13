# Задание №1
# import zipfile
# import os

# directory_to_extract_to = '...'     #директория извлечения файлов архива
# arch_file = '...' #путь к архиву

#Создать новую директорию, в которую будет распакован архив
#С помощью модуля zipfile извлечь содержимое архива в созданную директорию

from zipfile import ZipFile
import os, hashlib, requests, re, csv

print('Задание 1')
with ZipFile('tiff-4.2.0_lab1.zip', 'r') as zipObj:
   zipObj.extractall()

print('Задание 2')
for root, dirs, files in os.walk("./tiff-4.2.0"):
    for file in files:
        if file.endswith(".txt"):
            tmp = open(os.path.join(root, file), 'rb').read()
            print(os.path.join(root, file) + '; MD5: ' + hashlib.md5(tmp).hexdigest())

print('Задание 3')
link = ''
for root, dirs, files in os.walk("./tiff-4.2.0"):
    for file in files:
        if file.endswith(".sh"):
            tmp = open(os.path.join(root, file), 'rb').read()
            if hashlib.md5(tmp).hexdigest() == '4636f9ae9fef12ebd56cd39586d33cfb':
                print(tmp)
                link = tmp

print('Задание 4')
r = requests.get(link)
result_dct ={}
counter=0

lines = re.findall(r'<div class="Table-module_row__3TH83">.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>', r.text)
for line in lines:
    # извлечение заголовков таблицы
    if counter == 0:
        # Удаление тегов
        headers = re.sub('<.*?>', ' ', line)
        # Извлечение списка заголовков
        headers = re.findall(r'Заболели|Умерли|Вылечились|Активные случаи', headers)

    # Удаление тегов
    temp = re.sub('<.*?>', ';', line)
    resultArr = list(filter(None, temp.split(';')))
    for i in range(len(resultArr)):
        if '(+' in resultArr[i]:
            resultArr[i - 1] += resultArr[i]
            resultArr[i] = ''
    resultArr = list(filter(None, resultArr))


    if resultArr[0] == 'Заболели' or resultArr[0] == '📝  ':
        continue

    resultArr[0] = resultArr[0][4::]

    f = open('data.txt', 'a', encoding='utf-8')
    f.write(resultArr[0] + '\nЗаболели: ' + resultArr[1] + '\nУмерли: ' + resultArr[2] + '\nВылечились: ' + resultArr[
            3] + '\nАктивные случаи: ' + resultArr[4] + '\n\n')
    f.close()



    result_dct[resultArr[0]] = 'Заболели: ' + resultArr[1] + 'Умерли: ' + resultArr[2] + 'Вылечились' + resultArr[3] + 'Активные случаи' + resultArr[4] + ';'

tmpp = open('data.csv', 'w', encoding='utf-16')
writer = csv.writer(tmpp)
for key, value in result_dct.items():
    writer.writerow([key, value])

tmpp.close()

chooseCountry = input('Введите страну: ')
print(result_dct[chooseCountry])