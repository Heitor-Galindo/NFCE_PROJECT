# NFCE 0.2

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

## INSTALATION

1. Start Postgres 14.4.

    ```sh
    ./infrastructure-nfce-database.sh
    ```

2. Create a virtual environment. ( <https://docs.python.org/3/library/venv.html> )

    ```sh
    python3 -m venv env
    source env/bi/activate
    ```

3. Install packages. ( <https://pip.pypa.io/en/stable/cli/pip_install/> )

    ```sh
    pip install -r utils/requirements.txt
    ```

## DOCUMENTATION

---
|APLICATION         |LINK
|:---               |:---
|PSYCOPG 3.1        | <https://www.psycopg.org/psycopg3/docs/index.html>
|POSTGRES 14.4      | <https://www.postgresql.org/docs/current/index.html>
|BEATIFULSOUP 4     | <https://beautiful-soup-4.readthedocs.io/en/latest/#>
|DOTENV             | <https://github.com/theskumar/python-dotenv>
|PYTHON 3.10        | <https://docs.python.org/3/>
|REQUESTS           | <https://requests.readthedocs.io/en/latest/>
|PIP                | <https://pip.pypa.io/en/stable/getting-started/>
|DOCKER ENGINE      | <https://docs.docker.com/engine/>
|DOCKER COMPOSE     | <https://docs.docker.com/compose/>
|UNIDECODE          | <https://pypi.org/project/Unidecode/#description>

---

## TO-DO

create insertion for new qrcode links  
improve products table  
improve vendors tables  
add try/exceptions in functions  
create web interface  
create user area with auth (?)  
