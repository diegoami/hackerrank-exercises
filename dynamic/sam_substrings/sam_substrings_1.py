
inputarray =[
"123"
]

inputarray2 =[
"972698438521"
]
#sol 445677619#


from tools import input, initArrayInputter
initArrayInputter(inputarray2)



import sys
ncandies = input().strip()
element_list = [element for element in ncandies]+["0"]
sum_elements = [int(element) for element in ncandies]+[0]
concat_substring = [0]*(len(ncandies)+1)
for ncandies_index in range(len(ncandies)):
    curr_candy_char = element_list[ncandies_index]
    curr_candy_int  = int(curr_candy_char )
    print("Processing index {} : {} ".format(ncandies_index, curr_candy_char ),file=sys.stderr)
    print("Concatenation string before processing: {} ".format(concat_substring), file=sys.stderr)
    for string_index in range(ncandies_index+1,len(ncandies)+1):
        #sum_elements[string_index]  +=  curr_candy_int
        if (string_index == ncandies_index+1):
            print("    Adding {} to index {} ".format(concat_substring[ncandies_index], string_index),file=sys.stderr)
            concat_substring[string_index] +=  concat_substring[string_index-1]
        print("    Adding {} to index {} ".format(int(curr_candy_char + ncandies[ncandies_index + 1:string_index]), string_index),file=sys.stderr)
        concat_substring[string_index] += int(curr_candy_char+ncandies[ncandies_index+1:string_index] )
    print("Concatenation string after processing: {} ".format(concat_substring), file=sys.stderr)

print(concat_substring[-1] % 1000000007)




