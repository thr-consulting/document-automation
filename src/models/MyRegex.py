
from re import Pattern

class MyRegex:
    def __init__(self, groupRegex: Pattern, extractPosition: int):
        self.groupRegex = groupRegex
        self.extractPosition = extractPosition