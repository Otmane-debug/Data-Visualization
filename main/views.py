from django.shortcuts import render
from .forms import AddData, RangeData
from .models import Data
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
from django.utils import timezone
from datetime import datetime, timedelta, date


def app(request):        
        
    x_dates = []
    y_values = []
    
    if request.POST:
        tmp = request.POST["value"]
        tmp_1 = request.POST["date"]
        
        if Data.objects.filter(date__startswith=tmp_1).exists():
            print("Value exists !")
        else:       
            bd = Data(date=tmp_1, value=tmp)
            bd.save()
            
    elif request.GET :
        st = request.GET.get("data_start")
        en = request.GET.get("data_end")
        
        for d in Data.objects.filter(date__range=[st, en]).order_by("date"):
            x_dates.append(str(d))
        
        for val in x_dates:
            tmp_val =  Data.objects.get(date=str(val)).value
            y_values.append(tmp_val)
            
        
    # 1 month
               
    x_data = []
    y_data = []
    lt = []
    ex = ""

    if Data.objects.filter(date__startswith="2022-08").exists():   
        for dt in Data.objects.filter(date__startswith="2022-08"):
            x = str(dt.date)
            lt = x.split("-")
            x_data.append(lt[2])
        for dt in Data.objects.filter(date__startswith="2022-08"):
            y_data.append(dt.value)
    else:
        ex = "No Data found, enter data to see results."
        

    # All mondays 
    
    
    x_li = []
    y_li = []

    date_object = date(2022, 1, 1)
    date_object = date_object + timedelta(days=-date_object.weekday(), weeks=1)
    while date_object <= timezone.now().date():
        sum = 0
        x_li.append(date_object)
        gte = str(date_object)
        ld = str(date_object + timedelta(days=7))
        for i in Data.objects.filter(date__gte=gte, date__lt=ld):
            sum += Data.objects.get(date=i.date).value
        y_li.append(round(sum/7, 3))
        print("Week " + str(gte) + " avg : " + str(sum/7))
        date_object += timedelta(days=7)
    

    # all months

    avg_val = []
    mois_val = []
    ex_2 = ""
    
    if Data.objects.filter(date__startswith="2022-08").exists():   
        for i in range(1, 13):
            if Data.objects.filter(date__startswith="2022-"+str(i).zfill(2)).exists() == False:
                break
            elif Data.objects.filter(date__startswith="2022-"+str(i).zfill(2)).exists():
                mois_val.append(str(i).zfill(2))        
    
        for i in range (1, 13):
            if Data.objects.filter(date__startswith="2022-"+str(i).zfill(2)).exists() == False:
                break
            elif Data.objects.filter(date__startswith="2022-"+str(i).zfill(2)).exists():
                sum = 0
                l = len(Data.objects.filter(date__startswith="2022-"+str(i).zfill(2)))            
                
                for j in Data.objects.filter(date__startswith="2022-"+str(i).zfill(2)):
                    sum += j.value
                    
                avg_tmp = sum / l
                avg_tmp = round(avg_tmp, 3)
                    
                avg_val.append(avg_tmp)
    else:
        ex_2 = "No Data found, enter data to see results."
        
        
    #plotly func
    
    plot_days_div = plot([Scatter(x=x_data, y=y_data, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
    
    plot_months_div = plot([Scatter(x=mois_val, y=avg_val, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")
    
    plot_range_div = plot([Scatter(x=x_dates, y=y_values, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")

    plot_mondays_div = plot([Scatter(x=x_li, y=y_li, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', show_link=False, link_text="")

    
    # Data to render 
    
    form = AddData()
    form_1 = RangeData()

    context = {
        "form": form,
        "form_1": form_1,
        "plot_days_div": plot_days_div,
        "plot_mondays_div": plot_mondays_div,
        "plot_months_div": plot_months_div,
        "plot_range_div": plot_range_div,
        "ex": ex,
        "ex_2": ex_2,
    }
    

    return render(request, 'main/app.html', context)