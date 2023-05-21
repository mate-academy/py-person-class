class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"])
              if person["name"] not in Person.people
              else Person.people[person["name"]] for person in people]

    for person in people:
        if "wife" in person:
            wife_husband = "wife"
        elif "husband" in person:
            wife_husband = "husband"
        name_of_wife_husband = person[wife_husband]

        if name_of_wife_husband:
            wife_husband_object = None

            if name_of_wife_husband not in Person.people:
                wife_husband_object = Person(name_of_wife_husband, 0)
            else:
                wife_husband_object = Person.people[name_of_wife_husband]

            if wife_husband == "wife":
                Person.people[person["name"]].wife = wife_husband_object
            else:
                Person.people[person["name"]].husband = wife_husband_object

    return result
