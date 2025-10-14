class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    print("My print", people)
    answer = []
    for person in people:
        human = Person(person["name"], person["age"])

        answer.append(human)

    for index, person in enumerate(people):
        if person.get("wife"):
            answer[index].wife = [human
                                  for human in answer
                                  if human.name == person.get("wife")][0]

        if person.get("husband"):
            answer[index].husband = [human
                                     for human in answer
                                     if human.name == person.get("husband")][0]

    return answer
