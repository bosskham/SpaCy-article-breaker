import spacy

# Load the SpaCy model for sentence segmentation
nlp = spacy.load("en_core_web_sm")

def break_paragraph_to_sentences(paragraph_text):
    # Process the text through SpaCy pipeline
    doc = nlp(paragraph_text)
    
    # Extract sentences as a list of strings
    sentences = [sent.text.strip() for sent in doc.sents]
    
    return sentences

def process_text_file(input_filepath, output_filepath):
    # Read the input text file
    with open(input_filepath, 'r') as file:
        article_text = file.read()

    # Break the text into sentences using SpaCy
    sentences = break_paragraph_to_sentences(article_text)

    # Write the sentences to the output text file
    with open(output_filepath, 'w') as output_file:
        for sentence in sentences:
            output_file.write(f"{sentence}\n")
    
    print(f"Output saved to {output_filepath}")

# Example usage:
input_filepath = "input.txt"  # Your input file
output_filepath = "output.txt"  # Output file to save processed text

process_text_file(input_filepath, output_filepath)
