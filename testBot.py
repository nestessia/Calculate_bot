import telebot
from telebot import types
from math import sin

bot = telebot.TeleBot('2057128145:AAEpkSui9DUH5z0TqagLouwZlKFI0vYSKRU')


@bot.message_handler(commands=['start'])
def start(message):
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Поехали!")
    key.add(item1)
    bot.send_message(message.chat.id, "Привет! Я бот студентов РГПУ им. Герцена :) Я решаю задание для лабораторной работы по дисциплине Вычислителная математика✌️")
    bot.send_message(message.chat.id, 'Жми "Поехали!" для начала вычислений', reply_markup=key)
    bot.register_next_step_handler(message, keyboard)

def keyboard(message):
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("Численное интегрирование")
    item2 = types.KeyboardButton("Вычисление элементарной функции")
    item3 = types.KeyboardButton("Численное решение ДУ")
    key.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Какая тема вас интересует?",reply_markup=key)
    bot.register_next_step_handler(message, process)

@bot.message_handler(commands=["info"])
def info(m):
    bot.send_message(m.chat.id, 'Создатели: Стецук Максим, Крючкова Анастасия, Зухир Амира и Каргополов Денис из группы ИВТ 2-1. ')
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Максим", url='https://vk.com/makstulenchik')
    item2 = types.InlineKeyboardButton("Анастасия", url='https://vk.com/nestessia')
    item3 = types.InlineKeyboardButton("Амира", url='https://vk.com/amirazhr')
    item4 = types.InlineKeyboardButton("Денис", url='https://vk.com/lilexhausted')
    markup.add(item1, item2, item3, item4)
    bot.send_message(m.chat.id, "{0.first_name}, для связи с нами переходите по ссылкам ⬇".format(m.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=["text"])
def process(message):
    if message.text == "Численное интегрирование":
        integral(message)
    elif message.text == "Вычисление элементарной функции":
        elementary_fun(message)
    elif message.text == "Численное решение ДУ":
        dif(message)

def integral(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Постоянный шаг")
    item2 = types.KeyboardButton("Переменный шаг")
    item3 = types.KeyboardButton("Кратный интеграл")
    item4 = types.KeyboardButton("Назад")
    markup.add(item1, item2,item3, item4)
    bot.send_message(message.chat.id, text="{0.first_name}, какой cпособ тебя интересует? ".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, type_integral)
    
@bot.message_handler(content_types=["text"])
def type_integral(message):
    if message.text == "Постоянный шаг":
        constant_step(message)
    elif message.text == "Переменный шаг":
        variable_step(message)
    elif message.text == "Кратный интеграл":
        bot.send_message(message.chat.id, 'Введите количество разбиений по x')
        bot.register_next_step_handler(message, get_nx)  
    elif message.text == "Назад":
        keyboard(message)
        
def constant_step(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    item1 = types.KeyboardButton("Метод левых прямоугольников")
    item2 = types.KeyboardButton("Метод правых прямоугольников")
    item3 = types.KeyboardButton("Метод Симпсона(парабол)")
    item4 = types.KeyboardButton("Метод трапеций")
    item5 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, text="{0.first_name}, каким методом пользоваться? ".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, method_integral1)

def variable_step(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    item1 = types.KeyboardButton("Двойной пересчёт алгоритм 1")
    item2 = types.KeyboardButton("Двойной пересчёт алгоритм 2")
    item3 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, text="{0.first_name}, что именно тебя интересует? ".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, method_integral2)
               
@bot.message_handler(content_types=["text"])
def method_integral1(message):
    if message.text == "Метод левых прямоугольников":
        bot.send_message(message.chat.id, 'Введите количество разбиений')
        bot.register_next_step_handler(message, get_n_for_left)
    elif message.text == "Метод правых прямоугольников":
        bot.send_message(message.chat.id, 'Введите количество разбиений')
        bot.register_next_step_handler(message, get_n_for_right)   
    elif message.text == "Метод Симпсона(парабол)":
        bot.send_message(message.chat.id, 'Введите количество разбиений')
        bot.register_next_step_handler(message, get_n_for_parabola)        
    elif message.text == "Метод трапеций":
        bot.send_message(message.chat.id, 'Введите количество разбиений')
        bot.register_next_step_handler(message, get_n_for_trapecia)        
    elif message.text == "Назад":
        integral(message)
            
@bot.message_handler(content_types=["text"])
def method_integral2(message):
    if message.text == "Двойной пересчёт алгоритм 1":
        bot.send_message(message.chat.id, 'Введите точность')
        bot.register_next_step_handler(message, get_e_for_recalc1)
    elif message.text == "Двойной пересчёт алгоритм 2":
        bot.send_message(message.chat.id, 'Введите количество разбиений')
        bot.register_next_step_handler(message, get_e_for_recalc2)         
    elif message.text == "Назад":
        integral(message)
        
def elementary_fun(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    item1 = types.KeyboardButton("Вычисление элементарной функции")
    item2 = types.KeyboardButton("Вычисление элементарной функции методом итераций")
    item3 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, text="{0.first_name}, как будем вычислять? ".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, method_elementary_fun)
    
@bot.message_handler(content_types=["text"])
def method_elementary_fun(message):
    if message.text == "Вычисление элементарной функции":
        elementary_method1(message)  
    elif message.text == "Вычисление элементарной функции методом итераций":
        elementary_method2(message) 
    elif message.text == "Назад":
        keyboard(message)
        
def elementary_method1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("e^x")
    item2 = types.KeyboardButton("sin(x)")
    item3 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, text="Какое выражение тебя интересует?".format(message.from_user), reply_markup=markup) 
    bot.send_photo(message.chat.id, "https://github.com/nestessia/hepls/blob/main/ex.png?raw=true")
    bot.send_photo(message.chat.id, "https://github.com/nestessia/hepls/blob/main/sinx.png?raw=true")        
    bot.register_next_step_handler(message, which_elementary_fun1)

def elementary_method2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("sqrt(x)")
    item2 = types.KeyboardButton("1/sqrt(x)")
    item3 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, text="Какое выражение тебя интересует?".format(message.from_user), reply_markup=markup) 
    bot.send_photo(message.chat.id, "https://github.com/nestessia/hepls/blob/main/iter_2.png?raw=true")
    bot.send_photo(message.chat.id, "https://github.com/nestessia/hepls/blob/main/iter_1.png?raw=true")
    bot.register_next_step_handler(message, which_elementary_fun2)
        
@bot.message_handler(content_types=["text"])
def which_elementary_fun1(message):
    if message.text == "e^x":
        bot.send_message(message.chat.id, 'Введите x (x <= 1):')
        bot.register_next_step_handler(message, get_x_for_e_fun) 
    elif message.text == "sin(x)":
        bot.send_message(message.chat.id, 'Введите x (x <= pi/2):')
        bot.register_next_step_handler(message, get_x_for_sin) 
    elif message.text == "Назад":
        elementary_fun(message)
                
@bot.message_handler(content_types=["text"])
def which_elementary_fun2(message):
    if message.text == "sqrt(x)":
        bot.send_message(message.chat.id, 'Введите x:')
        bot.register_next_step_handler(message, get_x_for_iteration1)
    elif message.text == "1/sqrt(x)":
        bot.send_message(message.chat.id, 'Введите x:')
        bot.register_next_step_handler(message, get_x_for_iteration2) 
    elif message.text == "Назад":
        elementary_fun(message)
            
def dif(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    item1 = types.KeyboardButton("Метод Эйлера")
    item2 = types.KeyboardButton("Метод Рунге-Кутта")
    item3 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, text="{0.first_name}, что именно тебя интересует? ".format(message.from_user), reply_markup=markup)    
    bot.register_next_step_handler(message, method_dif)
    
@bot.message_handler(content_types=["text"])
def method_dif(message):
    if message.text == "Метод Эйлера":
        which_Eiler(message)
    elif message.text == "Метод Рунге-Кутта":
        which_Runge(message)
    elif message.text == "Назад":
        keyboard(message)
            
def which_Eiler(message):    
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    item1 = types.KeyboardButton("ДУ 1-го порядка")
    item2 = types.KeyboardButton("ДУ 2-го порядка")
    item3 = types.KeyboardButton("ДУ 3-го порядка")
    item4 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, text="{0.first_name}, ДУ какого порядка вас интересует? ".format(message.from_user), reply_markup=markup)    
    bot.register_next_step_handler(message, which_poryadok_Eiler)
        
@bot.message_handler(content_types=["text"])
def which_poryadok_Eiler(message):
    if message.text == "ДУ 1-го порядка":
        bot.send_message(message.chat.id, 'Введите ДУ первого порядка в нижнем регисте')
        bot.register_next_step_handler(message, get_exp_for_diff1)
    elif message.text == "ДУ 2-го порядка":
        bot.send_message(message.chat.id, 'Введите 1-е ДУ системы в нижнем регисте')
        bot.register_next_step_handler(message, get_exp1_for_diff2)     
    elif message.text == "ДУ 3-го порядка":
        bot.send_message(message.chat.id, 'Введите 1-е ДУ системы в нижнем регисте')
        bot.register_next_step_handler(message, get_exp1_for_diff3)     
    elif message.text == "Назад":
        dif(message)     
           
def which_Runge(message):    
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    item1 = types.KeyboardButton("ДУ 1-го порядка")
    item2 = types.KeyboardButton("ДУ 2-го порядка")
    item3 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, text="{0.first_name}, ДУ какого порядка вас интересует? ".format(message.from_user), reply_markup=markup)    
    bot.register_next_step_handler(message, which_poryadok_Runge)
        
@bot.message_handler(content_types=["text"])
def which_poryadok_Runge(message):
    if message.text == "ДУ 1-го порядка":
        bot.send_message(message.chat.id, 'Введите ДУ первого порядка в нижнем регисте')
        bot.register_next_step_handler(message, get_exp1_for_RK1)
    elif message.text == "ДУ 2-го порядка":
        bot.send_message(message.chat.id, 'Введите 1-е ДУ системы в нижнем регисте')
        bot.register_next_step_handler(message, get_exp1_for_RK2)         
    elif message.text == "Назад":
        dif(message)     
          
user_expression1 = ''
user_expression2 = ''
user_expression3 = ''
user_points = ''
user_z = ''
user_t = ''

#Эйлер.Вычисление ДУ 1 порядок
def get_exp_for_diff1(message):
    try:
        global user_expression1
        user_expression1 = message.text
        bot.send_message(message.chat.id, text='Введите нижнюю границу отрезка:')
        bot.register_next_step_handler(message, get_a_for_diff1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_a_for_diff1(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введите верхнюю границу отрезка:')
        bot.register_next_step_handler(message, get_b_for_diff1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_b_for_diff1(message):
    try:
        global user_b
        user_b = float(message.text)
        bot.send_message(message.chat.id, text='Введите x0:')
        bot.register_next_step_handler(message, get_x_for_diff1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
                
def get_x_for_diff1(message):
    try:
        global user_x
        user_x = float(message.text)
        bot.send_message(message.chat.id, text='Введите y0:')
        bot.register_next_step_handler(message, get_y_for_diff1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')    
        which_Eiler(message)
        
def get_y_for_diff1(message):
    try:
        global user_y
        user_y = float(message.text)
        bot.send_message(message.chat.id, text='Введите количество разбиений:')
        bot.register_next_step_handler(message, get_n_for_diff1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        which_Eiler(message)
        
def get_n_for_diff1(message):
    try:
        global user_n
        user_n = int(message.text)
        bot.send_message(message.chat.id, text='Введите количество точек:')
        bot.register_next_step_handler(message, get_points_diff1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        which_Eiler(message)
        
def get_points_diff1(message):
    try:
        global user_points
        user_points = int(message.text)
        Eiler_1(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        which_Eiler(message)
               
def Eiler_1(message):
    try:
        global user_b, user_a, user_n, user_x, user_y, user_points, user_expression1
        count = 0
        h = (user_b-user_a) / user_n
        x = user_x
        y = user_y
        while (x < user_b) and (count < user_points):
            y += h * eval(user_expression1)
            x += h
            bot.send_message(message.chat.id, 'x = ' + str(round(x,5)) + '   y = ' + str(round(y,5)))
            count += 1        
        keyboard(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново.')  
        which_Eiler(message)
        
#Эйлер.Вычисление ДУ 2 порядок
def get_exp1_for_diff2(message):
    try:
        global user_expression1
        user_expression1 = message.text
        bot.send_message(message.chat.id, text='Введите 2-е ДУ системы в нижнем регисте:')
        bot.register_next_step_handler(message, get_exp2_for_diff2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_exp2_for_diff2(message):
    try:
        global user_expression2
        user_expression2 = message.text
        bot.send_message(message.chat.id, text='Введите нижнюю границу отрезка:')
        bot.register_next_step_handler(message, get_a_for_diff2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_a_for_diff2(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введите верхнюю границу отрезка:')
        bot.register_next_step_handler(message, get_b_for_diff2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_b_for_diff2(message):
    try:
        global user_b
        user_b = float(message.text)
        bot.send_message(message.chat.id, text='Введите X0:')
        bot.register_next_step_handler(message, get_x_for_diff2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_x_for_diff2(message):
    try:
        global user_x
        user_x = float(message.text)
        bot.send_message(message.chat.id, text='Введите y0:')
        bot.register_next_step_handler(message, get_y_for_diff2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_y_for_diff2(message):
    try:
        global user_y
        user_y = float(message.text)
        bot.send_message(message.chat.id, text='Введите z0:')
        bot.register_next_step_handler(message, get_z_for_diff2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')       
        which_Eiler(message)
        
def get_z_for_diff2(message):
    try:
        global user_z
        user_z = float(message.text)
        bot.send_message(message.chat.id, text='Введите количество разбиений:')
        bot.register_next_step_handler(message, get_n_for_diff2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_n_for_diff2(message):
    try:
        global user_n
        user_n = int(message.text)
        bot.send_message(message.chat.id, text='Введите необходимое количество точек:')
        bot.register_next_step_handler(message, get_points_diff2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_points_diff2(message):
    try:
        global user_points
        user_points = int(message.text)
        Eiler_2(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        which_Eiler(message)     
                                                 
def Eiler_2(message):
    try:
        global user_b, user_a, user_n, user_x, user_y, user_z, user_points, user_expression1, user_expression2
        count = 0
        h = (user_b-user_a) / user_n
        x = user_x
        y = user_y
        z = user_z
        while (x < user_b) and (count < user_points):
            yBuf = y + h * eval(user_expression1)
            zBuf = z + h * eval(user_expression2)
            y = yBuf
            z = zBuf
            x += h
            bot.send_message(message.chat.id, 'x = ' + str(round(x, 5)) + '  y = ' + str(round(y, 5)) + '  z = ' + str(round(z, 5)))
            count += 1                             
        keyboard(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново.')  
        which_Eiler(message)
        
#Эйлер.Вычисление ДУ 3 порядок    
def get_exp1_for_diff3(message):
    try:
        global user_expression1
        user_expression1 = message.text
        bot.send_message(message.chat.id, text='Введите 2-е ДУ системы в нижнем регисте:')
        bot.register_next_step_handler(message, get_exp2_for_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_exp2_for_diff3(message):
    try:
        global user_expression2
        user_expression2 = message.text
        bot.send_message(message.chat.id, text='Введите 3-е ДУ системы в нижнем регисте:')
        bot.register_next_step_handler(message, get_exp3_for_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_exp3_for_diff3(message):
    try:
        global user_expression3
        user_expression3 = message.text
        bot.send_message(message.chat.id, text='Введите нижнюю границу отрезка:')
        bot.register_next_step_handler(message, get_a_for_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')       
        which_Eiler(message)
        
def get_a_for_diff3(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введите верхнюю границу отрезка:')
        bot.register_next_step_handler(message, get_b_for_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_b_for_diff3(message):
    try:
        global user_b
        user_b = float(message.text)
        bot.send_message(message.chat.id, text='Введите t0:')
        bot.register_next_step_handler(message, get_t_for_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)
        
def get_t_for_diff3(message):
    try:
        global user_t
        user_t = float(message.text)
        bot.send_message(message.chat.id, text='Введите y0:')
        bot.register_next_step_handler(message, get_x_for_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        which_Eiler(message)
        
def get_x_for_diff3(message):
    try:
        global user_x
        user_x = float(message.text)
        bot.send_message(message.chat.id, text='Введите y0:')
        bot.register_next_step_handler(message, get_y_for_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        which_Eiler(message)

def get_y_for_diff3(message):
    try:
        global user_y
        user_y = float(message.text)
        bot.send_message(message.chat.id, text='Введите z0:')
        bot.register_next_step_handler(message, get_z_for_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        which_Eiler(message)

def get_z_for_diff3(message):
    try:
        global user_z
        user_z = float(message.text)
        bot.send_message(message.chat.id, text='Введите количество разбиений:')
        bot.register_next_step_handler(message, get_n_for_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        which_Eiler(message)

def get_n_for_diff3(message):
    try:
        global user_n
        user_n = int(message.text)
        bot.send_message(message.chat.id, text='Введите количество разбиений:')
        bot.register_next_step_handler(message, get_points_diff3)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)

def get_points_diff3(message):
    try:
        global user_points
        user_points = int(message.text)
        Eiler_3(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Eiler(message)

def Eiler_3(message):
    try:
        global user_b, user_a, user_n, user_x, user_y, user_z, user_t, user_points, user_expression1, user_expression2, user_expression3
        count = 0
        h = (user_b-user_a) / user_n
        x = user_x
        y = user_y
        z = user_z
        t = user_t
        while (t < user_b) and (count < user_points):
            xBuf = x + h * eval(user_expression1)
            yBuf = y + h * eval(user_expression2)
            zBuf = z + h * eval(user_expression3)
            x = xBuf
            y = yBuf
            z = zBuf
            t += h
            bot.send_message(message.chat.id, 't = ' + str(round(t, 5)) + '  x = ' + str(round(x, 5)) + '  y = ' + str(round(y, 5)) + '  z = ' + str(round(z, 5)))
            count += 1                                          
        keyboard(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново.')  
        which_Eiler(message)    

#Рунге-Кутта.Вычисление ДУ 1 порядок     
def get_exp1_for_RK1(message):
    try:
        global user_expression1
        user_expression1 = message.text
        bot.send_message(message.chat.id, text='Введите нижнюю границу отрезка:')
        bot.register_next_step_handler(message, get_a_for_RK1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')     
        which_Runge(message)
        
def get_a_for_RK1(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введите верхнюю границу отрезка:')
        bot.register_next_step_handler(message, get_b_for_RK1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Runge(message)
        
def get_b_for_RK1(message):
    try:
        global user_b
        user_b = float(message.text)
        bot.send_message(message.chat.id, text='Введите x0:')
        bot.register_next_step_handler(message, get_x_for_RK1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Runge(message)
        
        
def get_x_for_RK1(message):
    try:
        global user_x
        user_x = float(message.text)
        bot.send_message(message.chat.id, text='Введите y0:')
        bot.register_next_step_handler(message, get_y_for_RK1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')    
        which_Runge(message)
        
def get_y_for_RK1(message):
    try:
        global user_y
        user_y = float(message.text)
        bot.send_message(message.chat.id, text='Введите количество разбиений:')
        bot.register_next_step_handler(message, get_n_for_RK1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        which_Runge(message)
        
def get_n_for_RK1(message):
    try:
        global user_n
        user_n = int(message.text)
        bot.send_message(message.chat.id, text='Введите количество точек:')
        bot.register_next_step_handler(message, get_points_RK1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        which_Runge(message)
        
def get_points_RK1(message):
    try:
        global user_points
        user_points = int(message.text)
        RK_1(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')      
        which_Runge(message)
        
def RK_1(message):
    try:
        global user_b, user_a, user_n, user_x, user_y, user_points, user_expression1
        count = 0
        h = (user_b - user_a) / user_n
        x = user_x
        y = user_y
        while (x < user_b) and (count < user_points):
            xbuffer = x
            ybuffer = y
            k1 = h * eval(user_expression1)
            x = xbuffer + h/2
            y = ybuffer + k1/2
            k2 = h * eval(user_expression1)
            x = xbuffer + h/2
            y = ybuffer + k2/2
            k3 = h * eval(user_expression1)
            x = xbuffer + h
            y = ybuffer + k3
            k4 = h * eval(user_expression1)
            F = (k1 + 2 * k2 + 2 * k3 + k4) / 6
            y = ybuffer + F
            x = xbuffer + h
            bot.send_message(message.chat.id, 'x = ' + str(round(x,5)) + '   y = ' + str(round(y,5)))
            count += 1
        keyboard(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')      
        which_Runge(message)
        
#Рунге-Кутта.Вычисление ДУ 2 порядок 
def get_exp1_for_RK2(message):
    try:
        global user_expression1
        user_expression1 = message.text
        bot.send_message(message.chat.id, text='Введите 2-е ДУ системы в нижнем регисте:')
        bot.register_next_step_handler(message, get_exp2_for_RK2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        which_Runge(message)
        
def get_exp2_for_RK2(message):
    try:
        global user_expression2
        user_expression2 = message.text
        bot.send_message(message.chat.id, text='Введите нижнюю границу отрезка:')
        bot.register_next_step_handler(message, get_a_for_RK2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново') 
        which_Runge(message)
        
def get_a_for_RK2(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введите верхнюю границу отрезка:')
        bot.register_next_step_handler(message, get_b_for_RK2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново') 
        which_Runge(message)
        
def get_b_for_RK2(message):
    try:
        global user_b
        user_b = float(message.text)
        bot.send_message(message.chat.id, text='Введите X0:')
        bot.register_next_step_handler(message, get_x_for_RK2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново') 
        which_Runge(message)
        
def get_x_for_RK2(message):
    try:
        global user_x
        user_x = float(message.text)
        bot.send_message(message.chat.id, text='Введите y0:')
        bot.register_next_step_handler(message, get_y_for_RK2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново') 
        which_Runge(message)
        
def get_y_for_RK2(message):
    try:
        global user_y
        user_y = float(message.text)
        bot.send_message(message.chat.id, text='Введите z0:')
        bot.register_next_step_handler(message, get_z_for_RK2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново')       
        which_Runge(message)
        
def get_z_for_RK2(message):
    try:
        global user_z
        user_z = float(message.text)
        bot.send_message(message.chat.id, text='Введите количество разбиений:')
        bot.register_next_step_handler(message, get_n_for_RK2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново') 
        which_Runge(message)
        
def get_n_for_RK2(message):
    try:
        global user_n
        user_n = int(message.text)
        bot.send_message(message.chat.id, text='Введите необходимое количество точек:')
        bot.register_next_step_handler(message, get_points_RK2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново') 
        which_Runge(message)
        
def get_points_RK2(message):
    try:
        global user_points
        user_points = int(message.text)
        RK_2(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново')
        which_Runge(message)
        
def RK_2(message):
    try:
        global user_b, user_a, user_n, user_x, user_y, user_z, user_points, user_expression1, user_expression2
        count = 0
        h = (user_b - user_a) / user_n
        x = user_x
        y = user_y
        z = user_z
        while (x < user_b) and (count < user_points):
            xbuffer = x
            ybuffer = y
            zbuffer = z
            q1 = eval(user_expression2)
            k1 = eval(user_expression1)
            x = xbuffer + h/2
            y = ybuffer + k1/2
            z = zbuffer + q1/2
            q2 = eval(user_expression2)
            k2 = eval(user_expression1)
            x = xbuffer + h / 2
            y = ybuffer + k2 / 2
            z = zbuffer + q2 / 2
            q3 = eval(user_expression2)
            k3 = eval(user_expression1)
            x = xbuffer + h
            y = ybuffer + k3
            z = zbuffer + q3
            q4 = eval(user_expression2)
            k4 = eval(user_expression1)
            x = xbuffer + h
            y = ybuffer + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            z = zbuffer + h / 6 * (q1 + 2 * q2 + 2 * q3 + q4)
            bot.send_message(message.chat.id, 'x = ' + str(round(x, 5)) + '  y = ' + str(round(y, 5)) + '  z = ' + str(round(z, 5)))
            count += 1
        keyboard(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Попробуйте заново')
        which_Runge(message)
        
#Вычисления элементарной функции
user_x = ''
user_y = ''
user_ebs = ''

def get_x_for_e_fun(message):
    try:
        global user_x
        user_x = float(message.text)
        resultPrint_for_e_fun(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        elementary_method1(message)   

def resultPrint_for_e_fun(message):
    global user_x
    res = e()
    bot.send_message(message.chat.id, "Результат: " + (str(res)))  
    keyboard(message)
    
def e():
    global user_x
    a = [0.9999998, 1.000000, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
    k = 1
    U = 1.0
    C = a[0]
    P = 1
    e = 2 * math.pow(10, -7)
    user_x = math.fabs(user_x)
    while (math.fabs(U) > e):
        P *= user_x
        U = P * a[k]
        C += U
        if k >= 7:
            break
        else:
            k += 1
    return C

def get_x_for_sin(message):
    try:
        global user_x
        user_x = float(message.text)
        resultPrint_for_sin(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        elementary_method1(message)   

def resultPrint_for_sin(message):
    global user_x
    res = sin()
    bot.send_message(message.chat.id, "Результат: " + (str(res))) 
    keyboard(message)
    
def sin():
    global user_x
    a = [1.000000002, -0.166666599, 0.008333075, -0.000198107, 0.000002608]
    k = 1
    U = 1.0
    P = 1
    pi = 3.14
    e = 6 * math.pow(10, -9)
    user_x = (pi * user_x) / 180
    C = a[0] * user_x
    while (math.fabs(U) > e):
        P *= user_x**2
        U = P * a[k] * user_x
        C += U
        if k >= 4:
            break
        else:
            k += 1
    return C

def get_x_for_iteration1(message):
    try:
        global user_x
        user_x = float(message.text)
        bot.send_message(message.chat.id, text='Введите y0:')
        bot.register_next_step_handler(message, get_y_for_iteration1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        elementary_method2(message)
        
def get_y_for_iteration1(message):
    try:
        global user_y
        user_y = float(message.text)
        bot.send_message(message.chat.id, text='Введите точность:')
        bot.register_next_step_handler(message, get_ebs1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        elementary_method2(message)
        
def get_ebs1(message):
    try:
        global user_ebs
        user_ebs = float(message.text)
        resultPrint_for_iteration1(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...  Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')        
        elementary_method2(message)
        
def resultPrint_for_iteration1(message):
    global user_x, user_y, user_ebs
    res = iteration1()
    bot.send_message(message.chat.id, "Результат: " + (str(res)))
    keyboard(message)
    
def iteration1():
    global user_x, user_y, user_ebs
    res = user_y
    while abs(user_x - res**2) > user_ebs:
        res = (1/2)*(res + user_x / res)
    return res       
    
def get_x_for_iteration2(message):
    try:
        global user_x
        user_x = float(message.text)
        bot.send_message(message.chat.id, text='Введите y0:')
        bot.register_next_step_handler(message, get_y_for_iteration2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        elementary_method2(message)
        
def get_y_for_iteration2(message):
    try:
        global user_y
        user_y = float(message.text)
        bot.send_message(message.chat.id, text='Введите точность:')
        bot.register_next_step_handler(message, get_ebs2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')    
        elementary_method2(message)
        
def get_ebs2(message):
    try:
        global user_ebs
        user_ebs = float(message.text)
        resultPrint_for_iteration2(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...  Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        elementary_method2(message)
        
def resultPrint_for_iteration2(message):
    global user_x, user_y, user_ebs
    res = iteration2()
    bot.send_message(message.chat.id, "Результат: " + (str(res)))
    keyboard(message)
    
def iteration2():
    global user_x, user_y, user_ebs
    res = user_y
    while abs(user_x - (1/res)**2) > user_ebs:
        res = (res / 2)*(3 - user_x * res**2)
    return res

    
user_e = ''
user_a = ''
user_b = ''
user_c = ''
user_d = ''
user_n = ''
user_nx = ''
user_ny = ''

#Вычисления
def task(x):
    return x*x+5*x+3 
 
#Для Метода левых прямоугольников   
def get_n_for_left(message,user_result = None):
    try:
        global user_n
        if user_result == None:
            user_n = int(message.text)
        else: 
            user_n = str(user_result)
        bot.send_message(message.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(message, get_a_for_left)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Попробуйте заново. ')      
        constant_step(message)
        
def get_a_for_left(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(message, get_b_for_left)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...  Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.') 
        constant_step(message)
        
def get_b_for_left(message):
    try:
        global user_b
        user_b = float(message.text)
        resultPrint_for_left(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        constant_step(message)
        
def left():    
    global user_a, user_b, user_n, user_result
    h = (user_b - user_a) / user_n
    x = user_a
    user_result = 0
    while x <= (user_b - h):
        user_result += task(x)
        x += h
    return h * user_result
    
def resultPrint_for_left(message):
    global user_a, user_b, user_n, user_result
    res = left()
    bot.send_message(message.chat.id, "Результат: " + (str(res)))   
    keyboard(message)

#Для Метода правых прямоугольников
def get_n_for_right(message,user_result = None):
    try:
        global user_n
        
        if user_result == None:
            user_n = int(message.text)
        else: 
            user_n = str(user_result)
        bot.send_message(message.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(message, get_a_for_right)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Попробуйте заново.')
        constant_step(message)
        
def get_a_for_right(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(message, get_b_for_right)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        constant_step(message)
        
def get_b_for_right(message):
    try:
        global user_b
        user_b = float(message.text)
        resultPrint_for_right(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        constant_step(message)
        
def right():
    global user_a, user_b, user_n, user_result  
    h = (user_b - user_a) / user_n
    x = user_a + h
    result = 0
    while x <= user_b:
        result += task(x)
        x += h
    return h * result
    
def resultPrint_for_right(message):
    global user_a, user_b, user_n, user_result
    res = right()
    bot.send_message(message.chat.id, "Результат: " + (str(res)))
    keyboard(message)
       
#Для Метода трапеции
def get_n_for_trapecia(message,user_result = None):
    try:
        global user_n
        
        if user_result == None:
            user_n = int(message.text)
        else: 
            user_n = str(user_result)
        bot.send_message(message.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(message, get_a_for_trapecia)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Попробуйте заново.')
        constant_step(message)
        
def get_a_for_trapecia(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(message, get_b_for_trapecia)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        constant_step(message)
        
def get_b_for_trapecia(message):
    try:
        global user_b
        user_b = float(message.text)
        resultPrint_for_trapecia(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        constant_step(message)
        
def trapecia():
    global user_a, user_b, user_n, user_result  
    h = (user_b - user_a) / user_n
    x = user_a + h
    result = 0
    while x <= (user_b - h):
        result += task(x)
        x += h
    return ((task(user_a) + task(user_b)) / 2 + result) * h
    
def resultPrint_for_trapecia(message):
    global user_a, user_b, user_n, user_result
    res = trapecia()
    bot.send_message(message.chat.id, "Результат: " + (str(res)))
    keyboard(message)
    
#Для Метода парабол
def get_n_for_parabola(message,user_result = None):
    try:
        global user_n
        
        if user_result == None:
            user_n = int(message.text)
        else: 
            user_n = str(user_result)
        bot.send_message(message.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(message, get_a_for_parabola)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так...  Вы точно ввели число? Попробуйте заново.')
        constant_step(message)
        
def get_a_for_parabola(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(message, get_b_for_parabola)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        constant_step(message)
        
def get_b_for_parabola(message):
    try:
        global user_b
        user_b = float(message.text)
        resultPrint_for_parabola(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        constant_step(message)
        
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
    
def resultPrint_for_parabola(message):
    global user_a, user_b, user_n, user_result
    res = parabola()
    bot.send_message(message.chat.id, "Результат: " + (str(res)))   
    keyboard(message)
     
#Для кратного интеграла   
def get_nx(message):
    try:
        global user_nx
        user_nx = float(message.text)
        bot.send_message(message.chat.id, text='Введите количество разбиений по y:')
        bot.register_next_step_handler(message, get_ny)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')   
    
def get_ny(m):
    try:
        global user_ny
        user_ny = float(m.text)
        bot.send_message(m.chat.id, text='Введите внешнюю нижнюю границу:')
        bot.register_next_step_handler(m, get_a)
    except Exception as e:
        bot.reply_to(m, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        
def get_a(m):
    try:
        global user_a
        user_a = float(m.text)
        bot.send_message(m.chat.id, text='Введите внешнюю верхнюю границу:')
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
        
def resultPrint_for_KratInt(message):
    res = calc_kratniy()
    bot.send_message(message.chat.id, "Результат: " + (str(res)))        
    keyboard(message)    
        
#Двойной перерасчет 1         
def get_e_for_recalc1(message,user_result = None):
    try:
        global user_e
        if user_result == None:
            user_e = float(message.text)
        else: 
            user_e = str(user_result)
        bot.send_message(message.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(message, get_a_for_recalc1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново. ')      
        variable_step(message)
        
def get_a_for_recalc1(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(message, get_b_for_recalc1)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        variable_step(message)
        
def get_b_for_recalc1(message):
    try:
        global user_b
        user_b = float(message.text)
        resultPrint_for_recalc1(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        variable_step(message)
    
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
       
def resultPrint_for_recalc1(message):
    res = doubleRecalc(user_e,user_a, user_b)
    bot.send_message(message.chat.id, "Результат: " + (str(res)))    
    keyboard(message) 
   
#Двойной перерасчет 2   
def get_e_for_recalc2(message,user_result = None):
    try:
        global user_e
        if user_result == None:
            user_e = float(message.text)
        else: 
            user_e = str(user_result)
        bot.send_message(message.chat.id, text='Введи нижнюю границу')
        bot.register_next_step_handler(message, get_a_for_recalc2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Скорее всего, вы ввели не число. Попробуйте заново ')      
        variable_step(message)
        
def get_a_for_recalc2(message):
    try:
        global user_a
        user_a = float(message.text)
        bot.send_message(message.chat.id, text='Введи верхнюю границу')
        bot.register_next_step_handler(message, get_b_for_recalc2)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')  
        variable_step(message)
        
def get_b_for_recalc2(message):
    try:
        global user_b
        user_b = float(message.text)
        resultPrint_for_recalc2(message)
    except Exception as e:
        bot.reply_to(message, 'Что-то пошло не так... Вы точно ввели число? Проверьте корректность написания вещественного числа и попробуйте заново.')
        variable_step(message)
        
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

def resultPrint_for_recalc2(message):
    res = doubleRecalcBetter(user_e,user_a, user_b)
    bot.send_message(message.chat.id, "Результат: " + (str(res)))  
    keyboard(message)  
                     
# Запуск бота
bot.polling(none_stop=True, interval=0)
