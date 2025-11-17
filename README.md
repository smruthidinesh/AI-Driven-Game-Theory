# Multi-Agent Systems and Game Theory: A Comprehensive Project

## 🎯 Project Overview

This project demonstrates the intersection of Multi-Agent Systems and Game Theory through practical implementations of classic games, auction mechanisms, and evolutionary dynamics. It serves as both an educational resource and a research platform for understanding strategic behavior in competitive environments.

## 🏗️ Project Architecture

multi_agent_game_theory/
├── 📁 src/                         # Core implementation
│   ├── __init__.py
│   ├── 🎮 game_theory/             # Game theory models
│   │   ├── __init__.py
│   │   ├── games/                  # Classic games
│   │   │   ├── __init__.py
│   │   │   ├── battle_of_the_sexes.py
│   │   │   ├── bayesian_game.py
│   │   │   ├── bargaining_game.py
│   │   │   ├── chicken_game.py
│   │   │   ├── coalition_formation.py
│   │   │   ├── coordination_game.py
│   │   │   ├── game_tree.py
│   │   │   ├── prisoner_dilemma.py
│   │   │   ├── repeated_game.py
│   │   │   ├── signaling_game.py
│   │   │   ├── sequential_game.py
│   │   │   └── stochastic_game.py
│   │   ├── equilibria/             # Nash equilibrium computation
│   │   │   ├── __init__.py
│   │   │   └── nash_equilibrium.py
│   │   └── auctions/               # Auction mechanisms
│   │       ├── __init__.py
│   │       ├── dutch_auction.py
│   │   ├── english_auction.py
│   │   ├── first_price_sealed_bid_auction.py
│   │   ├── all_pay_auction.py
│   │   ├── combinatorial_auction.py
│   │   └── vickrey_auction.py
│   ├── 🤖 multi_agent/             # Multi-agent system framework
│   │   ├── __init__.py
│   │   ├── agent.py                # Agent implementations
│   │   ├── communication.py        # Agent communication protocols
│   │   ├── environment.py          # Game environments
│   │   ├── q_learning_agent.py     # Q-Learning Agent implementation
│   │   ├── bounded_rational_agent.py # Bounded Rational Agent implementation
│   │   └── evolutionary_agent.py   # Evolutionary Agent implementation
│   ├── 📊 visualization/           # Visualization tools
│   │   ├── __init__.py
│   │   ├── game_plots.py           # Plotting and analysis tools
│   │   └── web_interface.py        # Interactive web interface
│   └── 🚀 advanced/                # Advanced features
│       ├── __init__.py
│       ├── machine_learning.py     # ML agents and RL
│       ├── mechanism_design.py     # Mechanism design algorithms
│       └── network_games.py        # Network game theory
├── 📁 examples/                     # Practical examples
│   ├── auction_simulations.py
│   ├── basic_games.py
│   ├── bayesian_game_example.py
│   ├── case_study_oligopoly.py
│   ├── comprehensive_demo.py
│   ├── game_tree_example.py
│   ├── interactive_demo.py
│   ├── mechanism_design_example.py
│   ├── parallel_simulation_example.py
│   ├── sequential_game_example.py
│   ├── stochastic_game_example.py
│   ├── train_rl_agent_bayesian.py
│   ├── train_rl_agent_sequential.py
│   └── train_rl_agent.py
├── 📁 docs/                         # Documentation
│   └── game_theory_basics.md
├── 📁 tests/                        # Test suite
│   ├── test_agents.py
│   ├── test_auctions.py
│   ├── test_battle_of_the_sexes.py
│   ├── test_bayesian_game.py
│   ├── test_chicken_game.py
│   ├── test_coordination_game.py
│   ├── test_equilibria.py
│   ├── test_games.py
│   └── test_sequential_game.py
├── 📄 requirements.txt             # Python dependencies
├── 📄 setup.py                     # Package installation
└── 📄 README.md                    # This file

## 🧠 Core Features

### 1. **Game Theory Models**
- **Prisoner's Dilemma**: Classic cooperation vs. defection scenario
- **Battle of Sexes**: Coordination game with multiple equilibria
- **Chicken Game**: Brinkmanship and conflict resolution
- **Coordination Game**: Learning dynamics and strategy evolution
- **Bayesian Games**: Games with incomplete information
- **Sequential Games**: Games where players move in a specific order, often represented by game trees
- **Stochastic Games**: Games with uncertainty and randomness
- **Repeated Games**: Games played multiple times, allowing for strategy evolution
- **Signaling Games**: Games with asymmetric information where one player signals their type
- **Bargaining Games**: Models of how players divide a resource or surplus
- **Coalition Formation**: How agents form groups to maximize collective utility

### 2. **Nash Equilibrium Computation**
- **Pure strategy Nash equilibria**: For N-player games.
- **Mixed strategy equilibria**: For 2x2 games.
- Support enumeration algorithms
- Optimization-based methods
- Efficiency analysis

### 3. **Auction Mechanisms**
- **English Auctions**: Open ascending price auctions
- **Dutch Auctions**: Descending price auctions
- **Vickrey Auctions**: Second-price sealed-bid auctions
- **First-Price Sealed-Bid Auctions**: Highest bidder wins and pays their bid
- **All-Pay Auctions**: All bidders pay their bid, highest bidder wins
- **Combinatorial Auctions**: Bidding on bundles of items for complex allocations

### 4. **Multi-Agent Systems**
- **Agent Framework**: Game agents, learning agents, strategic agents
- **Communication Protocols**: Negotiation, coordination, information sharing
- **Environment Simulation**: Dynamic multi-agent environments
- **Auction Agents**: Specialized bidding agents
- **Q-Learning Agents**: Agents that learn optimal strategies through reinforcement learning
- **Bounded Rational Agents**: Agents with cognitive limitations or biases
- **Evolutionary Agents**: Agents whose strategies evolve over generations using genetic algorithms

### 5. **Evolutionary Game Theory**
- **Replicator Dynamics**: Population strategy evolution
- **Evolutionarily Stable Strategies (ESS)**: Invasion resistance analysis
- **Learning Dynamics**: Strategy adaptation over time
- **Fitness Landscapes**: Visualization of evolutionary pressures

### 6. **Advanced Features**
- **Mechanism Design**: VCG mechanisms, Myerson optimal auctions
- **Network Games**: Coordination and contagion on networks
-- **Machine Learning**: Deep Q-Networks, Policy Gradient agents
- **Visualization**: Payoff matrices, strategy spaces, dynamics

## 📜 Game Rules and How to Play

This section provides a brief overview of the rules and interaction mechanisms for each game available in the simulator.

### **Prisoner's Dilemma**
- **Rules**: Two prisoners, acting in their own self-interest, do not produce the optimal outcome. Each can either 'Cooperate' (stay silent) or 'Defect' (betray).
- **How to Play**: Select a strategy for each agent. 'Cooperate' is mutually beneficial, but 'Defect' is a dominant strategy.

### **Battle of the Sexes**
- **Rules**: A couple wants to go out together but has different preferences ('Opera' vs. 'Football'). They must choose the same activity to get any payoff.
- **How to Play**: Choose 'Opera' or 'Football' for each agent. The highest payoffs occur when both select the same activity.

### **Chicken Game**
- **Rules**: Two drivers drive towards each other. The first to 'Swerve' is the 'chicken'. If neither swerves, they crash.
- **How to Play**: Choose 'Swerve' or 'Straight'. 'Straight' is a high-risk, high-reward strategy.

### **Coordination Game**
- **Rules**: Players get a higher payoff when they choose the same action. There are multiple pure strategy Nash equilibria.
- **How to Play**: Select 'A' or 'B' for each agent. Payoffs are higher when both agents select the same option.

### **Bayesian Game**
- **Rules**: A game of incomplete information where players have beliefs about the types of other players.
- **How to Play**: The simulation for this game is pre-calculated and shows the Bayesian Nash Equilibrium.

### **Bargaining Game**
- **Rules**: Two players decide how to divide a surplus. If they fail to agree, they both receive their 'disagreement point' payoff.
- **How to Play**: The simulation finds the Nash Bargaining Solution, which maximizes the product of the players' utilities.

### **Coalition Formation Game**
- **Rules**: A set of players can form coalitions. The value of each coalition is defined by a characteristic function.
- **How to Play**: The simulation can find the 'core' of the game, which is a set of payoff distributions that are stable.

### **Sequential Game (Centipede Game)**
- **Rules**: A sequential game where two players take turns choosing to either 'Take' a growing pot of money or 'Pass' it to the other player, which increases the pot.
- **How to Play**: The simulation solves the game using backward induction, showing that the first player should 'Take' the pot on the first move.

### **Repeated Game**
- **Rules**: A base game (like the Prisoner's Dilemma) is played for a specified number of rounds.
- **How to Play**: Agents can use strategies that depend on the history of the game.

### **Signaling Game**
- **Rules**: One player (the 'Sender') has private information and sends a signal to another player (the 'Receiver'), who then takes an action.
- **How to Play**: The simulation can be used to find pooling or separating equilibria.

### **Stochastic Game**
- **Rules**: A game with a set of states, where the game transitions from one state to another based on the players' actions and a probability distribution.
- **How to Play**: Agents choose actions in each state, and the game evolves over a series of episodes.

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd multi_agent_game_theory

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .

### Basic Usage

python
from src.game_theory.games import PrisonerDilemma
from src.multi_agent.agent import GameAgent

# Create a simple game
game = PrisonerDilemma()
agent1 = GameAgent("Agent1", strategy="Defect")
agent2 = GameAgent("Agent2", strategy="Cooperate")

# Play the game
result = game.play_game(agent1, agent2, rounds=1)
print(f"Payoffs: {result['average_payoff1']:.2f}, {result['average_payoff2']:.2f}")

### Interactive Tutorials

bash
# Launch Jupyter notebook
jupyter notebook notebooks/01_game_theory_basics.ipynb

### Run Examples

bash
# Basic games
python -m examples.basic_games

# Auction simulations
python -m examples.auction_simulations

# Comprehensive demonstration (generates a plot)
python -m examples.comprehensive_demo

# Game Tree Example
python -m examples.game_tree_example

# Mechanism Design Example
python -m examples.mechanism_design_example

# Stochastic Game Example
python -m examples.stochastic_game_example

# Parallel Simulation Example
python -m examples.parallel_simulation_example

# Train RL Agent (Prisoner's Dilemma)
python -m examples.train_rl_agent

# Train RL Agent (Bayesian Game)
python -m examples.train_rl_agent_bayesian

# Train RL Agent (Sequential Game)
python -m examples.train_rl_agent_sequential

# Q-Learning Prisoner's Dilemma Example
python -m examples.q_learning_prisoner_dilemma

# Bounded Rationality Prisoner's Dilemma Example
python -m examples.bounded_rationality_prisoner_dilemma

# Evolutionary Prisoner's Dilemma Example
python -m examples.evolutionary_prisoner_dilemma

## 📚 Educational Value

### **For Students:**
- Interactive Jupyter notebooks with step-by-step tutorials
- Comprehensive examples demonstrating key concepts
- Visual representations of abstract game theory concepts
- Hands-on experience with strategic decision-making

### **For Researchers:**
- Modular, extensible framework for game theory research
- Implementation of cutting-edge algorithms
- Tools for analyzing strategic behavior
- Foundation for developing new game-theoretic models

## 🔬 Research Applications

### **Economics:**
- Market mechanism design and analysis
- Auction theory and mechanism design
- Industrial organization and competition policy

### **Computer Science:**
- Distributed systems and algorithm design
- Multi-agent learning and coordination
- Mechanism design for online platforms

### **Social Sciences:**
- Understanding cooperation and competition
- Political science and international relations
- Behavioral economics and decision-making

### **Artificial Intelligence:**
- Multi-agent learning and coordination
- Strategic reasoning in AI systems
- Mechanism design for AI systems

## 🎓 Key Learning Outcomes

After working with this project, you will understand:

1. **Game Theory Fundamentals**
   - Nash equilibrium and solution concepts
   - Mixed strategies and evolutionary dynamics
   - Mechanism design and auction theory

2. **Multi-Agent Systems**
   - Agent architectures and communication protocols
   - Coordination and cooperation mechanisms
   - Learning and adaptation in multi-agent environments

3. **Practical Implementation**
   - Algorithm design and optimization
   - Visualization and analysis tools
   - Real-world applications and case studies

## 🛠️ Technical Features

- **30+ Python files** implementing core functionality
- **4 main modules**: Game Theory, Multi-Agent Systems, Auctions, Visualization
- **6 classic games** with full implementations
- **3 auction mechanisms** with strategy analysis
- **Multiple agent types** with different learning capabilities
- **Comprehensive test suite** covering all major features
- **Interactive Jupyter notebooks** for hands-on learning

## 📊 Project Statistics

- **Lines of Code**: 5,000+ lines of well-documented Python
- **Test Coverage**: Comprehensive test suite for all modules
- **Documentation**: Extensive documentation and examples
- **Dependencies**: Minimal dependencies for easy installation
- **Compatibility**: Python 3.8+ with cross-platform support

## 🔧 Dependencies

numpy>=1.21.0
matplotlib>=3.5.0
scipy>=1.7.0
pandas>=1.3.0
scikit-learn>=1.0.0
jupyter>=1.0.0
seaborn>=0.11.0
plotly>=5.0.0
networkx>=2.6.0
pytest>=6.0.0
torch>=1.9.0  # For machine learning features
```

## 🧪 Testing

bash
# Run all tests
python -m pytest

# Run specific test modules
python -m pytest tests/test_games.py
python -m pytest tests/test_agents.py

# Run with coverage
python -m pytest --cov=src tests/

## 📖 Documentation

- **Theoretical Foundations**: `docs/game_theory_basics.md`
- **Interactive Tutorials**: `notebooks/01_game_theory_basics.ipynb`
- **API Documentation**: Generated from docstrings
- **Examples**: Comprehensive examples in `examples/` directory

## 🤝 Contributing

Contributions are welcome! Please see the contributing guidelines for more information.

### Development Setup

bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov

# Run tests
python -m pytest tests/

# Run examples
python examples/comprehensive_demo.py

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

This project builds upon the rich literature in game theory, multi-agent systems, and mechanism design. Special thanks to the open-source community for the excellent libraries that made this project possible.

## 🚀 Interactive Simulation

This project includes an interactive web-based demonstration built with Streamlit.

First, ensure you have the necessary dependencies installed:
bash
pip install -r requirements.txt

To run the simulator, use the following command:
bash
streamlit run src/visualization/web_interface.py

This will open a new tab in your browser with the interactive simulator, where you can:
- Select from various classic game theory models.
- Read the rules and instructions for each game directly in the interface.
- Configure agent strategies and simulation parameters.
- Run simulations and visualize the outcomes in real-time.
- Analyze payoff matrices and historical performance.

**This project serves as a complete learning resource and research platform for understanding the fascinating intersection of Multi-Agent Systems and Game Theory.**