# HashBrowns-Python

![Banner](ignore/banner.png)

HashBrowns is a secure package for hashing and cryptography in Python with unique features. This package is mainly for cryptography and hashing, but it also has some other features for files and handling. All functions are listed in a section below and are explained in detail here [wiki](https://github.com/itzCozi/HashBrowns-Python/wiki/Functions) also this package being open source, you can view the source code here [source](https://github.com/itzCozi/HashBrowns-Python/tree/main/package).

## All Functions
All functions are listed here, and are explained in detail in the [wiki](https://github.com/itzCozi/HashBrowns-Python/wiki/Functions).

```
functions.clearconsole()     encryption.standard()
functions.checkfile()        encryption.double()
functions.mutilate()
functions.getinfo()          decryption.standard()
functions.wipefile()         decryption.double()

hash.hash()                  key.keypair()
hash.hashfile()              key.solokey()
hash.comparehash()           key.secure()
```

### Examples

Hashing a password and saving it to a database.
```python
from hashbrowns import hash
password = input("Enter your password here: ")

with open("Database.txt", "a") as file:
file.write(hash.hash(password))
```

Encrypting a message with a key.
```python
from hashbrowns import encryption

encryption.standard("test,txt", "Mario Judah")
```

Decrypting a message with a key.
```python
from hashbrowns import decryption

decryption.standard("test.txt", "kNpayatd")
```

Obfuscating a file.
```python
from hashbrowns import functions

functions.mutilate("test.txt")
```

## Extra
[Package on PyPi](https://pypi.org/project/hashbrowns/)  
[Latest Release](https://github.com/itzCozi/HashBrowns-Python/releases)  
[Quickstart Guide](https://github.com/itzCozi/HashBrowns-Python/wiki/Quickstart-Guide)

### Contact Me
discord: BadDevoleper#4200                                                                                                                                             
Email: Cooperransom08@outlook.com                                                                                                                                      
[Replit](https://replit.com/@cozi08) | 
[Twitter](https://twitter.com/ransom_cooper)