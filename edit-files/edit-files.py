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
    my_value = args.value
    file_path = args.list
    output_path = args.output if args.output else "output.txt"
    position = args.position

    if not file_path:
        merge_parser.print_help()
        return

    with open(file_path, 'r') as file:
        my_list = file.read().strip().splitlines()

    modified_list = add_value_after_alternates(my_value, my_list, position)

    create_file_with_list(output_path, modified_list)

def combine(args):
    username = args.username
    usernames_file = args.usernames_file
    passwords_file = args.passwords_file
    separator = args.separator
    output_path = args.output if args.output else "output.txt"

    if username and usernames_file:
        combine_parser.print_help()
        return

    if not passwords_file:
        combine_parser.print_help()
        return

    if usernames_file:
        with open(usernames_file, 'r') as file:
            usernames = file.read().strip().splitlines()
    else:
        usernames = [username]

    with open(passwords_file, 'r') as file:
        passwords = file.read().strip().splitlines()

    combined_list = [f"{u}{separator}{p}" for u in usernames for p in passwords]

    create_file_with_list(output_path, combined_list)

def affix(args):
    word = args.word
    range_string = args.range
    is_prefix = args.prefix
    is_suffix = args.suffix
    output_path = args.output if args.output else "output.txt"
    num_digits = args.digits

    if not range_string:
        affix_parser.print_help()
        return

    range_start, range_end = map(int, range_string.split('-'))

    if range_start > range_end:
        print("Invalid range: start value should be less than or equal to end value")
        return

    affixed_list = []
    for i in range(range_start, range_end + 1):
        number_str = str(i).zfill(num_digits)
        if is_prefix:
            affixed_word = f"{number_str}{word}"
        elif is_suffix:
            affixed_word = f"{word}{number_str}"
        else:
            affixed_word = f"{word}{number_str}"
        affixed_list.append(affixed_word)

    create_file_with_list(output_path, affixed_list)

parser = argparse.ArgumentParser(description='Tool to merge lists and combine usernames with passwords')
subparsers = parser.add_subparsers(dest='command', help='Available commands')

merge_parser = subparsers.add_parser('merge', help='Merge a list by adding a value after every alternate line')
merge_parser.add_argument('-w', '--value', help='The value to add after specified positions')
merge_parser.add_argument('-l', '--list', help='The file path of the list containing line-separated values')
merge_parser.add_argument('-o', '--output', help='The output file path')
merge_parser.add_argument('-v', '--position', type=int, default=1, help='The position of the value to be added (default: 1)')

combine_parser = subparsers.add_parser('combine', help='Combine usernames with passwords')
username_group = combine_parser.add_mutually_exclusive_group(required=True)
username_group.add_argument('-u', '--username', help='The username')
username_group.add_argument('-U', '--usernames-file', help='The file path of the usernames list')
combine_parser.add_argument('-p', '--passwords-file', help='The file path of the passwords list')
combine_parser.add_argument('-s', '--separator', default=':', help='The separator between username and password (default: ":")')
combine_parser.add_argument('-o', '--output', help='The output file path')

affix_parser = subparsers.add_parser('affix', help='Affix a range of numbers to a word')
affix_parser.add_argument('-w', '--word', help='The base word')
affix_parser.add_argument('-r', '--range', help='The range of numbers (e.g., 1-100)')
affix_parser.add_argument('-p', '--prefix', action='store_true', help='Add the range as a prefix')
affix_parser.add_argument('-s', '--suffix', action='store_true', help='Add the range as a suffix')
affix_parser.add_argument('-o', '--output', help='The output file path')
affix_parser.add_argument('-d', '--digits', type=int, default=0, help='The number of digits to use (default: 0)')

args = parser.parse_args()

if not args.command:
    parser.print_help()
    exit()

if args.command == 'merge':
    merge(args)
elif args.command == 'combine':
    combine(args)
elif args.command == 'affix':
    affix(args)
