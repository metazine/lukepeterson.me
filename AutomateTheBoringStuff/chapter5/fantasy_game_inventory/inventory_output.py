def main():
    stuff = {'rope': 1, 'sword': 1, 'gold coins': 123}

    displayInventory(stuff)

def displayInventory(inventory):
    print("Inventory: ")
    itemTotal = 0
    for name, value in inventory.items():
        print(value, name)
        itemTotal += value
    print("Total number of items:", itemTotal)
    
if __name__ == "__main__":
    main()