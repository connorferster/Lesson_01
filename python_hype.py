from IPython.display import HTML, Code, Image, YouTubeVideo, IFrame, Markdown

def python():
    display(Image(url = "https://python.rs/pylogo.png"))
   
def monty_python():
    display(YouTubeVideo(id = "T8XeDvKqI4E"))
    
def stack_overflow():
    display(YouTubeVideo(id = "cKzP61Gjf00", width = 900, start = 60))

def guido():
    display(Image(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Guido-portrait-2014-drc.jpg/1280px-Guido-portrait-2014-drc.jpg"))
    display(Image(url = "https://gvanrossum.github.io/images/guido-headshot-2019.jpg"))
    
def pycon():
    display(Image(url = "https://tulula.sfo2.cdn.digitaloceanspaces.com/prod/images/967ab9c21fb81dff1cd44f874affa27b1afdebb4f48629f9129049bfd44b0264.jpeg"))
    display(Image(url = "https://blog.pandata.co/wp-content/uploads/2019/07/20190503_101735-1040x780.jpg"))
    
def python_community():
    display(Image(url = "https://www.pythonistacafe.com/static/img/pythonistacafe-header.jpg"))
    
def top_ten_websites():
    display(IFrame(src = "https://learn.onemonth.com/10-famous-websites-built-using-python/", width = 1000, height = 500))
    
def economics_nobel():
    display(IFrame(src = "https://meterpreter.org/the-winner-of-the-2018-nobel-prize-in-economics-is-a-python-user/", width = 1000, height = 500))

def nature():
    display(IFrame(src = "https://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261", width = 1000, height = 500))

def jupyter():
    display(IFrame(src = "https://jupyter.org/", width = 1000, height = 500))
    
def black_hole():
    display(IFrame(src = "https://techcrunch.com/2019/04/10/the-creation-of-the-algorithm-that-made-the-first-black-hole-image-possible-was-led-by-mit-grad-student-katie-bouman/", width = 1000, height = 500))
    
def shortcuts():
    text = """
When in "Command Mode" (blue outline):

* Type `a` to add a cell *above*
* Type `b` to add a cell *below*
* Type `dd` to *delete* a cell
* Type `c` to *copy* a cell
* TYpe `x` to *cut* a cell
* Type `v` to *paste* a cell
* Type `z` to *undo* a Command Mode operation
* Type `[Enter]` to go from "Command Mode" to "Edit Mode"

When in "Edit Mode" (green outline):
* Type `[Esc]` to go from "Edit Mode" to "Command Mode"
* Type `[Shift]+[Enter]` to **Run** your cell and then advance
* Type `[Ctrl]+[Enter]` to **Run** your cell and stay on the cell

At any time, type `Ctrl-s` to save (either in Edit or Command Mode, does not matter).

However, Jupyter also has a convenient auto-save.
    """
    return Markdown(text)
    