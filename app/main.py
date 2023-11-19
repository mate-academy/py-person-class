
class Person:
    people = {}  # Атрибут класса для хранения экземпляров Person по их имени
    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.people[name] = self

def create_person_list(people):

    person_list = []

    for person_info in people:
        name = person_info["name"]
        age = person_info["age"]

        person_instance = Person(name, age)
        person_list.append(person_instance)

    for dct in people:
         obj = Person.people[dct.get("name")]
         if "wife" in dct:
             if dct["wife"]:
                obj.wife = Person.people[dct.get("wife")]
         else:
             if dct["husband"]:
                obj.husband = Person.people[dct.get("husband")]

    return person_list
