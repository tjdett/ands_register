from django.conf import settings
from django.test import TestCase
from tardis.tardis_portal.models import Experiment, Schema, User
from ..publishing import PublishHandler

class SchemaTestCase(TestCase):

    def testSchemaAutoloads(self):
        '''
        Check that the schema will load itself the first time it is needed.
        '''
        print settings.INSTALLED_APPS
        schema = PublishHandler.schema
        assert Schema.objects.filter(namespace=schema).count() == 0
        user = User(username='testuser')
        user.save()
        exp = Experiment(created_by=user)
        exp.save()
        PublishHandler(exp.id)
        assert Schema.objects.filter(namespace=schema).count() == 1
