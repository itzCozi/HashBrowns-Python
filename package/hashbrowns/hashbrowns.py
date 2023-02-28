try:
  import random
  import os
  import time
  import hashlib
  import string
except ImportError:
  print("Error: Missing module(s) please install the following module(s): random, time, hashlib, string")


# Global variables
class errorMessages():
  error = str("ERROR: An unknown error has occured.")
  fileUnreadable = str("ERROR: The file given cannot be read.")
  fileEmpty = str("ERROR: The given file is empty and contains no data.")
  insufficientPerm = str("ERROR: The file cannot be accessed due to insufficient permissions.")
  fileExists = str("ERROR: The file does not exist/the path can't be found.")
  fileOpen = str("ERROR: The file cannot be opened due to it being in use by another process.")


class hash():
  def hash(target, print=None):
    sha256 = hashlib.sha256()
    xO = random.randint(10, 200)
    targetConvert = list(target)
    for i in range(xO):
      random.shuffle(targetConvert)

    targetShuffled = ''.join(targetConvert)
    sha256.update(targetShuffled.encode())

    if print != None:
      print(sha256.hexdigest())
    else:
      return sha256.hexdigest()

  def hashfile(file):
    BUF_SIZE = os.path.getsize(file)

    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:
      while True:
        data = f.read(BUF_SIZE)

        if not data:
          break

    sha256.update(data)

    return sha256.hexdigest()

  def comparehash(hashA, hashB):
    if hashA is hashB:
      return True
    else:
      return False


class key():
  def keypair():
    threshold = random.randint(6, 14)
    buff = random.randint(300, 10000)
    length = random.randint(50, 350)
    iterable = 0
    tiny = random.uniform(0.001, 0.999)
    alphabet = string.ascii_letters + string.digits
    publicBase = '.'.join(random.choice(alphabet) for i in range(buff))
    privateBase = '.'.join(random.choice(alphabet) for i in range(buff))

    time.sleep(tiny)

    publicList = publicBase.split('.')
    privateList = privateBase.split('.')

    while iterable != threshold:
      x = privateList + publicList
      y = publicList + privateList
      for iteam in x, y:
        random.shuffle(x)
        random.shuffle(y)
      iterable += 1

    time.sleep(tiny)

    publicKey = ''.join(random.choice(x) for iterable in range(length))
    privateKey = ''.join(random.choice(y) for iterable in range(length))

    return publicKey, privateKey

  def solokey():
    threshold = random.randint(7, 12)
    primBuff = random.randint(500, 1000)
    secBuff = random.randint(500, 1000)
    length = random.randint(50, 350)
    iterable = 0
    tiny = random.uniform(0.001, 0.999)
    alphabet = string.ascii_letters + string.digits
    primaryBase = '.'.join(random.choice(alphabet) for i in range(primBuff))
    secondaryBase = '.'.join(random.choice(alphabet) for i in range(secBuff))

    time.sleep(tiny)

    primaryList = secondaryBase.split('.')
    secondaryList = primaryBase.split('.')

    while iterable != threshold:
      foo = primaryList + secondaryList
      bar = secondaryList + primaryList
      foobar = bar + foo
      for iteam in range(length):
        random.shuffle(foo)
        random.shuffle(bar)
        random.shuffle(foobar)
      iterable += 1

    time.sleep(tiny)

    soloKey = ''.join(random.choice(foobar) for iterable in range(length))

    return soloKey

  def secure(key):
    keyLength = len(key)
    keyList = list(key)
    olprime = random.randint(3, 8)
    buff = random.randint(200, 1000)
    alphabet = string.ascii_letters + string.digits + string.digits
    randomkey = list(random.choice(alphabet) for i in range(buff))

    for z in range(olprime):
      random.shuffle(keyList)
      random.shuffle(keyList)
      bar = keyList + randomkey
      for i in bar:
        random.shuffle(bar)

    newkey = ''.join(random.choice(bar) for i in range(keyLength))

    newList = list(newkey)

    for y in range(olprime):
      random.shuffle(randomkey)
      random.shuffle(randomkey)

    for x in range(olprime):
      random.shuffle(newList)
      random.shuffle(newList)
      foo = randomkey + newList
      for i in foo:
        random.shuffle(foo)

    returnKey = ''.join(random.choice(foo) for i in range(keyLength))

    return returnKey


class encryption():
  def standard(file, message):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      original = Fin.read()
      Fin.close()

    encrypted = fernet.encrypt(original)

    with open(file, 'wb') as Fout:
      Fout.write(encrypted)
      Fout.close()

    return key

  def double(file, message):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      original = Fin.read()
      Fin.close()

    encrypted = fernet.encrypt(original)
    doubled = fernet.encrypt(encrypted)

    with open(file, 'wb') as Fout:
      Fout.write(doubled)
      Fout.close()

    return key


class decryption():
  def standard(file, key):
    from cryptography.fernet import Fernet
    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      encrypted = Fin.read()
      Fin.close()

    decrypted = fernet.decrypt(encrypted)

    with open(file, 'wb') as Fout:
      Fout.write(decrypted)
      Fout.close()

  def double(file, key):
    from cryptography.fernet import Fernet
    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      encrypted = Fin.read()
      Fin.close()

    decrypted = fernet.decrypt(encrypted)
    doubled = fernet.decrypt(decrypted)

    with open(file, 'wb') as Fout:
      Fout.write(doubled)
      Fout.close()


class obfuscate():
  def mutilate(file):
    with open(file, "r+") as Fout:
      for line in Fout:
        lineList = list(line)
        randoms = list(string.printable)
        
        for i in lineList:
          newList = lineList + randoms
          random.shuffle(newList)
          
      newLine = ''.join(random.choice(newList) for i in range(len(lineList)))
      Fout.truncate(0)
      Fout.write(newLine)

