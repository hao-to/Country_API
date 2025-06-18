import requests

# Ask the user for a country name
country = input("Please enter a country name: ")

# Build the API URL and make a request to the REST Countries API
url = f"https://restcountries.com/v3.1/name/{country}"
response = requests.get(url)

if response.status_code != 200:
    print("Country not found. Please check your spelling and try again.")
    exit()

data = response.json()[0]


def show_menu():
    print(f"\nWhat would you like to know about {country.title()}?")
    print("1 - General information")
    print("2 - Population and area")
    print("3 - Languages")
    print("4 - Currency")
    print("5 - Borders")
    print("6 - Show flag")
    print("7 - Fun fact")
    print("0 - Exit")


def handle_choice(choice, data):
    if choice == "2":
        population = data.get("population", "Unknown")
        area = data.get("area", "Unknown")
        print(f"Population: {population}")
        print(f"Area: {area} km²")
    elif choice == "0":
        print("Goodbye!")
    else:
        print("Option not implemented yet.")



def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "0":
            print("Goodbye!")
            break
        handle_choice(choice, data)


if __name__ == "__main__":
    main()
