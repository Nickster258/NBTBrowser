# NBTBrowser
### A quick note
_Be careful when modifying NBT files using this application. When editing tags, **this editor parses from a serialized representation of NBT data** before applying changes to the loaded NBT object. Nothing is saved until you run `save`. Be sure you know what you are doing before saving a file using this editor! For more information on **stringified NBT**, view some examples [here](https://minecraft.gamepedia.com/Tutorials/Command_NBT_tags)._

### Installation
Install nbtbrowser using pip: `pip install --user git+https://github.com/Nickster258/NBTBrowser.git`

Depending on your platform, the executable may not be added to your paths. View the output of your `pip install` to see where the executable was placed.

### Using NBTBrowser
To use NBTBrowser, start it by running the following with the specified NBT file:

`nbtbrowser -f some_file.nbt`
### Commands:
#### `exit` - Exit the NBTBrowser.
#### `pwd` - Print your current working location in NBTBrowser.
#### `cd` - Change your location.
The `cd` command lets you change your location with respect to your current placement in the NBT structure.
The `cd` command supports three types of arguments: `..`, a `key`, and `index`.

To navigate up one directory: `cd ..`

To navigate into a compound tag, use its key: `cd someKey`

To navigate into a compound within a list, use its index: `cd 1`
#### `ls` - List files in the current. 
#### `ll` - Get a tabulated list of tags and types.
#### `cat` - Print the contents of a tag.
The `cat` command lets you print the serialized representation of either the current tag, or the specified tag.

The `cat` command supports three types of arguments: `.`, a `key`, and `index`.

To print the current tag: `cat .`

To print a tag, use its key: `cat someKey`

To print a tag within a list, use its index: `cat 1` 
#### `rm` - Remove a tag.
The `rm` command lets you remove a tag using the specified tag.

The `rm` command supports two types of arguments: a `key`, and `index`.

To remove a tag, use its key: `rm someKey`

To remove a tag within a list, use its index: `rm 1`
#### `set` - Set NBT data, overriding an existing tag.
The `set` command lets you set the contents of a tag using a serialized representation of NBT data. This command strictly overrides existing tags.

This command parses **stringified NBT** input. For more information on stringified NBT, look at some examples [here](https://minecraft.gamepedia.com/Tutorials/Command_NBT_tags). 

To set the contents of a tag: `set someKey {some:'data'}`

To set the contents of an item in a list: `set 0 {some:'data'}`
#### `add` - Add NBT data with a specified string.
The `add` command lets you add a serialized representation of NBT data to an existing compound or list. This command strictly adds tags.

This command parses **stringified NBT** input. For more information on stringified NBT, look at some examples [here](https://minecraft.gamepedia.com/Tutorials/Command_NBT_tags). 

To add a new tag: `add someKey {some:'data'}`

To add to a list: `add {some:'data'}`
#### `tree` - Print a tree representation of the current node.
#### `save` - Write your changes back to the file.
_**Careful! Make sure you know what you are doing before applying modified changes!**_
