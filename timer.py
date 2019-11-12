from colorama import init
init()
from colorama import Fore, Back, Style
import winsound
import time
import datetime

# frequency = 1200  # Set Frequency To 2500 Hertz
# duration = 1000  # Set Duration To 1000 ms == 1 second
def soundbeep():
    ''' Make sound '''
    winsound.Beep(329, 300)
    winsound.Beep(392, 600)
    winsound.Beep(392, 300)
    winsound.Beep(329, 600)
    winsound.Beep(440, 300)
    winsound.Beep(392, 300)
    winsound.Beep(440, 300)
    winsound.Beep(392, 300)
    winsound.Beep(440, 300)
    winsound.Beep(392, 300)
    winsound.Beep(440, 300)
    winsound.Beep(392, 300)
    winsound.Beep(440, 300)
    winsound.Beep(392, 600)

# print("\n" * 5)

print(Fore.WHITE + Back.CYAN + '(с) 2019 ТАЙМЕР ОБРАТНОГО ОТЧЁТА 11.11.2019  ')
print(Back.CYAN + '*********************************************')
print('                _______________              ')
print('               <   ОТДОХНИ!!!  >             ')
print('                ---------------              ')
print('                       \   ^__^              ')
print('                        \  (oo)\_______      ')
print('                           (__)\       )     ')
print('                               ||----w |     ')
print(' 0 - Save Log                  ||     ||     ')
print(Back.BLUE + '---------------------------------------------')
t = int(input(' Введи количество минут: '))
task = (input('          Введи задание: '))
if task == '':
        task = 'Wokr task'
print(Back.BLUE + '---------------------------------------------')
print(Back.BLUE + Fore.YELLOW + ' Время старта     ' ,time.asctime(), " ")
t = t * 60  #time in sec
c = 0       # counter
total = 0   # counter total time


while True:
    print(Fore.WHITE + Back.RED + '\r{}'.format(time.strftime(" %H:%M:%S")),task,int((t-(int(c)+1))/60),':',(t-(int(c)+1))%60,' ', end='')
    time.sleep(1)
    c = c + 1

    if t == c:
        c = 0
        total = total + t
        print(" Таймер!!! Прошло", int(t/60),'мин.')
        soundbeep()
        #break      #выход в консоль
        #continue   #запуск по кругу
        print(Back.GREEN + Fore.WHITE + '                  Итого времени:', int(total/60),' мин.')
        t = int(input(" Введи ещё раз количество минут: "))
        if t == 0:
            logFile = open('timer.dat', 'a')
            logFile.write(time.strftime("%d-%m-%Y %H:%M") + ' - ' + str(int(total/60)) + ' \n')
            logFile.close()
            break


        t = t * 60
        task = (input('                  Введи задание: '))
        if task == '':
            task = 'Wokr task'

print(' Save log')





