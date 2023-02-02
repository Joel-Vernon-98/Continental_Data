class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

    def __lt__(self, other):
        return self.name < other.name

    def get_attribute_mode(self, value):
        dictionary = dict()
        for country in self.countries:
            if dictionary.get(country.__dict__[value]) is not None:
                dictionary[country.__dict__[value]] += 1
            elif country.__dict__[value] is not None:
                dictionary[country.__dict__[value]] = 1
        return Continent.largest_dictionary_value(dictionary)

    @staticmethod
    def largest_dictionary_value(input_dictionary: dict):
        result_key = ""
        result_value = 0
        for key, value in input_dictionary.items():
            if value > result_value:
                result_value = value
                result_key = key
        return result_key

    def print_results(self):
        print(f"\nName of Continent: {self.name}",
              f"Currency: {self.get_attribute_mode('currency')}",
              f"Literacy Rate: {self.get_attribute_mode('literacy_rate')}",
              f"Time Zone: {self.get_attribute_mode('time_zone')}",
              f"Main Language: {self.get_attribute_mode('main_lang')}",
              f"Most Spoken Language: {self.get_attribute_mode('most_spoken_lang')}",
              f"Countries:", sep="\n")
        for country in self.countries:
            print(f" {country.name}")
