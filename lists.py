def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements)>=6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
        
    elif len(list_to_remove_elements)>=5:
        del list_to_remove_elements[5]
        del list_to_remove_elements[0]
        return list_to_remove_elements
        
    elif len(list_to_remove_elements)>0 and list_to_remove_elements<=4:
        del list_to_remove_elements[0]
        return list_to_remove_elements
list1=['Red', 'Green', 'White', 'Black', 'Pink','yellow']



def add_elements(list_to_add_elements):
    list2=['Red', 'Green', 'White', 'Black']
    list_to_add_elements.insert(0,'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements


    

def is_empty(list_to_check):
    lista3=[]
    if list_to_check==[]:
        return "La lista esta vacia"
    else:
        return "La lista no esta vacia"
 



def check_lists(list_to_compare1, list_to_compare2):
    list4=['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
    list5=['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
    if len(list_to_compare1)>=3 and len(list_to_compare2)>=3:
        if list_to_compare1[2]==list_to_compare2[2]:
            return 'True'
        else:
            return 'False'
    elif (len(list_to_compare1)>0 and len(list_to_compare1)<3) or (len(list_to_compare2)>0 and len(list_to_compare2)<3):
        return 'False'
    else:
        return 'False'




def list_of_lists(list_of_lists_to_modify):
    list6=[[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
    if len(list_of_lists_to_modify)>2:
        if len(list_of_lists_to_modify[0])>=1:
            el1=list_of_lists_to_modify[0][0:2]
        else:
            el1=[]
    if len(list_of_lists_to_modify[1])>=2:
        el2=list_of_lists_to_modify[1][1:4]
    else:
        el2=[]
    if len(list_of_lists_to_modify[2])>=1:
            el3=list_of_lists_to_modify[2][-2:]
    else:
        el3=[]
        return [el1,el2,el3]
