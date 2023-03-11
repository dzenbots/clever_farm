from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
DATABASE_PATH = env.str("DATABASE_PATH")
SENSORS_TIMEOUT_REQUEST = env.int("SENSORS_TIMEOUT_REQUEST")

MIN_AIR_TEMP = env.int("MIN_AIR_TEMP")
MAX_AIR_TEMP = env.int("MAX_AIR_TEMP")

MIN_AIR_HUM = env.int("MIN_AIR_HUM")
MAX_AIR_HUM = env.int("MAX_AIR_HUM")

MIN_GROUND_HUM = env.int("MIN_GROUND_HUM")
MAX_GROUND_HUM = env.int("MAX_GROUND_HUM")
