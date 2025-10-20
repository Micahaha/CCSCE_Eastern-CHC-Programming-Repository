## this one was complicated so i used a ton of comments and some ai to try 
## and undertand it better

def main():
    """
    Main program loop to read input.
    """
    while True:
        try:
            # Read a line of input
            line = input()
            # Convert it to an integer
            N = int(line)
            
            # 1. Exit Condition
            if N < 0:
                break
            
            # 2. Special Cases
            if N == 1:
                print("Too small")
            elif N % 2 == 0:
                print(f"{N} is even")
            
            # 3. Main Logic
            else:
                draw_door(N)
                
        except EOFError:
            # Stop if there is no more input
            break
        except ValueError:
            # Stop if the input is not an integer
            break

def draw_door(N):
    mid_point = (N - 1) // 2
    
    for i in range(N):

        row_chars = [' '] * N
        
        if i == 0 or i == N - 1:
            row_chars[0] = '+'
            row_chars[N - 1] = '+'
            for j in range(1, N - 1):
                row_chars[j] = '-'
        
        elif i == mid_point:
            row_chars[0] = '|'
            row_chars[N - 1] = '|'
            row_chars[mid_point] = 'X'
        
        else:
            row_chars[0] = '|'
            row_chars[N - 1] = '|'
            
            row_chars[i] = '\\' 
            
            row_chars[(N - 1) - i] = '/'
        
        print("".join(row_chars))

# Run the main program
if __name__ == "__main__":
    main()