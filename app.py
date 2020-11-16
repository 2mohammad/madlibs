from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route('/madlibs')
def madlibs():
    send_to = "/story"
    madlibs = {
        "place": "",
        "noun": "",
        "verb": "",
        "adjective": "",
        "plural_noun": "",
        "proverb": ""
    }
    return render_template("madlibs.html", madlibs=madlibs, sendto = send_to)

@app.route('/story')
def story():
    page = ''
    madlib = request.args.to_dict(flat=True)
    '''for key, value in madlib:
        page += '<h3>{0} : {1}</h3>'.format(key, value)'''
    '''typeq = f"<h1> tyoppahdha {madlib['place']}</h1>".format()'''
    typeq = story.generate(madlib)
    return render_template("story.html", madlibed=typeq)

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun", "proverb"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} merrily all the time {proverb} {plural_noun}."""
)