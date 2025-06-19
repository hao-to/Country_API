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
common_name = data["name"]["common"]


def show_menu():
    print(f"\nWhat would you like to know about {common_name.title()}?")
    print("1 - General information")
    print("2 - Population and area")
    print("3 - Languages")
    print("4 - Currency")
    print("5 - Borders")
    print("6 - Show flag")
    print("7 - Fun fact")
    print("0 - Exit")


def handle_choice(choice, data):
    if choice == "1":
        official_name = data["name"]["official"]
        capital = data["capital"][0] if "capital" in data else "Unknown"
        region = data.get("region", "Unknown")
        subregion = data.get("subregion", "Unknown")

        print(f"Official name: {official_name}")
        print(f"Capital city: {capital}")
        print(f"Region: {region} / {subregion}")

    elif choice == "2":
        population = data.get("population", 0)
        area = int(data.get("area", 0))
        density = population / area if area else 0
        print(f"Population: {population:,}")
        print(f"Area: {area:,} km²")
        print(f"(👉 That means, on average, you’ll find about {density:.0f} people per km² in {common_name}.)")

    elif choice == "3":
        languages = data.get("languages", {})
        if languages:
            language_list = ", ".join(languages.values())
            print(f"Languages spoken in {common_name}: {language_list}")
        else:
            print("No language data available.")
    elif choice == "4":
        currencies = data.get("currencies", {})
        if currencies:
            for code, currency in currencies.items():
                name = currency.get("name", "Unknown")
                symbol = currency.get("symbol", "?")
                print(f"{name} ({code}) – Symbol: {symbol}")
        else:
            print("No currency data available.")

    else:
        print("Option not implemented yet.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "0":
            print(f"Hmm, so... you're done here? "
                  f"\nOr have you caught the travel bug for {common_name}?"
                  f"\nBon voyage and good-bye 👋 🧳 ✈️!")
            break
        handle_choice(choice, data)


if __name__ == "__main__":
    main()
