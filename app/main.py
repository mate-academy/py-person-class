class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_people = []
    for person_dict in people:
        person = Person(name=person_dict["name"], age=person_dict["age"])
        person_people.append(person)

    for person in people:
        person_instance = Person.people.get(person["name"])
        if person_instance:
            if person.get("wife"):
                wife_name = person["wife"]
                person_instance.wife = Person.people.get(wife_name)
            elif person.get("husband"):
                husband_name = person["husband"]
                person_instance.husband = Person.people.get(husband_name)

    return person_people
