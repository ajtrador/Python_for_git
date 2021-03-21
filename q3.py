#June inputs

June2019 = float(input("June 2019:  "))
June2018 = float(input("June 2018:  "))

#calculation
diffjune = June2019 - June2018

#if statement
if diffjune < 0:
    print("June 2018 has more rain than 2019 by " + str(diffjune) + " inches.")
if diffjune > 0:
    print("June 2019 had more rain than 2018 by " + str(diffjune) + " inches.")
if diffjune == 0:
    print("No change")

#July inputs
July2019 = float(input("July 2019:  "))
July2018 = float(input("July 2018:  "))

#calculation
diffjuly = July2019 - July2018

#if statement
if diffjuly < 0:
    print("July 2018 has more rain than 2019 by " + str(diffjuly) + " inches.")
if diffjuly > 0:
    print("July 2019 had more rain than 2018 by " + str(diffjuly) + " inches.")
if diffjuly == 0:
    print("No change")

#August inputs
August2019 = float(input("August 2019:  "))
August2018 = float(input("August 2018:  "))

#calculations
diffaugust = August2019 - August2018

#if statement
if diffaugust < 0:
    print("June 2018 has more rain than 2019 by " + str(diffaugust) + " inches.")
if diffaugust > 0:
    print("June 2019 had more rain than 2018 by " + str(diffaugust) + " inches.")
if diffaugust == 0:
    print("No change")
