import mongoengine


# Create your models here.

class Wxa_o2o(mongoengine.Document):
    """
    类名就是集合名
    """
    appId = mongoengine.StringField(required=True, max_length=20)
    appSecret = mongoengine.StringField(required=True, max_length=40)
    adminId = mongoengine.StringField(required=True, max_length=15)
    o2oName = mongoengine.StringField(required=True, max_length=20)
    type = mongoengine.IntField(default=2, choices=(1, 2))
    isQmO2O = mongoengine.IntField(default=0, choices=(0, 1))

