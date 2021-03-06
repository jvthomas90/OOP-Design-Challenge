# OOP-Design-Challenge
Final Project for CS 1.1 

![Git'r'Done!](https://github.com/jvthomas90/OOP-Design-Challenge/blob/main/OOP%20Assignment%20Output.png?raw=true)

## A CLI note-taker and to-do list utility!

> **Nota Bene:** This app is in "alpha" stages of development. Right now it relies on demo-data to produce an output, but ideally later updates to this repo will allow it to be a fully interactive and immersive CLI experience!

- At it's core, all this does is save a string as a Note object. 
---
- Depending on if certain @tags are detected (not implemented yet) in the sentence, or of explicitly instantiated as such, this Note is elevated to a Task object.
  - The plain-text formatting is replaced with blue, and a to-do checkbox is prepended to the string.
---
- And if the tags aren't simply signalling the end-of-task lifecycle via @done or @dropped tags (once again, command-line inputs, automatic-parsing and dynamically created objects haven't been implemented in this early version... but this is the direction I envision further development going in) or if otherwise explicitly instantiated as such, certain tasks can be further formatted based on their priority status
  - Priority objects have tags that signify that they are important items for the user to flag for further review and complete
  - Priority is also determined based on ~parsing powered by the dateutil library and .timedelta() calculations~ explicit temporal tags, like @due
  - Priority objects will be further formatted with distinguishing colors and effects to font styling, plus a relevant symbol will be added to the checkbox
  ---
  
And that's the basic gist of it. Right now you can't actually write notes, but it does save strings as Note objects. I intend to iterate and improve upon this app over time.

![UML](https://github.com/jvthomas90/OOP-Design-Challenge/blob/main/OOP%20Design%20UML.png?raw=true)

### Requirements
This code relies upon importing the [sty](https://sty.mewo.dev/index.html) library for it's output to look pretty. Please `pip install sty` in order to see more than plain white text in your terminal output. Here is what the expected output is supposed to look like, according to my own testing 🌈

~[Expected Output](https://github.com/jvthomas90/OOP-Design-Challenge/blob/main/OOP%20Assignment%20Output.png?raw=true)
