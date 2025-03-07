class Phone:
    price = 12000
    color = 'blue'
    brand = 'apple'
    features = ['camera', 'musics', 'hammer']

    def hello(self):
        print('Calling Al Amin')

    def send_sms(self, phone, sms):
        return f"The phone number is {phone}, and the text is: {sms}"


my_phone = Phone()
print(my_phone.brand)
my_phone.hello()
print(my_phone.send_sms(1235245, 'Hello sir!!'))

