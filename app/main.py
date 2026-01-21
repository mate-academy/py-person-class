class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        spouse_name = person.get("wife") or person.get("husband")
        if not spouse_name:
            continue

        me = Person.people[person["name"]]
        spouse = Person.people.get(spouse_name)
        if not spouse or spouse is me:
            continue

        if person.get("wife"):
            me.wife = spouse
            spouse.husband = me
        elif person.get("husband"):
            me.husband = spouse
            spouse.wife = me

    return persons
