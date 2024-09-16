phonebook = {}
def add_contact(name, number):
    phonebook[name] = number
    return f"{name} added to contacts successfully"
def search_contacts(name):
    if name in phonebook:
        return f"{name}: {phonebook[name]}"
    else:
        return "Contact not found"
def display_contact():
    if phonebook:
        result = "Phonebook:\n"
        for name, number in phonebook.items():
            result += f"{name}: {number}\n"
        return result
    else:
        return "Phonebook is empty"
print(add_contact("Aayan", 12345678910))
print(search_contacts("Aayan"))
print(display_contact())