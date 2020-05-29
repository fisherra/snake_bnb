import mongoengine
import datetime

class Cage(mongoengine.Document): # tell mongo this is a top level document
    registered_date = mongoengine.DateTimeField(default = datetime.datetime.now)

    name = mongoengine.NotRegistered(required = True)
    price = mongoengine.FloatField(required = True)
    square_meters = mongoengine.FloatField(required= True)
    is_carpeted = mongoengine.BooleanField(required = True)
    has_toys = mongoengine.BooleanField(required = True)
    allow_dangerous_snakes = mongoengine.BooleanField(default = False)

    bookings = mongoengine.EmbeddedDocumentListField(Bookings)

    meta = {
        'db_alias': 'core',
        'collection': 'cages'
    }