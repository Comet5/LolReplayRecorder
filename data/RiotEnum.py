from enum import Enum


class Region(Enum):
    KR = 'kr'
    NA = 'na1'
    EUW = 'euw1'
    EUNE = 'eun1'
    OCE = 'oc1'
    JP = 'jp1'
    BR = 'br1'
    LAS = 'la2'
    LAN = 'la1'
    RU = 'ru'
    TR = 'tr1'
    SG = 'sg2'
    PH = 'ph2'
    TW = 'tw2'
    VN = 'vn2'
    TH = 'th2'


class QueueType(Enum):
    RANKED_SOLO_5x5 = 'RANKED_SOLO_5x5'
    RANKED_FLEX_SR = 'RANKED_FLEX_SR'
    RANKED_FLEX_TT = 'RANKED_FLEX_TT'