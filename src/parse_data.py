from bs4 import BeautifulSoup
from typing import List
from typing import Union

def parse_table(html_doc: str) -> List[dict]:
    result = []
    ignored = ['Card Type', '\xa0', '']
    soup = BeautifulSoup(html_doc, 'html.parser')

    list_table = soup.find('table', {'class': 'xl7428542'}).tbody.children

    for table_row in list_table:
        row_contents = table_row.contents

        if row_contents[0].text not in ignored:
            result.append({
                'card_type': row_contents[0].text,
                'card_name': row_contents[1].text,
                'advanced_format': row_contents[2].text,
                'traditional_format': row_contents[3].text,
                'remarks': row_contents[4].text.strip() if row_contents[4].text not in ignored else None
            })

    return result

def filter_table_make_diff(parsed_table_data: List[dict]) -> List[dict]:
    return list(filter(lambda item: item['remarks'] is not None, parsed_table_data))

def filter_table_make_subset(parsed_table_data: List[dict], subset: str) -> Union[List[dict], None]:
    subsets = ['Forbidden', 'Limited', 'Semi-Limited', 'Unlimited']

    if subset not in subsets:
        return None

    return list(filter(lambda item: (item['remarks'] is not None) and item['advanced_format'] == subset, parsed_table_data))
