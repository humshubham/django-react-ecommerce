# Django-React E-commerce

An e-commerce website using django at it's backend and React at front-end

## Requirements

Install python3 and run the following command in a terminal.

```python 
#for linux and macOs
pip3 install pipenv

#for windows users
pip install pipenv
```

## Usage

1. Download and extract or git clone this repository

2. Open a terminal in the main repository and run the following command. (It will install all dependencies.)

```python
pipenv install
```
3. Open the virtual environment shell and run the server.

```python
pipenv shell
cd ecom/
python manage.py runserver
```
4. In case of pending migrations, run the following commands in main/ecom/ and restart the server.
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
5. In order to access the admin panel of the project, create a superuser by running the following command in main/ecom/
```python
python manage.py createsuperuser
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)