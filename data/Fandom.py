from dataclasses import dataclass
from datetime import date
from typing import Optional

from dacite import from_dict


@dataclass
class Teams:
    name: Optional[str]
    overviewPage: Optional[str]
    short: Optional[str]
    location: Optional[str]
    teamLocation: Optional[str]
    region: Optional[str]
    organizationPage: Optional[str]
    image: Optional[str]
    twitter: Optional[str]
    youtube: Optional[str]
    facebook: Optional[str]
    instagram: Optional[str]
    discord: Optional[str]
    snapchat: Optional[str]
    vk: Optional[str]
    subreddit: Optional[str]
    website: Optional[str]
    rosterPhoto: Optional[str]
    isDisbanded: Optional[str]
    renamedTo: Optional[str]
    isLowercase: Optional[str]


@dataclass
class Players:
    id: Optional[str]
    overviewPage: Optional[str]
    player: Optional[str]
    image: Optional[str]
    name: Optional[str]
    nativeName: Optional[str]
    nameAlphabet: Optional[str]
    nameFull: Optional[str]
    country: Optional[str]
    nationality: Optional[str]
    nationalityPrimary: Optional[str]
    age: Optional[str]
    birthdate: Optional[str]
    residencyFormer: Optional[str]
    team: Optional[str]
    team2: Optional[str]
    currentTeams: Optional[list]
    teamSystem: Optional[str]
    team2System: Optional[str]
    residency: Optional[str]
    role: Optional[str]
    favChamps: Optional[list]
    soloqueueIds: Optional[str]
    askfm: Optional[str]
    discord: Optional[str]
    facebook: Optional[str]
    instagram: Optional[str]
    lolpros: Optional[str]
    reddit: Optional[str]
    snapchat: Optional[str]
    stream: Optional[str]
    twitter: Optional[str]
    vk: Optional[str]
    website: Optional[str]
    weibo: Optional[str]
    youtube: Optional[str]
    teamLast: Optional[str]
    roleLast: Optional[str]
    isRetired: Optional[str]
    toWildrift: Optional[str]
    isPersonality: Optional[str]
    isSubstitute: Optional[str]
    isTrainee: Optional[str]
    isLowercase: Optional[str]
    isAutoTeam: Optional[str]
    isLowContent: Optional[str]


def convertFromDict(data_class, data):
    return from_dict(data_class=data_class, data=data)

