class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    people = {}


def create_person_list(people: list) -> list:
    new_list = []
    for human in people:
        for person in Person.people:
            if person is human["name"]:
                new_list.append(Person.people[person])
        if "wife" in human and human["wife"] is not None:
            Person.people[human["name"]].wife \
                = Person.people[human["wife"]]
        if "husband" in human and human["husband"] is not None:
            Person.people[human["name"]].husband \
                = Person.people[human["husband"]]
    return new_list


# - - - - - - - - - - start self_check from here - - - - - - - - - - -
# - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - DATA - - - - - - - - - - - - - - - - -

person1 = Person("Ross", 30)
person2 = Person("Joey", 29)
person3 = Person("Phoebe", 31)
person4 = Person("Chandler", 30)
person5 = Person("Monica", 32)
person6 = Person("Rachel", 28)

people_list = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Phoebe", "age": 31, "husband": None},
    {"name": "Chandler", "age": 30, "wife": "Monica"},
    {"name": "Monica", "age": 32, "husband": "Chandler"},
    {"name": "Rachel", "age": 28, "husband": "Ross"},
]

# - - - - - - - - - - - - - - - TEST - - - - - - - - - - - - - - - - -
print(f"Нижче бачимо, що створено 6 об'єктів із лише двома аргументами\n"
      f"- - - - - - - - - -('name' та 'age')- - - - - - - - - - - - - : \n"
      f"{person1.__dict__}\n"
      f"{person2.__dict__}\n"
      f"{person3.__dict__}\n"
      f"{person4.__dict__}\n"
      f"{person5.__dict__}\n"
      f"{person6.__dict__}\n"
      f"\n"
      f"\n"
      f"Нижче бачимо, що функція відпрацьовує без помилок, \n"
      f"створюючи 6 об'єктів: \n"
      f"{create_person_list(people_list)}\n"
      f"\n"
      f"\n"
      f"Нижче бачимо, що функція додала відповідні жінку та чоловіка, \n"
      f"лише там де це треба: \n"
      f"{person1.__dict__} - це лінк до {person1.wife.name}\n"
      f"{person2.__dict__}\n"
      f"{person3.__dict__}\n"
      f"{person4.__dict__} - це лінк до {person4.wife.name}\n"
      f"{person5.__dict__} - це лінк до {person5.husband.name}\n"
      f"{person6.__dict__} - це лінк до {person6.husband.name}\n")
