import pandas as pd
links = pd.read_csv(r'C:\Users\jacoo\OneDrive\Desktop\jobs_scraping\utils\all_links.csv')
jobs_data = pd.read_csv(r'C:\Users\jacoo\OneDrive\Desktop\jobs_scraping\utils\job_details.csv')
jobs_data = jobs_data[['date', 'place', 'rate', 'description', 'time']]
links = links[['job_link']]
jobs_data['link'] = links['job_link']
jobs_data['rate'] = jobs_data['rate'].apply(lambda x: x[:4].replace(',', '.'))
jobs_data['rate'] = jobs_data['rate'].astype(str).astype(float)
jobs_data.to_csv(r'C:\Users\jacoo\OneDrive\Desktop\jobs_scraping\api\data.csv')