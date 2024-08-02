def Get_Hot_Num(Char, Arr):
	for i in range(0, len(Arr)): 
		if Char == Arr[i] : return i

def Get_One_Rand_Arr (Hot_Arr, Hot_Num, Hot_Rng):
	Rand_Arr  = []
	Rng_End = 0
	(Rng_End := Hot_Num + Hot_Rng) if (Hot_Num < len(Hot_Arr) - Hot_Rng) else (Rng_End := len(Hot_Arr))
	for i in range(Hot_Num, Rng_End)        : Rand_Arr.append(Hot_Arr[i])
	for i in range(0, Hot_Num)				: Rand_Arr.append(Hot_Arr[i])
	for i in range(Rng_End, len(Hot_Arr))	: Rand_Arr.append(Hot_Arr[i])
	return Rand_Arr

def Get_Rand_Arr(Hot_Arr, Hot_Key, Hot_Stg, Hot_Rng):
	Rand_Arr = Hot_Arr
	for i in range(0, Hot_Stg):
		for elm in Hot_Key:
			Hot_Num = Get_Hot_Num(elm, Hot_Arr)
			Rand_Arr = Get_One_Rand_Arr(Rand_Arr, Hot_Num, Hot_Rng)
	return Rand_Arr

def Get_Get_Hot(Set_Hot, Rand_Arr):
	Get_Hot = []
	for elm in Set_Hot:
		for i in range(0, len(Rand_Arr)):
			if elm == Rand_Arr[i] : Get_Hot.append(i)
	return Get_Hot

def Get_Set_Hot(Get_Hot, Rand_Arr):
	Set_Hot = ''
	for elm in Get_Hot:
		Set_Hot += Rand_Arr[elm]
	return Set_Hot

Hot_Arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "p", "q", "w", "e", "r", "t", "y", "u", "i", "o", ";", "a", "s", "d", "f", "g", "h", "j", "k", "l", "/", "z", "x", "c", "v", "b", "n", "m", ",", ".", ")", "!", "@", "#", "$", "%", "^", "&", "*", "(", "P", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", ":", "A", "S", "D", "F", "G", "H", "J", "K", "L", "?", "Z", "X", "C", "V", "B", "N", "M", "<", ">"]
# Hot_Arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "p", "q", "w", "e", "r", "t", "y", "u", "i", "o", ";", "a", "s", "d", "f", "g", "h", "j", "k", "l", "/", "z", "x", "c", "v", "b", "n", "m", ",", ".", ")", "!", "@", "#", "$", "%", "^", "&", "*", "(", "P", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", ":", "A", "S", "D", "F", "G", "H", "J", "K", "L", "?", "Z", "X", "C", "V", "B", "N", "M", "<", ">", " "]
# Hot_Arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "p", "q", "w", "e", "r", "t", "y", "u", "i", "o", ";", "a", "s", "d", "f", "g", "h", "j", "k", "l", "/", "z", "x", "c", "v", "b", "n", "m", ",", ".", ")", "!", "@", "#", "$", "%", "^", "&", "*", "(", "P", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", ":", "A", "S", "D", "F", "G", "H", "J", "K", "L", "?", "Z", "X", "C", "V", "B", "N", "M", "<", ">", " ", "[", "]", ]
# Hot_Arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "p", "q", "w", "e", "r", "t", "y", "u", "i", "o", ";", "a", "s", "d", "f", "g", "h", "j", "k", "l", "/", "z", "x", "c", "v", "b", "n", "m", ",", ".", ")", "!", "@", "#", "$", "%", "^", "&", "*", "(", "P", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", ":", "A", "S", "D", "F", "G", "H", "J", "K", "L", "?", "Z", "X", "C", "V", "B", "N", "M", "<", ">", " ", "[", "]", "_"]
Hot_Key = input("Enter Your Hot_key: ")
Hot_Stg = int(input("Enter Your Hot_Stg: "))
Hot_Rng = int(input("Enter Your Hot_Rng: "))
Rand_Arr = Get_Rand_Arr(Hot_Arr, Hot_Key, Hot_Stg, Hot_Rng)

# Example : ===================================================
# Set_Hot = input("Enter Your Set_Hot: ")
# print("Your Get_Hot is: ")
# print(Get_Get_Hot(Set_Hot, Rand_Arr))
		
# [38, 56, 28, 61, 45, 47, 56, 24, 61, 27, 51]
# Get_Hot = [38, 56, 28, 61, 45, 47, 56, 24, 61, 27, 51]
# print("Your Get_Hot is: ")
# print(Get_Set_Hot(Get_Hot, Rand_Arr))
	


# Set_Hot = input("Enter Your Set_Hot: ")
# print("Your Get_Hot is: ")
# print(Get_Get_Hot(Set_Hot, Rand_Arr))

# Get_Hot = 
# print("Your Get_Hot is: ")
# print(Get_Set_Hot(Get_Hot, Rand_Arr))










