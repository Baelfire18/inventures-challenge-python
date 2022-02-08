def read_data():
    with open('db/datos.csv', 'r', encoding='UTF-8') as file:
        lines = [ i.strip().split(',') for i in file.readlines() ]
    table_headers = lines.pop(0)

    lines.sort(key=lambda x: x[4])
    # lines.sort(key=lambda x: int( x[6].split('/')[0] ) )
    lines.sort(key=lambda x: int( x[6].split('/')[1] ) )

    # print(*lines, sep="\n")
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
        for string in row:
            table_row += f'''
                    <td class="p-3 py-4 text-center border border-grey-light">
                        {string}
                    </td>
                    '''
        table_row += '</tr>'
        table_body += table_row
    return table_body
