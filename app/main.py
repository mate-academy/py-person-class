class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for i in people:
        person = Person(i["name"], i["age"])
        result.append(person)

    for i in people:
        person = Person.people[i["name"]]
        if i.get("wife"):
            spouse = Person.people.get(i["wife"])
            if spouse:
                person.wife = spouse
                spouse.husband = person
        if i.get("husband"):
            spouse = Person.people.get(i["husband"])
            if spouse:
                person.husband = spouse
                spouse.wife = person

    return result
