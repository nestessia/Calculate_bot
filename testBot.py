import telebot
from telebot import types
from math import sin

bot = telebot.TeleBot('2057128145:AAEpkSui9DUH5z0TqagLouwZlKFI0vYSKRU')


# Команда /start 
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, 'Привет! Я бот студентов РГПУ им. Герцена :) Я решаю задание для лабораторной работы по дисциплине Вычислителная математика✌️ ')
    bot.send_message(m.chat.id, 'Мои команды:\n/start для запуска бота\n/info для уточнения информации о нас\n/integral для вычисления интеграла x*x+5*x+3 разными способами\n/elementary для вычисления элементарных функций e^x и sin(x), а так же вычисление элементарной функции 1/sqrt(x) методом итераций ')

    
@bot.message_handler(commands=["info"])
def info(m):
    bot.send_message(m.chat.id, 'Создатели: Стецук Максим, Крючкова Анастасия, Зухир Амира и Каргополов Денис из группы ИВТ 2-1. ')
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Максим", url='https://vk.com/makstulenchik')
    item2 = types.InlineKeyboardButton("Анастасия", url='https://vk.com/nestessia')
    item3 = types.InlineKeyboardButton("Амира", url='https://vk.com/amirazhr')
    item4 = types.InlineKeyboardButton("Денис", url='https://vk.com/lilexhausted')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(m.chat.id, "{0.first_name}, для связи с нами переходи по ссылкам ⬇".format(m.from_user), reply_markup=markup)
     
# Команда /integral
@bot.message_handler(commands=["integral"])
def integral(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Постоянный шаг")
    item2 = types.KeyboardButton("Переменный шаг")
    item3 = types.KeyboardButton("Кратный интеграл")
    markup.add(item1, item2,item3)
    bot.send_message(m.chat.id, text="{0.first_name}, какой cпособ тебя интересует? ".format(m.from_user), reply_markup=markup)

# Команда /elementary
@bot.message_handler(commands=["elementary"])
def elementary(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Вычисление элементарной функции")
    item2 = types.KeyboardButton("Вычисление элементарной функции методом итераций")
    markup.add(item1, item2)
    bot.send_message(m.chat.id, text="{0.first_name}, что именно тебя интересует? ".format(m.from_user), reply_markup=markup)

#Выбор метода вычислений для элементарной функции
@bot.message_handler(content_types=['text'])
def elementary_method(m):
    if(m.text == "Вычисление элементарной функции"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("e^x")
        item2 = types.KeyboardButton("sin(x)")
        markup.add(item1, item2)
        bot.send_message(m.chat.id, text="Какое выражение тебя интересует?".format(m.from_user), reply_markup=markup) 
    elif(m.text == "e^x"):
        bot.send_message(m.chat.id, 'Изначальные данные для выражения:\nТочность:2*10^-7\nЗначения для а: a0 = 0.9999998; a1 = 1.000000; a2 = 0.5000063; a3 = 0.1666674; a4 = 0.0416350; a5 = 0.0083298; a6 = 0.0014393; a7 = 0.0002040')


    
#Выбор метода вычислений для интеграла
@bot.message_handler(content_types=['text'])
def integral_method(m):
    if(m.text == "Постоянный шаг"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Метод левых частей")
        item2 = types.KeyboardButton("Метод правых частей")
        item3 = types.KeyboardButton("Метод Симпсона")
        item4 = types.KeyboardButton("Метод трапеций")
        item5 = types.KeyboardButton("Назад")
        markup.add(item1, item2,item3,item4,item5)
        bot.send_message(m.chat.id, text="Какой метод тебя интересует?".format(m.from_user), reply_markup=markup)     
    elif(m.text == "Переменный шаг"):   
        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        item1 = types.KeyboardButton("Двойной пересчёт алгоритм 1")
        item2 = types.KeyboardButton("Двойной пересчёт алгоритм 2")
        item3 = types.KeyboardButton("Назад")
        markup.add(item1, item2, item3)
        bot.send_message(m.chat.id, text="Выберите алгоритм:".format(m.from_user), reply_markup=markup)   
    elif(m.text == "Кратный интеграл"):
        bot.reply_to(m, 'Введите количество разбиений по x')
        bot.register_next_step_handler(m, get_nx)
    elif(m.text == "Метод левых частей"):
        bot.reply_to(m, 'Введи количество разбиений')
        bot.register_next_step_handler(m, get_n_for_left)
    elif(m.text == "Метод правых частей"):
        bot.reply_to(m, 'Введи количество разбиений')
        bot.register_next_step_handler(m, get_n_for_right)
    elif(m.text == "Метод Симпсона"):
        bot.reply_to(m, 'Введи количество разбиений')
        bot.register_next_step_handler(m, get_n_for_parabola)
    elif(m.text == "Метод трапеций"):
        bot.reply_to(m, 'Введи количество разбиений')
        bot.register_next_step_handler(m, get_n_for_trapecia)
    elif(m.text == "Двойной пересчёт алгоритм 1"):
        bot.reply_to(m, 'Введи точность')
        bot.register_next_step_handler(m, get_e_for_recalc1)
    elif(m.text == "Двойной пересчёт алгоритм 2"):
        bot.reply_to(m, 'Введи количество разбиений')
        bot.register_next_step_handler(m, get_e_for_recalc2)    
    elif(m.text == "Назад"):
        return integral(m)




user_e = ''
user_a = ''
user_b = ''
user_c = ''
user_d = ''
user_n = ''
user_nx = ''
user_ny = ''

#Вычисления интеграла
def task(x):
    return x*x+5*x+3 
   
#Для Метода левых прямоугольников   
def get_n_for_left(m,user_result = None):
    try:
        global user_n
        if user_result == None:
            user_n = int(m.text)
        else: 
            user_n = str(user_result)
        bot.send_message(m.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(m, get_a_for_left)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Попробуйте заново. ')      
    
def get_a_for_left(m):
    try:
        global user_a
        user_a = float(m.text)
        bot.send_message(m.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(m, get_b_for_left)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так...  Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 

def get_b_for_left(m):
    try:
        global user_b
        user_b = float(m.text)
        resultPrint_for_left(m)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
    
def left():    
    global user_a, user_b, user_n, user_result
    h = (user_b - user_a) / user_n
    x = user_a
    user_result = 0
    while x <= (user_b - h):
        user_result += task(x)
        x += h
    return h * user_result
    
def resultPrint_for_left(m):
    global user_a, user_b, user_n, user_result
    res = left()
    bot.send_message(m.chat.id, "Результат: " + (str(res)))   



#Для Метода правых прямоугольников
def get_n_for_right(m,user_result = None):
    try:
        global user_n
        
        if user_result == None:
            user_n = int(m.text)
        else: 
            user_n = str(user_result)
        bot.send_message(m.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(m, get_a_for_right)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Попробуйте заново.')

def get_a_for_right(m):
    try:
        global user_a
        user_a = float(m.text)
        bot.send_message(m.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(m, get_b_for_right)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  

def get_b_for_right(m):
    try:
        global user_b
        user_b = float(m.text)
        resultPrint_for_right(m)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
    
def right():
    global user_a, user_b, user_n, user_result  
    h = (user_b - user_a) / user_n
    x = user_a + h
    result = 0
    while x <= user_b:
        result += task(x)
        x += h
    return h * result
    
def resultPrint_for_right(m):
    global user_a, user_b, user_n, user_result
    res = right()
    bot.send_message(m.chat.id, "Результат: " + (str(res)))
    
    
    
#Для Метода трапеции
def get_n_for_trapecia(m,user_result = None):
    try:
        global user_n
        
        if user_result == None:
            user_n = int(m.text)
        else: 
            user_n = str(user_result)
        bot.send_message(m.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(m, get_a_for_trapecia)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Попробуйте заново.')

def get_a_for_trapecia(m):
    try:
        global user_a
        user_a = float(m.text)
        bot.send_message(m.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(m, get_b_for_trapecia)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  

def get_b_for_trapecia(m):
    try:
        global user_b
        user_b = float(m.text)
        resultPrint_for_trapecia(m)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
    
def trapecia():
    global user_a, user_b, user_n, user_result  
    h = (user_b - user_a) / user_n
    x = user_a + h
    result = 0
    while x <= (user_b - h):
        result += task(x)
        x += h
    return ((task(user_a) + task(user_b)) / 2 + result) * h
    
def resultPrint_for_trapecia(m):
    global user_a, user_b, user_n, user_result
    res = trapecia()
    bot.send_message(m.chat.id, "Результат: " + (str(res)))
    
    
    
#Для Метода парабол
def get_n_for_parabola(m,user_result = None):
    try:
        global user_n
        
        if user_result == None:
            user_n = int(m.text)
        else: 
            user_n = str(user_result)
        bot.send_message(m.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(m, get_a_for_parabola)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так...  Вы точно ввели число? Попробуйте заново.')

def get_a_for_parabola(m):
    try:
        global user_a
        user_a = float(m.text)
        bot.send_message(m.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(m, get_b_for_parabola)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  

def get_b_for_parabola(m):
    try:
        global user_b
        user_b = float(m.text)
        resultPrint_for_parabola(m)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
    
def parabola():
    global user_a, user_b, user_n, user_result  
    h = (user_b - user_a) / user_n
    S1 = 0
    x = user_a + h
    while x <= (user_b - h):
        S1 += task(x)
        x += 2 * h
    S2 = 0
    x = user_a + (2 * h)
    while x <= (user_b - (2 * h)):
        S2 += task(x)
        x += 2 * h
    return (task(user_a) + task(user_b) + (4 * S1) + (2 * S2)) * (h / 3)
    
def resultPrint_for_parabola(m):
    global user_a, user_b, user_n, user_result
    res = parabola()
    bot.send_message(m.chat.id, "Результат: " + (str(res)))   
    
    
     
#Для кратного интеграла   
def get_nx(m,user_result = None):
    try:
        global user_nx
        
        if user_result == None:
            user_nx = float(m.text)
        else: 
            user_nx = str(user_result)
        bot.send_message(m.chat.id, text='Введите количество разбиений по y')
        bot.register_next_step_handler(m, get_ny)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')    
    
def get_ny(m):
    try:
        global user_ny
        user_ny = float(m.text)
        bot.send_message(m.chat.id, text='Введите внешнюю нижнюю границу')
        bot.register_next_step_handler(m, get_a)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        
def get_a(m):
    try:
        global user_a
        user_a = float(m.text)
        bot.send_message(m.chat.id, text='Введите внешнюю верхнюю границу')
        bot.register_next_step_handler(m, get_b)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')        
        
def get_b(m):
    try:
        global user_b
        user_b = float(m.text)
        bot.send_message(m.chat.id, text='Введите внутреннюю нижнюю границу')
        bot.register_next_step_handler(m, get_c)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')        
        
def get_c(m):
    try:
        global user_c
        user_c = float(m.text)
        bot.send_message(m.chat.id, text='Введите внутреннюю верхнюю границу')
        bot.register_next_step_handler(m, get_d)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        
def get_d(m):
    try:
        global user_d
        user_d = float(m.text)
        resultPrint_for_KratInt(m)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')       
               
def KratInt(x,y):
    return sin(x+y)        
        
def calc_kratniy():
    global user_nx, user_ny, user_a, user_b, user_c, user_d
    hx = (user_b - user_a) / user_nx
    hy = (user_d - user_c) / user_ny
    S = 0
    x = user_a
    while x <= (user_b - hx):
        y = user_c
        while y <= (user_d - hy):
            S += KratInt(x, y)
            y += hy
        x += hx
    return S*hx*hy        
        
def resultPrint_for_KratInt(m):
    global user_nx, user_ny, user_a, user_b, user_c, user_d, user_result
    res = calc_kratniy()
    bot.send_message(m.chat.id, "Результат: " + (str(res)))        
        
        
 
#Двойной перерасчет 1         
def get_e_for_recalc1(m,user_result = None):
    try:
        global user_e
        if user_result == None:
            user_e = float(m.text)
        else: 
            user_e = str(user_result)
        bot.send_message(m.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(m, get_a_for_recalc1)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново. ')      
    
def get_a_for_recalc1(m):
    try:
        global user_a
        user_a = float(m.text)
        bot.send_message(m.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(m, get_b_for_recalc1)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  

def get_b_for_recalc1(m):
    try:
        global user_b
        user_b = float(m.text)
        resultPrint_for_recalc1(m)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        
    
    
def doubleRecalc(user_e,user_a, user_b ):
    n = 2
    f1 = 0
    f2 = left_for_recalc(n, user_a, user_b)
    while abs(f1-f2) > user_e:
        f1 = f2
        n = n * 2
        f2 = left_for_recalc(n, user_a, user_b)
    return f2 

def left_for_recalc(n, user_a, user_b):   
    h = (user_b - user_a) / n
    x = user_a
    user_result = 0
    while x <= (user_b - h):
        user_result += task(x)
        x += h
    return h * user_result
       
def resultPrint_for_recalc1(m):
    res = doubleRecalc(user_e,user_a, user_b)
    bot.send_message(m.chat.id, "Результат: " + (str(res)))    
    
   

#Двойной перерасчет 2   
def get_e_for_recalc2(m,user_result = None):
    try:
        global user_e
        if user_result == None:
            user_e = float(m.text)
        else: 
            user_e = str(user_result)
        bot.send_message(m.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(m, get_a_for_recalc2)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Скорее всего, вы ввели не число. Попробуйте заново ')      
    
def get_a_for_recalc2(m):
    try:
        global user_a
        user_a = float(m.text)
        bot.send_message(m.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(m, get_b_for_recalc2)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  

def get_b_for_recalc2(m):
    try:
        global user_b
        user_b = float(m.text)
        resultPrint_for_recalc2(m)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        
def doubleRecalcBetter(user_e,user_a, user_b):
    n = 2
    otst = (user_b - user_a)/2
    f1 = left_for_recalc(n, user_a, user_b)
    otst = otst / 2
    f2 = left_for_recalc(n, user_a + otst, user_b)
    while abs(f1-f2) > user_e:
        f1 = f2
        n = n * 2
        otst = otst / 2
        f2 = left_for_recalc(n, user_a+otst, user_b)
    return f2   

def resultPrint_for_recalc2(m):
    res = doubleRecalcBetter(user_e,user_a, user_b)
    bot.send_message(m.chat.id, "Результат: " + (str(res)))  
                      
# Запуск бота
bot.polling(none_stop=True, interval=0)