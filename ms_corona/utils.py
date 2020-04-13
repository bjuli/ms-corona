import re

def convert_written_out_number(str_num: str) -> str:
    number_dict = {"ein ": 1,
                   "eine ": 1,
                   "zwei ": 2,
                   "drei ": 3,
                   "vier ": 4,
                   "fünf ": 5,
                   "sechs ": 6,
                   "sieben ": 7,
                   "acht ": 8,
                   "neun ": 9
                   }
    if str_num in number_dict.keys():
        return number_dict[str_num]
    else:
        return str_num


def pattern_list_matching(pattern: str, str_list: list) -> str:
    pattern_list = [element for element in str_list if re.findall(pattern, element)]
    if len(pattern_list) > 0:
        pattern_list = pattern_list[0]
    return pattern_list


def number_in_string(text: str) -> int:
    results = re.findall(r'\d+|eine |ein |zwei |drei |vier |fünf |sechs |sieben |acht |neun ', str(text).lower())
    if len(results) > 0:
        results = results[0]
    else:
        results = 0
    return int(convert_written_out_number(results))
