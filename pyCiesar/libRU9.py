def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','и')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','й')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','к')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','л')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','м')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','н')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','о')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','п')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','р')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','с')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','т')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','у')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','ф')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','х')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','ц')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','ч')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','ш')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','щ')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','ъ')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','ы')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','ь')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','э')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','ю')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','я')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','а')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','б')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','в')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','г')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','д')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','е')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','ё')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','ж')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','з')+a[k+1:]
    return a