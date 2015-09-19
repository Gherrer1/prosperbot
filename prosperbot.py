import requests

invested = []

count = 0
iteration = 1

signal = raw_input("Hit enter to refresh")

username = ""
password = ""
#was using one of these 2 URL's 
url = 'https://' + username + ':' + password + '@api.prosper.com/api/Listings?$filter=(ProsperRating eq \'E\' or ProsperRating eq \'HR\') and ListingRequestAmount le 7000 and (IncomeRange eq 4 or IncomeRange eq 5 or IncomeRange eq 6) and ListingTerm eq 36 and InquiriesLast6Months le 2'
url2 = 'https://' + username + ':' + password + '@api.prosper.com/api/Listings?$filter=(ProsperRating eq \'E\' or ProsperRating eq \'HR\') and ListingRequestAmount le 6000 and (IncomeRange eq 4 or IncomeRange eq 5 or IncomeRange eq 6) and ListingTerm eq 36'
while(count < 2):
	req = requests.get(url2)
	print iteration, len(req.json())
	#we're interested in how many notes exist
	if(len(req.json()) > 0):
		for note in req.json():
			id = note['ListingNumber']
			#if we havent already invested in the note, invest in it
			if id not in invested:
				dataDict = {'listingId': id, 'amount': 30.00}
				buy = requests.post('https://' + username + ':' + password + '@api.prosper.com/api/Invest/', data=dataDict)
				print buy.json()['Status'], buy.json()['Message']
				if buy.json()['Status'] == 'SUCCESS':
					invested.append(id)
					count = count + 1

				#print note['ListingNumber']
	iteration = iteration + 1

print invested
print 'DONE'
