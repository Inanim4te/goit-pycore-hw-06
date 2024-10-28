from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
            if re.fullmatch(r'\d{10}', value):
                super().__init__(value)
            else:
                raise ValueError('Invalid phone number format.')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, new_phone):
        for phone in self.phones:
            if phone.value == new_phone:
                print(f'Phone {new_phone} already exists.')
                return False

        self.phones.append(Phone(new_phone))
        return True

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True

        print(f'Phone {old_phone} not found.')
        return False

    def remove_phone(self, phone_to_remove):
        for phone in self.phones:
            if phone.value == phone_to_remove:
                self.phones.remove(phone)
                return True

        print(f'Phone {phone_to_remove} not found.')
        return False

    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return phone.value

        print(f'Phone {phone_to_find} not found.')
        return False

    def __str__(self):
        return f'Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}'


class AddressBook(UserDict):
    def add_record(self, new_record):
        if new_record.name.value not in self.data:
            self.data[new_record.name.value] = new_record
            return True
        else:
            print(f'Record for "{new_record.name.value}" already exists.')
            return False

    def find(self, searched_name):
        if searched_name in self.data.keys():
            return self.data[searched_name]
        else:
            print(f'No record found for "{searched_name}".')
            return False

    def delete(self, searched_name):
        if searched_name in self.data.keys():
            del self.data[searched_name]
            return True
        else:
            print(f'No record found for "{searched_name}".')
            return False