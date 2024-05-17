from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import random
import math

class player:
    def __init__(self, playerID: int, ip):
        self.playerID = playerID
        self.ip = ip
        #self.mac = MAC
        self.score = 0
        self.multiplier = 1
        self.combo = 0
        
    def update_score(self, score: bool):
        if score:
            self.combo += 1
            self.score += 1 * self.multiplier
        else:
            self.combo = 0
            self.multiplier = 1
        if self.combo > 1:
            self.multiplier = math.log(self.combo, 2)

class GUAC:
    def __init__(self):
        self.sequence = None
        self.mRNA_sequence = None
        self.scoreboard = {}
        self.players = {}
        self.game_over = False
    
    def add_player(self, uname, ip):
        # Add a player to the game
        self.players[uname] = player(uname, ip)
        self.scoreboard[uname] = 0
        
    def generate_sequence(self):
        # Generate a random DNA sequence
        self.sequence = Seq("".join(random.choice("ATGC") for _ in range(20)), generic_dna)

    def checker(self, playerID, complement, timestamp):
        # Check if the string is valid
        if self.sequence[0] == complement:
            return True
        return False
    
    def scoreboard(self):
        # Update the scoreboard
        for player in self.players:
            self.scoreboard[player] = f''
            
        return self.scoreboard
        
    # def convert_to_mRNA(self):
    #     # Convert the DNA sequence to mRNA
    #     self.mRNA_sequence = self.sequence.transcribe()
