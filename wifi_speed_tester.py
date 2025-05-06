import speedtest

#Create a Spedtest Object

wifi=speedtest.Speedtest()

#Get the download and uplaod Speeds
download_speed=wifi.download() / 1_000_000
upload_speed=wifi.upload() / 1_000_000

print(f"Download Speed: {download_speed:.2f} Mbps")
print(f"Upload Speed: {upload_speed:.2f} Mbps")
