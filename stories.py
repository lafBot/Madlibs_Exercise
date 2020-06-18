"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

    #     >>> s = Story(
    #     ...     "Novel",
    #     ...     "A Novel Story",
    #     ...     ["noun", "verb"],
    #     ...     "I love to {verb} a good {noun}.")

    # To generate text from a story, pass in a dictionary-like thing
    # of {prompt: answer, promp:answer):

    #     >>> ans = {"verb": "eat", "noun": "mango"}
    #     >>> s.generate(ans)
    #     'I love to eat a good mango.'
    # """

    def __init__(self, identifier, title, words, text):
        """Create story with words and template text."""

        self.id = identifier
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "adventure",
    "An Exciting Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

stories = {s.id: s for s in [story1, story2]}