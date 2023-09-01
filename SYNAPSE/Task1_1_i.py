jumbled_superheroes = ['DocToR_sTRAngE', 'sPidERmaN', 'MoON_KnigHT', 'caPTAIN_aMERIca', 'hULK']
indices, decoded_names, name_lengths = [], [], []

for count, ele in (enumerate(jumbled_superheroes)):
    indices.append(count)
    decoded_names.append(ele.lower().replace('_', ' '))
print("Indices-", indices)
print("Decoded names-", decoded_names)

name_lengths = list(map(lambda x: len(x), decoded_names))
print("Name lengths-", name_lengths)

sort_list, new_indices = [], []
for i in range(5):
    sort_list.append(([name_lengths[i], indices[i], decoded_names[i]]))
sort_list.sort()

print("Phase 5 kickoff list :")
for i in range(len(sort_list)):
    print(i+1, ". ", sort_list[i][2].title(), sep="")