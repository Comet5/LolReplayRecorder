from dataclasses import dataclass
from typing import Optional

from dacite import from_dict


@dataclass
class Summoner:
    accountId: str
    profileIconId: int
    revisionDate: int
    name: str
    id: str
    puuid: str
    summonerLevel: int


@dataclass
class PerkStyleSelection:
    perk: int
    var1: int
    var2: int
    var3: int


@dataclass
class PerkStyle:
    description: str
    selections: list[PerkStyleSelection]
    style: int


@dataclass
class PerkStat:
    defense: int
    flex: int
    offense: int


@dataclass
class Perks:
    statPerks: PerkStat
    styles: list[PerkStyle]


@dataclass
class Challenge:
    # 12AssistStreakCount: int
    abilityUses: Optional[int]
    acesBefore15Minutes: Optional[int]
    alliedJungleMonsterKills: Optional[float]
    baronBuffGoldAdvantageOverThreshold: Optional[int]
    baronTakedowns: Optional[int]
    blastConeOppositeOpponentCount: Optional[int]
    bountyGold: Optional[int]
    buffsStolen: Optional[int]
    completeSupportQuestInTime: Optional[int]
    controlWardTimeCoverageInRiverOrEnemyHalf: Optional[float]
    controlWardsPlaced: Optional[int]
    damagePerMinute: Optional[float]
    damageTakenOnTeamPercentage: Optional[float]
    dancedWithRiftHerald: Optional[int]
    deathsByEnemyChamps: Optional[int]
    dodgeSkillShotsSmallWindow: Optional[int]
    doubleAces: Optional[int]
    dragonTakedowns: Optional[int]
    earliestBaron: Optional[float]
    earliestDragonTakedown: Optional[float]
    earlyLaningPhaseGoldExpAdvantage: Optional[int]
    effectiveHealAndShielding: Optional[float]
    elderDragonKillsWithOpposingSoul: Optional[int]
    elderDragonMultikills: Optional[int]
    enemyChampionImmobilizations: Optional[int]
    enemyJungleMonsterKills: Optional[float]
    epicMonsterKillsNearEnemyJungler: Optional[int]
    epicMonsterKillsWithin30SecondsOfSpawn: Optional[int]
    epicMonsterSteals: Optional[int]
    epicMonsterStolenWithoutSmite: Optional[int]
    flawlessAces: Optional[int]
    fullTeamTakedown: Optional[int]
    gameLength: Optional[float]
    getTakedownsInAllLanesEarlyJungleAsLaner: Optional[int]
    goldPerMinute: Optional[float]
    hadOpenNexus: Optional[int]
    highestCrowdControlScore: Optional[int]
    immobilizeAndKillWithAlly: Optional[int]
    initialBuffCount: Optional[int]
    initialCrabCount: Optional[int]
    jungleCsBefore10Minutes: Optional[float]
    junglerTakedownsNearDamagedEpicMonster: Optional[int]
    kTurretsDestroyedBeforePlatesFall: Optional[int]
    kda: Optional[float]
    killAfterHiddenWithAlly: Optional[int]
    killParticipation: Optional[float]
    killedChampTookFullTeamDamageSurvived: Optional[int]
    killsNearEnemyTurret: Optional[int]
    killsOnOtherLanesEarlyJungleAsLaner: Optional[int]
    killsOnRecentlyHealedByAramPack: Optional[int]
    killsUnderOwnTurret: Optional[int]
    killsWithHelpFromEpicMonster: Optional[int]
    knockEnemyIntoTeamAndKill: Optional[int]
    landSkillShotsEarlyGame: Optional[int]
    laneMinionsFirst10Minutes: Optional[int]
    laningPhaseGoldExpAdvantage: Optional[int]
    legendaryCount: Optional[int]
    lostAnInhibitor: Optional[int]
    maxCsAdvantageOnLaneOpponent: Optional[float]
    maxKillDeficit: Optional[int]
    maxLevelLeadLaneOpponent: Optional[int]
    moreEnemyJungleThanOpponent: Optional[float]
    multiKillOneSpell: Optional[int]
    multiTurretRiftHeraldCount: Optional[int]
    multikills: Optional[int]
    multikillsAfterAggressiveFlash: Optional[int]
    outerTurretExecutesBefore10Minutes: Optional[int]
    outnumberedKills: Optional[int]
    outnumberedNexusKill: Optional[int]
    perfectDragonSoulsTaken: Optional[int]
    perfectGame: Optional[int]
    pickKillWithAlly: Optional[int]
    playedChampSelectPosition: Optional[int]
    poroExplosions: Optional[int]
    quickCleanse: Optional[int]
    quickFirstTurret: Optional[int]
    quickSoloKills: Optional[int]
    riftHeraldTakedowns: Optional[int]
    saveAllyFromDeath: Optional[int]
    scuttleCrabKills: Optional[int]
    skillshotsDodged: Optional[int]
    skillshotsHit: Optional[int]
    snowballsHit: Optional[int]
    soloBaronKills: Optional[int]
    soloKills: Optional[int]
    stealthWardsPlaced: Optional[int]
    survivedSingleDigitHpCount: Optional[int]
    survivedThreeImmobilizesInFight: Optional[int]
    takedownOnFirstTurret: Optional[int]
    takedowns: Optional[int]
    takedownsAfterGainingLevelAdvantage: Optional[int]
    takedownsBeforeJungleMinionSpawn: Optional[int]
    takedownsFirstXMinutes: Optional[int]
    takedownsInAlcove: Optional[int]
    takedownsInEnemyFountain: Optional[int]
    teamBaronKills: Optional[int]
    teamDamagePercentage: Optional[float]
    teamElderDragonKills: Optional[int]
    teamRiftHeraldKills: Optional[int]
    threeWardsOneSweeperCount: Optional[int]
    tookLargeDamageSurvived: Optional[int]
    turretPlatesTaken: Optional[int]
    turretTakedowns: Optional[int]
    turretsTakenWithRiftHerald: Optional[int]
    twentyMinionsIn3SecondsCount: Optional[int]
    unseenRecalls: Optional[int]
    visionScoreAdvantageLaneOpponent: Optional[float]
    visionScorePerMinute: Optional[float]
    wardTakedowns: Optional[int]
    wardTakedownsBefore20M: Optional[int]
    wardsGuarded: Optional[int]

@dataclass
class Participant:
    assists: int
    baronKills: int
    bountyLevel: int
    challenges: Optional[Challenge]
    champExperience: int
    champLevel: int
    championId: int
    championName: str
    championTransform: int
    consumablesPurchased: int
    damageDealtToBuildings: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    deaths: int
    detectorWardsPlaced: int
    doubleKills: int
    dragonKills: int
    firstBloodAssist: bool
    firstBloodKill: bool
    firstTowerAssist: bool
    firstTowerKill: bool
    gameEndedInEarlySurrender: bool
    gameEndedInSurrender: bool
    goldEarned: int
    goldSpent: int
    individualPosition: str
    inhibitorKills: int
    inhibitorTakedowns: int
    inhibitorsLost: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    itemsPurchased: int
    killingSprees: int
    kills: int
    lane: str
    largestCriticalStrike: int
    largestKillingSpree: int
    largestMultiKill: int
    longestTimeSpentLiving: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    magicDamageTaken: int
    neutralMinionsKilled: int
    nexusKills: int
    nexusTakedowns: int
    nexusLost: int
    objectivesStolen: int
    objectivesStolenAssists: int
    participantId: int
    pentaKills: int
    perks: Perks
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    physicalDamageTaken: int
    profileIcon: int
    puuid: str
    quadraKills: int
    riotIdName: str
    riotIdTagline: str
    role: str
    sightWardsBoughtInGame: int
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int
    summoner1Casts: int
    summoner1Id: int
    summoner2Casts: int
    summoner2Id: int
    summonerId: str
    summonerLevel: int
    summonerName: str
    teamEarlySurrendered: bool
    teamId: int
    teamPosition: str
    timeCCingOthers: int
    timePlayed: int
    totalDamageDealt: int
    totalDamageDealtToChampions: int
    totalDamageShieldedOnTeammates: int
    totalDamageTaken: int
    totalHeal: int
    totalHealsOnTeammates: int
    totalMinionsKilled: int
    totalTimeCCDealt: int
    totalTimeSpentDead: int
    totalUnitsHealed: int
    tripleKills: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    unrealKills: int
    visionScore: int
    visionWardsBoughtInGame: int
    wardsKilled: int
    wardsPlaced: int
    win: bool


@dataclass
class Objective:
    first: bool
    kills: int


@dataclass
class Objectives:
    baron: Objective
    champion: Objective
    dragon: Objective
    inhibitor: Objective
    riftHerald: Objective
    tower: Objective


@dataclass
class Ban:
    championId: int
    pickTurn: int



@dataclass
class Team:
    bans: list[Ban]
    objectives: Objectives
    teamId: int
    win: bool


@dataclass
class Info:
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId:	int
    gameMode: str
    gameName: str
    gameStartTimestamp:	int
    gameType: str
    gameVersion: str
    mapId:	int
    participants: list[Participant]
    platformId:	str
    queueId: int
    teams: list[Team]
    tournamentCode:	str

# League
@dataclass
class MiniSeries:
    losses: int
    progress: str
    target: int
    wins: int


@dataclass
class LeagueEntry:
    leagueId: str
    summonerId: str
    summonerName: str
    queueType: str
    tier: str
    rank: str
    leaguePoints: int
    wins: int
    losses: int
    hotStreak: bool
    veteran: bool
    freshBlood: bool
    inactive: bool
    miniSeries: Optional[MiniSeries]


@dataclass
class Metadata:
    dataVersion: str
    matchId: str
    participants: list[str]


@dataclass
class Match:
    metadata: Metadata
    info: Info


def convertFromDict(data_class, data):
    return from_dict(data_class=data_class, data=data)
