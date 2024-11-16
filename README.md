## SpaCy Article Breaker
`**sab.py**` is a Python script that reads an article from a text file, breaks it into sentences using **SpaCy**, and writes those sentences into a new output text file, with one sentence per line.

This project also includes setting up a virtual environment for dependencies, making it easy to install and manage libraries.

## Requirements
- **Python 3.10.xx**  
- **SpaCy** library for natural language processing.
- **en_core_web_sm** SpaCy model.

## Setup Instructions

### 1. Create a Virtual Environment

Before running the script, it's best to set up a Python virtual environment to keep dependencies isolated:

```bash
python -m venv sab  # Create a virtual environment named 'sab'
```

### 2. Activate the Virtual Environment

- **Windows**:
  ```bash
  .\sab\Scripts\activate
  ```

- **Mac/Linux**:
  ```bash
  source sab/bin/activate
  ```

### 3. Install Dependencies

Once the virtual environment is activated, install the required dependencies (`spaCy`):

```bash
pip install spacy
```

Then, download the **SpaCy language model** for English:

```bash
python -m spacy download en_core_web_sm
```

### 4. Prepare Your Input File

- Create a text file named `input.txt` in the same directory as your script, or specify the path to the file in the script.
- Make sure the file contains the article you want to process.

### 5. Run the Script

With the virtual environment activated and dependencies installed, run the script:

```bash
python sab.py
```

This will process the `input.txt` file, break it into sentences, and save the output in `output.txt`.

### 6. Output

The sentences will be saved in `output.txt`, one sentence per line. The file will be generated in the same directory.

### Example Input (`input.txt`):
```
This is the first paragraph. It contains multiple sentences. Here's another one to show how SpaCy works.
SpaCy is a great tool for text processing. It can break paragraphs into sentences effectively.
```

### Example Output (`output.txt`):
```
This is the first paragraph.
It contains multiple sentences.
Here's another one to show how SpaCy works.
SpaCy is a great tool for text processing.
It can break paragraphs into sentences effectively.
```

## Deactivating the Virtual Environment

When you're done, deactivate the virtual environment with:

```bash
deactivate
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README file will guide users through the process of setting up the environment and running your script. Let me know if you need more adjustments!
