class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people_dicts):
    person_list = []
    for person_dict in people_dicts:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_dict in people_dicts:
        name = person_dict["name"]
        spouse_key = "wife" if "wife" in person_dict else "husband"
        spouse_name = person_dict.get(spouse_key)
        if spouse_name:
            if spouse_name in Person.people:
                setattr(Person.people[name], spouse_key, Person.people[spouse_name])
            else:
                print(f"Помилка: Людина з ім'ям '{spouse_name}' не знайдена.")

    return person_list
