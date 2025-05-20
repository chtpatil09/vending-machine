
from vending_machine.machine import VendingMachine

def main():
    vm = VendingMachine()
    print("Welcome to the Water Vending Machine!")
    print("Insert coins (1, 2, 5, 10) and select still or fizzy")

    try:
        while True:
            cmd = input("Command (insert/buy/quit): ").strip().lower()
            if cmd == "insert":
                coin = int(input("Insert coin: "))
                vm.insert_coin(coin)
                print(f"Balance: {vm.balance}")
            elif cmd == "buy":
                item = input("Enter item (still/fizzy): ").strip().lower()
                result = vm.buy(item)
                print("Result:", result)
            elif cmd == "quit":
                break
    except KeyboardInterrupt:
        print("\nExiting vending machine.")

if __name__ == "__main__":
    main()
