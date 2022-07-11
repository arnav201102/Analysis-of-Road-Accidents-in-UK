import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pywaffle import Waffle
import seaborn as sns
import plotly.express as px
acdata=pd.read_csv("Accidents0514.csv", low_memory=False)
acdata.head()

'''Accident_Index	Location_Easting_OSGR	Location_Northing_OSGR	Longitude	Latitude	Police_Force	Accident_Severity	Number_of_Vehicles	Number_of_Casualties	Date	...	Pedestrian_Crossing-Human_Control	Pedestrian_Crossing-Physical_Facilities	Light_Conditions	Weather_Conditions	Road_Surface_Conditions	Special_Conditions_at_Site	Carriageway_Hazards	Urban_or_Rural_Area	Did_Police_Officer_Attend_Scene_of_Accident	LSOA_of_Accident_Location
0	200501BS00001	525680.0	178240.0	-0.191170	51.489096	1	2	1	1	04/01/2005	...	0	1	1	2	2	0	0	1	1	E01002849
1	200501BS00002	524170.0	181650.0	-0.211708	51.520075	1	3	1	1	05/01/2005	...	0	5	4	1	1	0	0	1	1	E01002909
2	200501BS00003	524520.0	182240.0	-0.206458	51.525301	1	3	2	1	06/01/2005	...	0	0	4	1	1	0	0	1	1	E01002857
3	200501BS00004	526900.0	177530.0	-0.173862	51.482442	1	3	1	1	07/01/2005	...	0	0	1	1	1	0	0	1	1	E01002840
4	200501BS00005	528060.0	179040.0	-0.156618	51.495752	1	3	1	1	10/01/2005	...	0	0	7	1	2	0	0	1	1	E01002863
5 rows × 32 columns'''

casdata=pd.read_csv("Casualties0514.csv")
casdata.head()

'''Accident_Index	Vehicle_Reference	Casualty_Reference	Casualty_Class	Sex_of_Casualty	Age_of_Casualty	Age_Band_of_Casualty	Casualty_Severity	Pedestrian_Location	Pedestrian_Movement	Car_Passenger	Bus_or_Coach_Passenger	Pedestrian_Road_Maintenance_Worker	Casualty_Type	Casualty_Home_Area_Type
0	200501BS00001	1	1	3	1	37	7	2	1	1	0	0	-1	0	1
1	200501BS00002	1	1	2	1	37	7	3	0	0	0	4	-1	11	1
2	200501BS00003	2	1	1	1	62	9	3	0	0	0	0	-1	9	1
3	200501BS00004	1	1	3	1	30	6	3	5	2	0	0	-1	0	1
4	200501BS00005	1	1	1	1	49	8	3	0	0	0	0	-1	3	-1
'''

vehdata=pd.read_csv("Vehicles0514.csv")
vehdata.head()

'''Accident_Index	Vehicle_Reference	Vehicle_Type	Towing_and_Articulation	Vehicle_Manoeuvre	Vehicle_Location-Restricted_Lane	Junction_Location	Skidding_and_Overturning	Hit_Object_in_Carriageway	Vehicle_Leaving_Carriageway	...	Was_Vehicle_Left_Hand_Drive?	Journey_Purpose_of_Driver	Sex_of_Driver	Age_of_Driver	Age_Band_of_Driver	Engine_Capacity_(CC)	Propulsion_Code	Age_of_Vehicle	Driver_IMD_Decile	Driver_Home_Area_Type
0	200501BS00001	1	9	0	18	0	0	0	0	0	...	1	15	2	74	10	-1	-1	-1	7	1
1	200501BS00002	1	11	0	4	0	3	0	0	0	...	1	1	1	42	7	8268	2	3	-1	-1
2	200501BS00003	1	11	0	17	0	0	0	4	0	...	1	1	1	35	6	8300	2	5	2	1
3	200501BS00003	2	9	0	2	0	0	0	0	0	...	1	15	1	62	9	1762	1	6	1	1
4	200501BS00004	1	9	0	18	0	0	0	0	0	...	1	15	2	49	8	1769	1	4	2	1
5 rows × 22 columns
'''

acdata.dtypes
'''
Accident_Index                                  object
Location_Easting_OSGR                          float64
Location_Northing_OSGR                         float64
Longitude                                      float64
Latitude                                       float64
Police_Force                                     int64
Accident_Severity                                int64
Number_of_Vehicles                               int64
Number_of_Casualties                             int64
Date                                            object
Day_of_Week                                      int64
Time                                            object
Local_Authority_(District)                       int64
Local_Authority_(Highway)                       object
1st_Road_Class                                   int64
1st_Road_Number                                  int64
Road_Type                                        int64
Speed_limit                                      int64
Junction_Detail                                  int64
Junction_Control                                 int64
2nd_Road_Class                                   int64
2nd_Road_Number                                  int64
Pedestrian_Crossing-Human_Control                int64
Pedestrian_Crossing-Physical_Facilities          int64
Light_Conditions                                 int64
Weather_Conditions                               int64
Road_Surface_Conditions                          int64
Special_Conditions_at_Site                       int64
Carriageway_Hazards                              int64
Urban_or_Rural_Area                              int64
Did_Police_Officer_Attend_Scene_of_Accident      int64
LSOA_of_Accident_Location                       object
dtype: object
'''

casdata.dtypes
'''
Accident_Index                        object
Vehicle_Reference                      int64
Casualty_Reference                     int64
Casualty_Class                         int64
Sex_of_Casualty                        int64
Age_of_Casualty                        int64
Age_Band_of_Casualty                   int64
Casualty_Severity                      int64
Pedestrian_Location                    int64
Pedestrian_Movement                    int64
Car_Passenger                          int64
Bus_or_Coach_Passenger                 int64
Pedestrian_Road_Maintenance_Worker     int64
Casualty_Type                          int64
Casualty_Home_Area_Type                int64
dtype: object
'''

vehdata.dtypes
'''
Accident_Index                      object
Vehicle_Reference                    int64
Vehicle_Type                         int64
Towing_and_Articulation              int64
Vehicle_Manoeuvre                    int64
Vehicle_Location-Restricted_Lane     int64
Junction_Location                    int64
Skidding_and_Overturning             int64
Hit_Object_in_Carriageway            int64
Vehicle_Leaving_Carriageway          int64
Hit_Object_off_Carriageway           int64
1st_Point_of_Impact                  int64
Was_Vehicle_Left_Hand_Drive?         int64
Journey_Purpose_of_Driver            int64
Sex_of_Driver                        int64
Age_of_Driver                        int64
Age_Band_of_Driver                   int64
Engine_Capacity_(CC)                 int64
Propulsion_Code                      int64
Age_of_Vehicle                       int64
Driver_IMD_Decile                    int64
Driver_Home_Area_Type                int64
dtype: object'''

## Visualisation of number of Accidents over the years
acdata['Year']=acdata['Accident_Index'].map(lambda x: str(x)[:4])
acdata['Year']=acdata['Year'].apply(pd.to_numeric, errors='coerce')
year=[]
no_of_ac_yr=[]
for i in range(2005,2015):
    year.append(i)
    no_of_ac_yr.append(len(acdata[acdata['Year']==i]))
plt.plot(year,no_of_ac_yr,color='Tomato',alpha=0.6,marker='o')
plt.xlabel("Year")
plt.ylabel("Number of Accidents")
plt.title("Number of Accidents over the Years")
plt.fill_between(year,no_of_ac_yr,color='Coral',alpha=0.2)
plt.show()

## Visualisation of Percentage of accidents occured by Area
urban=len(acdata[acdata['Urban_or_Rural_Area']==1])
rural=len(acdata[acdata['Urban_or_Rural_Area']==2])
other=len(acdata[acdata['Urban_or_Rural_Area']==3])
total=urban+rural+other
urbanpt=(urban/total)*100
ruralpt=(rural/total)*100
otherpt=(other/total)*100
x=['Urban','Rural','Other']
y=[urbanpt,ruralpt,otherpt]
plt.pie(y,labels=x,colors=["CornflowerBlue","Aquamarine","#a030a1"],explode=[0.2,0,0])
plt.title("Percentage of Accidents occured by Area")
plt.legend()
plt.show()

plt.barh(x,y,color=["DarkMagenta","DarkCyan","#a030a1"]) 
plt.title("Percentage of Accidents occured by Area")
plt.xlabel("Accident Percentage")
plt.ylabel("Areas")
plt.show()

## Visualisation of Correlation b/w No. of Vehicles and Casualties
colors = np.random.randint(1640597, size=(1640597))
plt.scatter(acdata['Number_of_Vehicles'],acdata['Number_of_Casualties'],c=colors,cmap='Greens')
plt.xlabel("Number of Vehicles")
plt.ylabel("Number of Casualties")
plt.title("Correlation b/w No. of Vehicles and Casualties")
plt.colorbar()
plt.show()

## Visualisation of accidents because of different Road surface conditions
dry=0
wet=0
snow=0
ice=0
flood=0
oil=0
mud=0
unk=0
for i in acdata['Road_Surface_Conditions']:
    if(i==1):
        dry=dry+1
    elif(i==2):
        wet=wet+1
    elif(i==3):
        snow=snow+1
    elif(i==4):
        ice=ice+1
    elif(i==5):
        flood=flood+1
    elif(i==6):
        oil=oil+1
    elif(i==7):
        mud=mud+1
    else:
        unk=unk+1
        
totrs=dry+wet+snow+ice+flood+oil+mud+unk
dryp=(dry/totrs)*100
wetp=(wet/totrs)*100
snowp=(snow/totrs)*100
icep=(ice/totrs)*100
floodp=(flood/totrs)*100
oilp=(oil/totrs)*100
mudp=(mud/totrs)*100
unkp=(unk/totrs)*100
labrs=['Dry','Damp','Snow','Ice','Flood','Oil','Mud','NAN']
rs=[dryp,wetp,snowp,icep,floodp,oilp,mudp,unkp]
plt.pie(rs,labels=labrs,explode=[0.2,0.2,0.6,0.6,0.8,0.8,0.8,0.8])
plt.legend(bbox_to_anchor=(1.2, 1.15))
circle = plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(circle)
plt.show()

## Visualisation of Casualty Percentage of Drivers, Passengers, Pedestrians
driv=0
pas=0
ped=0
for i in casdata['Casualty_Class']:
    if(i==1):
        driv=driv+1
    elif(i==2):
        pas=pas+1
    else:
        ped=ped+1
totcc=driv+pas+ped
drivp=(driv/totcc)*100
pasp=(pas/totcc)*100
pedp=(ped/totcc)*100
dat={'cascc':['Driver or Rider','Passenger','Pedestrian'], 'cc':[drivp,pasp,pedp]}
df = pd.DataFrame(dat)
fig = plt.figure(
    FigureClass = Waffle,
    rows = 5,
    values = df.cc,
    labels = list(df.cascc),
    colors=['#0097A7','#E91E63','#9900CC']
)
plt.show()

## stacked bar chart to show comparison of number of accidents ocuured during different lighting grouped by days
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
ac_day1=[]
ac_day2=[]
ac_day3=[]
ac_day4=[]
ac_day5=[]
ac_day6=[]
for i in range(1,8):
    ac_day1.append(len(acdata[(acdata['Day_of_Week']==i)&(acdata['Light_Conditions']==1)]))
    ac_day2.append(len(acdata[(acdata['Day_of_Week']==i)&(acdata['Light_Conditions']==4)]))
    ac_day3.append(len(acdata[(acdata['Day_of_Week']==i)&(acdata['Light_Conditions']==5)]))
    ac_day4.append(len(acdata[(acdata['Day_of_Week']==i)&(acdata['Light_Conditions']==6)]))
    ac_day5.append(len(acdata[(acdata['Day_of_Week']==i)&(acdata['Light_Conditions']==7)]))
    ac_day6.append(len(acdata[(acdata['Day_of_Week']==i)&(acdata['Light_Conditions']==-1)]))
y1=np.array(ac_day1)
y2=np.array(ac_day2)
y3=np.array(ac_day3)
y4=np.array(ac_day4)
y5=np.array(ac_day5)
y6=np.array(ac_day6)
plt.bar(days, y1, color='#0089BA')
plt.bar(days, y2, bottom=y1, color='#4D8076')
plt.bar(days, y3, bottom=y1+y2, color='#FF9671')
plt.bar(days, y4, bottom=y1+y2+y3, color='#C6D634')
plt.bar(days, y5, bottom=y1+y2+y3+y4, color='#C34A36')
plt.bar(days, y6, bottom=y1+y2+y3+y4+y5, color='purple')
plt.legend(['Daylight','Darkness with streetlights','Kinda Dark','Complete Darkness',
            'Darkness-lighting unknown','NAN'],bbox_to_anchor =(0.65, 1.00))
plt.show()

## Visualisation of number of accidents over years and months through time series plot and heatmap plot
acdata['Month']=acdata['Date'].map(lambda x: str(x)[3:5])
acdata['Month']=acdata['Month'].apply(pd.to_numeric, errors='ignore')
acci=[]
yrl=[]
for i in range(2005,2015):
    for j in range(1,13):
        acci.append(len(acdata[(acdata['Month']==j) & (acdata['Year']==i)]))
        yrl.append(i)
mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monl=[]
for i in range(1,11):
    for j in mon:
        monl.append(j)
dfn=pd.DataFrame(list(zip(yrl,monl,acci)),columns=['Year','Month','No_of_Accidents'])
dfn.head()
'''
Year	Month	No_of_Accidents
0	2005	Jan	16278
1	2005	Feb	14521
2	2005	Mar	14977
3	2005	Apr	15661
4	2005	May	17032
'''
yrtp= dfn['Year'].unique()
f=plt.figure(figsize=(16,12), dpi= 80)
f.set_figwidth(9)
f.set_figheight(6)
for i, y in enumerate(yrtp):
    if i > 0:        
        plt.plot('Month','No_of_Accidents', data=dfn.loc[dfn.Year==y, :], label=y)
plt.title("Time Series Plot Showing Trend of Accidents over months and years")
plt.legend(bbox_to_anchor =(1.1, 1.0))
plt.show()

achm=dfn.pivot("Month","Year","No_of_Accidents")
ax = sns.heatmap(achm, linewidths=.6)

## comparison of various factors through interactive heatmap
dfhm=pd.DataFrame(list(zip(acdata['Number_of_Vehicles'],acdata['Day_of_Week'],acdata['Month'],
                           acdata['Light_Conditions'], acdata['Road_Surface_Conditions'],
                          acdata['Did_Police_Officer_Attend_Scene_of_Accident'])), 
                 columns=['Number_of_Vehicles','Day_of_Week','Month','Light_Conditions','Road_Surface_Conditions',
                          'Did_Police_Officer_Attend_Scene_of_Accident'])
fig = px.imshow(dfhm.corr())
fig.show()
purpose={1:'Journey as part of work',2:'Commuting to/from work',3:'Taking pupil to/from school',
        4:'Pupil riding to/from school',5:'Other',6:'Not known',15:'Not known/Other'}
drivage={1:'0 - 5',2:'6 - 10',3:'11 - 15',4:'16 - 20',5:'21 - 25',6:'26 - 35',7:'36 - 45',8:'46 - 55',
            9:'56 - 65',10:'66 - 75',11:'Over 75'}
drivarea={1:'Urban Area',2:'Small Town',3:'Rural'}
drivgen={1:'Male',2:'Female',3:'Other'}
dfbp=pd.DataFrame(data=vehdata, columns=['Vehicle_Reference','Sex_of_Driver','Age_of_Driver','Age_Band_of_Driver',
                                        'Driver_Home_Area_Type','Journey_Purpose_of_Driver'])
dfbp=dfbp[dfbp.Sex_of_Driver !=-1]
dfbp.head()
'''
Vehicle_Reference	Sex_of_Driver	Age_of_Driver	Age_Band_of_Driver	Driver_Home_Area_Type	Journey_Purpose_of_Driver
0	1	2	74	10	1	15
1	1	1	42	7	-1	1
2	1	1	35	6	1	1
3	2	1	62	9	1	15
4	1	2	49	8	1	15
'''
dfbp.Driver_Home_Area_Type=dfbp.Driver_Home_Area_Type.map(drivarea)
dfbp.Age_Band_of_Driver=dfbp.Age_Band_of_Driver.map(drivage)
dfbp.Sex_of_Driver=dfbp.Sex_of_Driver.map(drivgen)
dfbp.Journey_Purpose_of_Driver=dfbp.Journey_Purpose_of_Driver.map(purpose)
dfbp.head()
'''
Vehicle_Reference	Sex_of_Driver	Age_of_Driver	Age_Band_of_Driver	Driver_Home_Area_Type	Journey_Purpose_of_Driver
0	1	Female	74	66 - 75	Urban Area	Not known/Other
1	1	Male	42	36 - 45	NaN	Journey as part of work
2	1	Male	35	26 - 35	Urban Area	Journey as part of work
3	2	Male	62	56 - 65	Urban Area	Not known/Other
4	1	Female	49	46 - 55	Urban Area	Not known/Other
'''
plt.figure(figsize=(20,7))
sns.boxplot(x='Journey_Purpose_of_Driver',y='Age_of_Driver',data=dfbp)
plt.show()

sns.catplot(x='Age_of_Driver',y='Driver_Home_Area_Type',kind="violin",data=dfbp)
<seaborn.axisgrid.FacetGrid at 0x267fb2ceb20>

plt.figure(figsize=(19,5)) 
sns.barplot(x='Sex_of_Driver',y='Age_of_Driver',data=dfbp,hue='Journey_Purpose_of_Driver',
            palette='Paired',ci=None) 
plt.legend() 
plt.show()

vehtype={1:'Pedal cycle',2:'Motorcycle 50cc and under',3:'Motorcycle 125cc and under',
                  4:'Motorcycle over 125cc and up to 500cc',5:'Motorcycle over 500cc',8:'Taxi/Private hire car',
                  9:'Car',10:'Minibus (8 - 16 passenger seats)',11:'Bus or coach (17 or more pass seats)',
                  16:'Ridden horse',17:'Agricultural vehicle',18:'Tram',19:'Van / Goods 3.5 tonnes mgw or under',
                  20:'Goods over 3.5t. and under 7.5t',21:'Goods 7.5 tonnes mgw and over',22:'Mobility scooter',
                  23:'Electric motorcycle',90:'Other vehicle',97:'Motorcycle - unknown cc',
                  98:'Goods vehicle - unknown weight'}
propcode={1:'Petrol',2:'Heavy oil',3:'Electric',4:'Steam',5:'Gas',6:'Petrol/Gas (LPG)',7:'Gas/Bi-fuel',
          8:'Hybrid electric',9:'Gas Diesel',10:'New fuel technology',11:'Fuel cells',12:'Electric diesel'}
dfs=pd.DataFrame(data=vehdata,columns=['Vehicle_Reference','Vehicle_Type','Age_of_Vehicle','Engine_Capacity_(CC)','Propulsion_Code'])
dfs=dfs[dfs.Vehicle_Type!=-1]
dfs=dfs[dfs.Age_of_Vehicle!=-1]
dfs=dfs[dfs['Engine_Capacity_(CC)']!=-1]
dfs.head()
'''
Vehicle_Reference	Vehicle_Type	Age_of_Vehicle	Engine_Capacity_(CC)	Propulsion_Code
1	1	11	3	8268	2
2	1	11	5	8300	2
3	2	9	6	1762	1
4	1	9	4	1769	1
5	1	3	10	85	1
'''
dfs['Vehicle_Type']=dfs.Vehicle_Type.map(vehtype)
dfs['Propulsion_Code']=dfs.Propulsion_Code.map(propcode)
dfs.head()
'''
Vehicle_Reference	Vehicle_Type	Age_of_Vehicle	Engine_Capacity_(CC)	Propulsion_Code
1	1	Bus or coach (17 or more pass seats)	3	8268	Heavy oil
2	1	Bus or coach (17 or more pass seats)	5	8300	Heavy oil
3	2	Car	6	1762	Petrol
4	1	Car	4	1769	Petrol
5	1	Motorcycle 125cc and under	10	85	Petrol
'''
sns.catplot(x="Vehicle_Type",y="Engine_Capacity_(CC)",data=dfs)
plt.xticks(rotation ='vertical')
plt.show()

fig=px.pie(dfs,values='Vehicle_Reference',names='Vehicle_Type',labels={'Vehicle_Reference':'Count'})
fig.show()
fig = px.scatter(dfs,x='Propulsion_Code',y='Engine_Capacity_(CC)',color='Vehicle_Type',symbol='Vehicle_Type')
fig.show()
dfc=pd.DataFrame(data=casdata, columns=['Sex_of_Casualty','Age_of_Casualty','Age_Band_of_Casualty',
                                        'Casualty_Severity','Pedestrian_Location','Casualty_Class',
                                        'Casualty_Home_Area_Type'])
dfc=dfc[dfc.Sex_of_Casualty !=-1]
dfc=dfc[dfc.Age_of_Casualty !=-1]
dfc.head()

'''
Sex_of_Casualty	Age_of_Casualty	Age_Band_of_Casualty	Casualty_Severity	Pedestrian_Location	Casualty_Class	Casualty_Home_Area_Type
0	1	37	7	2	1	3	1
1	1	37	7	3	0	2	1
2	1	62	9	3	0	1	1
3	1	30	6	3	5	3	1
4	1	49	8	3	0	1	-1
'''

casage={1:'0 - 5',2:'6 - 10',3:'11 - 15',4:'16 - 20',5:'21 - 25',6:'26 - 35',7:'36 - 45',8:'46 - 55',
            9:'56 - 65',10:'66 - 75',11:'Over 75'}
casarea={1:'Urban Area',2:'Small Town',3:'Rural'}
casgen={1:'Male',2:'Female',3:'Other'}
cassev={1:'Fatal',2:'Serious',3:'Slight'}
casclass={1:'Driver/Rider',2:'Passenger',3:'Pedestrian'}
dfc.Casualty_Home_Area_Type=dfc.Casualty_Home_Area_Type.map(casarea)
dfc.Sex_of_Casualty=dfc.Sex_of_Casualty.map(casgen)
dfc.Age_Band_of_Casualty=dfc.Age_Band_of_Casualty.map(casage)
dfc.Casualty_Severity=dfc.Casualty_Severity.map(cassev)
dfc.Casualty_Class=dfc.Casualty_Class.map(casclass)
dfc.head()

'''
Sex_of_Casualty	Age_of_Casualty	Age_Band_of_Casualty	Casualty_Severity	Pedestrian_Location	Casualty_Class	Casualty_Home_Area_Type
0	Male	37	36 - 45	Serious	1	Pedestrian	Urban Area
1	Male	37	36 - 45	Slight	0	Passenger	Urban Area
2	Male	62	56 - 65	Slight	0	Driver/Rider	Urban Area
3	Male	30	26 - 35	Slight	5	Pedestrian	Urban Area
4	Male	49	46 - 55	Slight	0	Driver/Rider	NaN
'''

fig = px.histogram(dfc, x='Age_of_Casualty',marginal = 'box')
fig.show()
fig=px.box(dfc,x='Sex_of_Casualty',y='Age_of_Casualty',color='Casualty_Severity')
fig.show()

## Point Plot
ax = sns.catplot(x='Casualty_Home_Area_Type',y='Age_of_Casualty',hue='Casualty_Class',kind='point',data=dfc)
plt.savefig('output.png', dpi=300, bbox_inches='tight')
ax.fig.autofmt_xdate()

acdata['Time']=acdata['Time'].map(lambda x:str(x).split(':')[0]).apply(pd.to_numeric,errors='coerce')
time=[]
s1=[]
s2=[]
s3=[]
for i in range(0,25):
    time.append(i)
    s1.append(len(acdata[(acdata['Time']==i) & (acdata['Accident_Severity']==1)]))
    s2.append(len(acdata[(acdata['Time']==i) & (acdata['Accident_Severity']==2)]))
    s3.append(len(acdata[(acdata['Time']==i) & (acdata['Accident_Severity']==3)]))
import plotly.graph_objects as px
import plotly.graph_objects as go
plot = px.Figure()
plot.add_trace(go.Scatter(
    name = 'Fatal',
    x = time,
    y = s1,
    stackgroup='one'))
plot.add_trace(go.Scatter(
    name = 'Serious',
    x = time,
    y = s2,
    stackgroup='one'))
plot.add_trace(go.Scatter(
    name = 'Slight',
    x = time,
    y = s3,
    stackgroup='one'))
 
