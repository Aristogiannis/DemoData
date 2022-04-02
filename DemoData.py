import random
from full_names import first_names, last_names, up_letters, chats, addresses, low_letter,weatehr_cond
from datetime import date
from PIL import Image, ImageDraw, ImageFont

'''
Demo Data Person class Start
'''

global r_int
r_int = int(random.randint(0, 599))


class Person:

    def __init__(self):
        first = first_names[r_int]
        last = last_names[r_int]
        todays_date = date.today().year
        todays_date = int(todays_date) - 2000
        self.first_name = first
        self.last_name = last
        self.age = random.randint(18, 82)
        self.email = first + '.' + last + '@email.com'
        self.password = ""
        self.bank_bal = random.randint(0, 9999)
        self.bank_acc = ""
        self.iban = ""
        self.tel_number = ""
        self.bank_cvv = random.randint(0, 999)
        self.bank_exp_date = str(random.randint(1, 12)) + "/" + str(todays_date + int(random.randint(1, 10)))
        self.ssn = ""
        self.password=""

        for i in range(11):
            if random.randint(0, 1) == 1:
                self.password += str(random.randint(0, 9))
            else:
                self.password += str(low_letter[random.randint(0, 25)])
            if i < 3:
                self.ssn += str(random.randint(0, 9))
            elif 3 < i <= 5:
                self.ssn += str(random.randint(0, 9))
            elif 5 < i != 6:
                self.ssn += str(random.randint(0, 9))
            else:
                self.ssn += "-"

        for i in range(34):
            if i >= 2:
                self.iban += str(random.randint(0, 9))
            else:
                self.iban += str(up_letters[random.randint(0, 25)])

        for i in range(16):
            if i > 5:
                self.tel_number += str(random.randint(0, 9))

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def full_bank(self):
        return '{} {} {} {}'.format(self.bank_acc, self.bank_cvc, self.bank_exp_date, self.bank_bal)


'''
Demo Data Person class end
'''
class weather():
    def __init__(self):
        self.condition = weatehr_cond[random.randint(0,35)]
        self.temperature= random.randrange(-10,39)
    def temp_in_metric(self,metric):
        if metric == "C" or metric == "c":
            self.temperature = random.randrange(-10,39)
        elif metric == "F" or metric == "f":
            self.temperature = random.randrange(7,75)
        elif metric == "K" or metric == "k":
            self.temperature = random.randrange(269, 300)
        return '{}'.format(self.temperature)
    def limited_temp(self, low, hight):
        self.temperature =random.randrange(low, hight)
        return '{}'.format(self.temperature)


class address():
    def __init__(self):
        r = random.randint(0, 234)
        self.adress = addresses[r]["address"] + " " + addresses[r]["city"] + " " + addresses[r]["state"] + " " +addresses[r]["zip"]

    def parameter(self, addres_city_state_zip):
        return '{}'.format(addresses[random.randint(0, 234)][addres_city_state_zip])


class data():
    def __init__(self):
        self.uppercase_letter = up_letters[random.randint(0, 25)]
        self.lowercase_letter = low_letter[random.randint(0, 25)]

    def letters(self, num, case):
        for i in range(num):
            self.uppercase_letter += up_letters[random.randint(0, 25)]
            self.lowercase_letter += low_letter[random.randint(0, 25)]
        if case == "up":
            return '{}'.format(self.uppercase_letter)
        else:
            return '{}'.format(self.lowercase_letter)




class fakeChat():
    def startchat(self, num): # starts conversation
        pass
    def oneside(self, num): # starts one sidied chat
        if num == 0:
            pass
        else:
            pass



def silveralert(person_image_path, save_path, sname, sage, sdate, splace, seyes, sheight, sweight,
                sinfo):  # input all strings with \\ in every path
    img1 = Image.open("alert.jpg")  # base photo
    img2 = Image.open(person_image_path)  # Person Photo
    img_size = img2.resize((244, 330))
    back_im = img1.copy()
    back_im.paste(img_size, (35, 185))
    font1 = ImageFont.truetype("Lato-Black.ttf", 30)
    font2 = ImageFont.truetype("Lato-Black.ttf", 18)
    back_im1 = ImageDraw.Draw(back_im)
    new_input = ""
    b = False
    for i, letter in enumerate(sinfo):
        if i % 20 == 0 and i != 0 and letter == " ":
            new_input = new_input + "\n"
        elif i % 20 == 0 and i != 0:
            b = True

        if b and letter == " ":
            new_input = new_input + "\n"
            b = False
        new_input += letter

    back_im1.text((300, 188), sname, (255, 255, 255), font=font1)
    back_im1.text((355, 235), sage, (0, 0, 0), font=font2)
    back_im1.text((300, 290), sdate, (0, 0, 0), font=font2)
    back_im1.text((340, 330), splace, (0, 0, 0), font=font2)
    back_im1.text((360, 395), seyes, (0, 0, 0), font=font2)
    back_im1.text((350, 425), sheight, (0, 0, 0), font=font2)
    back_im1.text((357, 457), sweight, (0, 0, 0), font=font2)
    back_im1.text((550, 248), new_input, (0, 0, 0), font=font2)
    back_im.save(save_path)


print(weather().limited_temp(29,111))
person = Person()
print(person.fullname())
print(person.email)
# a = "Νεαρη anime κοπελα που σχεδον δεν ξερη τι της γινετε"
# silveralert("C:\\Users\\arist\\OneDrive\\Υπολογιστής\\unknown.png","D:\\alert.png","Γεωργια Νικολαιδου","18", "1/2/2022","Παγκρατι", "μαυρα", "138 cm","30 κιλα", a)
