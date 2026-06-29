def odd_or_even(n):
    return "even" if n % 2 == 0 else "odd"

if __name__ == "__main__":
    try:
        value = int(input().strip())
        print(odd_or_even(value))
    except Exception:
        print("Please enter a valid integer.")
