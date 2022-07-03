$ git clone https://github.com/bl4dylion4ik/test_faas.git

$ cd test_faas

$ virtualenv venv

$ source venv/bin/activate

$ pip install requests

$ deactivate

$ zip -r currency.zip venv \_\_main__.py

$ ibmcloud fn action create get_currency currency.zip --kind python:3.9

$ ibmcloud fn api create /currency /rate post get_currency --response-type json
