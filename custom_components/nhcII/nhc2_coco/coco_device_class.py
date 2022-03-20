from enum import Enum


class CoCoDeviceClass(Enum):
    SWITCHES = 'switches'
    LIGHTS = 'lights'
    SHUTTERS = 'shutters'
    FANS = 'fans'
    SWITCHED_FANS = 'switched-fans'
    SWITCHED_GENERIC = 'switched-generic'
    THERMOSTATS = 'thermostats'
    #PIR = 'pir'
    GENERIC = 'generic'
