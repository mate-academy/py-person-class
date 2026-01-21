class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts):
    person_list = [Person(person["name"], person["age"]) for person in people_dicts]
    for person_dict, person_instance in zip(people_dicts, person_list):
        if person_dict.get("wife"):
            person_instance.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband"):
            person_instance.husband = Person.people[person_dict["husband"]]
    return person_list


if __name__ == "__main__":
    people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"},
    ]
    person_list = create_person_list(people)

    print(isinstance(person_list[0], Person))
    print(person_list[0].name == "Ross")
    print(person_list[0].wife is person_list[2])
    print(person_list[0].wife.name == "Rachel")
    print(person_list[1].name == "Joey")
    try:
        print(person_list[1].wife)
    except AttributeError:
        print("AttributeError")
    print(isinstance(person_list[2], Person))
    print(person_list[2].name == "Rachel")
    print(person_list[2].husband is person_list[0])
    print(person_list[2].husband.name == "Ross")
    print(person_list[2].husband.wife is person_list[2])
    print(Person.people == {
        "Ross": person_list[0],
        "Joey": person_list[1],
        "Rachel": person_list[2],
    })