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

FOOTER ='''
    <div class="pt-6">
      <footer id="footer" class="relative z-50 dark:bg-gray-600">
        <div class="flex flex-col items-center justify-center mb-2">
          <p tabindex="0" class="mt-6 text-xs leading-none text-center text-gray-900 focus:outline-none lg:text-sm dark:text-gray-50">
            Made with ❤️ by
              <a href="https://github.com/Baelfire18">José Antonio Castro</a>
          </p>
          <br/>
        </div>
      </footer>
    </div>'''
