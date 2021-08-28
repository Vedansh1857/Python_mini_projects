from speedtest import Speedtest
st = Speedtest()
print("Your Connections download speed is : ",st.download())
print("Your Connections upload speed is : ",st.upload())