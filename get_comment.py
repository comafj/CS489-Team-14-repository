import pandas as pd

#dataset = pd.read_csv("./crawling_output/crawling_output_0.tsv", delimiter='\t')
def tsv_body(file_name):
    df = pd.read_csv(file_name, delimiter='\t')
    body = df.columns[2]
    return body

def tsv_comments(file_name):
    df = pd.read_csv(file_name, delimiter='\t')
    df = df.loc[~df.index.duplicated(keep='first')]
    result = []
    index_arr = df.index
    cnt=1
    for i in index_arr:
        if i == cnt:
            arr = []
            arr.append(cnt)
            arr.append(df.loc[cnt][0])
            arr.append(df.loc[cnt][1])            
            arr.append(df.loc[cnt][2])
            arr.append(df.loc[cnt][3])
            result.append(arr)
            cnt+=1
    return result

def only_tsv_comments(file_name):
    df = pd.read_csv(file_name, delimiter='\t')
    df = df.loc[~df.index.duplicated(keep='first')]
    result = []
    index_arr = df.index
    for i in index_arr:
        result.append(df.loc[i][0])
    return result

file_0 = "./crawling_output/crawling_output_0.tsv"
#print(tsv_body(file_0))
#print(tsv_comments(file_0))
#print(only_tsv_comments(file_0))