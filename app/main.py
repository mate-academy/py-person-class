class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    our_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        if human.get("husband"):
            person.husband = human["husband"]
        if human.get("wife"):
            person.wife = human["wife"]
        our_list.append(person)

    for item in our_list:
        if hasattr(item, "wife"):
            for i in our_list:
                if i.name == item.wife:
                    item.wife = i

        if hasattr(item, "husband"):
            for i in our_list:
                if i.name == item.husband:
                    item.husband = i

    return our_list
