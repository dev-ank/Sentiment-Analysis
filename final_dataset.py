'''

Code to prepare the training data for training through a deep neural network.

'''


import pandas as pd
import glob


df=pd.read_json('Clothing_Shoes_and_Jewelry.json',lines=True,chunksize=1000000)

counter=1
for chunk in df:
    chunk=chunk[['reviewText','overall','summary']]    #extracting equal number of positive, negative,neutral reviews to make the dataset balanced
    df1=chunk[chunk['overall']==1.0].sample(4000)
    df2=chunk[chunk['overall']==2.0].sample(4000)
    df3=chunk[chunk['overall']==3.0].sample(8000)
    df4=chunk[chunk['overall']==4.0].sample(4000)
    df5=chunk[chunk['overall']==5.0].sample(4000)
    
    combined_chunk=pd.concat([df1,df2,df3,df4,df5],axis=0,ignore_index=True)
    combined_chunk.to_csv(str(counter)+'.csv',index=False)
    print(f'{counter} out of 33')
    counter+=1

    
print('completed')


files=glob.glob('*.csv')  #combining all csv's into a single one

combined_csv=pd.concat([pd.read_csv(f) for f in files],axis=0,ignore_index=True)
combined_csv.to_csv('final_dataset.csv',index=False)




    


    
    
    
    
    
    
    
    