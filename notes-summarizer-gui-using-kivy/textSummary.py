from transformers import PegasusForConditionalGeneration
from transformers import PegasusTokenizer
# Pick model
model_name = "google/pegasus-xsum"

# Load pretrained tokenizer
pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)

f1 = open("speech.txt", 'r')
example_text= f1.read()

# Define PEGASUS model
pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

# Create tokens
tokens = pegasus_tokenizer(example_text, truncation=True, padding="longest", return_tensors="pt")

# Summarize text
encoded_summary = pegasus_model.generate(**tokens)

# Decode summarized text
decoded_summary = pegasus_tokenizer.decode(
      encoded_summary[0],
      skip_special_tokens=True
)
f = open("Summary.txt", 'w')
f.write(decoded_summary)
print(decoded_summary)
