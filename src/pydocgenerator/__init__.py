from transformers import AutoTokenizer, AutoModelForCausalLM

model_type = 'kdf/python-docstring-generation'
tokenizer = AutoTokenizer.from_pretrained(model_type)
model = AutoModelForCausalLM.from_pretrained(model_type)


# Save the model and tokenizer to a directory
model.save_pretrained("../../docgen_model")
tokenizer.save_pretrained("../../docgen_model")