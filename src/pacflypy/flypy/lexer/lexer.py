# The flypy Lexer for Working with flypy Extensions
import pacflypy.command as command
import pacflypy.string as string
import pacflypy.system as system
import re
import shutil

content = """
create pyclass Example
    classfunc init(self, name -> str <- None)
        pyvar -> self.name = name

    classfunc write_name(self)
        pyshow str(#_self.name_#)

pyfunc add_sum_as_string(a -> int <- 0, b -> int <- 0)
    give_back str(#_a_# + #_b_#)

/// * This is a Doc String for flypy
/// * flypy should a Extension Language for Python in Combination with pacflypy
/// * In there You can Write Python Classes and Function Easier and Can Bind him In
/// * The flypy Extension Language
"""

class _TOKEN:
    """
    Class for Token with all Accepted Token
    """
    TOKEN = {
        'CLASS': r'\bpyclass\b',
        'CLASSFUNC': r'\bclassfunc\b',
        'PYVAR': r'\bpyvar\b',
        'PYSHOW': r'\bpyshow\b',
        'PYFUNC': r'\bpyfunc\b',
        'GIVE_BACK': r'\bgive_back\b',
        'STR': r'\bstr\b',
        'INT': r'\bint\b',
        'NONE': r'\bnone\b',
        'DOC': r'\b///\*',
        '': r'\b\b',
    }

class lexer:
    """
    Class for Lexing the flypy Extension Language
    """
    def __init__(self, content: str) -> str:
        """
        Init the Lexer with Given Content
        """
        self.content = content
        token = self._tokenize(content=self.content)

    def _tokenize(self, content: str) -> dict:
        """
        Tokenize the Content and Return A Directory with all Tokens
        """
        # Erstelle ein Dictionary fuer die Token
        token = {}

        # Werte content aus und Parse diese zu Token
