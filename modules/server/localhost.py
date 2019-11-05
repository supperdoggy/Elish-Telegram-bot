import datetime
import os
import json


def TotalIncome(price, thing):
    if os.path.exists("Checks/TotalIncome %s.json" % datetime.date.today()):
        f = open("Checks/TotalIncome %s.json" % datetime.date.today(), "r")
        data = json.load(f)
        f.close()

        data["TotalMoney"] += int(price)
        data["Things"] += " %s" % thing

        f = open("Checks/TotalIncome %s.json" % datetime.date.today(), "w")
        json.dump(data, f)
        f.close()

    else:
        f = open("Checks/TotalIncome %s.json" % datetime.date.today(), "w+")
        data = {
            "TotalMoney": price,
            "Things": thing
        }
        json.dump(data, f)
        f.close()

class file:
    def data(self, price, id):
        f = open('Checks/Data.txt', 'a+')
        f.write(str('%s\n' % datetime.datetime.now()))
        f.write(str(self) + ' - послуга' + '\n')
        f.write(str(price) + ' - ціна' + '\n')
        f.write(str(id) + ' - id касира' + '\n')
        f.write(' - ' * 25 + '\n')
        f.close()

        if os.path.exists("Checks/Data.json"):
           f = open("Checks/Data.json", "r")
           data = json.load(f)
           f.close()

           data["Thing"] += ", %s" % self
           data["Price"] = int(data["Price"]) + int(price)

           f = open("Checks/Data.json", "w")
           json.dump(data, f)
           f.close()
        else:
            data = {
                "Thing": "%s" % self,
                "Price": "%s" % price
            }
            f = open("Checks/Data.json", "w+")
            json.dump(data, f)

        doc = open("Checks/" + str(datetime.date.today()) + '.txt', 'a+')
        doc.write(str('%s\n' % datetime.datetime.now()))
        doc.write(str(self) + ' - послуга' + '\n')
        doc.write(str(price) + ' - ціна' + '\n')
        doc.write(str(id) + ' - id касира' + '\n')
        doc.write(' - ' * 25 + '\n')
        doc.close()

        TotalIncome(price, self)

        print('Послуга : ', self, ' ' * 2, price, ' грн ', ' ' * 2, ' касир : ', id)

    def delete_data(self, message):
        doc = open('Checks/Data.txt', 'rb')
        self.send_document(message.chat.id, doc)
        self.send_message(message.chat.id, 'Готово')
        doc.close()

        os.rename('Checks/Data.txt', '%s.txt' % datetime.datetime.now())
        os.rename('Checks/Data.json', '%s.json' % datetime.datetime.now())

        self.send_message(message.chat.id, 'Готово')

    def Checkout(self, message):
        f = open("Checks/Data.json", "r")
        data = json.load(f)
        self.send_message(message.chat.id, '%s' % data["Thing"])
        self.send_message(message.chat.id, '%s' % data["Price"])
        f.close()
        os.rename('Checks/Data.json', '%s.json' % datetime.datetime.now())

    def Total(self, message):
        f = open("Checks/TotalIncome %s.json" % datetime.date.today(), "r")
        data = json.load(f)
        f.close()
        self.send_message(message.chat.id, 'Прибуток за сьогодні становить: %s гривень' % data["TotalMoney"])
