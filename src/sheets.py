import time
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

class Sheet:
    CACHE_TIME = 60 * 30

    def __init__(self, db):
        self.db = db
        self.data = None
        self.last_updated = time.time()

    def get_sheet(self):
        return self.db

    def get_data(self):
        curr_time = time.time()
        if not self.data or curr_time - self.last_updated > self.CACHE_TIME:
            self.data = self.db.get_all_records(numericise_ignore=["all"])
            self.last_updated = curr_time
            print(f"Updating database from web")

        return self.data


class SheetManager:
    def __init__(self):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive",
        ]
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(
                os.path.abspath("creds.json"), scope
            )
            client = gspread.authorize(creds)
            self.user_db = Sheet(client.open("User Database").sheet1)  # Open the spreadhseet
            print("User Database Loaded")
            self.activity_db = Sheet(client.open_by_url(
                "https://docs.google.com/spreadsheets/d/1aLBb1J2ifoUG2UAxHHbwxNO3KrIIWoI0pnZ14c5rpOM/edit?usp=drive_web&ouid=104398832910104737872"
            ).sheet1)
            print("Activity Log Loaded")
            self.waiver_db = Sheet(client.open("Waiver Signatures").sheet1)
            print("Waiver Database Loaded")
        except:
            print("An ERROR has ocurred connecting to google sheets")

    def get_user_db(self):
        return self.user_db.get_sheet()
    
    def get_activity_db(self):
        return self.activity_db.get_sheet()
    
    def get_waiver_db(self):
        return self.waiver_db.get_sheet()

    def get_user_db_data(self):
        return self.user_db.get_data()
    
    def get_activity_db_data(self):
        return self.activity_db.get_data()
    
    def get_waiver_db_data(self):
        return self.waiver_db.get_data()