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
letter = input("Enter a letter: ")
for i in letter:
    if i == "a" or i == "A":
        print("'A' found")
        break
    else:
        print("'A' not found")
numbers = [-5, -111001, 5, 10]
sum_of_positives = 0
for number in numbers:
    if number < 0:
        continue
    sum_of_positives += number
print(sum_of_positives)
x = int(input("Enter number: "))
if x % 20 == 0:
    print(20)
elif x % 15 == 0:
    pass
elif x % 3 == 0:
    print(3)
else:
    print(x)
fruits = ["apple", "banana", "cherry", "date", "elderberry", "mango"]
for fruit in fruits:
    if fruit == "mango":
        print("Mango found")
        break
print("Search over")
