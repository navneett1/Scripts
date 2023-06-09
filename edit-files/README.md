
# edit-files.py

This script can be used to make a list by combining two wordlists.  
Like you can use two wordlists containing usernames and passwords and make a new wordlist in which the username and passwords are seperated by commas(,) or colons(:)  

#### You can use following functions in this  script :-
- **merge:** It can be used to add a particular value after a number of lines in a list. (Like there are times when you need a wordlist where a particular word has to be in the alternate line. So you can use it there) 

- **combine:** It can be used when you want a wordlist with username and password with any seperator you want. When you want them in the form of "username:password".


## Usage

``` 
python3 edit-files.py -h

```
```
python3 edit-files.py merge -h
```
```
python3 edit-files.py combine -h
```

## Example

This command will add a single word after every alternate line in a list:
```
python3 edit-files.py merge -w word -l usernames.txt -o output.txt
```
  
The following command will make a file containing a single username and take the values from the password file an seperate them with a seperator:
  
```
python edit-files.py combine -u username -p passwords.txt -s : -o output.txt
```
The following command will take values from username file one by one and add all the values from the password file seperated by a seperator:
```
python edit-files.py combine -U usernames.txt -p passwords.txt -s : -o output.txt
```