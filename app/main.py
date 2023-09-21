class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_persons = [0 for _ in range(len(people))]
    people_copy = people[:]
    for i, humain in enumerate(people_copy):
        person = Person(humain["name"], humain["age"])
        if "wife" in humain.keys():
            if humain["wife"]:
                person.wife = humain["wife"]
                for index, humain_ch in enumerate(people_copy):
                    if humain_ch["name"] == humain["wife"]:
                        person_wife = Person(humain_ch["name"],
                                             humain_ch["age"])
                        person.wife = person_wife
                        person_wife.husband = person
                        list_persons[index] = person_wife
                        people_copy.remove(humain_ch)
        else:
            if humain["husband"]:
                person.husband = humain["husband"]
                for index, humain_ch in enumerate(people_copy):
                    if humain_ch["name"] == humain["husband"]:
                        person_husband = Person(humain_ch["name"],
                                                humain_ch["age"])
                        person.husband = person_husband
                        person_husband.wife = person
                        list_persons[index] = person_husband
                        people_copy.remove(humain_ch)
        list_persons[i] = person

    return list_persons
