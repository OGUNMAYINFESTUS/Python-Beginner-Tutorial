# Using dictionary to find the capital cities of countries in Africa.
countries = {
    "Nigeria": "Abuja",
    "Algeria": "Algiers",
    "Egypt": "Cairo",
    "Libya": "Tripoli",
    "Morocco": "Rabat"
}
country = input("Enter the name of your country! ")
print("The capital city of " + country + " is " + countries[country])