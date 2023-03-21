class Person:
    people = {}

<<<<<<< HEAD
    def __init__(self, name: str, age: int) -> None:
=======
    def __init__(self, name, age):
>>>>>>> 01ad4f92f5532eafb486f3e0143c39d22245b63b
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
<<<<<<< HEAD
    person_list = [Person(peo["name"], peo["age"]) for peo in people]
    for hus in people:
        if "wife" in hus and hus.get("wife"):
            Person.people.get(hus.get("name")).wife = \
                Person.people[hus.get("wife")]
        if "husband" in hus and hus.get("husband"):
            Person.people.get(hus.get("name")).husband = \
                Person.people[hus.get("husband")]
=======
    person_list = [Person(person["name"], person["age"])
                   for person in people]
    for hum in people:
        if "wife" in hum and hum["wife"]:
            Person.people[hum["name"]].wife = Person.people[hum["wife"]]
        if "husband" in hum and hum["husband"]:
            Person.people[hum["name"]].husband = Person.people[hum["husband"]]
>>>>>>> 01ad4f92f5532eafb486f3e0143c39d22245b63b
    return person_list
