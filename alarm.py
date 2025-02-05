import requests
import time
import argparse
import winsound
import sys
import datetime

def get_price(crypto):
    url = f"https://www.okx.com/api/v5/market/ticker?instId={crypto}"
    response = requests.get(url)
    data = response.json()
    return float(data["data"][0]["last"])

def main():
    parser = argparse.ArgumentParser(description="Мониторинг цены")
    parser.add_argument("crypto", type=str, help="Торговая пара")
    parser.add_argument("operator", type=str, choices=["<", ">"], help="Оператор сравнения")
    parser.add_argument("price", type=float, help="Необходимая цена")
    parser.add_argument("interval", type=int, help="Интервал реквестов в секундах")
    
    args = parser.parse_args()

    while True:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end=' ')
        try:
            price = get_price(args.crypto)
            print(f"Цена {args.crypto}: {price} USDT")
            
            if args.operator == "<" and price < args.price:
                print("\nЦена упала ниже порога\n")
                winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)
            elif args.operator == ">" and price > args.price:
                print("\nЦена превысила порог\n")
                winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)

        except Exception as e:
            sys.exit(f"Ошибка: {e}")

        time.sleep(args.interval)

if __name__ == "__main__":
    main()

