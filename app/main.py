class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name:
            if wife_name not in Person.people:
                wife_instance = Person(wife_name, 0)
            else:
                wife_instance = Person.people[wife_name]
            person_instance.wife = wife_instance
            wife_instance.husband = person_instance
        elif husband_name:
            if husband_name not in Person.people:
                husband_instance = Person(husband_name, 0)
            else:
                husband_instance = Person.people[husband_name]
            person_instance.husband = husband_instance
            husband_instance.wife = person_instance

        person_list.append(person_instance)
    return person_list
