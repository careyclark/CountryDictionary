#CareyClark
#CIS261
#January 28, 2023
#Countries Dictionary

def display_menu():
    print("Country Code Dictionary")
    print()
    print("Command Menu")
    print("view - View a country name")
    print("add - Add a Country")
    print("del - Delete a Country")
    print("exit - Exit Program")
    print()
    
def display_codes(countries):
    codes = list(countries.keys())
    codes.sort() #Sort Country codes
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " " 
    print(codes_line)
    
def view(countries):
    display_codes(countries)
    code = input("Enter your country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country Name:: {name}.\n")
    else:
        print("There is no country with that code.\n")
        
def add(countries):
    code = input("Enter your country code: ")
    code = code.upper() #Convert to uppercase. Codes in Dictionary are UpperCase
    if code in countries: #If value in countries, 
        name = countries[code] #Assign value associated with country to name
        print(f"{name} is already using this code.\n")
    else:
        name = input("Enter country name: ")
        name = name.title() #convert first letter of words to UpperCase
        countries[code] = name # assign entered key(code) to entered name
        print(f"{name} was added.\n")
    
def delete(countries):
    code = input("Enter your country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code) #remove from dictionary the values associated with key(code)
        print(f"{name} was deleted.\n")
    else:
        print("There is no country with that code. \n")
        
def main(): #Create Dictionary. Entries have Key: Value
    countries = {"CA": "Canada",
                 "US": "United States",
                 "MX": "Mexico",    
                }
                
    display_menu()
    while True:
        command = input("Command: ")
        command = command.lower() #assign lowercase value and compare
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "del":
            delete(countries)
        elif command == "exit":   
            print("Bye!")
            break #Exit Loop
        else:
            print("Not a valid command. Please try again.\n")
            
if __name__ == "__main__":
    main()