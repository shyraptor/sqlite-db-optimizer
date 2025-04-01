#!/usr/bin/env python3
"""
SQLite Database Optimizer

A simple utility to optimize SQLite databases by running VACUUM and ANALYZE operations.
"""

import sqlite3
import argparse
from pathlib import Path


def optimize_database(db_path, quiet=False):
    """
    Optimize an SQLite database by running VACUUM and ANALYZE operations.
    
    Args:
        db_path (str or Path): Path to the SQLite database file.
        quiet (bool): If True, suppress output messages.
    
    Returns:
        tuple: Original size, new size, and size reduction in bytes.
    """
    db_path = Path(db_path)
    if not quiet:
        print(f"Optimizing database: {db_path}")
    
    original_size = db_path.stat().st_size
    if not quiet:
        print(f"Original database size: {original_size / (1024*1024):.2f} MB")
    
    try:
        with sqlite3.connect(str(db_path)) as conn:
            cursor = conn.cursor()
            
            if not quiet:
                print("Running VACUUM...")
            cursor.execute("VACUUM")
            
            if not quiet:
                print("Running ANALYZE...")
            cursor.execute("ANALYZE")
            
            conn.commit()
            if not quiet:
                print("Optimization completed successfully.")
    
    except sqlite3.Error as e:
        if not quiet:
            print(f"An error occurred: {e}")
        return original_size, original_size, 0
    
    new_size = db_path.stat().st_size
    size_reduction = original_size - new_size
    
    if not quiet:
        print(f"New database size: {new_size / (1024*1024):.2f} MB")
        print(f"Size reduction: {size_reduction / (1024*1024):.2f} MB")
    
    return original_size, new_size, size_reduction


def main():
    """Parse command line arguments and run the optimizer."""
    parser = argparse.ArgumentParser(description='Optimize SQLite database files.')
    parser.add_argument('db_path', help='Path to the SQLite database file')
    parser.add_argument('--quiet', '-q', action='store_true', help='Suppress output')
    
    args = parser.parse_args()
    
    db_path = Path(args.db_path)
    if not db_path.exists():
        if not args.quiet:
            print(f"Error: Database file not found: {db_path}")
        return 1
    
    optimize_database(db_path, quiet=args.quiet)
    return 0


if __name__ == "__main__":
    exit(main())