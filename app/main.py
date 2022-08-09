class Person:
    people = dict()

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    out_person_list = []
    for each_people in people:
        person = Person(each_people["name"], each_people["age"])
        if each_people.get("wife", "No key") != "No key":
            key = "wife"
        else:
            key = "husband"
        if each_people[key] is not None:
            spouse = Person.people.get(each_people[key], None)
            if spouse is not None:
                if key == "wife":
                    person.wife = spouse
                    spouse.husband = person
                else:
                    person.husband = spouse
                    spouse.wife = person
        out_person_list.append(person)
    print(out_person_list)
    return out_person_list
