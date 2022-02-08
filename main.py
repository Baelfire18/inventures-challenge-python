from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from functions import read_data, get_table_headers, get_table_body, get_resume_table_body, get_resume_dict, get_resume_table_headers
from params import STYLE, FOOTER

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def root():
    headers, data = read_data()

    table_headers = get_table_headers(headers)
    table_body = get_table_body(data)

    dicc = get_resume_dict(data)
    head_resume = get_resume_table_headers()
    body_resume = get_resume_table_body(data, dicc)
    
    return f'''
    <html>
        <head>
            <title>Company</title>
            <link rel="shortcut icon" href="https://inventures.cl/favicon-32x32.png?v=57fbe07a287dc2f549231ebe0bdda9a7"/>
            <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
            {STYLE}
        </head>
        <body>
            <div class="min-h-screen py-5 bg-gray-400">
                <h1 class="mt-0 mb-2 text-6xl leading-normal text-center font-sanserif text-gray-50">
                    Company
                </h1>
                <div class="flex items-center justify-center">
                    <div class="container">
                        <table class="table-header-group flex-row flex-no-wrap w-full my-5 overflow-hidden bg-gray-700 rounded-lg shadow-lg">
                            <thead class="bg-gray-900">
                                <tr class="flex-col table-row mb-2 text-white bg-teal-600 rounded-none rounded-l-lg flex-no wrap">
                                {head_resume}
                                </tr>
                            </thead>
                            <tbody class="flex-1">
                                {body_resume}
                            </tbody>
                        </table>
                    </div>
                </div>
                <br />
                <div class="flex items-center justify-center">
                    <div class="container">
                        <table class="table-header-group flex-row flex-no-wrap w-full my-5 overflow-hidden bg-gray-700 rounded-lg shadow-lg">
                            <thead class="bg-gray-900">
                                <tr class="flex-col table-row mb-2 text-white bg-teal-600 rounded-none rounded-l-lg flex-no wrap">
                                {table_headers}
                                </tr>
                            </thead>
                            <tbody class="flex-1">
                                {table_body}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            {FOOTER}
        </body>
    </html>
    '''
