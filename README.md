# Django CSV to GraphQL API

This is a Django project that reads data from a CSV file and exposes it as a
GraphQL API.

## Demo (Screenshot)

![screenshot](/demo/screenshot.png)

## Prerequisites

- Python 3.x
- pip

## Project Structure

```
django-graphql-api/            # Root project folder
├── mygraphqlproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── schema.py
├── data/                      # Folder for CSV files
│   └── challenges.csv
├── manage.py                  # Django management script
├── requirements.txt           # Project dependencies
├── .gitignore
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repo

```
git clone --url--
```

2. Create a virtual environment

```
python3 -m venv myenv
```

3. Activate the virtual environment:

```
source myenv/bin/activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Run server:

```
python manage.py runserver
```

6. Access the API in the browser and go to:

```
http://127.0.0.1:8000/graphql/
```

and paste below to test the api.

```
{
  challenges {
    challengeId
    challengeName
    challengeSuccessRate
  }
}
```
