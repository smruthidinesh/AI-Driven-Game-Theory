class Node:
    def __init__(self, player=None, actions=None, payoffs=None, name=None):
        self.player = player  # Player whose turn it is at this node
        self.actions = actions if actions is not None else []  # List of possible actions from this node
        self.payoffs = payoffs  # Payoffs if this is a terminal node (tuple)
        self.children = {}  # Dictionary mapping action to child Node
        self.name = name # Optional name for the node

    def add_child(self, action, child_node):
        self.children[action] = child_node

    def is_terminal(self):
        return not self.children

class GameTree:
    def __init__(self, root_node):
        self.root = root_node

    def build_centipede_game(self, rounds):
        # This method will build a Centipede game tree
        # For simplicity, let's assume 2 players
        
        def build_node(current_round, current_pot, player_to_move):
            node_name = f"R{current_round}P{current_pot}"
            if current_round > rounds:
                # Terminal node: last player passed, both get 0
                return Node(payoffs=(0, 0), name=node_name)
            
            node = Node(player=player_to_move, actions=["Take", "Pass"], name=node_name)
            
            # Action: Take
            if player_to_move == 1:
                take_payoffs = (current_pot, current_pot - 1)
            else:
                take_payoffs = (current_pot - 1, current_pot)
            node.add_child("Take", Node(payoffs=take_payoffs, name=f"{node_name}_Take"))
            
            # Action: Pass
            next_player = 2 if player_to_move == 1 else 1
            next_pot = current_pot * 2
            node.add_child("Pass", build_node(current_round + 1, next_pot, next_player))
            
            return node

        self.root = build_node(1, 1, 1) # Start with round 1, pot 1, Player 1 to move
        return self.root

    def print_tree(self, node=None, indent=0):
        if node is None:
            node = self.root

        prefix = "  " * indent
        if node.is_terminal():
            print(f"{prefix}- {node.name}: Payoffs {node.payoffs}")
        else:
            print(f"{prefix}- {node.name} (Player {node.player})")
            for action, child in node.children.items():
                print(f"{prefix}  Action: {action}")
                self.print_tree(child, indent + 2)
