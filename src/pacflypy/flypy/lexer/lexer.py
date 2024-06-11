import re
import pacflypy

class _TOKEN:
    """
    Klasse für Token mit allen akzeptierten Token
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
        'COMMENT': r'///.*',
        'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
        'OPERATOR': r'->|<-',
        'NUMBER': r'\b\d+\b',
        'NEWLINE': r'\n',
        'WHITESPACE': r'\s+',
        'UNKNOWN': r'.'
    }

class lexer:
    """
    Klasse zum Lexen der flypy-Erweiterungssprache
    """
    def __init__(self, content: str):
        self.content = content
        self.tokens = self._tokenize(content=self.content)

    def _tokenize(self, content: str) -> dict:
        token_dict = {}
        for token_type, regex in _TOKEN.TOKEN.items():
            matches = re.finditer(regex, content, re.MULTILINE)
            token_dict[token_type] = [match.group(0) for match in matches]
        return token_dict

    def get(self):
        return self.tokens