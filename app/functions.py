from datetime import datetime
from app.params import ROLES

def read_data():
    with open('app/db/datos.csv', 'r', encoding='UTF-8') as file:
        lines = [ i.strip().split(',') for i in file.readlines() ]
    table_headers = lines.pop(0)

    lines.sort(key=lambda x: x[4]) # SORT ALPHANUMERIC BY ROL
    lines.sort(key=lambda x: int( x[6].split('/')[0] ) ) # SORT BY DAY
    lines.sort(key=lambda x: int( x[6].split('/')[1] ) ) # SORT BY MONTH

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
    if aux in ROLES:
        color = ROLES[aux]
    else:
        color = "purple"
    aux = f'''<span class="w-1/3 px-2 pb-1 text-sm font-semibold text-white bg-{color}-600 rounded-full"> 
                {aux}
            </span> '''
    return aux

def get_roles(data):
    roles = list(set([ i[4] for i in data ]))
    roles.sort()
    return roles

def get_resume_table_headers():
    table_headers_info = '<th class="px-3 py-4 text-sm font-semibold uppercase"> Rol </th>'
    for month in range(1, 13):
        table_headers_info += f'''<th class="px-3 py-4 text-sm font-semibold uppercase">
                                      {datetime.strptime(str(month), '%m').strftime('%b')} 
                                  </th>'''
    return table_headers_info

def get_resume_table_body(data, dicc):
    roles = get_roles(data)
    table_body = ''
    for rol in roles:
        table_row = f'''<tr class="flex-col table-row mb-2 flex-no wrap text-white hover:bg-gray-600">
                            <th class="p-3 py-4 text-center border border-grey-light">
                                {get_color_to_rol(rol)}
                            </th>'''
        for i in range(1, 13):
            if rol not in dicc[i]:
                count = 0
            else:
                count = dicc[i][rol]
            table_row += f'''
                    <td class="p-3 py-4 text-center border border-grey-light">
                        {count}
                    </td>
                    '''
        table_row += '</tr>'
        table_body += table_row
    return table_body

def get_resume_dict(data):
    dicc = {}
    for i in range(1, 13):
        dicc[i] = {} 
    for linea in data:
        if linea[4] in dicc[int(linea[6].split('/')[1])]:
            dicc[int(linea[6].split('/')[1])][linea[4]] += 1
        else:
            dicc[int(linea[6].split('/')[1])][linea[4]] = 1
    return dicc
