import requests
import wikipedia
import textwrap

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


def get_fun_fact(country_name):
    wikipedia.set_lang("en")
    try:
        return wikipedia.summary(country_name, sentences=2, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        suggestions = ", ".join(e.options[:3])
        return (
            f"Hmm, '{country_name}' could refer to several topics. 🤔\n"
            f"Maybe you meant: {suggestions}..."
        )
    except wikipedia.exceptions.PageError:
        return (
            f"Oh no! Wikipedia doesn't seem to have an article for '{country_name}'. "
            "Double-check the name?"
        )
    except Exception as unexpected_error:
        return f"Unexpected error occurred: {unexpected_error}"


def handle_choice(choice, country_data):
    if choice == "1":
        official_name = country_data["name"]["official"]
        capital = country_data["capital"][0] if "capital" in country_data else "Unknown"
        region = country_data.get("region", "Unknown")
        subregion = country_data.get("subregion", "Unknown")

        print(f"Official name: {official_name}")
        print(f"Capital city: {capital}")
        print(f"Region: {region} / {subregion}")

    elif choice == "2":
        population = country_data.get("population", 0)
        area = int(country_data.get("area", 0))
        density = population / area if area else 0
        print(f"Population: {population:,}")
        print(f"Area: {area:,} km²")
        print(f"(👉 That means, on average, you’ll find about {density:.0f} people per km² in {common_name}.)")

    elif choice == "3":
        languages = country_data.get("languages", {})
        if languages:
            language_list = ", ".join(languages.values())
            print(f"Languages spoken in {common_name}: {language_list}")
        else:
            print("No language data available.")
    elif choice == "4":
        currencies = country_data.get("currencies", {})
        if currencies:
            for code, currency in currencies.items():
                name = currency.get("name", "Unknown")
                symbol = currency.get("symbol", "?")
                print(f"{name} ({code}) – Symbol: {symbol}")
        else:
            print("No currency data available.")
    elif choice == "5":
        borders = country_data.get("borders", [])
        if borders:
            print(f"{common_name} shares land borders with the following countries (by code):")
            print(", ".join(borders))
        else:
            print(f"{common_name} has no land borders.")
    elif choice == "6":
        flag_data = country_data.get("flags", {})
        flag_url = flag_data.get("png") or flag_data.get("svg")
        alt_text = flag_data.get("alt", "Flag description not available.")

        if flag_url:
            print(f"🏳️  Flag of {common_name}:")
            print(f"URL: {flag_url}")
            print(f"Description: {alt_text}")
        else:
            print("No flag data available.")

    elif choice == "7":

        print(f"\n🤓 Fun fact about {common_name}:")
        print("-" * 40)

        fact = get_fun_fact(common_name)
        wrapped_text = textwrap.fill(fact, width=80)  # or 70, 60, depending ond terminal
        print(wrapped_text)

        print("-" * 40)
        print("Okay... maybe not *fun* fun. But hey, still a fact! 😅")
        print("🚧 A real fun fact feature is coming soon (maybe?!)... 👉 stay curious!")

    else:
        print("Option not implemented yet.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if not choice.isdigit() or int(choice) not in range(0, 8):
            print("Invalid input. Please enter a number between 0 and 7.")
            continue
        if choice == "0":
            print(f"Hmm, so... you're done here? "
                  f"\nOr have you caught the travel bug for {common_name}?"
                  f"\nBon voyage and good-bye 👋 🧳 ✈️!")
            break
        handle_choice(choice, data)


if __name__ == "__main__":
    main()
