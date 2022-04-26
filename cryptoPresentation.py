import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Initialize lists used to stores token names and 7 day transfer totals
erc20_list = []
transfer_list = []

# for the website used below there are 50 pages in total, so if you would like to pull all those pages change range(1,2) to range(1, 51)
for i in range(1, 2):
  # pulls our website data and creates our BeautifulSoup object
  webpage_response = requests.get("https://bloxy.info/list_tokens/ERC20?page=" + str(i))
  webpage = webpage_response.content
  soup = BeautifulSoup(webpage, "html.parser")

  # finds all our tags that contain the token names
  erc20Tags_list = soup.find_all(attrs={"class": "ellipsis"})

  # appends token name to list
  for token in erc20Tags_list:
    erc20_list.append(token.a.string)

  # finds all our tags that contain the 7 day transfer total (unfiltered)
  sevenDayTransfer_list = soup.find_all(attrs={"class": "text-right"})

  # filters tags for only our specified data and appends to list
  for transfer in sevenDayTransfer_list:
      if (str(transfer.string).isnumeric()):
        transfer_list.append(transfer.string)

# graphs our token names vs 7 day transfer totals using matplotlib  
plt.plot(erc20_list, transfer_list)
plt.xlabel('ERC-20 Tokens')
plt.ylabel('7 Day Transfer Total')
plt.gca().invert_yaxis()
plt.yticks(fontsize = 8)
plt.xticks(rotation = (90), fontsize = 5)
plt.show()
