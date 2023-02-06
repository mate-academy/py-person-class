class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # self.wife = None
        # self.husband = None
        self.__class__.people[name] = self


def create_person_list(people_list: list) -> list:
    person_list = []
    for prs in people_list:
        person = Person(prs["name"], prs["age"])
        spouse = prs.get("wife") or prs.get("husband")
        if spouse:
            if spouse in Person.people:
                spouse_link = Person.people[spouse]
                if "wife" in prs:
                    person.wife = spouse_link
                    spouse_link.husband = person
                else:
                    person.husband = spouse_link
                    spouse_link.wife = person
        person_list.append(person)
    return person_list
