for found_stem_1 in found_stem:
	##print ("found_stem _1 = " + str(found_stem_1))
	for sente in found_stem_1:		
		##print("senetences")
		#print("The sentence is \n ")
		#print (str(sente).encode("utf-8"))
		for word in sente:			
			##print(str(word).encode("utf-8"), ': ', str(list(word.children)).encode("utf-8"))
			bach=list(word.children)
			
			for child in bach:
				##print("Parent: " + str(word) + "Child :")
				##print(str(child).encode('utf-8'))
				counter=-1
				
				for K in Key_Words:
					counter+=1
					##print(counter)
					if (str(word) in K):
						#print(action[counter].encode('utf-8'))
						#print( "One word Action found_stem")
						list_action_count.append(counter)

					if ((str(word) + " " + str(child) in K ) or (str(child) + " " + str(word) in K )):
						##print("Counter = "  + str(counter))
						#print((str(child) + " " + str(word)))
						#print("found_stem Action")
						##print(action[counter].encode('utf-8'))
						list_action_count_two.append(counter)
						#print("\n")




##print(list_action_count)

c=Counter(list_action_count)
print(sorted(c))

#print ("For two ")

##print(list_action_count_two)

c_two=Counter(list_action_count_two)
print(sorted(c_two))
