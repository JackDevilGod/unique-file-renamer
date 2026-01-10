# Unique File Renamer

A tool that deduplicates files by renaming them based on their SHA256 content hash.

## How It Works

The script recursively walks through all files in the `in/` directory and:

1. **Computes a SHA256 hash** of each file's contents
2. **Renames the file** to `<hash>.<original_extensions>` (preserving all file extensions)
3. **Detects duplicates**: If two files have identical content, they produce the same hash. The second file is deleted since it's a duplicate.

This effectively deduplicates your directory structure while preserving file types through original extensions.

## Usage

```bash
python main.py
```

Place files you want to deduplicate in the `in/` directory (or its subdirectories). The script will:
- Traverse all subdirectories recursively
- Rename each file based on its content hash
- Remove duplicate files
- Keep the directory structure intact

## Example

**Before:**
```
in/
  image.png        (content: "ABC...")
  copy_of_image.png (content: "ABC...")
  document.txt     (content: "DEF...")
```

**After:**
```
in/
  3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f.png
  def1234567890abcdef1234567890abcdef1234567890abcdef1234567890ab.txt
```

The duplicate `copy_of_image.png` is deleted because it has the same hash as `image.png`.

## Requirements

- Python 3.9+
- Standard library only (no external dependencies)

## Why Use This?

- **Find duplicates**: Same content = same hash
- **Free up space**: Automatically delete duplicate files
- **Organize archives**: Useful for deduplicating photo/media libraries or backup folders
