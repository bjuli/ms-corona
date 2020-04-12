import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


def get_url_content(url: str) -> BeautifulSoup:
    try:
        response = requests.get(url)
    except ValueError:
        return ("Please provide a url")
    if response.status_code != 200:
        print("The url you provided returned an error: {}".format(response.status_code))
    else:
        return BeautifulSoup(response.text, "lxml")


def bs_to_list(soup: BeautifulSoup) -> list:
    events_element = soup.find_all("ul")[7]
    events_list = events_element.find_all('li')
    return [event.getText() for event in events_list]


def create_dataframe(events: list) -> pd.DataFrame:
    datas = [{"datum": event.split(":")[0],
              "infiziert": number_of_string(r"fiziert|Infektion", event),
              "genesen": number_of_string("genesen", event),
              "gestorben": number_of_string("gestorben", event),
              "Kommentar": event.split(":")[1:]}
             for event in events]
    # fiziert = [pattern_list_matching("fiziert", event.split(".")).isdigit() for event in events]
    # print(datas)
    return pd.DataFrame.from_dict(datas)


def convert_written_out_number(str_num: str) -> int:
    number_dict = {"ein": 1,
                   "eine": 1,
                   "zwei": 2,
                   "drei": 3,
                   "vier": 4,
                   "fünf": 5,
                   "sechs": 6,
                   "sieben": 7,
                   "acht": 8,
                   "neun": 9
                   }
    if str_num in number_dict.keys():
        return int(number_dict[str_num])
    else:
        return int(str_num)

def number_of_string(pattern: str, text: str) -> list:
    results = re.findall(r'\d+|eine|ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun',
                       str(pattern_list_matching(pattern, text.split("."))).lower())
    if len(results) > 0:
        results = results[0]
    else:
        results = 0
    return convert_written_out_number(results)


def pattern_list_matching(pattern: str, str_list: list) -> str:
    pattern_list = [element for element in str_list if re.findall(pattern, element)]
    # print(pattern_list)
    if len(pattern_list) > 0:
        pattern_list = pattern_list[0]
    return pattern_list


if __name__ == "__main__":
    webpage = "https://www.muenster.de/corona.html"
    resp = get_url_content(webpage)
    listes = bs_to_list(resp)
    df = create_dataframe(listes)
    print(df)
    print(convert_written_out_number("sechs"))
    # print(type(listes[0]))
