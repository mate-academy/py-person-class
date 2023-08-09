class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self

    people_list = []
    for person in people:
        person_temp = Person(person["name"], person["age"])
        if "wife" in person.keys() and person["wife"] is not None:
            wife = Person.people.get(person["wife"])
            if wife:
                person_temp.wife = wife
                wife.husband = person_temp
        elif "husband" in person.keys() and person["husband"] is not None:
            husband = Person.people.get(person["husband"])
            if husband:
                person_temp.husband = husband
                husband.wife = person_temp

        people_list.append(person_temp)

    return people_list
