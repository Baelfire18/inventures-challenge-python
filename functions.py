from datetime import datetime
from params import ROLES

def read_data():
    with open('db/datos.csv', 'r', encoding='UTF-8') as file:
        lines = [ i.strip().split(',') for i in file.readlines() ]
    table_headers = lines.pop(0)

    lines.sort(key=lambda x: x[4])
    # lines.sort(key=lambda x: int( x[6].split('/')[0] ) )
    lines.sort(key=lambda x: int( x[6].split('/')[1] ) )

    return table_headers, lines

def get_table_headers(raw_table_headers):
    table_headers_info = ''
    for table_header in raw_table_headers:
        table_headers_info += f'<th class="px-3 py-4 text-sm font-semibold uppercase"> {table_header.capitalize()} </th>'
    return table_headers_info

def get_table_body(raw_table_body):
    table_body = ''
    for row in raw_table_body:
        table_row = '<tr class="flex-col table-row mb-2 flex-no wrap text-white hover:bg-gray-600">'
        for i in range(len(row)):
            aux = row[i]
            if i == 6:
                aux = format_date(aux)
            elif i == 4:
                aux = get_color_to_rol(aux)
            elif i == 3:
                aux = format_phone_number(aux)

            table_row += f'''
                    <td class="p-3 py-4 text-center border border-grey-light">
                        {aux}
                    </td>
                    '''
        table_row += '</tr>'
        table_body += table_row
    return table_body

def format_date(aux):
    datetime_object = datetime.strptime(aux, '%d/%m/%Y')
    datetime_object = datetime_object.strftime('%d %b')
    return datetime_object

def format_phone_number(aux):
    try:
        return f"""<a href="tel:+56{aux}" class="underline text-blue-600 hover:text-blue-800 visited:text-purple-600">
                +56 {aux[0]} {aux[1:5]} {aux[5::]}
                </a>"""
    except IndexError:
        return aux


def get_color_to_rol(aux):
    try:
        color = ROLES[aux]
    except KeyError:
        color = "purple"
    aux = f'''<span class="w-1/3 px-2 pb-1 text-sm font-semibold text-white bg-{color}-600 rounded-full"> 
                {aux}
            </span> '''
    return aux
