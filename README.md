# Ange1Encrypt3r

A python-based 3-step CLI encrypter that I made for the funnies :D

If you like to encrypt random stuff, or you actually want to keep something safe.. well it's better than keeping it in plaintext..

## Features
- 3-step encryption
  - Substitution
    - Given the option to use your own pattern
    - If not given it defaults to the standard [+1, -14, +7, -5, +12]
  - Hexing
  - AES encryption
    - Takes a user given password and hashes it
    - Uses the hashed password as a key for encryption

## Why this exists
The beginning that predates all of many random posts that track my progress as a programmer. Why predates, since this is legit just a repost of an old repo that was stupidly messy (hence why the style is very different...)

The idea of this came from wanting to make my own CTF that used encryption. So I had made this, but I could never figure out how to make it CTF style, so I turned it into a standard encryption tool :D

The substitution is a little easter egg that reminds me of my partner <3

And while working on UltraCTF, I figured I could use this as a reference point for it so yeah..

So behold the um, minus one? of all my repos (it did come before everything else back in like I think July?) to come about my progress and improvement. If anyone who sees this has any tips, ideas or comments, just lemme know, all feedback is much appreciated.

## How to run
```bash
git clone https://github.com/kaizokuv/Ange1Encrypt3r.git
cd Ange1Encrypt3r
python -m venv venv && source venv/bin/activate && pip install --upgrade pip
pip install -r requirements.txt
python3 main.py
```

## For those of you who are lazy and willing to tweak around with aliases
Here are some aliases you guys can use for your terminal shells (bash, fish, zsh) to simplify calling the tool. 

Mind you you will still need to clone the repo first, and this is assuming you cloned the repo into your desktop and not a file. 

The alias will cd in a subshell so that once you're done using the tool, you'll go back to your original directory.

### For bash/zsh shell
```bash
ange1encrypt3r() {
  pushd ~/Ange1Encrypt3r > /dev/null || return
  echo "Starting Venv.."
  python -m venv venv && source venv/bin/activate && pip install --upgrade pip > /dev/null
  echo "Installing Requirements.."
  pip install -r requirements.txt > /dev/null
  python main.py
  deactivate
  popd > /dev/null || return
}
```
Change '~/Ange1Encrypt3r' to the desired file path if you want to set a custom file path

### For fish shell
```bash
function ange1encrypt3r
  pushd ~/Ange1Encrypt3r > /dev/null
  echo "Starting Venv.."
  python -m venv venv && source venv/bin/activate.fish && pip install --upgrade pip > /dev/null
  echo "Installing Requirements.."
  pip install -r requirements.txt > /dev/null
  python main.py
  popd > /dev/null
end
```
Change '~/Ange1Encrypt3r' to the desired file path if you want to set a custom file path


# Thank you for using my tools :D
