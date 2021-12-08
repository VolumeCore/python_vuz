import pandas as pd
from multiprocessing import Pool
from time import time
from matplotlib import pyplot as plt

url = 'data.csv'
df = pd.read_csv(url, sep = ',', encoding='cp1251')

def getResult(*args):
    sum = 0
    sumSick = 0
    for i, j in df.iterrows():
        sum = sum + j['Вылечились']
        if j['Заболели'][len(j['Заболели']) - 2] == ' ':
            j['Заболели'] = j['Заболели'][1:len(j['Заболели']) - 2]
        else:
            j['Заболели'] = j['Заболели'][1:len(j['Заболели']) - 1]
        sumSick = sumSick + int(j['Заболели'])
    return (sum, sumSick)

def testt(*args):
    sick = list(args[0])
    healthy = list(args[1])

    for i in range(len(sick)):
        if sick[i][len(sick[i]) - 2] == ' ':
            sick[i] = sick[i][1:len(sick[i]) - 2]
        else:
            sick[i] = sick[i][1:len(sick[i]) - 1]
        sick[i] = int(sick[i])

    return sum(healthy)/sum(sick)

if __name__ == '__main__':
    print('Вылечились', getResult()[0])
    print('Заболели', getResult()[1])

    sizes = []

    for i in range(2, 5):
        time0 = time()
        with Pool(i * i) as pool:
            res = pool.apply(testt, [df['Заболели'], df['Вылечились']])
        sizes.append(time() - time0)

        print(time() - time0)

    print(res)

    labels = '4', '9', '16'  # заголовки, против часовой
    explode = (0, 0, 0)  # парметры выделения кусков диаграммы

    fig1, ax1 = plt.subplots(figsize=(7, 7))
    plt.title('Диаграмма зависимости времени выполнения\n от количества процессов', fontsize=20)
    ax1.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=120)
    ax1.axis('equal')  # чтобы получился круг
    plt.show()
