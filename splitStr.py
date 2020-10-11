#split the string and format it using end

str = 'Noctis, Ignis, Prompto, Gladio, Iris, Cid, Cindy, Luna, Ardyn'

def separate(str):
    str_list = str.split(',')
    for i in str_list:
        str_list = print(i, end='')
        
separate(str)
