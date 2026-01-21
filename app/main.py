class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instance_list = []
    for i in range(len(people)):
        person = Person(people[i]["name"], people[i]["age"])
        instance_list.append(person)
        if "wife" in people[i] and people[i]["wife"] is not None:
            person.wife = Person.people.get(people[i]["wife"])
            if person.wife:
                person.wife.husband = person
        elif "husband" in people[i] and people[i]["husband"] is not None:
            person.husband = Person.people.get(people[i]["husband"])
            if person.husband:
                person.husband.wife = person

    return instance_list
