# Password Strength Calculator

A program for calculating password strength

The program asks for an input after it is started, and gives the user feedback on how strong the password would be against dictionary attacks.

## Example usage

```
$ Enter password to test: password
$ Password Strength: Very Weak
```

### Installation

```
$ pipenv install
```

### Run

```
$ pipenv run python main.py
```

or

```
$ pipenv shell
$ python main.py
```

### Compiling via pyinstaller

```
$ pyinstaller -F -y -n {{FileName}} main.py
```
