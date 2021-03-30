#!/usr/bin/env python3

def main():
    pass

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/",min_gb=2, min_percent=2)

main()
