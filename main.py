from JottedThoughts import Note, Task
from SignificantStuff import Priority
from BulletJournal import Notebook

# Instantiating Notes, Tasks, and Priority objects with some demo data
note0 = Note("Here's a thought that I penned down, now I'll never forget it!")
journal_log_entry = Note("And here I'll jot down another idea I just had!")
action_item = Task('This is an actionable to-do list item')
dropped_or_cancelled = Priority("This task was @dropped due to unforseen circumstances")
done_or_complete = Priority("This task has been @completed and @done to death!")
flagged_or_starred = Priority("This is an @important task")
time_sensitive = Priority("This task is @due(2020.10.20)")
# new_entry = Priority("This is an @important thought!")

# Toggle formatting based on object type and content (i.e. @tags)
# new_entry._toggle_task()
action_item._toggle_task()
flagged_or_starred._toggle_task()
dropped_or_cancelled._toggle_task()
done_or_complete._toggle_task()
time_sensitive._toggle_task()

# saving all the newly constructed Note, Task and Priority objects to a new instance of Notebook
doc = Notebook([note0, journal_log_entry, action_item, dropped_or_cancelled, done_or_complete, flagged_or_starred, time_sensitive])

# Program output ( ͡° ͜ʖ ͡°)ﾉ⌐■-■ 
doc.display_notes() # (⌐ ͡■ ͜ʖ ͡■)