OpenAI - https://openai.com/


Step 1. Create the training data

GPT-3 expects your finetune dataset to be in a specific JSONL file format, which looks like this -

`{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}`


Step 2. Install OpenAI

`pip install openai`

Step 3. Prepare the Training Data

`openai tools fine_tunes.prepare_data -f 'depression.jsonl'`

Step 4. Set OpenAI API KEY

`set OPENAI_API_KEY=<YOUR-API-KEY>`

Step 5. Create Fine Tuned Model

`openai api fine_tunes.create -t "depression_prepared.jsonl" -m davinci`

Step 6. Start chatting with the new chatbot

There are two ways to chat with the fine tuned model. 

a. Login to OpenAI account and go to OpenAI Playground and select newly created fine tuned model and start chatting.


b. Using the command line to chat with the bot
   
`openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>`
