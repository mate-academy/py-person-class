class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = list()
    for person in people:
        temp_person = Person(person["name"], person["age"])
        if person.get("wife"):
            temp_person.wife = Person.people.get(person["wife"])
            if temp_person.wife:
                temp_person.wife.husband = temp_person
        if person.get("husband"):
            temp_person.husband = Person.people.get(person["husband"])
            if temp_person.husband:
                temp_person.husband.wife = temp_person
        person_list.append(temp_person)
    return person_list
