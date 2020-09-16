class Carbase:
    def __init__(self, car_type, brand, photo_le_na_me, carrying):
        self.car_type = car_type
        self.carrying = carrying
        self.photo_le_na_me = photo_le_na_me
        self.brand = brand

    def get_photo_le_ext(self):
        ext = '.' + self.photo_le_na_me.split('.')[-1]
        return ext


class Car(Carbase):
    def __init__(self, car_type, brand, photo_le_na_me, carrying, passenger_seats_count):
        self.car_type = car_type
        self.passenger_seats_count = passenger_seats_count
        self.carrying = carrying
        self.photo_le_na_me = photo_le_na_me
        self.brand = brand


class Truck(Carbase):
    def __init__(self, car_type, brand, photo_le_na_me, carrying, body_whl):
        self.car_type = car_type
        self.body_whl = body_whl
        self.carrying = carrying
        self.photo_le_na_me = photo_le_na_me
        self.brand = brand
        if body_whl == '':
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0
        self.body_length = self.body_whl.split('x')[0]
        self.body_width = self.body_whl.split('x')[1]
        self.body_height = self.body_whl.split('x')[2]

    def get_body_volume(self):
        return float(self.body_length) * float(self.body_width) * float(self.body_height)


class Specmachine(Carbase):
    def __init__(self, car_type, brand, photo_le_na_me, carrying, extra):
        super().__init__(car_type, brand, photo_le_na_me, carrying)
        self.car_type = car_type
        self.extra = extra
        self.carrying = carrying
        self.photo_le_na_me = photo_le_na_me
        self.brand = brand





def get_car_list(filename):
    with open(filename, 'r') as f:
        car_list = []
        list_type = ['car', 'truck', 'spec_machine']
        for k in f:
            if k.split(';')[0] in list_type:
                car_type = k.split(';')[0]
                brand = k.split(';')[1]
                photo_le_na_me = k.split(';')[3]
                carring = k.split(';')[5]
                if car_type == list_type[0]:
                    passenger = k.split(';')[2]
                    ex_car = Car(car_type, brand, photo_le_na_me, carring, passenger)
                if car_type == list_type[1]:
                    body_whl = k.split(';')[4]
                    if body_whl == '':
                        body_whl = '0x0x0'
                    ex_car = Truck(car_type, brand, photo_le_na_me, carring, body_whl)
                if car_type == list_type[2]:
                    extra = k.split(';')[6]
                    ex_car = Specmachine(car_type, brand, photo_le_na_me, carring, extra)
                car_list.append(ex_car)
        return car_list




def main():
    pass

if __name__ == '__main__':
    main()
print(get_car_list('solution.txt'))
