# File Organization & Renaming Tools

A collection of utility tools for organizing and renaming files in your directories with an interactive command-line interface.

## Overview

This project provides several file manipulation tools that help you:
- Clean up file names by removing spaces
- Rename files based on their content hashes to identify duplicates
- Work with any directory you choose

## Features

### Tools Available

1. **Remove Spaces from Filenames**
   - Removes spaces from individual filenames
   - Option to also clean up folder names
   - Preserves file extensions and directory structure

2. **Remove Spaces (Including Folders)**
   - Comprehensive cleanup that renames both files and folders
   - Useful for cleaning up entire directory structures
   - Preserves nested hierarchy

3. **Rename Files to Content Hash**
   - Renames each file to a SHA256 hash of its contents
   - Automatically removes duplicate files (files with identical content get the same hash)
   - Preserves original file extensions
   - Great for finding and removing duplicates

4. **Exit**
   - Terminates the application

## Installation

No external dependencies required! This project uses only Python's standard library.

### Requirements
- Python 3.9 or higher

## Usage

```bash
python main.py
```

The application will guide you through each step:

1. **Select a Directory**: Enter the path to the directory you want to work with
2. **View Statistics**: See how many subfolders and files are in the selected directory
3. **Choose a Tool**: Select from the available tools using the number corresponding to each option
4. **Perform Action**: The selected tool will process the files
5. **Continue**: You can select another tool or exit

## How It Works

### PathContainer
The `PathContainer` class manages the directory operations by:
- Tracking the base path and counting total files and subfolders
- Using a queue-based approach for recursive directory traversal
- Providing statistics about the selected directory

### Interactive Menu
The `tool_menu` function provides an easy-to-use interface:
- Displays available tools with numbered options
- Handles user input validation
- Clears previous output for a clean interface
- Passes the selected path to the chosen tool function

## File Tools

### Removing Spaces
The `no_spaces` function uses a breadth-first search approach to traverse directories and rename files/folders by replacing spaces with underscores. It handles nested structures and preserves file extensions.

### Unique File Renaming
The `unique_file_renamer` function:
1. Reads each file's contents in binary mode
2. Computes a SHA256 hash of the file content
3. Renames the file to `<hash><original_extensions>`
4. Automatically deletes files with duplicate hashes (same content = same hash)

## Directory Traversal

All tools use a queue-based traversal method that:
- Processes directories recursively
- Handles both files and subdirectories
- Maintains the original directory structure
- Processes items in a breadth-first order

## Project Structure

```
.
├── main.py                    # Main entry point
├── README.md                  # This file
├── tools/                     # File manipulation tools
│   ├── no_spaces.py          # Remove spaces from filenames
│   └── unique_file_renamer.py # Rename files by content hash
├── pathing/                   # Directory handling utilities
│   └── path_container.py     # PathContainer class
├── menu/                      # Interactive menu components
│   ├── get_path.py           # Path selection input
│   ├── tool_select.py        # Tool selection menu
│   └── help/
│       └── delete_last_lines.py # Console output cleanup
```

## Use Cases

- **Clean up filenames**: Remove spaces from file and folder names
- **Duplicate detection**: Find and remove duplicate files by content
- **File organization**: Rename files based on content for easier identification
- **Archive management**: Process large collections of files consistently

## Benefits

- **No external dependencies**: Uses only Python standard library
- **Interactive interface**: Easy-to-use menu system
- **Recursive processing**: Handles entire directory structures
- **Safe operations**: Preserves file extensions and directory hierarchy
- **Flexible**: Choose different tools or chain them together
