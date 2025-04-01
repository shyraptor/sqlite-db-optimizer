# SQLite Database Optimizer

A simple command-line utility for optimizing SQLite databases.

## Features

- Reduces database file size with VACUUM command
- Improves query performance with ANALYZE command
- Reports before and after file sizes
- Simple command-line interface

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/sqlite-optimizer.git
cd sqlite-optimizer
```

No additional dependencies required beyond the Python standard library.

## Usage

```bash
python sqlite_optimizer.py path/to/your/database.db
```

### Examples

Basic usage:
```bash
$ python sqlite_optimizer.py my_database.db
Optimizing database: my_database.db
Original database size: 105.42 MB
Running VACUUM...
Running ANALYZE...
Optimization completed successfully.
New database size: 89.73 MB
Size reduction: 15.69 MB
```

Quiet mode (useful for scripts):
```bash
$ python sqlite_optimizer.py my_database.db --quiet
```

## Why Optimize SQLite Databases?

SQLite databases can become fragmented and larger than necessary over time, especially after many delete or update operations. This utility helps:

1. Reduce file size by reclaiming unused space
2. Improve read performance by reducing fragmentation
3. Enhance query planner decisions by updating statistics

## License

MIT License
