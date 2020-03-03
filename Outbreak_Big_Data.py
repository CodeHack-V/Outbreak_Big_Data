#coding:utf-8
import requests,re,json
req=requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92%E8%82%BA%E7%82%8E&sa=searchpromo_yqdt_dbhs')
req.encoding = "utf-8"
data=req.text
res=re.search('\{"confirmed":"(\d{5,})"\,"died":"(\d{4,})"\,"cured":"(\d{5,})","unconfirmed":"(\d{3,})"\,"relativeTime":"\d{10}"\,"confirmedRelative":"(\d{3,})"\,"unconfirmedRelative":"(\d{3,})"\,"curedRelative":"(\d{4,})"\,"diedRelative":"(\d{2,})"\,"icu":"(\d{1,})"\,"icuRelative":"(\-\d{3,})","curConfirm":"(\d{5,})"\,"curConfirmRelative":"(\-\d{4,})"\,"icuDisable":"1"\}',data).group()
data=json.loads(res)
def strcatch(str):
    if(str[0] == '-'):
        return str
    elif (str[0] == '+'):
        return str
    else:
        return '+'+str
print ('现有确诊:'.decode('utf-8')+data['curConfirm']+'\t昨日:'.decode('utf-8')+strcatch(data['curConfirmRelative'])+'\n'+
       '现有疑似:'.decode('utf-8')+data['unconfirmed']+'\t昨日:'.decode('utf-8')+strcatch(data['unconfirmedRelative'])+'\n'+
       '现有重症:'.decode('utf-8')+data['icu']+'\t昨日:'.decode('utf-8')+strcatch(data['icuRelative'])+'\n'+
       '累计确诊:'.decode('utf-8')+data['confirmed']+'\t昨日:'.decode('utf-8')+strcatch(data['confirmedRelative'])+'\n'+
       '累计治愈:'.decode('utf-8')+data['cured']+'\t昨日:'.decode('utf-8')+strcatch(data['curedRelative'])+'\n'+
       '累计死亡:'.decode('utf-8')+data['died']+'\t昨日:'.decode('utf-8')+strcatch(data['diedRelative'])+'\n'
       )