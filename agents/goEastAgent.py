import glob
import logging
import time

import util
from game import Actions, Agent, Directions
from pacman import GameState


class GoEastAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        if Directions.EAST in state.getLegalPacmanActions():
            return Directions.EAST
        else:
            return Directions.STOP