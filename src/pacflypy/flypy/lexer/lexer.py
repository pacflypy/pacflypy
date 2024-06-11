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