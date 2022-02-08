ROLES = {
    'Ejecutivo': 'green',
    'Gestor': 'yellow',
    'Encargado': 'red',
    'Operador': 'blue'
}

STYLE = '''
        <style>
            html,
            body {{
            height: 100%;
            }}

            @media (min-width: 0px) {{
            table {{
                display: inline-table !important;
            }}

            thead tr:not(:first-child) {{
                display: none;
            }}
            }}

            @media (max-width: 640px) {{
            .container {{
                margin: 0% 10%;
            }}
            }}

            td:not(:last-child) {{
            border-bottom: 0;
            }}

            th:not(:last-child) {{
            border-bottom: 2px solid rgba(0, 0, 0, .1);
            }}
        </style>
'''
