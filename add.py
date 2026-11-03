def add_func(a,b):
    return a + b

def main():
    print("addition function")
    
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = add_func(a, b)
            print("Result:", result)
        except ValueError:
            print("Error: Please enter valid numbers.")
        except Exception as e:
            print("An unexpected error occurred:", e)
            
if __name__ == "__main__":
    main()