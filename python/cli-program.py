from functions import *

def print_menu():
    print("\nMenu Options:")
    print("1. Search devices")
    print("2. Get parameters")
    print("3. Set parameters")
    print("4. Enter client/device settings")
    print("5. Print menu")
    print("6. Exit")

if __name__ == '__main__':
    while True:
        print_menu()
        command = input('Enter your choice: ')

        if command == '1':
            broadcast = input('Enter broadcast IP address: ')
            search_devices(broadcast)
        elif command == '2':
            get_param(device_id, key, client)
        elif command == '3':
            param_input = input("Enter the params you want to change (e.g., 'Param=Value'): ")
            set_param(device_id, key, client, params=[param_input])
        elif command == '4':
            client = input('Enter client IP address: ')
            device_id = input('Enter unique ID of the device: ')
            key = input('Enter unique key of the device: ')
        elif command == '5':
            print_menu()
        elif command == '6':
            exit(1)
        else:
            print("Invalid option. Please choose a valid option.")