def prime_factors(n: int):
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while (n % divisor) == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    number = int(input("Enter a number to factorize: "))
    print(f"Prime factors: {prime_factors(number)}")
