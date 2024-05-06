# costas
Costas (back in portuguese) is a backup script I use every week. It creates encrypted snapshots of directories with an ignore list to prevent bloat and slowdowns.

## Setup
First, create a gpg key pair. Then, you should copy the key ID and write the configuration file.

## Configuration
Costas needs to be configured properly in order to work. Create a file (or copy it from `examples/costas.json`) in `~/.config/costas/costas.json` and add the following data:
* "gpg-keyid", with the gpg key ID for the recipent you want costas to encript to (probably your own key),
* "base-directory", with the directory the tar command will execute,
* "directories", with a list of directories relative to the "base-directory" costas will encrypt, and
* "ignore", with a list of directories/files relative to the "base-directory" not to encrypt, taking precedence over "directories".
* "output-directory", with the output file diretory to store. Note that if it is inside the "diretories" list, problems might occur.

## Running costas
Then, if you want this program to create a single snapshot, run `./costas.py`.
