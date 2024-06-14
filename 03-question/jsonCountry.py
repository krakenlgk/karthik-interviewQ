import json

def count_by_country(data, countries):
    count = 0
    for person in data:
        country = person["person_details"]["details"]["country"]
        if country in countries:
            count += 1
    return count

# Read JSON data from file
with open('data.json', 'r') as file:
    json_data = json.load(file)

# 1. Number of people living in India and USA
india_count = count_by_country(json_data, ["INDIA"])
usa_count = count_by_country(json_data, ["USA"])
print(f"Number of people living in India: {india_count}")
print(f"Number of people living in USA: {usa_count}")

# 2. Number of different countries
countries = set(person["person_details"]["details"]["country"] for person in json_data)
print(f"Number of different countries: {len(countries)}")

# 3. Number of people whose first name is starting with the letter K
names = [person["person_details"]["name"].split()[0] for person in json_data]
k_names_count = sum(1 for name in names if name.startswith("K"))
print(f"Number of people whose first name starts with 'K': {k_names_count}")

# 4. All the different towns in the address (sorted)
towns = set(person["person_details"]["details"]["address"]["detailed"]["town"] for person in json_data)
sorted_towns = sorted(towns)
print("All different towns in the address (sorted):")
for town in sorted_towns:
    print(town)

# 5. Count of people living in each city
city_counts = {}
for person in json_data:
    town = person["person_details"]["details"]["address"]["detailed"]["town"]
    city_counts[town] = city_counts.get(town, 0) + 1

print("\nCount of people living in each city:")
for city, count in city_counts.items():
    print(f"{city}: {count}")
