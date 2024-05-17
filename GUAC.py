from Bio.Seq import Seq
import random
import math
import pprint

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
    """
    GUAC class represents a game where players guess the complement of a DNA sequence.
    """

    def __init__(self):
        self.sequence = None
        self.mRNA_sequence = None
        self.scoreboard = {}
        self.players = {}
        self.game_over = False
    
    def add_player(self, uname, ip):
        """
        Add a player to the game.

        Parameters:
        - uname (str): The username of the player.
        - ip (str): The IP address of the player.
        """
        self.players[uname] = player(uname, ip)
        self.scoreboard[uname] = 0
        
    def generate_sequence(self):
        """
        Generate a random DNA sequence.
        """
        self.sequence = Seq("".join(random.choice("ATGC") for _ in range(20)))

    def checker(self, playerID, complement, timestamp):
        """
        Check if the string is valid.

        Parameters:
        - playerID (str): The ID of the player.
        - complement (str): The complement string to check.
        - timestamp (int): The timestamp of the check.

        Returns:
        - bool: True if the complement is valid, False otherwise.
        """
        if self.sequence[0] == complement:
            return True
        return False
    
    def update_scoreboard(self):
        """
        Update the scoreboard.

        Returns:
        - dict: The updated scoreboard with player usernames as keys and scores as values.
        """
        for player in self.players.values():
            self.scoreboard[player.playerID] = player.score
            
        return self.scoreboard
        
    
    # def convert_to_mRNA(self):
    #     # Convert the DNA sequence to mRNA
    #     self.mRNA_sequence = self.sequence.transcribe()
