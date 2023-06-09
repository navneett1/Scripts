import argparse

def add_value_after_alternates(value, my_list, position):
    new_list = []
    for i, item in enumerate(my_list):
        new_list.append(item)
        if i % position == position - 1:
            new_list.append(value)
    return new_list

def create_file_with_list(file_path, my_list):
    with open(file_path, 'w') as file:
        file.write('\n'.join(my_list))
    print(f"File '{file_path}' created successfully!")

def merge(args):
    # Extract the value, list, output file path, and position from the command-line arguments
    my_value = args.value
    file_path = args.list
    output_path = args.output
    position = args.position

    # Read the list from the file
    with open(file_path, 'r') as file:
        my_list = file.read().strip().splitlines()

    # Add the value after specified positions in the list
    modified_list = add_value_after_alternates(my_value, my_list, position)

    # Create the file with the modified list
    create_file_with_list(output_path, modified_list)

def combine(args):
    # Extract the username, usernames list, password list, separator, and output file path from the command-line arguments
    username = args.username
    usernames_file = args.usernames_file
    passwords_file = args.passwords_file
    separator = args.separator
    output_path = args.output

    # If both username and usernames_file are provided, raise an error
    if username and usernames_file:
        raise ValueError("Only one of '-u' or '-U' can be specified.")

    # Read the usernames list from the file or use the provided username
    if usernames_file:
        with open(usernames_file, 'r') as file:
            usernames = file.read().strip().splitlines()
    else:
        usernames = [username]

    # Read the password list from the file
    with open(passwords_file, 'r') as file:
        passwords = file.read().strip().splitlines()

    # Combine the usernames with each password using the specified separator
    combined_list = [f"{u}{separator}{p}" for u in usernames for p in passwords]

    # Create the file with the combined list
    create_file_with_list(output_path, combined_list)

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Tool to merge lists and combine usernames with passwords')
subparsers = parser.add_subparsers(dest='command', help='Available commands')

# Create a parser for the 'merge' command
merge_parser = subparsers.add_parser('merge', help='Merge a list by adding a value after every alternate line')
merge_parser.add_argument('-w', '--value', help='The value to add after specified positions')
merge_parser.add_argument('-l', '--list', help='The file path of the list containing line-separated values')
merge_parser.add_argument('-o', '--output', help='The output file path')
merge_parser.add_argument('-v', '--position', type=int, default=1, help='The position of the value to be added (default: 1)')

# Create a parser for the 'combine' command
combine_parser = subparsers.add_parser('combine', help='Combine usernames with passwords')
username_group = combine_parser.add_mutually_exclusive_group(required=True)
username_group.add_argument('-u', '--username', help='The username')
username_group.add_argument('-U', '--usernames-file', help='The file path of the usernames list')
combine_parser.add_argument('-p', '--passwords-file', help='The file path of the passwords list')
combine_parser.add_argument('-s', '--separator', default=':', help='The separator between username and password (default: ":")')
combine_parser.add_argument('-o', '--output', help='The output file path')

# Parse the command-line arguments
args = parser.parse_args()

# Display help section if no command is provided
if not args.command:
    parser.print_help()
    exit()

# Call the respective command function
if args.command == 'merge':
    merge(args)
elif args.command == 'combine':
    combine(args)
