from transformers import AutoTokenizer, AutoModelForCausalLM
import re
import ast
import astunparse


class PyDOC():

    def __init__(self, input_file_path):
        with open(input_file_path, 'r') as file:
            self.source_code = file.read()
            self.input_file_path = input_file_path
        # Load the models once in the constructor
        self.tokenizer = AutoTokenizer.from_pretrained(r"../../docGen_model")
        self.model = AutoModelForCausalLM.from_pretrained(r"../../docGen_model")


    def generate_docstring(self, function_source):
        inputs = self.tokenizer(function_source, return_tensors='pt')

        doc_max_length = 128

        generated_ids = self.model.generate(
            **inputs,
            max_length=inputs.input_ids.shape[1] + doc_max_length,
            do_sample=False,
            return_dict_in_generate=True,
            num_return_sequences=1,
            output_scores=True,
            pad_token_id=50256,
            eos_token_id=50256  # <|endoftext|>
        )
        docString = self.tokenizer.decode(
            generated_ids.sequences[0], skip_special_tokens=False)
        docstring_match = re.search(r'"""(.*?)"""', docString, re.DOTALL)
        if docstring_match:
            return docstring_match.group(1).strip()
        else:
            return None

    def process_python_file(self):
        # Parse the source code
        module = ast.parse(self.source_code)
        # Find all function definitions
        functions = [node for node in module.body if isinstance(
            node, ast.FunctionDef)]
        
        # Generate docstrings for each function
        for function in functions:
           # Convert the function AST back into source code
            function_source = astunparse.unparse(function)
            # Generate the docstring
            docstring = self.generate_docstring(
                function_source)  # pass the function object
            # Insert the docstring into the function AST
            function.body.insert(0, ast.Expr(value=ast.Str(s=docstring)))
            # Unparse the modified AST back into source code
            self.source_code = astunparse.unparse(module)

        return self.source_code


    @staticmethod
    def insert_docstring(function_source, docstring):
        # Split the function source code into lines
        lines = function_source.split('\n')
        # Insert the docstring after the function definition
        lines.insert(1, f'    """{docstring}"""')
        # Join the lines back together
        return '\n'.join(lines)


    def write_to_file(self):
        with open(self.input_file_path, 'w') as file:
            file.write(self.process_python_file())

