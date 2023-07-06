# TP CALYX

This is a final project for Calyx Services at finish of course. Developed in Python 3.10. It is divided into three stages:
1) Create a bot that downloads the last record of transfers, performing the necessary navigation and searches to reach the file.
2) Once downloaded, process the information contained in the file to be able to send it to an API.
3) Develop an API with FastAPI and SQLalchemy. Create the endpoints that are specified in the final project statement.

## Installation

1) Clone the repository
2) Inside the repository in local machine create a virtual environment:

```python
python -m venv .env
```
3) Activate virtual environment

```python
source .env/bin/activate      
```
4) Install the libraries from the requirements.txt file

```python
pip install -r requirements.txt      
```

## Usage

1) Inside the activated virtual environment, run the server

```python
uvicorn main:app --reload   
```

2) From a new terminal run the following command to start the bot

```python
python bot_navigate_dataset.py  
```

Once the process is finished, the information will be available in the API

## Endpoints
### POST
/countries - Receives the info to create a country.

Body example:
```json
{
 "name":"Argentina",
 "code":"ARG", 
 }
```

/provinces - Receives the info to create a province.

Body example:
```json
{
 "name":"Cordoba",
 "code":"79", 
 "country_code":"ARG"
 }
```
/procedures - Receives the information to create a procedure.

Body example:
```json
{
 "code_number":"5478",
 "type":"Transferencia nacional", 
 "province_code":"79"
 }
```

### GET
/countries/{code} - Returns a country based on the code sent.
 
/countries - Returns all countries

/provinces/{code} - Returns a province based on the code sent.

/provinces - Returns all provinces.


/procedures/{code_number} - Returns a procedure based on the code_number sent.

/procedures - Returns all procedures.

/provinces/{code}/procedures_quantity - Returns the number of procedures for a province.

/provinces/{code}/procedures - Returns all the procedures of the indicated province.

