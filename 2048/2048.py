import logic

def print_grid(mat):
    for row in mat:
        print(row)

def main():
    mat = logic.start_game()
    print_grid(mat)
    while True:
        command = input("Press the command: ").strip().lower()
        if command == 'w':
            mat, changed = logic.move_up(mat)
        elif command == 's':
            mat, changed = logic.move_down(mat)
        elif command == 'a':
            mat, changed = logic.move_left(mat)
        elif command == 'd':
            mat, changed = logic.move_right(mat)
        else:
            print("Invalid Key Pressed")
            continue
        
        if changed:
            logic.add_new_2(mat)
        
        print(logic.get_current_state(mat))
        print_grid(mat)
        
        if logic.get_current_state(mat) == 'WON' or logic.get_current_state(mat) == 'LOST':
            break

if __name__ == "__main__":
    main()
