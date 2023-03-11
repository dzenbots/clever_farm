import logging

from peewee import SqliteDatabase

from data import DATABASE_PATH, MIN_AIR_TEMP, MAX_AIR_TEMP, MIN_AIR_HUM, MAX_AIR_HUM, MIN_GROUND_HUM, MAX_GROUND_HUM, \
    SENSORS_TIMEOUT_REQUEST

db = SqliteDatabase(database=DATABASE_PATH, pragmas={'foreign_keys': 1})

from .db_models import TempHumSensor, TempHumValues, GroundSensor, GroundValues, SystemParams


def on_startup_sqlite():
    db.connect()
    db.create_tables([
        TempHumSensor,
        TempHumValues,
        GroundSensor,
        GroundValues,
        SystemParams
    ], safe=True)
    logging.info('DB is connected successfully')
    if SystemParams.select().count() < 1:
        SystemParams.create(
            min_air_temp=MIN_AIR_TEMP,
            max_air_temp=MAX_AIR_TEMP,
            min_air_hum=MIN_AIR_HUM,
            max_air_hum=MAX_AIR_HUM,
            min_ground_hum=MIN_GROUND_HUM,
            max_ground_hum=MAX_GROUND_HUM,
            request_timeout=SENSORS_TIMEOUT_REQUEST
        )


def on_shutdown_sqlite():
    db.close()
    logging.info('DB connection closed successfully')


__all__ = [on_startup_sqlite, on_shutdown_sqlite, TempHumSensor, TempHumValues, GroundSensor, GroundValues,
           SystemParams]
