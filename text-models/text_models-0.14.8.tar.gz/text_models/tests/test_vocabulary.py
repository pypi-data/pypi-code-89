# Copyright 2020 Mario Graff Guerrero

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from abc import abstractclassmethod
from text_models.vocabulary import Vocabulary, Tokenize, BagOfWords


def test_init():
    from microtc.utils import Counter
    day = dict(year=2020, month=2, day=14)
    voc = Vocabulary(day, lang="En")
    assert isinstance(voc.voc, Counter)
    assert voc._n_words > 0
    voc2 = Vocabulary(voc.voc)
    assert voc2["love"] == voc["love"]    
    voc = Vocabulary(day, lang="En", country="US")
    assert isinstance(voc.voc, Counter)
    voc = Vocabulary(day, lang="Es", country="MX", states=True)
    assert isinstance(voc.voc, dict)
    day2 = dict(year=2021, month=2, day=14)
    voc = Vocabulary([day2, day])
    assert isinstance(voc.voc, Counter)
    voc = Vocabulary([day2, day], lang="En", country="US")
    assert isinstance(voc.voc, Counter)
    voc = Vocabulary([day2, day], lang="Es", country="MX", states=True)
    assert isinstance(voc.voc, dict)


def test_common_words():
    voc = Vocabulary(dict(year=2020, month=2, day=14))
    words = voc.common_words()
    assert len(words) > 10000
    w = voc.common_words(quantile=0.85)
    print(len(w))
    w2 = voc.common_words(quantile=0.85, bigrams=False)
    assert len(w) > len(w2)
    w3 = voc.common_words(quantile=0.80, bigrams=False)
    assert len(w2) > len(w3)
    print(len(w3))


def test_co_occurrence():
    voc = Vocabulary(dict(year=2020, month=2, day=14))
    data = voc.co_occurrence("amor")
    assert isinstance(data, dict)
    assert "amistad" in data
    voc = Vocabulary(dict(year=2020, month=2, day=14), country="MX", states=True)
    data = voc.co_occurrence("amor")
    assert "MX-DIF" in data
    assert "amistad" in data["MX-DIF"]


def test_remove():
    voc = Vocabulary(dict(year=2020, month=2, day=14))
    numterms = len(voc.voc)
    voc.remove(voc.common_words())
    assert numterms > len(voc.voc)
    voc = Vocabulary(dict(year=2020, month=2, day=14))
    numterms = len(voc.voc)
    voc.remove(voc.common_words(quantile=0.85), bigrams=False)
    assert numterms > len(voc.voc)


def test_date():
    from datetime import datetime
    voc = Vocabulary(dict(year=2020, month=2, day=14))
    assert isinstance(voc.date, datetime)
    days = [dict(year=2020, month=2, day=14),
            dict(year=2021, month=2, day=14)]
    voc = Vocabulary(days)
    assert voc.date is None


def test_day_words():
    voc = Vocabulary(dict(year=2020, month=2, day=14), lang="En")
    words = voc.day_words()
    assert words is not None
    assert isinstance(words, Vocabulary)
    print(words.date)


def test_remove_qgrams():
    voc = Vocabulary(dict(year=2020, month=2, day=14), lang="En")
    voc.remove_qgrams()


def test_previous_day():
    from os.path import basename

    voc = Vocabulary(dict(year=2020, month=2, day=14), lang="En")
    prev = voc.previous_day()
    assert prev.date.day == 13


def test_dict_functions():
    voc = Vocabulary(dict(year=2020, month=2, day=14))

    assert len(voc) == len([x for x in voc])
    data = [k for k, v in voc.items()]
    assert len(voc) == len(data)
    assert data[0] in voc
    assert "BLABLA" not in voc
    assert voc.get("BLABLA") == 0
    assert voc[data[0]] == voc.get(data[0])


def test_remove_emojis():
    voc = Vocabulary(dict(year=2020, month=2, day=14))
    voc.remove_qgrams()
    voc.remove_emojis()


def test_country():
    date = dict(year=2020, month=2, day=14)
    voc = Vocabulary(date, lang="Es", country="MX")
    assert len(voc)
    voc2 = Vocabulary(date, lang="Es")
    print(len(voc2), len(voc))
    assert voc2.voc.update_calls > voc.voc.update_calls


def test_vocabulary_dict():
    class D(object):
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

    voc = Vocabulary(dict(year=2020, month=2, day=14))
    assert voc["buenos"]
    voc2 = Vocabulary(D(2020, 2, 14))
    assert voc["buenos"] == voc2["buenos"]


def test_probability():
    day = dict(year=2020, month=2, day=14)
    voc = Vocabulary(day, lang="En")
    voc.probability()
    assert voc["the"] > 0 and voc["the"] < 1


def test_vocabulary_data_lst():
    import pandas as pd

    d = list(pd.date_range("2020-02-13", "2020-02-14"))
    print(len(d))
    vocs = Vocabulary(d)
    assert vocs["buenos"]
    assert len(d) == 2


def test_tokenize_fit():
    # voc1 = Vocabulary(dict(year=2020, month=7, day=21), token_min_filter=0)
    # print(voc1.voc)
    tok = Tokenize().fit(["hola", "holas", "mma", "ma~xa", "hola"])
    assert len(tok.vocabulary) == 4
    assert tok.vocabulary["ma~xa"] == 3


def test_tokenize_find():
    # voc1 = Vocabulary(dict(year=2020, month=7, day=21), token_min_filter=0)
    # print(voc1.voc)
    tok = Tokenize().fit(["hola", "holas", "mma", "ma~xa", "hola"])
    cdn = "holas~mmado~hola"
    wordid, pos = tok.find(cdn)
    assert wordid == 1 and pos == 5
    wordid, pos = tok.find(cdn, i=pos)
    assert wordid == -1
    wordid, pos = tok.find(cdn, i=pos+1)
    assert wordid == 2
    wordid, pos = tok.find("xa")
    assert wordid == -1


def test_tokenize__transform():
    # voc1 = Vocabulary(dict(year=2020, month=7, day=21), token_min_filter=0)
    # print(voc1.voc)
    tok = Tokenize().fit(["hola", "holas", "mma", "ma~xa", "hola"])
    cdn = "holas~mmado~hola~xa~ma~xa~hola"
    _ = tok._transform(cdn)
    for a, b in zip(_, [1, 2, 0, 3, 0]):
        assert a == b


def test_tokenize_transform():
    # voc1 = Vocabulary(dict(year=2020, month=7, day=21), token_min_filter=0)
    # print(voc1.voc)
    tok = Tokenize().fit(["hola", "holas", "mma", "ma~xa", "hola"])
    cdn = "holas mmado hola xa ma xa hola"
    _ = tok.transform(cdn)
    for a, b in zip(_, [1, 2, 0, 3, 0]):
        assert a == b
    _ = tok.transform([cdn])
    assert len(_) == 1
    assert len(_[0]) == 5


def test_BagOfWords_init():
    from microtc.utils import load_model
    from EvoMSA.utils import download    
    tm = BagOfWords()
    xx = list(load_model(download("b4msa_Es.tm")).model.word2id.keys())
    tm2 = BagOfWords(tokens=xx)
    assert len(tm.tokenize.vocabulary) == len(tm2.tokenize.vocabulary)
    # inv = {v: k for k, v in tm.tokenize.vocabulary.items()}
    # print(len(inv))
    # print([inv[x] for x in tm.tokenize.transform("buenos dias mujer madres zorra")])
    # print([x for x in tm.tokenize.vocabulary.keys() if len(x) == 1])
    # assert False


def test_BagOfWords_fit():
    from EvoMSA.tests.test_base import TWEETS
    from microtc.utils import tweet_iterator
    from scipy.sparse import csr_matrix

    X = list(tweet_iterator(TWEETS))
    bg = BagOfWords().fit(X)
    bg = BagOfWords().fit([x["text"] for x in X])
    xx = bg._transform(["buenos y felices dias"])
    print(len(xx), len(xx[0]), xx)
    assert len(xx) == 1 and len(xx[0]) == 3 and len(xx[0][1]) == 2
    xx = bg.transform(["buenos y felices dias"])
    assert isinstance(xx, csr_matrix)
    # inv = bg.id2word
    # print([(inv(k), v) for k, v in bg.tfidf[xx[0]]])
    # assert False
    # print(bg._cnt)
    # 
    # for k, v in bg._cnt.most_common(10):
    #     print(inv[k], v)
    # assert False