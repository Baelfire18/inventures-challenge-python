# Inventures Challenge Python

You can see the app in production from here:
<https://inventures-challenge-python.herokuapp.com/>

For running this app you need to create and open the enviroment:
```bash
python3 -m venv env
```

```bash
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

Then run the app with reload:

```bash
uvicorn main:app --reload
```
