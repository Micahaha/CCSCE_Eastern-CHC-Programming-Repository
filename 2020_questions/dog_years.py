## super easy, took like five minutes

def main():

    while True:
     dog_years = input("name and age for dog years")
     if "quit" in dog_years:
         break
     
     name, age = dog_years.split()   
     print(f"{name} is {int(age) * 7} years old in dog years")

main()