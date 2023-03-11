from peewee import Model, FloatField, DateTimeField, ForeignKeyField

from . import db


class BaseModel(Model):
    class Meta:
        database = db


class TempHumSensor(BaseModel):
    temperature = FloatField()
    humidity = FloatField()


class GroundSensor(BaseModel):
    humidity = FloatField()


class TempHumValues(BaseModel):
    timestamp = DateTimeField(formats='%Y-%m-%d %H:%M:%S')
    sensor1 = ForeignKeyField(TempHumSensor, backref='all_values')
    sensor2 = ForeignKeyField(TempHumSensor, backref='all_values')
    sensor3 = ForeignKeyField(TempHumSensor, backref='all_values')
    sensor4 = ForeignKeyField(TempHumSensor, backref='all_values')


class GroundValues(BaseModel):
    timestamp = DateTimeField(formats='%Y-%m-%d %H:%M:%S')
    sensor1 = ForeignKeyField(GroundSensor, backref='all_values')
    sensor2 = ForeignKeyField(GroundSensor, backref='all_values')
    sensor3 = ForeignKeyField(GroundSensor, backref='all_values')
    sensor4 = ForeignKeyField(GroundSensor, backref='all_values')
    sensor5 = ForeignKeyField(GroundSensor, backref='all_values')
    sensor6 = ForeignKeyField(GroundSensor, backref='all_values')


class SystemParams(BaseModel):
    min_air_temp = FloatField()
    max_air_temp = FloatField()
    min_air_hum = FloatField()
    max_air_hum = FloatField()
    min_ground_hum = FloatField()
    max_ground_hum = FloatField()
    request_timeout = FloatField()
