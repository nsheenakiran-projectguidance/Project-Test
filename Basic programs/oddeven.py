def main():
    try:
        n = int(input().strip())
        print("even" if n % 2 == 0 else "odd")
    except Exception:
        pass


if __name__ == "__main__":
    main()
