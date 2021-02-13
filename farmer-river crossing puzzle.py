#Towett has a goat, a dog , a cabbage. He wishes to take them across the river, but can only take them one at a time. If he takes the dog first, the goat will eat the cabbage. if he takes the cabbage first, the dog will eat the goat. The following program helps Towet decide which of his items he should first take across the River.#
import os  
import time 
 
names = {"T": "Towet",
         "D": "Dog",
         "G": "Goat",
         "C": "Cabbage"}
 
forbidden_states = [{"D", "G"}, {"G", "C"}, {"G", "C", "D"}]
 
 
def print_story():
    print("""
#### GROUP 2 RIVER CROSSING PUZZLE ####
 Towet is tasked with taking a goat, cabbage and a dog across the river
How does he do it?
""")
    input("Press enter to continue.")
 
 
def clear():
  
    print("*" * 60, "\n")  
 
 
def print_state(state):
    left_bank, right_bank = state
    print("# CURRENT STATE OF PUZZLE #")
    print()
    left_bank_display = [names[item] for item in left_bank]
    right_bank_display = [names[item] for item in right_bank]
    print(left_bank_display, "|", right_bank_display if right_bank else "[]")
    print()
 
 
def get_move():
    print("Which item do you wish to take across the river?")
    answer = ""
    while answer.upper() not in ["T", "D", "G", "C"]:
        answer = input("Just Towet (t), Dog (d), Goat (g) or Cabbage (c)? ")

 
    return answer.upper()
 
 
def process_move(move, state):
    # We need to "think ahead" to see if move is illegal.
    temp_state = [state[0].copy(), state[1].copy()]
    containing_set = 0 if move in state[0] else 1
    if "T" not in state[containing_set]:
        print("Illegal move.")
        print()
        time.sleep(1)
        return state
    if containing_set == 0:
        temp_state[0].difference_update({move, "T"})
        temp_state[1].update([move, "T"])
    elif containing_set == 1:
        temp_state[1].difference_update({move, "T"})
        temp_state[0].update([move, "T"])
    if temp_state[0] not in forbidden_states and temp_state[1] not in forbidden_states:
        state = [temp_state[0].copy(), temp_state[1].copy()]
    else:
        print("Illegal move.")
        print()
        time.sleep(1)
    print()
    return state
 
 
def is_win(state):
    return state[1] == {"T", "D", "G", "C"}
 
 
def main():
    left_bank = {"T", "D", "G", "C"}
    right_bank = set()
    state = [left_bank, right_bank]
    print_story()
    while not is_win(state):
        clear()
        print_state(state)
        move = get_move()
        state = process_move(move, state)
 
    print("Well done - you solved the puzzle!")
 
 
main()
 
