## Function for comparing backbone mutation and variant mutation 
## Result is mutation introduced
def introduced_mutations(bb_mut, var_mut):
    bb_list = str.split(bb_mut)
    var_list = str.split(var_mut)
    
    diff_list = []
    for i in var_list:
        if i not in bb_list:
            diff_list.append(i)
    intro_mut_str = ' '.join(diff_list)
    return(intro_mut_str)
    
    
#### Part 1 (get mutation information from variant data)
## Merge purified data from KC with Variant data using a left join
merged_data = pd.merge(purified_data, variant_data, how='left', on='Sample')

purified_data['Total Mutation'] = merged_data['Total Mutation_y'].where(~merged_data['Total Mutation_y'].isnull(), purified_data['Total Mutation'])
#purified_data.head()
########################################

#### Part 2 (clean and  prepare purified data)
## Imputation of undefined values in Total mutation column. 
## 0 is replaced with NAN first and subsequently all NANs are converted to blanks (for ease of reading)
purified_data['Total Mutation'].replace(0, np.nan, inplace = True)
purified_data['Total Mutation'].replace(np.nan, '', inplace = True)
#purified_data

## If there is no backbone mutation column, add it
if 'Backbone_mutation' not in purified_data.columns:
    purified_data['Backbone_mutation'] = ''
########################################

####Part 3 (update introduced mutations)
## Loop through all rows of the data frame and set value of Backbone mutation, 
## by looking up the backbone in Sample column and getting it's Total mutation value
for index, row in purified_data.iterrows(): #Iterate through the dataframe
    backbone = row['Back bone'] #Get the backbone for each row
   
    try:
        # Check if the above backbone has a record under Sample colum. If it does, get the first such row
        sample_mut_row = purified_data[purified_data['Sample']==backbone].index[0] 
    except IndexError as error:
        # No mutation found for the backbone
        print("No mutation found for BB " + str(backbone))
        bb_mut_val = ''
        #purified_data.loc[index, 'Backbone_mutation'] = '' #Set the backbone mutation to be empty
        #next
        
    # Get Total mutation column value for the row found above
    bb_mut_val = purified_data.loc[purified_data.index[sample_mut_row], 'Total Mutation']
    #Set that as the value for the bb mutation
    purified_data.loc[index, 'Backbone_mutation'] = bb_mut_val
    
    var_mut_val = row['Total Mutation']
    intro_mut_val = introduced_mutations(bb_mut_val, var_mut_val)
    purified_data.loc[index, 'Mutation introduced'] = intro_mut_val
