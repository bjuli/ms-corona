import requests
from bs4 import BeautifulSoup
import pandas as pd

from ms_corona.utils import pattern_list_matching, number_in_string


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
              "infiziert": number_in_string(pattern_list_matching(r"fiziert|Infektion", event.split("."))),
              "genesen": number_in_string(pattern_list_matching(r"genesen", event.split("."))),
              "gestorben": number_in_string(pattern_list_matching(r"gestorben", event.split("."))),
              "kommentar": event.split(":")[1:]}
             for event in events]

    return pd.DataFrame.from_dict(datas)


def main(webpage: str = "https://www.muenster.de/corona.html"):
    url_content = get_url_content(webpage)
    events = bs_to_list(url_content)
    return create_dataframe(events)


if __name__ == "__main__":
    df = main()
    print(df)

