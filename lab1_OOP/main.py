class Bank:
    count = 0

    @staticmethod
    def getCount():
        return Bank.count

    def __init__(self, name, clientNumber, creditNumber):
        Bank.count += 1
        self.name = name
        self.clientNumber = clientNumber
        self.creditNumber = creditNumber

    def __str__(self):
        return f"The name of the bank: {self.name} \n" \
               f"The number of clients of the bank: {self.clientNumber} \n" \
               f"The number of the issued credits of the bank: {self.creditNumber} \n" \

    def __del__(self):
        Bank.count -= 1

def main():
    first_bank = Bank("PrivatBank", 10000000, 5000000)
    second_bank = Bank("MonoBank", 3000000, 1500000)
    third_bank = Bank("AlfaBank", 5000000, 2000000)
    print(first_bank.__str__())
    print(second_bank.__str__())
    print(third_bank.__str__())
    print(f"The amount of objects in this class: {Bank.getCount()} ")

if __name__ == "__main__":
    main()






