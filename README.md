# Bungalow Property Management Service

### Note
- This is my fist time developing a Django web service.
- I have used pycharm as IDE and `pipenv` for python package management. 
- I have used the default sqlite3. 
- Data will be imported from csv only on first import. I have used zillow_id as unique id in the record. Hence, a record with the same zillow_id will not be accepted again.
- I have created a super user account 'maruthi' (pwd:Ia3doinggood) to work with DB

### Assumptions
1. Pagination is needed
2. For 'Price' property I used character field as it is having $ and M. With some preprocessing, Decimal type can be used.
3. I assumed the zillo_id is unique and will always be provided as input. So, I did not create any unique ID for the db records.
4. Caching does not need to be implemented for queries


## Instructions
1. Clone the repository
2. Install pipenv
3. Run `pipenv update`
4. Start the Django application
5. The command implemented to ingest the data is ```ingestdata```. The command can be run  as follows: 
``
python manager.py ingestdata .\challenge_data.csv
``


## API Specs
I have created a swagger OpenAPI specification and it is published on the following link.<br>
[Bungalow Property Management APIs](https://app.swaggerhub.com/apis/maruthihr/property-management-service/1.0.0)

<br>
<br>
<br>

#### Thank you!!

