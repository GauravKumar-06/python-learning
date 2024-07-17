score = 85;
has_done_extra_activities = True;
has_recommendation_letter = False;
interview = "excellent"

if score>=80:
    if has_done_extra_activities:
        if has_recommendation_letter:
            if interview == "excellent":
                print("Admitted with scholarship")
            else:
                print("Admitted without scholarship")
        else:
            print("Can be admitted but require recommendation letter")
    else:
        print("Must do some extra activites")
else:
    print("Rejected")