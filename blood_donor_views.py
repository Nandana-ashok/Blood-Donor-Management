import datetime

import mysql.connector

class BloodDonorManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nandana@2004',
            database='blood_db'
        )
        print('Connected successfully....')
    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query = 'select * from donor where id = %s'
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query='''
            insert into donor(name,blood_group,phone,city,blood_donation)
            values (%s,%s,%s,%s,%s)'''
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print('Donor added successfully....')
        except Exception as a:
            print(a)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = 'select * from donor'
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            # print(records)
            for d in records:
                print(d)

        except Exception as a:
            print(a)
    def retrieval(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query = 'select * from donor where id =%s'
            values =(id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            print(record)
        except Exception as a:
            print(a)

    def delete(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = 'select * from donor where id =%s'
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            if record != None:
                query = 'delete from donor where id =%s'
                self.cursor.execute(query,values)
                self.connection.commit()
                print('Donor deleted successfully...')
            else:
                print('Donor not found...')
        except Exception as a:
            print(a)
    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor=self.connection.cursor()
                placeholder=''
                for k in kwargs.keys():
                    placeholder += k + '=%s, '
                placeholder = placeholder.rstrip(', ')
                query = f'update donor set {placeholder} where id =%s'
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print('Donor detail updated successfully......')
            else:
                print('Donor not found...')
        except Exception as e:
            print(e)
donor_object = BloodDonorManager()
# donor_object.post(name='nandana',blood_group='B+',phone='1023205486',city='kottayam',blood_donation=datetime.datetime.today())
# donor_object.post(name='ansa',blood_group='A+',phone='8563205486',city='pala',blood_donation=datetime.datetime.today())
# donor_object.post(name='navya',blood_group='AB+',phone='1523695486',city='tvm',blood_donation=datetime.datetime.today())
# donor_object.post(name='vandana',blood_group='A+',phone='1023225486',city='kottayam',blood_donation=datetime.datetime.today())

# donor_object.get()
print('---------Details of one blood donor--------------')
donor_object.retrieval(id=3)
print('----------Delete operation-------------')
donor_object.delete(id=3)
print('-------------------------------------------')
donor_object.get()
print('---------------Donor presence----------------------------')
print(donor_object.get_object(1))
print('-------------- Update operation-----------------------------')
donor_object.put(1,name='Nandana',city='Trivandrum')
print('--------------After updation-----------------------------')
print(donor_object.get_object(5))
