# Inventures Challenge Python

This proyect was made as a challenge for <https://inventures.cl/>.

It was developed with [FastApi v0.73](https://fastapi.tiangolo.com/) and it consumes the [CSV data in here](app/db/datos.csv).

You can see the app in production from here:
<https://inventures-challenge-python.herokuapp.com/>

## Start developing

For running this app locally you need to `git clone` this repository and then create and open an enviroment:

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

Then run the app (with reload included):

```bash
uvicorn main:app --reload
```
