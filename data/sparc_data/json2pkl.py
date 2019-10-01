import pickle
import json
import sys 

with open(sys.argv[1]) as jsonfile:
    interaction_list = json.load(jsonfile)

new_objs = [] 
for i, obj in enumerate(interaction_list):
    new_interaction = []
    for ut in obj["interaction"]:
        sql = ut["sql"]
        sqls = [sql]
        tok_sql_list = []
        for sql in sqls:
            results = []
            tokenized_sql = sql.split()
            tok_sql_list.append((tokenized_sql, results))
        ut["sql"] = tok_sql_list
        new_interaction.append(ut)
    obj["interaction"] = new_interaction
    new_objs.append(obj)

with open(sys.argv[2],'wb') as outfile:
    pickle.dump(new_objs, outfile)