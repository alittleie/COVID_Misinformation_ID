from pathlib import Path
import pandas as pd

states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
for path in Path(r"C:\Users\mxr29\Covid Data\COVID-19-master\COVID-19-master\csse_covid_19_data\csse_covid_19_daily_reports").iterdir():
    if path.name.endswith('.csv'):
        print(path)
        df = pd.read_csv(path)

        for s in range(len(states)):
            keep_binary = []
            for j in range(len(df)):
                try:
                    state_check = str(df['Province_State'].values[j])

                except:
                    state_check = "hold"

                if state_check == states[s]:
                    keep_binary.append(1)
                else:
                    keep_binary.append(0)
            df["keep"] = keep_binary
            dfk = df[df['keep']==1]
            path_str= str(path)
            file_name= path_str[-14:]
            state_name = states[s] +"/"
            dir="/gpfs/group/engr/covid19/Covid_Case_Data/US_Data_State/" + state_name + file_name
            print(dir)
            dfk.to_csv(dir)
