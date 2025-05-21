filename = input("Enter the filename to read: ")

try:
    file = open(filename, 'r')

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied" )

else:
    print("File content: ")
    print(file.read())
    file.close()

finally:
    print("Execution completed (finally block)")