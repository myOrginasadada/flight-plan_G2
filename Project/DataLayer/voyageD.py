import csv
from models.voyageM import Voyage

class VoyageData:
    voyages = {}
    FILE_NAME = "dataLayer\\voyage.csv"

    def __init__(self):
        pass

#    def load_data_from_file(self):
#        with open(self.FILE_NAME, newline='') as csvfile:
#            reader = csv.reader(csvfile)
#            next(reader)  # skps the header row
#            for row in reader:
#                voyage_id = row[0]
#                voyage_info = row[1:]
#                voyage = Voyage.from_row(voyage_id, voyage_info)
#                self.voyages[voyage_id] = voyage

    def get_all_voyages(self):
        voyage_list = []
        with open(self.FILE_NAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                voyage_list.append(row)
        return voyage_list

    def save_data_to_file(self):
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for voyage in self.voyages.values():
                writer.writerow(voyage.serialize())

    def create_voyage(self, voyage: Voyage):
        self.voyages[voyage.voyage_id] = voyage
        self.save_data_to_file()

    def get_voyage_by_id(self, voyage_id):
        return self.voyages.get(voyage_id, None)

