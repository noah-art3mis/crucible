from crucible.classes.Result import Result


class Report:
    def __init__(self):
        self.header: str = ""
        self.results: list[Result] = []
