class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    Person.people.clear()
    out_list = []
    out_list = [
        Person(human["name"], human["age"]) for human in people_list
    ]
    for inst, p in zip(out_list, people_list):
        print(inst, p)
        if p.get("wife"):
            inst._wife_name = p["wife"]
        if p.get("husband"):
            inst._husband_name = p["husband"]

    # for human in people_list:
    #     new_person = Person(human["name"], human["age"])
    #     if human.get("husband"):
    #         new_person.husband = human["husband"]
    #     elif human.get("wife"):
    #         new_person.wife = human["wife"]
    #     out_list.append(new_person)

    for name, human in Person.people.items():
        if hasattr(human, "wife"):
            human.wife = Person.people[human.wife]
        elif hasattr(human, "husband"):
            human.husband = Person.people[human.husband]

    return out_list

people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)
