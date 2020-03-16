sde_dict = [('Assessment_End', 'Assessment_End', 'Date'), ('Assessment_Start', 'Assessment_Start', 'Date'), ('Concrete/Masonry Dams Physical Score', 'Concrete_Masonry_Dams_Physical_Score', 'Integer'), ('Cracking (Width of Crack)', 'Cracking__Width_of_Crack_', 'String'), ('CreationDate', 'CreationDate', 'Date'), ('Creator', 'Creator', 'String'), ('EditDate', 'EditDate', 'Date'), ('Editor', 'Editor', 'String'), ('Email', 'Email', 'String'), ('Exposed Reinforcement', 'Exposed_Reinforcement', 'String'), ('Foreign Key Placeholder for Asset ID', 'Foreign_Key_Placeholder_for_Asset_ID', 'String'), ('GlobalID', 'GlobalID', 'String'), ('Hatch and Grate Physical Condition Score', 'Hatch_and_Grate_Physical_Condition_Score', 'Integer'), ('Joint Deterioration', 'Joint_Deterioration', 'String'), ('Leaks', 'Leaks', 'String'), ('Lift Station', 'Lift_Station', 'String'), ('Liner Failure', 'Liner_Failure', 'String'), ('OBJECTID', 'OBJECTID', 'OID'), ('Overall Physical Condition Score', 'Overall_Physical_Condition_Score', 'Integer'), ('Please type any notes here.', 'Please_t_1', 'String'), ('Please type any notes here.', 'Please_t_2', 'String'), ('Please type any notes here.', 'Please_type_any_notes_here_', 'String'), ('Spalling, Exposed Aggregate, Pitting, Delamination', 'Spalling__Exposed_Aggregate__Pitting__Delamination', 'String'), ('Structural Damage', 'Structural_Damage', 'String'), ('Surface Corrosion', 'Surface_Corrosion', 'String'), ('Username', 'Username', 'String'), ('x', 'x', 'Double'), ('y', 'y', 'Double')]
# print(sde_dict[0])
# print(sde_dict[0][0])
for i in sde_dict:
    alias = i[0]
    if alias == 'GlobalID':
        del i
    elif alias == 'OBJECTID':
        del i
print(sde_dict)
