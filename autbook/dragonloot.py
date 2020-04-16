import pprint
# inventory.py

dragonLoot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print (str(v)+' '+ k)
        item_total+=1
    print("Total number of items: " + str(item_total))
    
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(str(item), 0)
        inventory[item] += 1


while True:
    print ('You are some RPG character. You love items. Let\'s see what you have.')
    input()
    inv = {'gold coin':20,'rope':1}
    dragonLoot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    

    displayInventory(inv)
    print('You killed a dragon!')
    input()
    addToInventory(inv,dragonLoot)
    displayInventory(inv)
    break



