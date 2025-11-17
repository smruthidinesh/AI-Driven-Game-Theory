
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide", page_title="Game Theory Simulator")

from src.game_theory.games.prisoner_dilemma import PrisonerDilemma
from src.game_theory.games.battle_of_the_sexes import BattleOfTheSexes
from src.game_theory.games.chicken_game import ChickenGame
from src.game_theory.games.coordination_game import CoordinationGame
from src.game_theory.games.bayesian_game import BayesianGame
from src.multi_agent.agent import GameAgent

def run_simulation(game_instance, agent1, agent2, rounds):
    payoffs1 = []
    payoffs2 = []
    for _ in range(rounds):
        strategy1 = agent1.strategy
        strategy2 = agent2.strategy
        payoff1, payoff2 = game_instance.play_round(strategy1, strategy2)
        payoffs1.append(payoff1)
        payoffs2.append(payoff2)
    return payoffs1, payoffs2

st.title("Game Theory Simulator")

st.markdown(
    """
    Welcome to the interactive Game Theory Simulator!
    Explore various game theory models, simulate agent interactions, and visualize outcomes.
    Use the sidebar to select a game and configure its parameters.
    """
)

game_options = ["Prisoner's Dilemma", "Battle of the Sexes", "Chicken Game", "Coordination Game", "Bayesian Game"]
selected_game = st.sidebar.selectbox("Select a Game", game_options)

# Game descriptions
game_info = {
    "Prisoner's Dilemma": {
        "rules": "Two prisoners, acting in their own self-interest, do not produce the optimal outcome. Each prisoner can either 'Cooperate' with their partner by staying silent or 'Defect' by betraying them.",
        "how_to_play": "Select a strategy for each agent. 'Cooperate' is generally the best mutual outcome, but 'Defect' is a dominant strategy."
    },
    "Battle of the Sexes": {
        "rules": "A couple wants to go out together but has different preferences. One prefers the 'Opera', and the other prefers 'Football'. They must choose the same activity to get any payoff.",
        "how_to_play": "Choose 'Opera' or 'Football' for each agent. The highest payoffs occur when both choose the same activity."
    },
    "Chicken Game": {
        "rules": "Two drivers drive towards each other. The first to 'Swerve' is the 'chicken'. If neither swerves, they crash. If both swerve, they are both safe.",
        "how_to_play": "Choose 'Swerve' or 'Straight'. 'Straight' is a high-risk, high-reward strategy."
    },
    "Coordination Game": {
        "rules": "Players get a higher payoff when they choose the same action. There are multiple pure strategy Nash equilibria.",
        "how_to_play": "Select 'A' or 'B' for each agent. Payoffs are higher when both agents select the same option."
    },
    "Bayesian Game": {
        "rules": "A game of incomplete information where players have beliefs about the types of other players. This example is a simplified entry game.",
        "how_to_play": "The simulation for this game is pre-calculated. The solution shows the Bayesian Nash Equilibrium."
    }
}

with st.expander("Game Rules and How to Play"):
    info = game_info.get(selected_game)
    if info:
        st.markdown(f"**{selected_game}**")
        st.markdown(f"**Rules:** {info['rules']}")
        st.markdown(f"**How to Play:** {info['how_to_play']}")

base_game_instance = None
if selected_game == "Prisoner's Dilemma":
    game = PrisonerDilemma()
    strategy_options = ["Cooperate", "Defect"]
elif selected_game == "Battle of the Sexes":
    game = BattleOfTheSexes()
    strategy_options = ["Opera", "Football"]
elif selected_game == "Chicken Game":
    game = ChickenGame()
    strategy_options = ["Swerve", "Straight"]
elif selected_game == "Coordination Game":
    game = CoordinationGame()
    strategy_options = ["A", "B"]
elif selected_game == "Bayesian Game":
    st.subheader("Bayesian Game (Simplified Example)")
    # Define a simple 2x2 entry game for demonstration
    players = ["Entrant", "Incumbent"]
    types = {"Incumbent": ["Strong", "Weak"]}
    strategies = {"Entrant": ["Enter", "Stay Out"], "Incumbent": ["Fight", "Accommodate"]}
    payoffs = {
        ("Entrant", None, "Enter", "Fight", "Strong"): -1,
        ("Entrant", None, "Enter", "Accommodate", "Weak"): 1,
        ("Entrant", None, "Stay Out", "Fight", "Strong"): 0,
        ("Entrant", None, "Stay Out", "Accommodate", "Weak"): 0,
        ("Incumbent", "Strong", "Fight", "Enter", None): 1,
        ("Incumbent", "Strong", "Accommodate", "Enter", None): -1,
        ("Incumbent", "Strong", "Fight", "Stay Out", None): 0,
        ("Incumbent", "Strong", "Accommodate", "Stay Out", None): 0,
        ("Incumbent", "Weak", "Fight", "Enter", None): -1,
        ("Incumbent", "Weak", "Accommodate", "Enter", None): 2,
        ("Incumbent", "Weak", "Fight", "Stay Out", None): 0,
        ("Incumbent", "Weak", "Accommodate", "Stay Out", None): 0,
    }
    game = BayesianGame("Entry Game", players, types, strategies, payoffs)
    solution = game.solve()
    st.write("Solution:")
    st.json(solution)
    # Set strategy_options to empty or default as it's not applicable for direct simulation
    strategy_options = []


if selected_game != "Bayesian Game":
    st.sidebar.markdown("### **Agent Strategies**")
    strategy1 = st.sidebar.selectbox("Agent 1 Strategy", strategy_options, index=0)
    strategy2 = st.sidebar.selectbox("Agent 2 Strategy", strategy_options, index=1)

    agent1 = GameAgent("Agent 1", strategy=strategy1)
    agent2 = GameAgent("Agent 2", strategy=strategy2)

    rounds = st.sidebar.slider("Number of Rounds (for single-shot games)", 1, 100, 20)

    if st.sidebar.button("Run Simulation"):
        st.markdown(f"## **{selected_game} Simulation Results**")
        payoffs1, payoffs2 = run_simulation(game, agent1, agent2, rounds)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Total Payoffs")
            st.write(f"  - Agent 1: {sum(payoffs1)}")
            st.write(f"  - Agent 2: {sum(payoffs2)}")
        with col2:
            st.subheader("Payoffs Over Time")
            df = pd.DataFrame({
                'Round': range(1, len(payoffs1) + 1),
                'Agent 1 Payoff': payoffs1,
                'Agent 2 Payoff': payoffs2
            })

            chart = alt.Chart(df.melt('Round', var_name='Agent', value_name='Payoff')).mark_line().encode(
                x='Round',
                y='Payoff',
                color='Agent'
            ).properties(
                title='Payoffs Over Time'
            )
            st.altair_chart(chart, use_container_width=True)

        # Payoff Matrix Heatmap for 2x2 games
        if selected_game in ["Prisoner's Dilemma", "Battle of the Sexes", "Chicken Game", "Coordination Game"]:
            with st.expander("View Payoff Matrix Heatmap"):
                st.subheader("Payoff Matrix Heatmap")
                
                # Extract payoff matrix
                payoff_data = []
                player1_strategies = sorted(list(set([k[0] for k in game.payoff_matrix.keys()])))
                player2_strategies = sorted(list(set([k[1] for k in game.payoff_matrix.keys()])))

                for s1 in player1_strategies:
                    for s2 in player2_strategies:
                        p1_payoff, p2_payoff = game.payoff_matrix[(s1, s2)]
                        payoff_data.append({"Player1 Strategy": s1, "Player2 Strategy": s2, "Agent 1 Payoff": p1_payoff, "Agent 2 Payoff": p2_payoff})
                
                df_payoff = pd.DataFrame(payoff_data)

                # Heatmap for Agent 1 Payoff
                heatmap1 = alt.Chart(df_payoff).encode(
                    x=alt.X('Player2 Strategy:N', title='Agent 2 Strategy'),
                    y=alt.Y('Player1 Strategy:N', title='Agent 1 Strategy'),
                    color=alt.Color('Agent 1 Payoff:Q', scale=alt.Scale(range='heatmap')),
                    tooltip=['Player1 Strategy', 'Player2 Strategy', 'Agent 1 Payoff', 'Agent 2 Payoff']
                ).mark_rect().properties(title='Agent 1 Payoffs')

                text1 = heatmap1.mark_text().encode(
                    text=alt.Text('Agent 1 Payoff:Q', format='.1f'),
                    color=alt.value('black')
                )

                # Heatmap for Agent 2 Payoff
                heatmap2 = alt.Chart(df_payoff).encode(
                    x=alt.X('Player2 Strategy:N', title='Agent 2 Strategy'),
                    y=alt.Y('Player1 Strategy:N', title='Agent 1 Strategy'),
                    color=alt.Color('Agent 2 Payoff:Q', scale=alt.Scale(range='heatmap')),
                    tooltip=['Player1 Strategy', 'Player2 Strategy', 'Agent 1 Payoff', 'Agent 2 Payoff']
                ).mark_rect().properties(title='Agent 2 Payoffs')

                text2 = heatmap2.mark_text().encode(
                    text=alt.Text('Agent 2 Payoff:Q', format='.1f'),
                    color=alt.value('black')
                )
                
                st.altair_chart(heatmap1 + text1, use_container_width=True)
                st.altair_chart(heatmap2 + text2, use_container_width=True)
