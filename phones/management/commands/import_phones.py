import csv

from django.apps import apps
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from main.settings import CSV_PATH


class Command(BaseCommand):
    help = 'Creating model objects according the file path and some other options specified'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help="file path")
        parser.add_argument('-d','--delim', type=str, help="delimiter in csv file")
        parser.add_argument('-m_n','--model_name', type=str, help="model name")
        parser.add_argument('-a_n','--app_name', type=str,
                            help="django app name that the model is connected to")

    def handle(self, *args, **options):
        file_path = CSV_PATH
        delim = ';'
        app_name = 'phones'
        model_name = 'Phone'

        if options['path']:
            file_path = options['path']
        if options['delim']:
            delim = options['delim']
        if options['app_name']:
            app_name = options['app_name']
        if options['model_name']:
            model_name = options['model_name']
        _model = apps.get_model(app_name, model_name)
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=delim)
            header = next(reader)
            for row in reader:
                _object_dict = {key: value for key, value in zip(header, row)}
                _object_dict['slug'] = slugify(_object_dict['name'])
                _model.objects.create(**_object_dict)