import numpy as np
import cosinesimilarilty as cossimilarity
def evaluation(doc_set,qry_set,D,N,total_vocab,DF):
    rel_set = {}
    with open('CISI/CISI.REL') as f:
        for l in f.readlines():
            qry_id = l.lstrip(" ").strip("\n").split("\t")[0].split(" ")[0]
            doc_id = int(l.lstrip(" ").strip("\n").split("\t")[0].split(" ")[-1])
            if qry_id in rel_set:
                rel_set[qry_id].append(doc_id)
            else:
                rel_set[qry_id] = []
                rel_set[qry_id].append(doc_id)

    precision_list = []
    recall_list = []
    accuracy_list = []

    for i in range(1, len(doc_set)):
        try:
            result_from_cosine = cossimilarity.cosine_similarity(6, qry_set[str(i)],D,N,total_vocab,DF).tolist()
            result_from_ground_truth = rel_set[str(i)]

            true_Positive = len(set(result_from_cosine) & set(result_from_ground_truth))
            false_Positive = len(np.setdiff1d(result_from_cosine, result_from_ground_truth))
            false_Negative = len(np.setdiff1d(result_from_ground_truth, result_from_cosine))
            true_negative = (len(doc_set) - (true_Positive + false_Negative + false_Positive))

            try:
                precission = (true_Positive) / (true_Positive + false_Positive)
                recall = (true_Positive) / (true_Positive + false_Negative)

                accuracy = (true_negative + true_Positive) / (true_negative + true_Positive + false_Negative + false_Positive)

            except ZeroDivisionError:
                pass

            precision_list.append(precission)
            recall_list.append(recall)
            accuracy_list.append(accuracy)

        except KeyError:
            pass

#for i in rang(1,len(result_from_cosine)):
   # doc=result_from_cosine[i]
   # if(result_from_tgroup.__cosine__(doc)):
  #      rr_list.append(i)
   #     break

    average_precision = sum(precision_list)
    average_recall = sum(recall_list)
    Accuracy = sum(accuracy_list)
    F_Measure = (2 * average_precision * average_recall) / (average_precision + average_recall)
    print("Average Precision is : ", average_precision)
    print("Precision is : ", precission)
    print("Average Recall is : ", average_recall)
    print("Recall is : ", recall)
    print("F-score is : " ,F_Measure)
    print("Accuracy : " ,Accuracy)
   # return average_precision,average_recall,F_Measure,Accuracy
