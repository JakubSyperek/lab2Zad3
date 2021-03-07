przedmioty = {'CAD':'CAD - komputerowe wspomaganie programowania', 'WD':'Wizualizacja danych', 'JA':'Język angielski','RRiC':'Rachunek różniczkowy i całkowy','EMD':'Elementy matematyki dyskretnej','PS':'Programowanie strukturalne'}
print(przedmioty)
ctr = sum(map(len, przedmioty.values()))
print('Liczba elementow:',ctr)