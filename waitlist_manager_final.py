# Create a Node class to represent each customer in the waitlist
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            return f"{name} added to the end of the waitlist."
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f"{name} added to the end of the waitlist."
    
    def remove(self, name):
        current = self.head
        previous = None
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return f"Removed {name} from the waitlist."
            previous = current
            current = current.next
        return f"{name} not found."
    
    def print_list(self):
        if not self.head:
            print("The waitlist is empty")
            return
        current = self.head
        print("Current Waitlist:")
        while current:
            print(f"- {current.name}")
            current = current.next

        
        
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    


def waitlist_generator():
    waitlist = LinkedList()
    # Create a new linked list instance
    
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
            print(f"{name} added to the front of the waitlist.")
            # Call the add_front method
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            message = waitlist.add_end(name)
            print(message)
            # Call the add_end method
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            message = waitlist.remove(name)
            print(message)
            # Call the remove method
            
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()
            # Print out the entire linked list using the print_list method.
            
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
if __name__ == "__main__":
    waitlist_generator()


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''

'''
- The waitlist is built using a singly linked list. 
Each customer is represented by a node that stores their name and a reference to the nect node. 
When a name is added to the front or end of the list, a new node is created and linked to the chain. 
Removing a customer name involves finding their node and updating the previous node's next pointer to skip over it. 
Printing the waitlist starts at the head and follows each next pointer until the end so it shows everyone in order.
- The head plays a very important role because it always points to the first customer in the list. 
Without it there wouldnt be a starting point and we couldnt access the rest of the waitlist.
- A real engineer might use a custom list like this for multiple different reasons.
For example, say a resturant needs a waitlist where customers can be added or removed quickly.
Or maybe a music playlist that is constantly being updated. 
A linked list can grow and shrink very easily without having to move all the other elements around, 
which makes them very efficent for these types of operations. '''
