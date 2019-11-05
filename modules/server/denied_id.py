import datetime


def deny(message):
    f = open('logs/Denied id.txt', 'a+')
    f.write(str(datetime.datetime.now()) + '\n')
    f.write(str(message.chat.id) + '\n')
    f.write(str(message.text) + '\n')
    f.write(' - ' * 25 + '\n')
    f.close()


def log(message):
    f = open('logs/Log ' + str(datetime.date.today()) + '.txt', 'a+')
    f.write(str(datetime.datetime.now()) + '\n')
    f.write(str(message.chat.id) + '\n')
    f.write(str(message.text) + '\n')
    f.write(' - ' * 25 + '\n')
    f.close()
