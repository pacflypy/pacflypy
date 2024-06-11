# The flypy Lexer for Working with flypy Extensions

content = """
create pyclass Example
    classfunc init(self, name -> str <- None)
        pyvar -> self.name = name

    classfunc write_name(self)
        give_back str(#_self.name_#)

pyfunc add_sum_as_string(a -> int <- 0, b -> int <- 0)
    give_back str(#_a_# + #_b_#)
"""