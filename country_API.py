import requests

# Ask the user for a country name
country = input("Please enter a country name: ")

# Build the API URL and make a request to the REST Countries API
url = f"https://restcountries.com/v3.1/name/{country}?"
response = requests.get(url)
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


def main():
    show_menu()
    choice = input("Enter your choice: ")
    print(f"You selected option {choice}.")


if __name__ == "__main__":
    main()
