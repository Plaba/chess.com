from typing import Optional


class DailyPuzzle:
    def __init__(self,
                 title: str = None,
                 url: str = None,
                 publish_time: int = None,
                 fen: str = None,
                 pgn: str = None,
                 image_url: str = None
                 ):
        self.title = title  # example: A Moment of Clarity
        self.url = url  # example: https://www.chess.com/forum/view/daily-puzzles/6-30-2020-a-moment-of-clarity
        self.publish_time = publish_time  # example: 1593500400
        self.fen = fen  # example: r3k2r/1pp2p2/3p2pp/p2Pp2n/1PPnP1bP/P1N1QqP1/2BKNP2/R6R b kq - 0 1
        self.pgn = pgn  # example: [Result "*"]...
        self.image_url = image_url


class Settings:
    def __init__(self,
                 rules: str = None,
                 time_class: str = None,
                 time_control: int = None,
                 time_increment: int = None,
                 min_team_players: int = None,
                 min_required_games: int = None,
                 autostart: bool = None
                 ):
        self.rules = rules
        self.time_class = time_class
        self.time_control = time_control
        self.time_increment = time_increment
        self.min_team_players = min_team_players
        self.min_required_games = min_required_games
        self.autostart = autostart

    @staticmethod
    def _create_from_dict(data: dict):
        return Settings(
            rules=data['rules'],
            time_class=data['time_class'],
            time_control=data['time_control'],
            time_increment=data['time_increment'],
            min_team_players=data['min_team_players'],
            min_required_games=data['min_required_games'],
            autostart=data['autostart']
        )


class LiveMatchTeam:
    def __init__(self,

                 id: str = None,
                 name: str = None,
                 url: str = None,
                 score: int = None,
                 result: str = None,
                 players: list = None,
                 fair_play_removals: list = None
                 ):
        self.id = id
        self.name = name
        self.url = url
        self.score = score
        self.result = result
        self.players = players
        self.fair_play_removals = fair_play_removals

    @staticmethod
    def _create_from_dict(data: dict):
        return LiveMatchTeam(
            id=data['@id'],
            name=data['name'],
            url=data['url'],
            score=data['score'],
            result=data['result'],
            players=data['players'],
            fair_play_removals=data['fair_play_removals']
        )


class LiveTeamMatchInfo:
    def __init__(self,
                 id: str = None,
                 name: str = None,
                 url: str = None,
                 start_time: int = None,
                 end_time: int = None,
                 status: str = None,
                 boards: int = None,
                 settings: Settings = None,
                 teams: list = None
                 ):
        self.id = id
        self.name = name
        self.url = url
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.boards = boards
        self.settings = settings
        self.teams = teams

    @staticmethod
    def _create_from_dict(data: dict):
        return LiveTeamMatchInfo(
            id=data['@id'],
            name=data['name'],
            url=data['url'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            status=data['status'],
            boards=data['boards'],
            settings=Settings._create_from_dict(data['settings']),
            teams=[LiveMatchTeam._create_from_dict(data['teams']['team1']),
                   LiveMatchTeam._create_from_dict(data['teams']['team2'])]
        )