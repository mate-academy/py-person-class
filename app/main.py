class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for item in people:
        person = Person(item["name"], item["age"])
        for key in item.keys():
            if key == "wife":
                person.wife = item["wife"]
                person.husband = None
            if key == "husband":
                person.husband = item["husband"]
                person.wife = None
        person_list.append(person)

    for person in person_list:
        if person.wife is not None:
            for i in range(len(person_list)):
                if person.wife == person_list[i].name:
                    person.wife = person_list[i]
        if person.husband is not None:
            for i in range(len(person_list)):
                if person.husband == person_list[i].name:
                    person.husband = person_list[i]
        if person.wife is None:
            del person.wife
        if person.husband is None:
            del person.husband
    return person_list
