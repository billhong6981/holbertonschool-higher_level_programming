#!/usr/bin/python3
"""replaces string in heap region"""

import sys


if __name__ == "__main__":

    def print_usage_and_exit():
        """exit failure functure"""
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    if len(sys.argv) != 4:
        print_usage_and_exit()

    pid = int(sys.argv[1])
    if pid <= 0:
        print_usage_and_exit()
    search_string = str(sys.argv[2])
    if search_string == "":
        print_usage_and_exit()
    replace_string = str(sys.argv[3])
    if replace_string == "":
        print_usage_and_exit()

    # open the maps and mem files of the process
    maps_filename = "/proc/{}/maps".format(pid)
    mem_filename = "/proc/{}/mem".format(pid)
    # open the files
    try:
        maps_file = open(maps_filename, "r")
    except IOError as e:
        print(e)
        sys.exit(1)
    for line in maps_file:
        sline = line.split()
        if sline[-1] != "[heap]":
            continue
        # found [heap]
        addr = sline[0]
        perm = sline[1]
        if perm[0] != 'r' or perm[1] != 'w':
            print("[*] does not have read/write permission")
            maps_file.close()
            sys.exit(1)
        # get memory address
        addr = addr.split("-")
        if len(addr) != 2:
            print(" [*] wrong address\n")
            maps_file.close()
            sys.exit(1)
        addr_start = int(addr[0], 16)
        addr_end = int(addr[1], 16)
        print("\tAddr start [{:x}] | end [{:x}]".format(addr_start, addr_end))

        # open and read mem
        try:
            mem_file = open(mem_filename, 'rb+')
        except IOError as e:
            print(e)
            maps_file.close()
            sys.exit(1)
        mem_file.seek(addr_start)
        heap = mem_file.read(addr_end - addr_start)

        # find string
        try:
            i = heap.index(bytes(search_string, "ASCII"))
            print("what is i: [{}], and index do".format(i))
        except Exception:
            print("Can't find '{}'".format(search_string))
            maps_file.close()
            mem_file.close()
            sys.exit(1)
        print("[*] Found '{}' at {:x}".format(search_string, i))

        # write the new string
        mem_file.seek(addr_start + i)
        mem_file.write(bytes(replace_string + '\0', "ASCII"))
        print("replace: [{}]\n".format(replace_string))
        mem_file.close()
