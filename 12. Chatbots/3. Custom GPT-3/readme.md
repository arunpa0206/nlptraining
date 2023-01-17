read me for fine tuning gpt 3

1. Preparing the training data
GPT-3 expects your finetune dataset to be in a specific JSONL file format, which looks like this -

{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}


2.pip install openai

3.openai tools fine_tunes.prepare_data -f '/content/gdrive/MyDrive/depression-data/depression.jsonl'

4.set OPENAI_API_KEY=<YOUR-API-KEY>

5.openai api fine_tunes.create -t "/content/gdrive/MyDrive/depression-data/depression_prepared.jsonl" -m davinci

6. Login to OpenAI account and go to OpenAI Playground and select newly created fine tuned model
   OR
   Using the command line to chat with the bot
   
   openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>
