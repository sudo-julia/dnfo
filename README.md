# dnd_info

Search the [DnD5e API](https://www.dnd5eapi.co) and return relevant information

## Usage

`dnfo` takes an argument for an endpoint and an index of that endpoint, in the
format of `python3 dnfo \[endpoint] \[index]`. To get available
endpoints, run the command with no arguments,
or a help flag \(`-h|--help|help`).  
To get available indexes of an endpoint, run the command without an index:
`python3 dnfo \[endpoint]`.

## TODO

- [ ] Store responses in a database
  - [ ] Populate the database and create a .lock file, with a regeneration
if requested by the user
- [ ] Tests
- [ ] Formatting of gear packs/starting equipment
- [X] Print rows that fit the size of the command prompt
- [X] Store all options in arrays and check arguments against them
- [X] Format all received data in a rich Table
