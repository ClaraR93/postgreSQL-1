from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
os.system('cls')


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

class Places(base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    capital_city = Column(String)
    population = Column(Integer, primary_key=False)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelave",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hoper = Programmer(
    first_name="Grace",
    last_name="Hoper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

clara_reynolds = Programmer (
    first_name = "Clara",
    last_name = "Reynolds",
    gender = "F",
    nationality = "Czech",
    famous_for = "Being kl"
)

czech = Places (
    country = "Czech Republic",
    capital_city = "Prague",
    population = 200000000
)

# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hoper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(clara_reynolds)



# programmer = session.query(Programmer).filter_by(id=9).first() 
# programmer.famous_for = "World President"



# people = session.query(Programmer)
# for person in people:
#    if person.gender == "F":
#        person.gender = "Female"
#    elif person.gender == "M":
#        person.gender = "Male"
#    else: 
#        print("Gender not defined")
#    session.commit()

# fname = input("Enter a name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
# if programmer is not None:
#    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#    confirmation = input("Are you sure you want to delete this record? (y/n) ")
#    if confirmation.lower() == "y":
#        session.delete(programmer)
#        session.commit()
#    else:
#        print("Programmer has not been deleted")
# else:
#   print("No records found")

session.add(czech)
session.commit()

programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )

places = session.query(Places)
for place in places:
    print(
        place.id,
        place.country, 
        place.capital_city,
        place.population,
        sep=" | "
    )


