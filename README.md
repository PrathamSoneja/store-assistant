# Store Assistant

Store Assistant is an application that helps customers understand products without the need for a sales representative. It uses the BERT-large-uncased-whole-word-masking-finetuned-SQUAD model to answer customer questions.
## How it works

Customers can scan a QR code located near a product and receive information about the product. If they have any questions, they can ask the Store Assistant and receive an accurate and detailed answer.
## Technical details

The application is built using the BERT-large-uncased-whole-word-masking-finetuned-SQUAD model, which is a pre-trained transformer-based model that has been fine-tuned on the SQuAD dataset for question answering tasks.
The application uses the Hugging Face's transformers library to fine-tune the model and generate answers.

## Installation and usage

1. Clone the repository:

    git clone https://github.com/PrathamSoneja/store-assistant.git

2. Install the required packages:

    pip install -r requirements.txt

3. Run the application:

    python app.py

4. Scan the QR code located near the product and ask questions using the interface provided.

## Contributions

Pull requests and suggestions for improvement are welcome.

## Licensing

This project is licensed under the MIT License. See LICENSE for more information.
