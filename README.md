# dnd_info

Search the [DnD5e API](https://www.dnd5eapi.co) and return relevant information

## Usage

[`dnfo_lite.py`](./dnfo_lite.py) is a portable version of `dnfo`. It has
simpler argument handling, and is contained in one file. It depends on
[requests](https://github.com/psf/requests) for accessing the API, and
[rich](https://github.com/willmcgugan/rich) for some text formatting.

It takes an argument for an endpoint and an index of that endpoint, in the
format of `python3 dnfo_lite.py \[endpoint] \[index]`. To get available
endpoints, run the command with no arguments,
or a help flag \(`-h|--help|help`).  
To get available indexes of an endpoint, run the command without an index:
`python3 dnfo_lite.py \[endpoint]`.

## TODO

- [ ] Store responses in a database
  - [ ] Populate the database and create a .lock file, with a regeneration
if requested by the user
- [X] Print rows that fit the size of the command prompt
- [ ] Store all options in arrays and check arguments against them
  - [ ] Integrate the above point with the "choices" option for add_argument
