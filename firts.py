def calculator():
    print("\n=== Modern Calculator ===")
    print("------------------------")
    
    while True:
        print("\n📝 Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Percentage (%)")
        print("8. Modulus (mod)")
        print("9. Exit")
        
        choice = input("\n➡️ Enter operation number (1-9): ")
        
        if choice == '9':
            print("\n👋 Thank you for using the calculator!")
            break
            
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("\n❌ Invalid choice! Please try again.")
            continue
            
        if choice == '6':  # Square Root needs only one number
            num1 = float(input("Enter number: "))
            result = num1 ** 0.5
            print(f"\n✨ Result: √{num1} = {result:.2f}")
            continue
            
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = num1 + num2
            print(f"\n✨ Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"\n✨ Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"\n✨ Result: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("\n❌ Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"\n✨ Result: {num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()