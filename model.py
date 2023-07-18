import spacy
from spacy.lang.es.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from summary import Summary

class Model:
    def __init__(self, file_path, per) -> None:
        self.summary = Summary(file_path)
        self.text = self.summary.extractText()
        self.per = per

    def summarize(self):
        nlp = spacy.load('es_core_news_sm')
        doc = nlp(self.text)
        tokens = [token.text for token in doc]
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in list(STOP_WORDS):
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word]/max_frequency
        sentence_tokens = [sent for sent in doc.sents]
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]
        select_length = int(len(sentence_tokens)*self.per)
        summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
        final_summary = [word.text for word in summary]
        summary = ' '.join(final_summary)
        return summary
    
    def __str__(self) -> str:
        return self.summarize()
    
    def __repr__(self) -> str:
        return self.summarize()
    
# if __name__ == '__main__':
#     model = Model('CV_Johan_Franco_Rogel.pdf', 0.3)
#     print(model)