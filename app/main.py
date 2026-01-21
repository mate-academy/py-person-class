class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        personage = Person(person["name"], person["age"])\
            if person["name"] not in Person.people\
            else Person.people[person["name"]]
        person_list.append(personage)

    for person in people:
        wife_or_husband = "wife" if "wife" in person else "husband"
        name_of_wife_or_husband = person[wife_or_husband]

        if name_of_wife_or_husband:
            wife_husband_object = None
            if name_of_wife_or_husband not in Person.people:
                wife_husband_object = Person(name_of_wife_or_husband, 0)
            else:
                wife_husband_object = Person.people[name_of_wife_or_husband]

            if wife_or_husband == "wife":
                Person.people[person["name"]].wife = wife_husband_object
            else:
                Person.people[person["name"]].husband = wife_husband_object

    return person_list
