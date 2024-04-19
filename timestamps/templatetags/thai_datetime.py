from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='thai_datetime')
def thai_datetime(value):
    thai_months = [
        'มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน',
        'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม',
        'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม'
    ]
    
    # แปลงเป็นวัตถุ datetime
    dt = value

    # แปลงวันที่เป็นรูปแบบไทย
    thai_date = f"{dt.day} {thai_months[dt.month - 1]} {dt.year + 543}"

    # แปลงเวลาเป็นรูปแบบไทย
    thai_time = dt.time()

    return f"{thai_date} เวลา {thai_time} น."
