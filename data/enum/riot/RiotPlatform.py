from enum import Enum

class RiotPlatform(Enum):
    KR = ('kr', 'kr')
    EUN1 = ('eun1', 'eune')
    EUW1 = ('euw1', 'euw')
    NA1 = ('na1', 'na')
    LA1 = ('la1', 'las')
    LA2 = ('la2', 'lan')
    BR1 = ('br1', 'br')
    JP1 = ('jp1', 'jp')
    OC1 = ('oc1', 'oce')
    TR1 = ('tr1', 'tr')
    RU = ('ru', 'ru')
    PH2 = ('ph2', 'ph')
    SG2 = ('sg2', 'sg')
    TH2 = ('th2', 'th')
    TW2 = ('tw2', 'tw')
    VN2 = ('vn2', 'vn')

    def __init__(self, riotId, opggId):
        self.riotId = riotId
        self.opggId = opggId

