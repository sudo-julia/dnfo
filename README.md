# dnfo

Search the [DnD5e API](https://www.dnd5eapi.co) and return relevant information

## Requirements

- Python ^3.7
- [appdirs](https://github.com/ActiveState/appdirs)>=1.4.4 for finding
what directories to store data in (helps this function as a
platform-independent application)
- [GitPython](https://github.com/gitpython-developers/GitPython)>=3.1.14 for
downloading the database repository
- [pymongo](https://github.com/mongodb/mongo-python-driver)>=3.11.3 for querying
a local database
- [requests](https://github.com/psf/requests)>=2.25.1 for querying the database
at <https://dnd5eapi.co/api>
- [rich](https://github.com/willmcgugan/rich)>=9.13.0 for formatting retrieved information

## Optional Requirements

- If you want to query a local database (it's faster and works offline!),
install [`mongodb`](https://docs.mongodb.com/manual/installation/)
and make sure it's running on the default host and port.

## Usage

`dnfo` takes an argument for an endpoint and an index of that endpoint, in the
format of `python3 dnfo \[endpoint] \[index]`. To get available
endpoints, run the command with no arguments,
or a help flag \(`-h|--help|help`).  
To get available indexes of an endpoint, run the command without an index:
`python3 dnfo \[endpoint]`.

## Using a Local Database

1. Make sure `mongod` is running on the default host and port.
2. Run `dnfo --build` to build the [database](https://github.com/5e-bits/5e-database)
used by the [DnD 5th Edition API](https://www.dnd5eapi.co/).
3. Run `dnfo` with the `--local` flag to use the local database instead of the
online API.

## Configuration

*Coming soon...*

## TODO

- [ ] Tests
- [ ] Formatting of dictionaries as values in a dict
- [ ] If disconnected from internet and database is built, use the db
- [ ] Config file
  - [ ] Configurable host and port for mongo database
- [X] Store responses in a database
  - [X] Populate the database and create a .lock file, with a regeneration
if requested by the user
- [X] Print rows that fit the size of the command prompt
- [X] Store all options in arrays and check arguments against them
- [X] Format all received data in a rich Table
