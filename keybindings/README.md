# Keybindings and Shortcuts

## Swap modifiers

Put [altwin](./altwin) in `/usr/share/X11/xkb/symbols` and check "Meta is mapped to Win" in "GNOME Tweak Tool > Keyboard & Mouse > Additional Layout Options > Alt/Win key behavior".

Download [autokey](https://github.com/autokey/autokey) and use config files in `autokey/data/Mac`. (Acknowledgement: It is based on the work from https://github.com/xortim/autokey)

Some useful tools and commands:
- `xev`: get keycodes and to check how your keymap works.
- `dconf-editor`: directly edit dconf settting file (`org/gnome/desktop/input-sources/xkb-options`) instead of using GNOME Tweak Tool.
- `dconf watch /`: see which dconf setting is changed.

## Capslock as Shift

Put [capslock](./capslock) in `/usr/share/X11/xkb/symbols` and check "Make Caps Lock an additional Menu key" in "GNOME Tweak Tool > Keyboard & Mouse > Additional Layout Options > Caps Lock behavior".

## System Settings

Change shortcuts to whatever you like.

## IntelliJ IDEA

Go to "File > Settings > Keymap" and select "Default for macOS".

## Visual Studio Code

Move [keybindings.json](./keybindings.json) to `~/.config/Condig/User/`.
