import sys

# 간단한 환율 정보 (USD 기준 가정)
# 실제 환율과 다를 수 있으며, 예시용
exchange_rates = {
    "EUR": 0.90,  # 1 USD -> 0.90 EUR (예시 환율)
    "JPY": 135.0, # 1 USD -> 135.0 JPY
    "KRW": 1300.0 # 1 USD -> 1300 KRW
}

def convert_from_usd(amount, rates):
    results = {}
    for currency, rate in rates.items():
        results[currency] = amount * rate
    return results

def main():
    # 명령줄 인자 처리
    # 사용법: python converter.py <amount_in_usd>
    if len(sys.argv) < 2:
        print("Usage: python converter.py <amount_in_usd>")
        sys.exit(1)

    try:
        amount = float(sys.argv[1])
    except ValueError:
        print("Please provide a numeric amount.")
        sys.exit(1)

    # 환율 변환
    converted = convert_from_usd(amount, exchange_rates)

    # 결과 출력
    print(f"\nUSD {amount} is equivalent to:")
    for currency, value in converted.items():
        print(f" - {currency}: {value}")
    print()

if __name__ == "__main__":
    main()
