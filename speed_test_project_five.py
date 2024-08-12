from pystyle import *
import speedtest
Write.Print("[-] this program for Speed Test\n",Colors.red_to_purple, interval=0.01)

print(Box.DoubleCube("Example (5)"))

st = speedtest.Speedtest()

Write.Print(Box.SimpleCube("Please Wait..."), Colors.orange, interval=0.02)
st.get_best_server()

download = st.download() / (1024 ** 2)
upload = st.upload() / (1024 **2)

Write.Print(Box.DoubleCube(f"Speed Test:\nDownload: {download:.2f} Mbps\nUpload: {upload:.2f} Mbps\n"), Colors.green, interval=0.01)

Write.Print(Box.SimpleCube("Finish"), Colors.green, interval=0.01)
