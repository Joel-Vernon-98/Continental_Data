from typing import TextIO, Optional
from split_function import split_function
from country import Country
from continent import Continent


def parse_file(input_file: TextIO) -> dict[str:Continent]:

    def find_literacy_rate(line_parts: list) -> int:
        return int(line_parts[2].strip("\n "))

    def find_name(line_parts: list) -> str:
        return line_parts[0].strip("\n ")

    def find_currency(line_parts: list) -> str:
        return line_parts[1].strip("\n ")

    def find_time_zone(line_parts: list) -> float:
        return float(line_parts[3].strip("\n "))

    def find_continent(line_parts: list) -> str:
        return line_parts[4].strip("\n ")

    def find_main_language(line_parts: list) -> str:
        return line_parts[5].strip("\n ")

    def find_most_spoken_language(line_parts: list) -> Optional[str]:
        try:
            return line_parts[6].strip('\n ')
        except IndexError:
            return None

    # Go through the file line by line and create a new country object for each line. Then, using the continent
    # attribute of the country object, match the country object to its continent.
    continent_dict = dict()
    for line in input_file:
        file_line = split_function(line, ",")
        country_object = Country(name=find_name(file_line),
                                 currency=find_currency(file_line),
                                 literacy_rate=find_literacy_rate(file_line),
                                 time_zone=find_time_zone(file_line),
                                 continent=find_continent(file_line),
                                 main_lang=find_main_language(file_line),
                                 most_spoken_lang=find_most_spoken_language(file_line))

        # Create new entry in continent dictionary if country object is part of a new continent that is not in the
        # dictionary, Otherwise add the country to the list of countries in the correct continent object.
        continent_exist = continent_dict.get(country_object.continent) is not None
        if continent_exist:
            continent_dict[country_object.continent].countries.append(country_object)
            continue
        continent_dict[country_object.continent] = Continent(name=country_object.continent,
                                                             countries=[country_object])
    return continent_dict
