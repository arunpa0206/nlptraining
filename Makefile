activate:
	source ../nlpenv/bin/activate

wine:
	cd 5.neuralnetworks/5.2.wine
	python3 wine.py
	cd ../..

news:
	cd 5.neuralnetworks/5.3.news
	python3 news.py
	cd ../..

word2vec:
	cd 6.embeddingModels
	python3 1.word2vec.py
	cd ..

rnnimdb:
	cd 7.rnn/RNN
	python3 1.simplernnimdb.py
	cd ../..

rnnreuters:
	cd 7.rnn/RNN
	python3 5.simplernnreuters.py
	cd ../..

lstmimdb:
	cd 7.rnn/LSTM
	python3 lstmimdb.py
	cd ../..

lstmreuters:
	cd 7.rnn/LSTM
	python3 lstmreuters.py
	cd ../..

bilstmimdb:
	cd 7.rnn/Bi_LSTM
	python3 bilstmimdb.py
	cd ../..

bilstmreuters:
	cd 7.rnn/Bi_LSTM
	python3 bilstmreuters.py
	cd ../..

bilstmfakenewsclassification:
	cd 7.rnn/Bi_LSTM
	python3 fake_news_classification.py
	cd ../..

gruimdb:
	cd 7.rnn/GRU
	python3 gruimdb.py
	cd ../..

grureuters:
	cd 7.rnn/GRU
	python3 gruretuters.py
	cd ../..

machine_translation:
	cd 13.Transformers
	python3 1.Machine_Translation.py
	cd ..

text_summarization:
	cd 13.Transformers
	python3 2.Text_Summarization.py
	cd ..

bert:
	cd 6.embeddingModels
	python3 3.bert.py
	cd ..

rasa:
	open https://drive.google.com/file/d/103mDeUoxI9pPHo2pctHOJDN96kPPxLEg/view?usp=sharing
	open https://drive.google.com/file/d/1HdFwOAN3uKBXkUfQqNLwMZXPvqVsVI_X/view?usp=sharing
	
google_dialogflow:
	open https://drive.google.com/file/d/1l01NiKjBQfIlVu1uHCIY5KaERYAeUbVf/view?usp=sharing

gpt-3:
	open https://drive.google.com/file/d/1NL9rWVsnK1vRWYRN1BI8P04LYMlwSAK2/view?usp=sharing

topic-modeling:
	cd 9.applications/2.topicmodelling
	python3 main.py
	cd ../..

optimization:
	cd 11.hyperparametertuning
	python3 1.simplernnoptimization.py
	cd ..