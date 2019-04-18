# Cryptonet

Cryptonet is a command line based encryption and decryption utility program.

## Packages

Cryptonet uses the python cryptography library which can be installed using [pip](https://pip.pypa.io/en/stable/)

```bash
pip3 install cryptography
```

## Usage

- First initialize a key to begin encryption and decryption
```bash
python3 main.py generate_key
```
- To encrypt a file
```bash
python3 main.py encrypt_file your_file
```

- To encrypt a string
```bash
python3 main.py encrypt your_string
```
- To decrypt a file
```bash
python3 main.py decrypt your_file
```
- To use a different cryptographic key, simply replace the key.key file in the directory


## Note
- A system file "key.key" is  generated each time generate_key is entered. A specific key is used to both encrypt and decrypt

- A file with the extension ".enc" is created when a file is encrypted

- All decrypted files are in ".txt" file format

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
