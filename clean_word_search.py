direction_dict = {
			0 : (0, 1), 
			1 : (1, 1), 
			2 : (1, 0), 
			3 : (1, -1), 
			4 : (0, -1), 
			5 : (-1, -1), 
			6 : (-1, 0), 
			7 : (-1, 1)}
#this is just a big dictionary of all the different directions (north, northwest, etc)
#you can split this into like an x value and a y value or you van use this 
#    int x[] = {0, 1, 1,  1,  0, -1, -1, -1};
#    int y[] = {1, 1, 0, -1, -1, -1,  0,  1};
#this is how i split it for my c++ class 


def matrix_search(matrix, word):
	row_size = len(matrix[0]) #how many rows 
	col_size = len(matrix) #how many cols 

	for startR in range(row_size): 

		for startC in range(col_size): 

			start_char = matrix[startC][startR]
			#this is the character of the first letter you are looking for 
			if start_char == word[0]: 

				for dirr in range(8): 
					col_offset, row_offset = direction_dict[dirr] 
					#pull from dict a value like (-1, 0) and then -1 will be how much the col is manipulated 

					col_target = col_offset + startC 
					#so col_target is the new column value were looking at to see if it has the right character 
					#we get to this value by adding the offset (so value from dict) and the starting col position

					row_target = row_offset + startR
					#same but row 

					if ((col_target >= col_size or col_target < 0) or (row_target >= row_size or row_target < 0)): 
						continue #if we hit this, it goes to the next direction or kill loop if done 
						#but if the col or row target is out of bounds, we just continue checking 
						#meaning we continue to try different directions 

					if matrix[col_target][row_target] == word[1]: 
						#will run loop regardless 
						found = True 

						for i in range(2, len(word)): 
							#we have already checked the first two letters so were checking the rest of the word 
							char_target = word[i] #word is stored in character 
							col_target += col_offset 
							row_target += row_offset 
							if ((col_target >= col_size or col_target < 0) or (row_target >= row_size or row_target < 0)):
								print('F') 
								found = False 
								break #we hit the edge n didnt find word 
							if matrix[col_target][row_target] != char_target:
								#if its not the right char then break 
								print('F')
								found = False
								break

						if found: 
							return ((startC, startR), (col_target, row_target))
			


if __name__ == '__main__':  
	num_cases = int(input())  #taking in the number of cases 

	for l in range(num_cases):
		input() 
		#just a spacer 

		num_row_col = input() 
		# taking in the amt of rows and cols 

		matrix = []
		#initializing matrix 

		split_nrc = num_row_col.split()	 
		#you are given two numbers as a string in num_row_col

		row = int(split_nrc[0])	
		#turn first num into int and assign it as the num of rows 
		col = int(split_nrc[1])	 
		#same but cols 

		for i in range(row): 
			val = input()
			#taking in all the rows 
			val = val.replace(" ", "")
			matrix.append(val)
			#idk but its formatting 

		word = input()
		#word youre looking for 



		output = matrix_search(matrix, word)
		#go to the function 
		print('Searching for "%s" in matrix %d yields:' % (word, l))
		if matrix_search(matrix, word) == None:
			print('The pattern was not found.\n')
		else:
			start = matrix_search(matrix, word)[0]
			end = matrix_search(matrix, word)[1]
			print("Start pos: %s to End pos: %s\n" % (start, end))



