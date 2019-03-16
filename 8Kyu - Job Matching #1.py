def match(candidate, job):
    #your code here
    return candidate['min_salary']*0.9 <= job['max_salary'] 
