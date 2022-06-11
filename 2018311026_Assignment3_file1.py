class Store(object):
    def __init__(self, id, name, address, tel):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__tel = tel

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def tel(self):
        return self.__tel

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("id must be int")
        self.__id = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be str")
        self.__name = value

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("add must be str")
        self.__address = value

    @tel.setter
    def tel(self, value):
        if not isinstance(value, int):
            raise TypeError("tel must be int")
        self.__tel = value

    def __str__(self):
        return 'ID : {}, Name : {}, Address : {}, Tel : {}'\
            .format(self.__id,self.__name,self.__address,self.__tel)

class Staff(object):
    def __init__(self, id, ssn, name, address, jobtitle, salary):
        self.__id = id
        self.__ssn = ssn
        self.__name = name
        self.__address = address
        self.__jobtitle = jobtitle
        self.__salary = salary

    @property
    def id(self):
        return self.__id

    @property
    def ssn(self):
        return self.__ssn

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def jobtitle(self):
        return self.__jobtitle

    @property
    def salary(self):
        return self.__salary

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("id must be int")
        self.__id = value

    @ssn.setter
    def ssn(self, value):
        if not isinstance(value, int):
            raise TypeError("ssn must be int")
        self.__ssn = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be str")
        self.__name = value

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("address must be str")
        self.__address = value

    @jobtitle.setter
    def jobtitle(self, value):
        if not isinstance(value, str):
            raise TypeError("Jobtitle must be str")
        self.__jobtitle = value

    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            raise TypeError("salary must be int")
        self.__salary = value

    def __str__(self):
        return 'ID : {}, SSN : {}, Name : {}, Address : {}, Jobtitle : {}, salary : {}'\
            .format(self.__id,self.__ssn,self.__name,self.__address,self.__jobtitle,self.__salary)

class Customer(object):
    def __init__(self, ssn, name, address, purchasing_points, tel, memberships=[]):
        self.__ssn = ssn
        self.__name = name
        self.__address = address
        self.__purchasing_points = purchasing_points
        self.__tel = tel
        self.__memberships = memberships

    @property
    def ssn(self):
        return self.__ssn

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def purchasing_points(self):
        return self.__purchasing_points

    @property
    def tel(self):
        return self.__tel

    @property
    def membership(self):
        return self.__memberships

    @ssn.setter
    def ssn(self, value):
        if not isinstance(value, int):
            raise TypeError("ssn must be int")
        self.__ssn = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str")
        self.__name = value

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("address must be str")
        self.__address = value

    @purchasing_points.setter
    def purchasing_points(self, value):
        if not isinstance(value, int):
            raise TypeError("purpoint must be int")
        self.__purchasing_points = value

    @tel.setter
    def tel(self, value):
        if not isinstance(value, int):
            raise TypeError("Name must be int")
        self.__tel = value

    @membership.setter
    def membership(self, value):
        if not isinstance(value, str):
            raise TypeError("address must be str")
        self.__memberships = value

    def __str__(self):
        return 'SSN : {}, Name : {}, Address : {}, purchasing points : {}, tel : {}, membership : {}'\
            .format(self.__ssn,self.__name,self.__address,self.__purchasing_points,self.__tel,self.__memberships)

class Product(object):
    def __init__(self, productcode, name, description, price, points):
        self.__productcode = productcode
        self.__name = name
        self.__description = description
        self.__price = price
        self.__points = points

    @property
    def productcode(self):
        return self.__productcode

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @property
    def points(self):
        return self.__points

    @productcode.setter
    def productcode(self, value):
        if not isinstance(value, int):
            raise TypeError("productcode must be int")
        self.__productcode = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be str")
        self.__name = value

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("description must be str")
        self.__description = value

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError("price must be int")
        self.__price = value

    @points.setter
    def points(self, value):
        if not isinstance(value, int):
            raise TypeError("points must be int")
        self.__points = value

    def __str__(self):
        return 'ProductCode : {}, Name : {}, Description : {}, Price : {}, Points = {}'\
            .format(self.__productcode,self.__name,self.__description,self.__price,self.__points)

class Order(object):
    def __init__(self,store,customer,staff,quantity,product=[]):
        self.__store = store
        self.__customer = customer
        self.__staff = staff
        self.__quantity = quantity
        self.__product = product


    def addProduct(self):
        self.__quantity = self.__quantity+1
        return self.__product

    def printReceipt(self):
        print('\tWelcome to ' + self.__store.name)
        print('\tStaff : '+self.__staff.name)
        print('\tCustomer : '+self.__customer.name)
        print('\n\t\tRECEIPT')
        print('\tStore id : ',self.__store.id)
        print('Product Name\tProductCode\t\tPrice')
        total = 0
        total_points = self.__customer.purchasing_points
        for i in range(len(self.__product)) :
            print('\t'+self.__product[i].name +'\t\t\t',self.__product[i].productcode,'\t\t',self.__product[i].price)
            total = total+self.__product[i].price
            total_points = total_points + self.__product[i].points
        print("\n\tTOTAL : \t\t\t\t\t",total)
        print('\n\tQuantity of all : ',self.__quantity)
        print('\n\tITEMS SOLD' ,self.__quantity)
        print("\tTotal Points : ",total_points)


print("--------------- 1 ---------------\n")
store = Store(1234,"Homeplus","Suwon", 8201012345678)
print(store)
print("\n")
print("--------------- 2 ---------------\n")
c1 = Customer(123,'customer1','Seoul',10,8201011112222)
c1.membership.append("Samsung")
c1.membership.append("Lotte")
c2 = Customer(456,'customer2','Suwon',5,8201033334444)
c2.membership.append("Uri")
c2.membership.append("Lotte")
st1 = Staff(11111111,111,"staff1",'Seoul','job1',5000000)
st2 = Staff(22222222,222,"staff2",'Seoul','job1',6000000)
print("customer1 -> \n",c1)
print()
print("customer2 -> \n",c2)
print("\nstaff1 -> \n",st1)
print("\nstaff2 -> \n",st2)
print("\n")
print("--------------- 3 ---------------\n")
c3 = Customer(789,'Kim MinSu','Suwon',20,8201055556666)
c3.membership.append("Samsung")
c3.membership.append("NH")
st3 = Staff(33333333,333,"Lee JaeSung",'Suwon','Homeplus',7000000)
store2 = Store(2345,"Homeplus","Suwon",8201077778888)
product1 = Product(120,"Bread","description1",2000,2)
product2 = Product(121,"Milk","description2",3000,3)
product3 = Product(122,"Eggs","description3",7000,4)
product4 = Product(123,"Meat","description4",8000,5)

order = Order(store2, c3, st3,0)
order.addProduct().append(product1)
order.addProduct().append(product2)
order.addProduct().append(product3)
order.addProduct().append(product4)
order.printReceipt()
