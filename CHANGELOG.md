# Changelog

## Version 1.0.0

Released 2021-04-06

### The Database Release (New Features)

`dnfo` now ships with five new options: `--build`, `--clear`, `--rebuild`,
`--local` and `--web`.  
Once a local database is built with `--build`, it's available for use
by inserting `--local` anywhere in your `dnfo` command! Using the local
database is faster, and works offline.  
Is your database broken, or do you no longer have use for it? Rebuild a database
in place with the `--rebuild` command, or clear your data with `dnfo --clear`.  
The `--web` option queries information from <https://dnd5eapi.co>, which is
the default behavior and was the only option before this release.

### Bugfixes

- Less errors with arguments handling
- More verbose/transparent error handling
- Even more bugfixes that I'm forgetting, as I forgot to keep this updated
during development :)

## Version 0.2.0

Released 2021-03-19

- first release (version 0.1.0 only lasted a few minutes)
