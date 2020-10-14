from model.Auto import Auto
from model.Student import Student
from model.Docent import Docent
from model.Persoon import Persoon
from model.Ouder import Ouder


def test_student():
    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "NMCT", 1992)
    studenten = [student1, student2, student3]
    print(f"De studenten: {studenten}")
    print(f"{student1} is de oudste")

    if student1 == student2:
        print("Gelijk")
    else:
        print("Verschillend")

# test_student()


def test_docent():
    docent1 = Docent("Walcarius", "Stijn", 1125234, 1977)
    docent1.geeft_les_in("MCT")

    docent2 = Docent("Laprudence", "Christophe", 1685854, 1980)
    docent2.geeft_les_in("MCT")
    docent2.geeft_les_in("MIT")

    print(docent1)
    print(docent2)

    if (docent1 == docent2):
        print("Gelijk")
    else:
        print("verschillend")


# test_docent()


def werkt_dit():
    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "NMCT", 1992)
    docent1 = Docent("Walcarius", "Stijn", 1125234, 1977)
    docent2 = Docent("Laprudence", "Christophe", 1685854, 1980)
    print(Docent.vereniging)
    print(f"Aantal: {Persoon.geef_aantal_personen()}")

    for p in [student1, student2, student3, docent1, docent2]:
        print(f"{p} is {p.leeftijd} jaren oud.")

    # DOEL: controleren of een variabele een object van een kasse is die erft van een basisklasse
    # werkt wel
    if isinstance(student1, Persoon):
        print("Via isinstance testen of student1 een persoon is")

    # type werkt niet voor controle op basis klasse
    if type(student1) is Persoon:
        print("Via type testen of student1 een persoon is")

    # type werkt enkel voor de subklasse
    if type(student1) is Student:
        print("Via type testen of student1 een student is")


# werkt_dit()


def test_auto():
    student1 = Student("Spriet", "Nick", 199510548, "MCT", 1995)
    docent1 = Docent("Walcarius", "Stijn", 1125234, 1977)
    docent2 = Docent("Laprudence", "Christophe", 1685854, 1980)

    auto1 = Auto("1-HOW-125", docent1)
    auto2 = Auto("1-SWC-123", docent2)
    auto3 = Auto("1-LAP-945", student1)

    for auto in [auto1, auto2, auto3]:
        print(auto)


# test_auto()

# LABO


def test_ouder():

    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "NMCT", 1992)

    ouder1 = Ouder("Spriet", "Marc", 1951)
    ouder1.voeg_student_toe(student1)
    ouder1.voeg_student_toe(student2)
    ouder1.voeg_student_toe(student3)
    print(ouder1)
    print(ouder1.geef_info_studenten())
    print("opleidingen")
    print(ouder1.geef_opleidingen_studenten())
    print(ouder1.geef_info_studenten())
    print(
        f"De verschillende opleidingen van de kinderen zijn: {ouder1.geef_opleidingen_studenten()}")
    # bespreek onderstaande code mbv de verschillende klasses
    print("\nOuder wordt de eigenaar van een auto:")
    auto1 = Auto("1-DVX-656", ouder1)
    print(auto1)
    print("\nOuder geeft auto door aan één van zijn kinderen:")
    auto1.eigenaar = student1
    print(auto1)


test_ouder()
