import numpy as np

def calculate(list):

    if(len(list)!=9):
        raise ValueError("List must contain nine numbers.")
    
    #making dict variable
    result = {}

    #Converting array into 3x3 matrix
    matrix = np.reshape(list, (3,3))
    
    #Calculating 'mean' values
    result['mean'] = [matrix.mean(axis=0).tolist() , matrix.mean(axis=1).tolist(), matrix.mean().tolist()]

    #Calculating 'variance' values
    result['variance'] = [matrix.var(axis=0).tolist() , matrix.var(axis=1).tolist(), matrix.var()]

    #Calculating 'standard deviation' values
    result['standard deviation'] = [matrix.std(axis=0).tolist() , matrix.std(axis=1).tolist(), matrix.std()]

    #Calculating 'max' values
    result['max'] = [matrix.max(axis=0).tolist() , matrix.max(axis=1).tolist(), matrix.max()]

    #Calculating 'min' values
    result['min'] = [matrix.min(axis=0).tolist() , matrix.min(axis=1).tolist(), matrix.min()]

    #Calculating 'sum' values
    result['sum'] = [matrix.sum(axis=0).tolist() , matrix.sum(axis=1).tolist(), matrix.sum()]

    return result

