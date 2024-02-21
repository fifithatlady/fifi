#!/usr/bin/python3
"""Console for fifithatlady  Nanny Job Listings"""

import cmd

# Dummy data for testing purposes
nanny_jobs = []

class QuickSearchConsole(cmd.Cmd):
    """Command-line interface for fifithatlady - Nanny Job Listings"""

    prompt = '(fifithatlady) '

    def do_EOF(self, arg):
        """Exit the console"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def default(self, line):
        """Handle default command"""
        args = line.split()
        if len(args) == 0:
            print("*** Unknown syntax: missing command ***")
            return
        command = args[0]
        if command == "list":
            self.list_nanny_jobs()
        else:
            print("*** Unknown command ***")

    def do_create(self, arg):
        """Create a new nanny job listing"""
        # Implement logic to create a new nanny job listing
        pass

    def list_nanny_jobs(self):
        """List all nanny job listings"""
        for job in nanny_jobs:
            print(f"ID: {job['id']}, Title: {job['title']}, Location: {job['location']}, Salary: {job['salary']}")

if __name__ == '__main__':
    fifithatladyConsole().cmdloop()

