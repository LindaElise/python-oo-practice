"""Word Finder: finds random words from a dictionary."""
"""Getting a random number fuction from python module"""
import random
class WordFinder:
    ...
    def __init__(self,path):
        """It reports the number of items read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """List the list of words"""
        return [w.strip() for w in dict_file]
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
"""swf = SpecialWordFinder("complex.txt")
    3 words read"""
    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]