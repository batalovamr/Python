import telebot
from telebot import types


bot = telebot.TeleBot("5667499166:AAH73f_c6d7GBZem62b1Umr0_O6r2rVvNxs")
flag = None
answer = None


@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, f"Приветствую вас в калькуляторе! Для работы с комплексными числами введи 1, для работы с рациональными числами введи 2: ")
    bot.register_next_step_handler(message, user_input)

def user_input(message):
    global flag
    flag = int(message.text)
    while True:
        bot.send_message(message.chat.id, f"Введите выражение. Пожалуйста отделяйте цифры от знака операции пробелом: ")
        bot.register_next_step_handler(message, calc1, calc2, in_data)

def calc1(message):
    global answer
    data = message.text.split()
    sign = data[1]
    if sign == "+":
        answer = float(data[0]) + float(data[2])
    elif sign == "-":
        answer = float(data[0]) - float(data[2])
    elif sign == "*":
        answer = float(data[0]) * float(data[2])
    elif sign == "/":
        if data[2] == "0":
            answer = "!Деление на ноль!"
        else: answer = float(data[0]) / float(data[2])
    bot.send_message(message.chat.id, f"Ваш результат: {answer}")
    bot.register_next_step_handler(message, out_data)

def calc2(message):
    global answer
    data = message.text.split()
    sign = data[1]
    first_num = complex(data[0])
    second_num = complex(data[2])
    if sign == "+":
        answer = first_num + second_num
    elif sign == "-":
        answer = first_num - second_num
    elif sign == "*":
        answer = first_num * second_num
    elif sign == "/":
        answer = first_num / second_num
    bot.send_message(message.chat.id, f"Ваш результат: {answer}")
    bot.register_next_step_handler(message, out_data)

def in_data(message):
    logwrite("Вы ввели: ", message)

def out_data(message):
    logwrite("Результат вычисления: ", message)

from datetime import datetime as dt
def logwrite(note, message_text):
    from datetime import datetime as dt
    log_file = open('log_file.txt', 'a')
    operation_time = dt.now().strftime('%H:%M')
    log_file.write(operation_time + ' ' + note + str(message_text) + '\n')

bot.infinity_polling()



