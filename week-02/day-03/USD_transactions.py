xml_file_name = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\transcactions.xml"

import xml.dom.minidom
def usd_transactions(xml_file_name):
    dom = xml.dom.minidom.parse(xml_file_name)
    root = dom.documentElement
    from_data = root.getElementsByTagName("from")
    to_data = root.getElementsByTagName("to")
    amount_data = root.getElementsByTagName("amount")

    for index in range(len(amount_data)):
        if amount_data[index].getAttribute("currency") == "USD":
            print(f"From {from_data[index].firstChild.data} to {to_data[index].firstChild.data}: {amount_data[index].firstChild.data} USD")

usd_transactions(xml_file_name)