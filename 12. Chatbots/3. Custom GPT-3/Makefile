dep:
	pip install openai

build:
	openai tools fine_tunes.prepare_data -f 'depression.jsonl'
	set OPENAI_API_KEY=<YOUR-API-KEY>
	openai api fine_tunes.create -t "depression_prepared.jsonl" -m davinci

test:
	openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>
