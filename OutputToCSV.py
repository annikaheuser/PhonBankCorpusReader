import ProvidenceUtils
from ProvidenceCorpusReader import ProvidenceCorpusReader
import os

path = "/Users/annika/Desktop/Penn/Year3/Liaison/Paris"
fileids = ProvidenceUtils.getFileIds(path, True)

#paris = ProvidenceCorpusReader(path, fileids)

csv_dir = '/Users/annika/Desktop/Penn/Year3/Liaison/ParisData'

for child in fileids.keys():
    if child != "Anae":
        continue

    paris = ProvidenceCorpusReader(path, fileids[child])

    child_file = open(os.path.join(csv_dir, '%s_child.csv' % child), 'w', encoding='utf-8')
    child_file.write('child,fileid,age,orthography,stem,model,actual,pos,utt_num,start_time,end_time\n')
    parent_file = open(os.path.join(csv_dir, '%s_parent.csv' % child), 'w',encoding='utf-8')
    parent_file.write('child,fileid,age,orthography,stem,phonemes,pos,utt_num,start_time,end_time\n')


    child_words = paris.words_info(fileids[child][:1],speaker=["CHI"])
    mot_words = paris.words_info(fileids[child][:1],speaker=["MOT"])

    for word in mot_words:
        parent_file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (child,word.fileid, word.age, word.orthography,
                                                      word.stem, '.'.join(word.transcription), word.pos,
                                                            word.utt_num, ','.join(str(t) for t in word.media_times)))
    for word in child_words:
        child_file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (child,word.fileid, word.age,word.orthography, word.stem,
                                                        '.'.join(word.transcription.model), 
                                                        '.'.join(word.transcription.actual), word.pos,
                                                              word.utt_num, ','.join(str(t) for t in word.media_times)))


print('Done.')
