import sys
import os
import pytest

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

print(f"Project Root added to sys.path: {project_root}")
print(f"Current sys.path: {sys.path}")

try:
    import src
    print("Successfully imported 'src' as a top-level package.")
except ImportError as e:
    print(f"Failed to import 'src' as a top-level package: {e}")

from src.game_theory.equilibria.nash_equilibrium import NashEquilibrium
from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.game_theory.games.battle_of_the_sexes import BattleOfTheSexes
from src.game_theory.games.chicken_game import ChickenGame
from src.game_theory.games.coordination_game import CoordinationGame

def test_prisoner_dilemma_pure_strategy_equilibria():
    game = PrisonerDilemma()
    ne = NashEquilibrium(game)
    equilibria = ne.find_pure_strategy_equilibria()
    assert equilibria == [("Defect", "Defect")]

def test_battle_of_the_sexes_pure_strategy_equilibria():
    game = BattleOfTheSexes()
    ne = NashEquilibrium(game)
    equilibria = ne.find_pure_strategy_equilibria()
    assert set(equilibria) == set([("Opera", "Opera"), ("Football", "Football")])

def test_chicken_game_pure_strategy_equilibria():
    game = ChickenGame()
    ne = NashEquilibrium(game)
    equilibria = ne.find_pure_strategy_equilibria()
    assert set(equilibria) == set([("Swerve", "Straight"), ("Straight", "Swerve")])

def test_coordination_game_pure_strategy_equilibria():
    game = CoordinationGame()
    ne = NashEquilibrium(game)
    equilibria = ne.find_pure_strategy_equilibria()
    assert set(equilibria) == set([("A", "A"), ("B", "B")])

def test_battle_of_the_sexes_mixed_strategy_equilibria():
    game = BattleOfTheSexes()
    ne = NashEquilibrium(game)
    equilibria = ne.find_mixed_strategy_equilibria()
    assert len(equilibria) == 1
    p1_strats, p2_strats = equilibria[0]
    assert p1_strats["Opera"] == pytest.approx(3.0/5.0)
    assert p2_strats["Football"] == pytest.approx(3.0/5.0)

def test_chicken_game_mixed_strategy_equilibria():
    game = ChickenGame()
    ne = NashEquilibrium(game)
    equilibria = ne.find_mixed_strategy_equilibria()
    assert len(equilibria) == 1
    p1_strats, p2_strats = equilibria[0]
    assert p1_strats["Swerve"] == pytest.approx(0.9)
    assert p2_strats["Swerve"] == pytest.approx(0.9)
