# Store Assistant

Store Assistant is an application that helps customers understand products without the need for a sales representative. It uses the GPT-3 text-davinci-003 model to answer customer questions.
## How it works

Customers can scan a QR code located near a product and receive information about the product. If they have any questions, they can ask the Store Assistant and receive an accurate and detailed answer.
## Technical details

The application uses a customized api to fetch data of the product from an SQLite database.

The application is built using the GPT-3 Davinci model, which is a powerful language generation model developed by OpenAI.

The application uses the OpenAI's API to fine-tune the model and generate answers.

The consumer can scan the QR code from any application like Google Lens, Gpay, Paytm, etc.
    
## Installation and usage

Add product details in the database using Postman. 
    
    The API endpoint for POST method is https://540zfa.deta.dev/item/
    
    Checkout API documentation at https://540zfa.deta.dev/docs
    
Generate a QR code for the product by embedding this link "https://prathamsoneja-store-assistant-app-p5vz0t.streamlit.app/?item_id={id}". 

    Replace the id with product id.

    Scan the QR code located near the product and ask questions using the interface provided.

## Limitations

The model is only as good as the description of the product, so it may not be able to answer all questions accurately.
The model is only able to answer questions in English.
The GPT-3 model has certain usage limits and cost associated with it.

## Future work

Adding support for multiple languages.
    
## Contributions

Pull requests and suggestions for improvement are welcome.

## Licensing

This project is licensed under the MIT License. See LICENSE for more information.

## Note

This application is just for demonstration purposes and the usage of GPT-3 model is subject to OpenAI's API terms of service.
If you want to use the model in production, you may need to consider the cost and usage limits of the API.
