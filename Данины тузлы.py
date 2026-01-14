import scratchattach as sa
import os
os.system('color')
aac = 1
aae = 0
aaf = 0
from termcolor import colored
import keyboard
import time
def cl():
    for aaa in range(64):
        print()
def cl1():
    try:
        os.system(cls)
    except:
        cl()
def menugen(ilist, text):
    while keyboard.is_pressed("enter"):
        time.sleep(0)
    select = 0
    print(text)
    print()
    print(colored("используй w/s для перемещения курсора, enter для выборки",'dark_grey'))
    for aab in range(len(ilist)):
        if aab == select:
            print(colored(("> "+ilist[aab]), 'cyan'))
        else:
            print(colored((" "+ilist[aab]), 'magenta'))
    while not keyboard.is_pressed("enter"):
        if keyboard.is_pressed("s"):
            select = select + 1
            if select == len(ilist):
                select = 0
            cl1()
            print(text)
            print()
            print(colored("используй w/s для перемещения курсора, enter для выборки",'dark_grey'))
            for aab in range(len(ilist)):
                if aab == select:
                    print(colored(("> "+ilist[aab]), 'cyan'))
                else:
                    print(colored((" "+ilist[aab]), 'magenta'))
            while keyboard.is_pressed("s"):
                time.sleep(0)
        if keyboard.is_pressed("w"):
            select = select - 1
            if select < 0:
                select = len(ilist)-1
            cl1()
            print(text)
            print()
            print(colored("используй w/s для перемещения курсора, enter для выборки",'dark_grey'))
            for aab in range(len(ilist)):
                if aab == select:
                    print(colored(("> "+ilist[aab]), 'cyan'))
                else:
                    print(colored((" "+ilist[aab]), 'magenta'))
            while keyboard.is_pressed("w"):
                time.sleep(0)
    while keyboard.is_pressed("enter"):
        time.sleep(0)
    return(select+1)
while aac != 5:
    aac = menugen(["Скретч","М.Я.У. (бета)","глаз боба","О создателях","Выйти"], "DanevermasToolZ 1.0.1")
    cl1()
    if aac == 5:
        pass
    if aac == 3:
        cl1()
        print('паааатоооом сдееелаааююююю [enter]')
        while not keyboard.is_pressed("enter"):
            if keyboard.is_pressed("enter"):
                pass
    if aac == 2:
        cl1()
        print('МЯУ (Массированный ядерный удар) будет готов... ...когда-то. Следи за обновами, чтож [enter]')
        while not keyboard.is_pressed("enter"):
            if keyboard.is_pressed("enter"):
                pass
    if aac == 4:
        cl1()
        print('Приложуху создал:', colored('@MrDaneverma','cyan'),'(тг)')
        print('Спасибо', colored('TimMcCool','cyan'),'за ScratchAttach, без него раздел Скретч не работал-бы')
        print('Ещё', colored('@gervatyy','cyan'),'(тг) хотел бранчнуть и говорил жди пул реквест а в итоге где ано')
        print('Нажми ENTER что-бы выйти')
        while not keyboard.is_pressed("enter"):
            if keyboard.is_pressed("enter"):
                pass
    if aac == 1:
        cl1()
        aad = menugen(["Залогинится","Глянуть инфу о акках данивермы","Быстрое","Назад"], "Шо делать будем?")
        if aad = 3:
            cl1()
            print("Уважаемые люди, сделайте тут просмоторщик профилей, у нас тут исходный код открытый") #MrDaneverma
            while not keyboard.is_pressed("enter"):
                if keyboard.is_pressed("enter"):
                    pass
        if aad == 4:
            pass
        if aad == 2:
            cl1()
            print('У меня есть идея как это реализовать, но не сейчас, жди 1.1')
            print('(это будет костыльный костыль)')
            print('нажми ентер чтоб выйти')
            while not keyboard.is_pressed("enter"):
                if keyboard.is_pressed("enter"):
                    pass
        if aad == 1:
            while aae == 0:
                aae = 1
                cl1()
                print("Напиши ник: (ОНО СНАЧАЛО СИЛЬНО ТУПИТ НИЧЕГО НЕКОТОРОЕ ВРЕМЯ НЕ НАЖИМАЙ Я НЕ ЗНАЮ ПОЧЕМУ ОНО ТАК)")
                ni = input('>')
                print("А теперь пароль: (Я их никуда не сохраняю, можешь в коде проверить)")
                pa = input('>')
                time.sleep(2)
                try:
                    session = sa.login(str(ni), str(pa))
                except:
                    print("войти не получилосъ")
                    time.sleep(3)
                    aae = 0
            if aae == 1:
                if session.banned == False:
                    while aaf != 4:
                        aaf = menugen(["Узнать свои данные (не показывай это остальным!)","Хакнуть облачные переменные (тут есть ещё логи)","Активности на сайте","Выйти из акка и отсюда"], "Ты залогинился как "+ni+", шо хочешь на скретче сделать?")
                        if aaf == 1:
                            cl1()
                            user = session.connect_user(ni)
                            print(colored("Инфа о тебе:",'green'))
                            print("Сэшн айди:",colored(session.id,"cyan"))
                            print("Твой ник:",colored(session.username,"cyan"))
                            print("Икс-токен:",colored(session.xtoken,"cyan"))
                            print("Ты новый скретчер? (True - да, False - нет):",colored(session.new_scratcher,"cyan"))
                            print("Тебя замутили?:",colored(session.mute_status,"cyan"))
                            print("Электронная почка, на которую зареган акк:",colored(session.email,"cyan"))
                            try:
                                print("Неверифнутый емэил:",colored(session.new_email_address,"cyan"))
                            except:
                                print('У тебя',colored("нет","green"),"неверифнутого емэила")
                            print("Ты эл.почту подтвердил?:",colored(session.has_outstanding_email_confirmation,"cyan"))
                            print("Ты присоеденился:",colored(user.join_date,"cyan"))
                            print("Ты о себе:",colored(user.about_me,"cyan"))
                            print("Ты работаешь над:",colored(user.wiwo,"cyan"))
                            print("Ты новый скретчер? (True - да, False - нет):",colored(session.new_scratcher,"cyan"))
                            print("Ты откуда?:",colored(user.country,"cyan"))
                            print("Ссылка на твою аву:",colored(user.icon_url,"cyan"))
                            print("Твой айди:",colored(user.id,"cyan"))
                            print("Ты в СТ?:",colored(user.scratchteam,"cyan"))
                            while not keyboard.is_pressed("enter"):
                                if keyboard.is_pressed("enter"):
                                    pass
                else:
                    cl1()
                    print("слющай, акк",colored("забанен.",'red'))
                    print("Нажми ентер чтоб вернутся")
                    while not keyboard.is_pressed("enter"):
                        if keyboard.is_pressed("enter"):
                            ni = ""
                            pa = ""
                            pass
                    


