from JottedThoughts import Task, Note
from sty import ef, fg, bg, rs

class Priority(Task):
	def __init__(self, note, checkmark=False):

		super().__init__(note)
	
	def _toggle_task(self):

		if "@" in self._note:
			self._note = self._note.strip("[ ❌ ✅ ]")

			# if @contextual_tag signifies priority
			if "@importan" in self._note: # includes "@important". "@importance"
				self._note = "[⭐️] " + ef.u + self._note + " " + fg(255,150,50) + "@important" + rs.all
			elif "@flag" in self._note: # "@flag" includes "@flagged"
				self._note = "[⭐️] " + ef.u + self._note + " " + fg(255,150,50) + "@flagged" + rs.all
			elif "@star" in self._note: # "@star" includes "@starred"
				self._note = "[⭐️] " + ef.u + self._note + " " + fg(255,150,50) + "@starred" + rs.all

			# use @temporal-tags the significance is time-sensitive in nature
			elif "@start" in self._note: # "start" also catches started, starting, etc
				self._note = "[🗓️ ] " + self._note + " " + fg.yellow + "@start-on-date" + rs.fg
			elif "@defer" in self._note: # defer ▶️ deferred, deferring, deferral, etc
				self._note = "[🗓️ ] " + self._note + " " + fg.yellow + "@deferred-till-date" + rs.fg
			elif "@remind" in self._note: # remind, reminder
				self._note = "[🗓️ ] " + self._note + " " + fg.yellow + "@reminder-at-date" + rs.fg
			elif "@due" in self._note:
				self._note = "[🗓️ ] " + self._note + " " + fg.yellow + "@due-by-date" + rs.fg

			# Only override to add extended functionality, i.e. keep the task completion/cancellation toggles in play as-is
			elif "@cancel" in self._note:	# @cancel, @cancelled, cancelling, cancellation, etc
				self._note = "[❌] " + ef.b + self._note + " " + bg.red + "@cancelled" + rs.all
			elif "@complete" in self._note:	# @complete, @completed, @completion date, etc
				self._note = "[✅] " + ef.i + self._note + " " + fg.green + "@completed" + rs.all
			elif "@drop" in self._note:	# drop, dropped, etc
				self._note = "[❌] " + ef.b + self._note + " " + bg.red + "@dropped" + rs.all
			elif "@done" in self._note:	# @done tasks will aleays be tagged in the past tense... Which makes sense.
				self._note = "[✅] " + ef.i + self._note + " " + fg.green + "@done" + rs.all

			else: # if no relevant tags towards to-do list prioritization were found
				non_priority_task = Task(self._note) # Reassign current content to new object of type Task
				non_priority_task._toggle_task
				del self #destructor method for Python garbage collection

		else: # if no tags were found, period, then there's no need to strip away checkboxes or otherwise reformat this 
			regular_old_note = Note(self.note) #This is clearly just a scribble. A thought you jotted down. Cool beans.
			del self #destructor method. No anxiety-inducing urgent red-font for you. You just chill with your cool blue text while Python clears this off the table for ya 🐍
			return regular_old_note
		

