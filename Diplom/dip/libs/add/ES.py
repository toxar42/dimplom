from pyknow import *
import json

class CARS(KnowledgeEngine):
    @Rule(Fact('комфорт'),
    Fact('1000000-2000000'),
    Fact('седан'),
    Fact('городские поездки'),
    Fact('задний'))
    def car1(self):
        self.declare(Fact(car='Mercedes-Benz C-Class 180 2011'))

    @Rule(Fact('вместимость'),
    Fact('1000000-2000000'),
    Fact('универсал'),
    Fact('городские поездки'),
    Fact('передний'))
    def car2(self):
        self.declare(Fact(car='Kia Ceed 2016'))

    @Rule(Fact('экономичность'),
    Fact('1000000-2000000'),
    Fact('седан'),
    Fact('городские поездки'),
    Fact('передний'))
    def car3(self):
        self.declare(Fact(car='Volkswagen Polo V 2017'))
    
    @Rule(Fact('экономичность'),
    Fact('1000000-2000000'),
    Fact('кроссовер'),
    Fact('поездки загород'),
    Fact('полный'))
    def car4(self):
        self.declare(Fact(car='Opel Mokka 2013'))
    
    @Rule(Fact('вместимость'),
    Fact('1000000-2000000'),
    Fact('универсал'),
    Fact('off-road приключения'),
    Fact('полный'))
    def car5(self):
        self.declare(Fact(car='Subaru Outback 2010'))

    @Rule(Fact('вместимость'),
    Fact('1000000-2000000'),
    Fact('кроссовер'),
    Fact('городские поездки'),
    Fact('полный'))
    def car6(self):
        self.declare(Fact(car='Nissan Qashqai 2015'))

    @Rule(Fact('комфорт'),
    Fact('1000000-2000000'),
    Fact('седан'),
    Fact('городские поездки'),
    Fact('передний'))
    def car7(self):
        self.declare(Fact(car='Mazda 6 2014'))

    @Rule(Fact('комфорт'),
    Fact('1000000-2000000'),
    Fact('седан'),
    Fact('городские поездки'),
    Fact('передний'))
    def car8(self):
        self.declare(Fact(car='Kia Optima 2016'))

    @Rule(Fact('комфорт'),
    Fact('1000000-2000000'),
    Fact('кроссовер'),
    Fact('городские поездки'),
    Fact('передний'))
    def car9(self):
        self.declare(Fact(car='Geely Coolray 2020'))

    @Rule(Fact('экономичность'),
    Fact('1000000-2000000'),
    Fact('универсал'),
    Fact('поездки загород'),
    Fact('передний'))
    def car10(self):
        self.declare(Fact(car='Volvo V60 2014'))

    @Rule(Fact('вместимость'),
    Fact('2000000-3000000'),
    Fact('кроссовер'),
    Fact('поездки загород'),
    Fact('полный'))
    def car11(self):
        self.declare(Fact(car='Nissan X-Trail 2018'))

    @Rule(Fact('комфорт'),
    Fact('2000000-3000000'),
    Fact('универсал'),
    Fact('поездки загород'),
    Fact('полный'))
    def car12(self):
        self.declare(Fact(car='Skoda Superb 2018'))

    @Rule(Fact('комфорт'),
    Fact('2000000-3000000'),
    Fact('седан'),
    Fact('городские поездки'),
    Fact('передний'))
    def car13(self):
        self.declare(Fact(car='Audi A6 2016'))

    @Rule(Fact(Fact('комфорт'),
    '2000000-3000000'),
    Fact('седан'),
    Fact('городские поездки'),
    Fact('передний'))
    def car14(self):
        self.declare(Fact(car='Volkswagen Passat 2017'))

    @Rule(Fact('комфорт'),
    Fact('3000000-4000000'),
    Fact('кроссовер'),
    Fact('поездки загород'),
    Fact('полный'))
    def car15(self):
        self.declare(Fact(car='Volkswagen Tiguan 2018'))

    @Rule(Fact('комфорт'),
    Fact('3000000-4000000'),
    Fact('седан'),
    Fact('городские поездки'),
    Fact('полный'))
    def car16(self):
        self.declare(Fact(car='Audi A4 2020'))

    @Rule(Fact('вместимость'),
    Fact('3000000-4000000'),
    Fact('кроссовер'),
    Fact('off-road приключения'),
    Fact('полный'))
    def car17(self):
        self.declare(Fact(car='Mitsubishi Outlander 2022'))

    @Rule(Fact('комфорт'),
    Fact('3000000-4000000'),
    Fact('седан'),
    Fact('городские поездки'),
    Fact('задний'))
    def car18(self):
        self.declare(Fact(car='Tesla Model 3 Standart Plus 2021'))

    @Rule(Fact('комфорт'),
    Fact('3000000-4000000'),
    Fact('седан'),
    Fact('поездки загород'),
    Fact('полный'))
    def car19(self):
        self.declare(Fact(car='Volvo S90 2021'))

    @Rule(Fact('комфорт'),
    Fact('3000000-4000000'),
    Fact('универсал'),
    Fact('off-road приключения'),
    Fact('полный'))
    def car20(self):
        self.declare(Fact(car='Volvo V90 2020'))                                                            

#правило срабатывает,
#когда в базе знаний появляется факт с атрибутом car
    @Rule(Fact(car=MATCH.a))
    def print_result(self,a):
        global identify_auto
        identify_auto = '{}'.format(a)
        return(identify_auto)

    def factz(self,l):
        for x in l:
            self.declare(x)
  
def identify(x):
    #Объявление списка фактов предоставленных пользователем
    mass = x 
    ex1 = CARS() 
    ex1.reset()
    # экспертная система добавляет факты которые указал пользователь для сравнения.
    ex1.factz(mass)
    # экспертная система применяет правила к фактам в базе знаний, чтобы идентифицировать автомобиль.
    ex1.run()
    with open("identified_car.json", "w") as f:
        json.dump({"car": identify_auto}, f) #запись идентифицированного автомобиля.

def read_identified_car():
    with open("identified_car.json", "r") as f:
        data = json.load(f)
        car = data.get("car")
        return(car)

def clear_identified_car():
    with open("identified_car.json", "r") as f:
        pass
