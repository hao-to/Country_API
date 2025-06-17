import requests

# Ask the user for a country name
country = input("Please enter a country name: ")

# Build the API URL and make a request to the REST Countries API
url = f"https://restcountries.com/v3.1/name/{country}"
response = requests.get(url)
data = response.json()[0]

# Print the full response data (just for exploration)
print(data)

# Test if pulling specific info like population works
print(f"Population: {data.get('population', 'Unknown')}")
