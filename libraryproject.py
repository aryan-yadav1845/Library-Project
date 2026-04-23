import math
# Use a dictionary to manage records
# books = { "Book Name": quantity }
books = {"Python Basics": 5, "Data Science 101": 3}
# issued_records = { "Book Name": {"student": name, "days_allotted": int, "days_taken": int} }
issued_records = {}

def calculate_fine(extra_days):
    """
    Calculates fine based on tiered logic:
    Week 1: 10/day
    Week 2: 10*2/day
    Week 3: 10*2*3/day
    """
    if extra_days <= 0:
        return 0
    
    fine = 0
    weeks_late = math.ceil(extra_days / 7)
    
    for day in range(1, extra_days + 1):
        current_week = math.ceil(day / 7)
        # Factorial-style multiplier: Week 1=1, Week 2=2, Week 3=6, Week 4=24...
        multiplier = math.factorial(current_week)
        fine += 10 * multiplier
    return fine

def add_books():
    print("\n--- ➕ ADD NEW BOOKS ---")
    name = input("Enter the Book name: ").strip()
    qty = int(input(f"How many copies of '{name}' are you adding? "))
    books[name] = books.get(name, 0) + qty
    print(f"✅ Success: {qty} copies of '{name}' added to inventory.")

def show_books():
    print("\n--- 📚 CURRENT INVENTORY ---")
    if not books:
        print("Empty: No books available in the library.")
    else:
        print(f"{'Book Title':<25} | {'Quantity':<10}")
        print("-" * 40)
        for name, qty in books.items():
            if qty > 0:
                print(f"{name:<25} | {qty:<10}")

def issue_books():
    show_books()
    print("\n--- 📖 ISSUE A BOOK ---")
    name = input("Enter the book name to issue: ").strip()

    if name in books and books[name] > 0:
        student = input("Enter Student Name: ").strip()
        days = int(input("Issue for how many days? "))
        
        # Update records
        books[name] -= 1
        issued_records[name] = {
            "student": student,
            "days_allotted": days
        }
        
        print("\n" + "="*30)
        print(f"📝 NOTICE FOR {student.upper()}")
        print(f"Book '{name}' issued for {days} days.")
        print("⚠️  LATE FEE POLICY:")
        print(" - Week 1: 10 Rs/day")
        print(" - Week 2: 20 Rs/day")
        print(" - Week 3: 60 Rs/day")
        print("="*30)
    else:
        print("❌ Error: Book not available or stock empty.")

def return_books():
    print("\n--- 🔙 RETURN A BOOK ---")
    name = input("Enter the name of the book being returned: ").strip()

    if name in issued_records:
        record = issued_records[name]
        days_held = int(input(f"How many days did {record['student']} keep the book? "))
        
        extra_days = days_held - record['days_allotted']
        
        if extra_days > 0:
            fine = calculate_fine(extra_days)
            print(f"⚠️  LATE RETURN: {extra_days} days overdue.")
            print(f"💰 TOTAL FINE APPLIED: {fine} Rs.")
        else:
            print("✅ Returned on time. No fine applied.")

        # Update inventory
        books[name] = books.get(name, 0) + 1
        del issued_records[name]
        print(f"Book '{name}' is now back in stock.")
    else:
        print("❌ Error: This book was not marked as issued in our system.")

def library():
    while True:
        print("\n" + "★"*10 + " LIBRARY MANAGEMENT SYSTEM " + "★"*10)
        print("1. ➕ Add Books")
        print("2. 🔍 Show Available Books")
        print("3. 📑 Issue a Book")
        print("4. 🔄 Return a Book")
        print("5. 🚪 Exit")
        
        try:
            choice = input("\nSelect an option (1-5): ")
            
            if choice == '1':
                add_books()
            elif choice == '2':
                show_books()
            elif choice == '3':
                issue_books()
            elif choice == '4':
                return_books()
            elif choice == '5':
                print("\nShutting down system... Goodbye!")
                break
            else:
                print("❗ Invalid selection. Please choose 1-5.")
        except ValueError:
            print("❗ Input Error: Please enter a valid number.")

if __name__ == "__main__":
    library()