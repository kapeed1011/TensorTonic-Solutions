def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    top_k=recommended[:k]
    precision=len(set(top_k).intersection(relevant))/k
    recall=len(set(top_k).intersection(relevant))/len(relevant)
    return [precision,recall]
    # Write code here