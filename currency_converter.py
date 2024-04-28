import requests

API_KEY = 'fca_live_PauisHXtMjMeJRbpZGMEp6u3bJ3p3GDWjKbQi4Ew'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCY_DIC = {
    "EUR": "Euro",
    "USD": "US Dollar",
    "JPY": "Japanese Yen",
    "BGN": "Bulgarian Lev",
    "CZK": "Czech Republic Koruna",
    "DKK": "Danish Krone",
    "GBP": "British Pound Sterling",
    "HUF": "Hungarian Forint",
    "PLN": "Polish Zloty",
    "RON": "Romanian Leu",
    "SEK": "Swedish Krona",
    "CHF": "Swiss Franc",
    "ISK": "Icelandic Króna",
    "NOK": "Norwegian Krone",
    "HRK": "Croatian Kuna",
    "RUB": "Russian Ruble",
    "TRY": "Turkish Lira",
    "AUD": "Australian Dollar",
    "BRL": "Brazilian Real",
    "CAD": "Canadian Dollar",
    "CNY": "Chinese Yuan",
    "HKD": "Hong Kong Dollar",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel",
    "INR": "Indian Rupee",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "SGD": "Singapore Dollar",
    "THB": "Thai Baht",
    "ZAR": "South African Rand"
}

for shortcut, fullN in CURRENCY_DIC.items():
    available_currencies = f"{shortcut}: {fullN}"
    print(available_currencies, end="\n")


def currency_ecxhange(base, exhanched=""):
    url = f"{BASE_URL}&base_currency={base}&currencies={exhanched}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]

    except:
        print(f"Invalid currency.")
        return None


def ger_result(data , amount):
    try:
        for key, value in data.items():
            print(f"{key}: {float(amount) * value:.2f}$")

    except:
        print("Please enter number only.")
        main()


def main():
    while True:
        convert = input("Do you want to convert to all currencies? Y/N (q to quit).").upper().strip()
        if convert == "Q":
            break

        elif convert == "Y":
            try:
                base = input("Enter the currency you want exchange from: ").upper().strip()
                amount = input("Enter the amount of money to be converted: $").strip()

            except:
                print("Error Please Enter Numbers only.")
                main()

            data = currency_ecxhange(base)
            if not data:
                print("One of base currinces or converted too not invalid.")
                main()
            del data[base]
            ger_result(data, amount)

        elif convert == "N":
            try:
                base = input("Enter the currency you want exchange from: ").upper().strip()
                exchanged = input("Enter the currency you want exchange too: ").upper().strip()
                amount = input("Enter the amount of money to be converted: $").strip()

            except ValueError :
                print("Error Please Enter Numbers only.")
                main()

            data = currency_ecxhange(base, exchanged)
            if not data:
                print("One of base currinces or converted too not invalid.")
                main()
            ger_result(data, amount)

        else:
            main()


main()