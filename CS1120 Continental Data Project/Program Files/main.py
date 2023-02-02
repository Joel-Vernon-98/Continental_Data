from continent import Continent
from parse_file import parse_file


def main():

    file_name = input("Enter file name: ")
    try:
        with open(file_name, "r") as file:
            continents = parse_file(file)
    except FileNotFoundError:
        print(f"File {file_name} was not found.")
    else:
        for continent in sorted(continents.values()):
            Continent.print_results(continent)


if __name__ == "__main__":
    main()
