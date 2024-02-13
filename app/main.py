class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    res = []
    for people_data in people:
        person = Person(people_data["name"], people_data["age"])
        if people_data.get("wife") in Person.people:
            person.wife = Person.people[people_data["wife"]]
            person.wife.husband = person
        # it"s bad code, I know, wht cond.should I add to get rid of this code
        # I don"t fully understand it, ChatGPT helped me to refactor my code
        else:
            pass
        if people_data.get("husband") in Person.people:
            person.husband = Person.people[people_data["husband"]]
            person.husband.wife = person
        else:
            pass
        res.append(person)
    return res
