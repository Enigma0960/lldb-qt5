import lldb
from builtins import chr


def QString_SummaryProvider(valobj,):
    d = valobj.GetChildMemberWithName('raw_data')
    offset = int(d.GetChildMemberWithName('offset').GetValueAsUnsigned() / 2)
    size = valobj.GetChildMemberWithName('size').GetValueAsUnsigned()
    data = d.GetPointeeData(0, size).uint16
    text = "".join([chr(data[offset + i]) for i in range(size)])
    return f"{text}"
