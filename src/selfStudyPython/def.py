#A function is defined using the keyword def.
#Functions allows us to reuse the same block of code
#whenever we want.




def checkPerson(name):
  your_Name = input("Enter your name: ")
  if your_Name == "Andrei":
        print(f"Oh Hello Master {your_Name}")
  else:
        print (f"\nMy name is {name}. I am an artificial intelligence dedicated to serving the Camata bloodline.\n")


def info(version, year, status):
    print(f"version: {version}")
    print ("Year: " + str(year))
    print (f"Status: {status}")



checkPerson("Xen")
info("v1.0.0", 2025, "Offline")




