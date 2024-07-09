# Using dictionary to find the capital cities of countries in Africa.
countries = {
    "Nigeria": "Abuja",
    "Algeria": "Algiers",
    "Egypt": "Cairo",
    "Libya": "Tripoli",
    "Morocco": "Rabat",
    "Sudan": "Khartoum",
    "Tunisia": "Tunis",
    "Burundi": "Gitega",
    "Comoros": "Moroni",
    "Djibouti": "Djibouti",
    "Eritrea": "Asmara",
    "Ethiopia": "Addis Ababa",
    "Kenya": "Nairobi",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Mozambique": "Maputo",
    "Rwanda": "Kigali",
    "Somalia Mogadishu": "Mogadishu",
    "South Sudan Juba": "Juba",
    "Tanzania": "Dodoma",
    "Seychelles": "Victoria"
}
# Loop through the countries and their capitals.
for country, capital in countries.items():
    # For each country, ask the user the capital.
    answer = input("What is the capital city of " + country + "? ")
    # If correct, say "You are correct!".
    if answer == capital:
        print("You are correct! ")
    # If wrong, say "You are wrong!".
    else:
        print("You are wrong! ")
        break
