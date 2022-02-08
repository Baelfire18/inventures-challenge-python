from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from functions import read_data, get_table_headers, get_table_body

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def root():
    headers, data = read_data()

    table_headers = get_table_headers(headers)
    table_body = get_table_body(data)
    
    
    return f'''
    <html>
        <head>
            <title>Company</title>
            <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
        </head>
        <body>
            <h1 class="mt-0 mb-2 text-6xl leading-normal text-center font-sanserif text-gray-50">
                Company
            </h1>
            <div class="flex items-center justify-center">
                <div class="container">
                    <table class="table-header-group flex-row flex-no-wrap w-full my-5 overflow-hidden bg-gray-700 rounded-lg shadow-lg">
                        <thead class="bg-gray-900">
                            <tr class="flex-col table-row mb-2 text-white bg-teal-400 rounded-none rounded-l-lg flex-no wrap">
                            {table_headers}
                            </tr>
                        </thead>
                        <tbody class="flex-1">
                            {table_body}
                        </tbody>
                    </table>
                </div>
            </div>
        </body>
    </html>
    '''
