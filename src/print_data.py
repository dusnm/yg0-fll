import json
from texttable import Texttable
from typing import List

def print_data_as_table(data: List[dict]) -> None:
    table_header = ['Card Type', 'Card Name', 'Advanced Format', 'Traditional Format', 'Remarks']
    table_data = list(map(lambda item: [item['card_type'], item['card_name'], item['advanced_format'], item['traditional_format'], item['remarks']], data))
    table_data.insert(0, table_header)

    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_max_width(100)
    table.add_rows(table_data)

    print(table.draw())

def print_data_as_json(data: List[dict]) -> None:
    print(json.dumps(data, indent=4))

def print_data(data: List[dict], output_format: str) -> None:
    if output_format == 'table':
        print_data_as_table(data)
    elif output_format == 'json':
        print_data_as_json(data)
    else:
        print('')
