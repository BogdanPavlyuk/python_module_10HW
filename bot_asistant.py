from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value
        
    def __repr__(self) -> str:
        return self.value
    
class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
            
    def add_phone(self, phone: Phone):
        if isinstance(phone, Phone):
            self.phones.append(phone)
            return f"{phone.value} add succes to contact {self.name.value}"
        return f"Sorry, phone must be a Phone instance"
    
    def delete_phone(self, phone):
        self.phones.remove(phone)
        
    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        self.phones[self.phones.index(old_phone)] = new_phone
        
        
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record



if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')