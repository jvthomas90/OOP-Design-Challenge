import uuid
from sty import ef, bg, fg, rs

class Note:
    # Class attributes
    # Titele? Doesn't make much sense for a single string display on the command line interface...
    # tags = []

    def __init__(self, note):
        """
        Note constructor method
        """

        # Note is protected because the subclasses (i.e. to-do tasks, project actions, calendar agendas, etc) 
        # are just notes with additional formatting, so they should be able to modify it.
        # Alternatively, there is no need for something like the Notebook class to alter it
        self._note = "     " + note # Added spacing to display notes in line with tasks that have preceding checkboxes

        # Assigns a random, unique ID for each note entry and make it private
        # This way, even if the note content is identical between 2 entries,
        # there will be no duplicate entries in the Notebook
        self.__id = self.__set_id()

    def print_note(self):
        print(self._note)

    # Getter method
    def __get_id(self):
        return self.__id

    # Setter method
    def __set_id(self):
        return uuid.uuid4().hex

class Task(Note):

    def __init__(self, note, checkmark=False):

        super().__init__(note)
        
        self.__isChecked = checkmark
        self._note = ('[✅] ' if self.__isChecked == True else '[  ]') + fg.li_blue + note + rs.fg

    def _toggle_task(self):

        self._note = self._note.strip("[❌ ✅]")
        
        if "@cancel" in self._note: # @cancel, @cancelled, cancelling, cancellation, etc
            self.__isChecked = False
            self._note = "[❌] " + ef.b + self._note + " " + bg.red + "@cancelled" + rs.all
        
        elif "@complete" in self._note: # @complete, @completed, @completion date, etc
            self.__isChecked = True
            self._note = "[✅] " + ef.i + self._note + " " + bg.da_green + "@completed" + rs.all
            
        elif "@drop" in self._note: # drop, dropped, etc
            self.__isChecked = False
            self._note = "[❌] " + ef.b + self._note + " " + bg.red + "@dropped" + rs.all
        
        elif "@done" in self._note: # @done tasks will aleays be tagged in the past tense... Which makes sense.
            self.__isChecked = True
            self._note = "[✅] " + ef.i + self._note + " " + bg.da_green + "@done" + rs.all
        
        else:   # If you aren't giving up, and you aren't getting things done either... you've still got shit to do 🤯
            self.__isChecked = False
            self._note = "[  ] " + self._note