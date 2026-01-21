class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list):
    Person.people.clear()

    # Створюємо список об’єктів Person через list comprehension
    person_objects = [Person(pdata["name"], pdata["age"]) for pdata in people_list]

    # Встановлюємо wife/husband тільки якщо значення існує
    for pdata in people_list:
        person = Person.people[pdata["name"]]
        wife_name = pdata.get("wife")
        husband_name = pdata.get("husband")
        if wife_name:
            person.wife = Person.people[wife_name]
        if husband_name:
            person.husband = Person.people[husband_name]

    return person_objects
