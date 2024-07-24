from sqlalchemy import func

import common.DbConnection as db
from entity.LolVersion import LolVersion
from entity.Match import Match

with db.session() as session:
  max_game_version = session.query(Match.gameVersion).order_by(Match.playDatetime.desc()).limit(1).scalar()

  if max_game_version is None or max_game_version == '' or session.query(LolVersion).filter(LolVersion.version == max_game_version).count() != 0:
    exit(0)

  lol_version = LolVersion(max_game_version, func.now())
  session.add(lol_version)
  session.commit()
  print(f"New version added: {max_game_version}")



