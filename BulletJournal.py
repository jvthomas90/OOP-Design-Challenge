class Notebook():
    # Class attributes here

    def __init__(self, entries=[]):
        """
        Document constructor method
        """
        # journal_entries is public because we can use helper functions to string together a list of all our
        # notes, tasks, and priority items, then write it to a file, or display it via our Notebook database, etc
        self.journal_entries = entries

    def display_notes(self):
        """
        Method to output all the current note, task and project contents of the notebook
        """
        for entry in self.journal_entries:
            entry.print_note()