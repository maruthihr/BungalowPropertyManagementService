from django.core.management.base import BaseCommand, CommandError
from property_manager.serializers import PropertySerializer
from property_manager.models import AreaUnit, Property
import logging
from dateutil.parser import parse
import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('filename', type=str)


    def handle(self, *args, **options):
        # read file
        filename = options['filename']
        logging.info("Reading data from csv file {}".format(filename))
        with open(filename) as file:
            line = file.readline()
            fields = line[:-1].split(",")
            for line in file.readlines():
                values  = line[:-1].split(",")
                # create a dict
                data = dict(zip(fields, values))
                logging.debug('data before validation {}'.format(data))
                # data validation
                self._validate_data_fields(data)
                logging.debug('data after validation {}'.format(data))

                serializer = PropertySerializer(data=data)
                if serializer.is_valid():
                    if not Property.objects.filter(zillow_id=data['zillow_id']).exists():
                        logging.info("Saving record in DB")
                        serializer.save()
                else:
                    print("Error in row {}".format(values))


    def _validate_textchoices(self, key, value, choices):
        if value != '':
            for choice in choices:
                if value not in choice:
                    logging.info("Incompatible choice {} for {}. Saving anyway".format(value, key))
            return True
        else:
            logging.info("Value not specified for {}. Setting to None".format(key))
            return False

    def _convert_date_to_iso(self, key, value):
        logging.debug('date {}'.format(value))
        if value != '':
            try:
                date_object = parse(value)
                iso_date = date_object.date().isoformat()
                logging.debug('iso_date after conversion {}'.format(iso_date))
            except:
                iso_date = datetime.datetime.now().date().isoformat()
                logging.debug('iso_date from current time {}'.format(iso_date))
                logging.error("Invalid date {} for {}".format(value, key))
        else:
            iso_date = datetime.datetime.now().date().isoformat()
        return iso_date

    def _validate_data_fields(self, data):
        for key, value in data.items():
            if key == 'area_unit':
                if not self._validate_textchoices(key, value, AreaUnit.choices):
                    data[key] = 'None'

            if key == 'bathrooms':
                pass

            if key == 'bedrooms':
                if value == '':
                    logging.error('The field {} cannot be empty. Skipping the record'.format(key))

            if key == 'home_size':
                if value == '':
                    data[key] = 0

            if key == 'home_type':
                if value == '':
                    data[key] = 0

            if key == 'last_sold_date':
                # convert the date to ISO or take current date
                data[key] = self._convert_date_to_iso(key, value)

            if key == 'last_sold_price':
                if value == '':
                    data[key] = 0

            if key == 'link':
                if value == '':
                    data[key] = 0

            if key == 'price':
                if value == '':
                    data[key] = 0

            if key == 'property_size':
                if value == '':
                    data[key] = 0

            if key == 'rent_price':
                if value == '':
                    data[key] = 0

            if key == 'rentzestimate_amount':
                if value == '':
                    data[key] = 0

            if key == 'rentzestimate_last_updated':
                data[key] = self._convert_date_to_iso(key, value)

            if key == 'tax_value':
                if value == '':
                    data[key] = 0

            if key == 'tax_year':
                if value == '':
                    data[key] = 0

            if key == 'year_built':
                if value == '':
                    data[key] = 0

            if key == 'zestimate_amount':
                if value == '':
                    data[key] = 0

            if key == 'zestimate_last_updated':
                data[key] = self._convert_date_to_iso(key, value)

            if key == 'zillow_id':
                if value == '':
                    data[key] = 0

            if key == 'address':
                if value == '':
                    data[key] = 0

            if key == 'city':
                if value == '':
                    data[key] = 0

            if key == 'state':
                if value == '':
                    data[key] = 0

            if key == 'zipcode':
                if value == '':
                    data[key] = 0




