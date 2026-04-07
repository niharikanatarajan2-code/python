test_dict={
    "id1":"apple",
    "id2":"banana",
    "id3":"apple",
    "id4":"orange",
    "id5":"apple"
}
freq_dict={}
for value in test_dict.values():
    if value in freq_dict:
        freq_dict[value]+=1
    else:
        freq_dict[value]=1
print(freq_dict)