from typing import Optional


class DailyPuzzle:
    def __init__(self,

                 title: Optional[str, None] = None,
                 url: Optional[str, None] = None,
                 publish_time: Optional[int, None] = None,
                 fen: Optional[str, None] = None,
                 pgn: Optional[str, None] = None,
                 image_url: Optional[str, None] = None,
                 ):
        self.title = title  # example: A Moment of Clarity
        self.url = url  # example: https://www.chess.com/forum/view/daily-puzzles/6-30-2020-a-moment-of-clarity
        self.publish_time = publish_time  # example: 1593500400
        self.fen = fen  # example: r3k2r/1pp2p2/3p2pp/p2Pp2n/1PPnP1bP/P1N1QqP1/2BKNP2/R6R b kq - 0 1
        self.pgn = pgn  # example: [Result "*"]...
        self.image_url = image_url

    class LiveTeamMatchInfo:
        def __init__(self,

                     @ id: Optional[str, None] = None,
                     name: Optional[str, None] = None,
                     url: Optional[str, None] = None,
                     start_time: Optional[int, None] = None,
                     end_time: Optional[int, None] = None,
                     status: Optional[str, None] = None,
                     boards: Optional[int, None] = None,
                     settings: Optional[Settings, None] = None,
                     teams: Optional[Teams, None] = None,
                     ):
            self. @ id =

            @id

        self.name = name
        self.url = url
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.boards = boards
        self.settings = settings
        self.teams = teams


class Settings:
    def __init__(self,

                 rules: Optional[str, None] = None,
                 time_class: Optional[str, None] = None,
                 time_control: Optional[int, None] = None,
                 time_increment: Optional[int, None] = None,
                 min_team_players: Optional[int, None] = None,
                 min_required_games: Optional[int, None] = None,
                 autostart: Optional[bool, None] = None,
                 ):
        self.rules = rules

    self.time_class = time_class
    self.time_control = time_control
    self.time_increment = time_increment
    self.min_team_players = min_team_players
    self.min_required_games = min_required_games
    self.autostart = autostart


class Teams:
    def __init__(self,

                 team1: Optional[Team1, None] = None,
                 team2: Optional[Team2, None] = None,
                 ):
        self.team1 = team1

    self.team2 = team2


class Team1:
    def __init__(self,

                 id: Optional[str, None] = None,
                 name: Optional[str, None] = None,
                 url: Optional[str, None] = None,
                 score: Optional[int, None] = None,
                 result: Optional[str, None] = None,
                 players: Optional[list, None] = None,
                 fair_play_removals: Optional[list, None] = None,
                 ):
        self.id = id

        self.name = name
        self.url = url
        self.score = score
        self.result = result
        self.players = players
        self.fair_play_removals = fair_play_removals


class Team2:
    def __init__(self,
                 id: Optional[str, None] = None,
                 name: Optional[str, None] = None,
                 url: Optional[str, None] = None,
                 score: Optional[int, None] = None,
                 result: Optional[str, None] = None,
                 players: Optional[list, None] = None,
                 fair_play_removals: Optional[list, None] = None,
                 ):
        self. id = id
        self.name = name
        self.url = url
        self.score = score
        self.result = result
        self.players = players
        self.fair_play_removals = fair_play_removals