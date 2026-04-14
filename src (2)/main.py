def inventory_menu():
    inventory = [] 
    
    while True:
        print("\n--- 📦 Hardware Inventory System 📦 ---")
        print("1. Add New Item")
        print("2. Display All Items")
        print("3. Add Tag to Item")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            name = input("Enter Item Name (e.g., Motherboard): ")
            quantity = int(input("Enter Quantity in Stock: "))
            
            location = ("Aisle 4", "Rack B") 
            
            tags_input = input("Enter tags (comma separated, e.g., components, core): ")
            tags = tags_input.split(",")
            
            item = {
                "name": name,
                "quantity": quantity,
                "location": location,
                "tags": [t.strip() for t in tags] 
            }
            
            inventory.append(item)
            print("✅ Item added successfully!")

        elif choice == '2':
            if not inventory:
                print("⚠️ Inventory is currently empty.")
            else:
                for i, item in enumerate(inventory):
                    print(f"{i+1}. {item['name']} | Qty: {item['quantity']} | Location: {item['location'][0]}-{item['location'][1]} | Tags: {', '.join(item['tags'])}")

        elif choice == '3':
            if inventory:
                idx = int(input("Enter item number to update: ")) - 1
                
                if 0 <= idx < len(inventory):
                    new_tag = input("Enter new tag to add: ")
                    inventory[idx]["tags"].append(new_tag.strip())
                    print("✅ Tag updated!")
                else:
                    print("❌ Invalid item number.")
            else:
                print("⚠️ No items in inventory to update.")

        elif choice == '4':
            print("Exiting Inventory System. Goodbye!")
            break
            
        else:
            print("❌ Invalid choice, please enter a number from 1 to 4.")

if __name__ == "__main__":
    inventory_menu()