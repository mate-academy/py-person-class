class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    married = set()
    for person in people:
        new_person = Person(person["name"], person["age"])
        my_name = new_person.name
        if person.get("husband"):
            husband = person["husband"]
            if husband not in married and Person.people.get(husband):
                new_person.husband = Person.people[husband]
                new_person.husband.wife = new_person
                map(married.add, [husband, my_name])

        if person.get("wife"):
            wife = person["wife"]
            if wife not in married and Person.people.get(wife):
                new_person.wife = Person.people[wife]
                new_person.wife.husband = new_person
                map(married.add, [wife, my_name])

    return list([data for person, data in Person.people.items()])
