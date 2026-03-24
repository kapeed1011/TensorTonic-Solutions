import math
def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """
    # Write code here
    n=len(production_log)
    production_accuracy=0
    shallow_accuracy=0
    latency_shallow=[]
    agreement=0
    for i in range(len(production_log)):
        latency_shallow.append(shadow_log[i]['latency_ms'])
        if production_log[i]['prediction']==production_log[i]['actual']:
            production_accuracy+=1
        if shadow_log[i]['prediction']==shadow_log[i]['actual']:
            shallow_accuracy+=1
        if production_log[i]['prediction']==shadow_log[i]['prediction']:
            agreement+=1
    agreement_rate=agreement/n
    production_accuracy=production_accuracy/n
    shallow_accuracy=shallow_accuracy/n
    sorted_latency=sorted(latency_shallow)
    rank=math.ceil(0.95*n)
    p95_value=sorted_latency[rank-1]
    output={}
    min_accuracy_gain=shallow_accuracy-production_accuracy
    flag=False
    if min_accuracy_gain>=criteria['min_accuracy_gain'] and p95_value<=criteria['max_latency_p95'] and agreement_rate>=criteria['min_agreement_rate']:
        flag=True
    output['promote']=flag
    output['metrics']={'shadow_accuracy':shallow_accuracy,'production_accuracy':production_accuracy,'accuracy_gain':min_accuracy_gain,'shadow_latency_p95':p95_value,'agreement_rate':agreement_rate}
    return output
    
        
    